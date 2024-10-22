#ifndef _BSPLINE_HPP
#define _BSPLINE_HPP

#include <cassert>
#include <cmath>
#include <omp.h>
#include <cstdlib>
#include <cstring>
#include <cstdio>


/*
 * binary search with guess (for general BSplines)
 *
 * largely borrowed from numpy/core/src/multiarray/compile_base.c
 */
#define LIKELY_IN_CACHE_SIZE 8
template<class Scalar>
int binary_search_with_guess(Scalar key, Scalar *arr, int len, int guess)
{
   int imin = 0, imax = len;

   /* key outside grid boundaries */
   if (key < arr[0])
      return -1;
   if (key > arr[len - 1])
      return len;

   /* if len<=4, perform a linear search */
   if (len <= 4)
   {
      int i;
      for (i = 1; i < len && key >= arr[i]; ++i)
         ;
      return i - 1;
   }

   /* try the values close to guess */
   if (guess > len - 3)
      guess = len - 3;
   if (guess < 1)
      guess = 1;

   /* check most likely values: guess-1, guess, guess+1 */
   if (key < arr[guess])
   {
      if (key < arr[guess - 1])
      {
         imax = guess - 1;
         if (guess > LIKELY_IN_CACHE_SIZE &&
             key >= arr[guess - LIKELY_IN_CACHE_SIZE])
         {
            imin = guess - LIKELY_IN_CACHE_SIZE;
         }
      }
      else
      {
         return guess - 1;
      }
   }
   else /* key >= arr[guess] */
   {
      if (key < arr[guess + 1])
      {
         return guess;
      }
      else
      {
         if (key < arr[guess + 2])
         {
            return guess + 1;
         }
         else
         {
            imin = guess + 2;
            if (guess < len - LIKELY_IN_CACHE_SIZE - 1 &&
                key < arr[guess + LIKELY_IN_CACHE_SIZE])
            {
               imax = guess + LIKELY_IN_CACHE_SIZE;
            }
         }
      }
   }

   /* still not found, but we now have a (imin, imax), so try a bisection */
   while (imin < imax)
   {
      const int imid = imin + ((imax - imin) >> 1);
      if (key >= arr[imid])
         imin = imid + 1;
      else
         imax = imid;
   }
   return imin - 1;
}
#undef LIKELY_IN_CACHE_SIZE

/*
 * Seems to be faster than np.digitize
 */
template<class Scalar>
void binary_search(Scalar *key, int *index, int N, Scalar *arr, int len)
{
   int i, guess = len >> 1;
   #pragma omp parallel for
   for (i = 0; i < N; i++)
   {
      index[i] = binary_search_with_guess(key[i], arr, len, guess);
      guess = index[i];
   }
}


/*
 * blossoming function: compute the spline values, at the requested
 * order for the x's passed in argument. Return triplets (i,j,B) which
 * are used to construct a sparse jacobian matrix: B_j(x_i)
 *
 * args
 * ----
 *  - x     : the x values, rescaled on the integer grid: [order-1, jmax]
 *  - nx    : size of the x array
 *  - i, j  : line and column indices of the jacobian matrix
 *  - B     : values of the jacobian matrix (B_j(x_i))
 *  - N     : size of the i,j and B vectors ( = nx*order)
 *  - order_stop : stop blossoming at order_stop (<order)
 *  - order : spline order
 *  - nj  : size of the spline basis
 *
 * returns
 * -------
 *   void
 *
 * Note: for the x's which are outside the basis range, we return 0.
 */
template<class Scalar>
void blossom(Scalar *x, int nx, int *i, int *j, Scalar *B, int N, int order_stop, int order, int nj)
{
   int p, q;
   const int deg = order - 1;
   assert(N == nx * order);

   /* -------------------------------------------------------------- */
   /* initialize i, j, B                                             */
   /*                                                                */
   /*   i    ... | k | k | k | ... | k       | ...                   */
   /*   j    ... |   |   |   | ... | E(x_i)  | ...                   */
   /*   B    ... | 0 | 0 | 0 | ... | 1       | ...                   */
   /*                                                                */
   /* -------------------------------------------------------------- */
   #pragma omp parallel for private(p, q)
   for (int k = 0; k < nx; k++)
   {
      p = order * k;
      B[p + deg] = 1.;
      i[p + deg] = k;
      j[p + deg] = (int)floor(x[k]);
      for (q = deg - 1; q >= 0; q--)
      {
         i[p + q] = k;
         j[p + q] = j[p + q + 1] - 1;
      }

      if (x[k] < deg || x[k] >= nj)
      {
         B[p + deg] = 0.;
         for (q = deg; q >= 0; q--)
         {
            j[p + q] = 0;
         }
      }
   }

   /* blossom */
   Scalar xx, o1, o2;
   Scalar l1, l2;
   /* loop on the spline orders */
   for (int oo = 2; oo <= order_stop; oo++)
   {
      const Scalar scale = 1. / (Scalar)(oo - 1);

      // loop on the xi's
      #pragma omp parallel for private(p, q, xx, o1, o2, l1, l2)
      for (int k = 0; k < nx; k++)
      {
         p = order * k;
         xx = x[k];
         o1 = (xx - j[p + deg]) * scale;
         l1 = o1 * B[p + deg];
         /* loop on the splines that have non-zero values */
         for (q = deg - 1; q >= (order - oo); q--)
         {
            o1 = (xx - j[p + q]) * scale;
            o2 = (xx - j[p + q + 1]) * scale;
            l2 = l1;
            l1 = o1 * B[p + q] + (1. - o2) * B[p + q + 1];
            B[p + q + 1] = l2;
         }
         B[p + q + 1] = l1;
      }
   }
}


