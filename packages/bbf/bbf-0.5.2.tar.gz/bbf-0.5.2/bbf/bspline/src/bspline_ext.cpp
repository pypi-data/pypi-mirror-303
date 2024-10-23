#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>

#include "bspline.hpp"


namespace nb = nanobind;

using namespace nb::literals;


template<class Scalar>
void blossom_ext(
   const nb::ndarray<nb::numpy, Scalar, nb::shape<-1>>& x,
   nb::ndarray<nb::numpy, int, nb::shape<-1>>& i,
   nb::ndarray<nb::numpy, int, nb::shape<-1>>& j,
   nb::ndarray<nb::numpy, Scalar, nb::shape<-1>>& B,
   int order_stop, int order, int size)
{
   blossom<Scalar>(
      x.data(), x.size(),
      i.data(), j.data(), B.data(), B.size(),
      order_stop, order, size);
}


template<class Scalar>
void blossom_grid_ext(
   const nb::ndarray<nb::numpy, Scalar, nb::shape<-1>>& t,
   const nb::ndarray<nb::numpy, Scalar, nb::shape<-1>>& x,
   nb::ndarray<nb::numpy, int, nb::shape<-1>>& i,
   nb::ndarray<nb::numpy, int, nb::shape<-1>>& j,
   nb::ndarray<nb::numpy, Scalar, nb::shape<-1>>& B,
   int order_stop, int order, int size)
{
   blossom_grid<Scalar>(
      t.data(), t.size(),
      x.data(), x.size(),
      i.data(), j.data(), B.data(), B.size(),
      order_stop, order, size);
}


template<class Scalar>
void deriv_grid_ext(
   const nb::ndarray<nb::numpy, Scalar, nb::shape<-1>>& t,
   nb::ndarray<nb::numpy, int, nb::shape<-1>>& i,
   nb::ndarray<nb::numpy, int, nb::shape<-1>>& j,
   nb::ndarray<nb::numpy, Scalar, nb::shape<-1>>& B,
   int x_size, int order)
{
   deriv_grid<Scalar>(
      t.data(), t.size(),
      i.data(), j.data(), B.data(), B.size(),
      x_size, order);
}


NB_MODULE(bspline_ext, m)
{
    m.doc() = "Wrappers to C implementation for fast bspline computation";

    // double version
    m.def(
       "_blossom_d", blossom_ext<double>,
       "x"_a, "i"_a, "j"_a, "B"_a, "order_stop"_a, "order"_a, "size"_a);
    m.def(
       "_blossom_grid_d", blossom_grid_ext<double>,
       "t"_a, "x"_a, "i"_a, "j"_a, "b"_a, "order_stop"_a, "order"_a, "size"_a);
    m.def(
       "_deriv_grid_d", deriv_grid_ext<double>,
       "t"_a, "i"_a, "j"_a, "B"_a, "nx"_a, "order"_a);

    // float version
    m.def(
       "_blossom_f", blossom_ext<float>,
       "x"_a, "i"_a, "j"_a, "B"_a, "order_stop"_a, "order"_a, "size"_a);
    m.def(
       "_blossom_grid_f", blossom_grid_ext<float>,
       "t"_a, "x"_a, "i"_a, "j"_a, "b"_a, "order_stop"_a, "order"_a, "size"_a);
    m.def(
       "_deriv_grid_f", deriv_grid_ext<float>,
       "t"_a, "i"_a, "j"_a, "B"_a, "nx"_a, "order"_a);
}