/*
 * same as above, but the grid can be irregular.
 */
template<class Scalar>
void blossom_grid(
   Scalar *t, int nt,
   Scalar *x, int nx,
   int *i, int *j, Scalar *B, int N,
   int order_stop, int order, int nj)
{
   int p, q;
   const int deg = order - 1;
   assert(N == nx * order);

   int *jj = new int[nx];
   Scalar *scales = new Scalar[nt];

   /* we cannot escape a binary search to locate the x's in the grid */
   binary_search<Scalar>(x, jj, nx, t, nt);

   /* initialize i,j,B */
   #pragma omp parallel for private(p, q)
   for (int k = 0; k < nx; k++)
   {
      p = order * k;
      B[p + deg] = 1.;
      i[p + deg] = k;
      j[p + deg] = jj[k];
      for (q = deg - 1; q >= 0; q--)
      {
         i[p + q] = k;
         j[p + q] = j[p + q + 1] - 1;
      }
      if (jj[k] < deg || jj[k] >= nj)
      {
         B[p + deg] = 0;
         for (q = deg; q >= 0; q--)
            j[p + q] = 0;
      }
   }

   /* blossom */
   int jx;
   Scalar xx, o1, o2;
   Scalar l1, l2, s;
   for (int oo = 2; oo <= order_stop; oo++)
   {
      /* compute the scales */
      #pragma omp parallel for
      for (p = 0; p < nt - 1; p++)
      {
         s = 0.;
         jx = p + oo - 1;
         if (jx < nt)
            s = t[jx] - t[p];
         if (s > 0.)
            scales[p] = 1. / s;
         else
            scales[p] = 0.;
      }
      /* B-Spline values, from the preceding order */
      #pragma omp parallel for private(p, q, xx, o1, o2, l1, l2)
      for (int k = 0; k < nx; k++)
      {
         p = order * k;
         xx = x[k];
         jx = j[p + deg];
         o1 = (xx - t[jx]) * scales[jx];
         l1 = o1 * B[p + deg];
         for (q = deg - 1; q >= (order - oo); q--)
         {
            jx = j[p + q];
            o1 = (xx - t[jx]) * scales[jx];
            o2 = (xx - t[jx + 1]) * scales[jx + 1];
            l2 = l1;
            l1 = o1 * B[p + q] + (1. - o2) * B[p + q + 1];
            B[p + q + 1] = l2;
         }
         B[p + q + 1] = l1;
      }
   }

   delete[] jj;
   delete[] scales;
}

/*
 *  deriv
 *
 *  implement the formula:
 *    dB_{jk}/dx = (k-1) * (-B_{j+1,k-1}/(t_{j+k}-t_{j+1}) + B_{j,j-1}/(t_{j+k-1}-t_{j}))
 */
template<class Scalar>
void deriv_grid(Scalar *t, int nt, int *i, int *j, Scalar *B, int N, int nx, int order)
{
   int p, q, k, jx;
   const int deg = order - 1;
   const Scalar km1 = order - 1.;
   Scalar s, l1, l2;
   Scalar *scale = new Scalar[nt];

   #pragma omp parallel for
   for (p = 0; p < nt; p++)
   {
      if (p + order >= nt)
      {
         scale[p] = 0.;
      }
      else
      {
         s = t[p + order - 1] - t[p];
         scale[p] = s > 0. ? 1. / s : 0.;
      }
   }

   #pragma omp parallel for private(p, q, jx, l1, l2)
   for (k = 0; k < nx; k++)
   {
      p = order * k;
      jx = j[p + deg];
      l1 = B[p + deg] * scale[jx] * km1;
      for (q = deg - 1; q >= 0; q--)
      {
         jx = j[p + q];
         l2 = l1;
         l1 = (-B[p + q + 1] * scale[jx + 1] + B[p + q] * scale[jx]) * km1;
         B[p + q + 1] = l2;
      }
      B[p + q + 1] = l1;
   }

   delete[] scale;
}


#endif  // _BSPLINE_HPP
