from bbf.sncosmoutils import retrieve_bandpass_model
import sncosmo.bandpasses


# there was a bug here betwwen bbf and cosmoutils
def test_retrieve_bandpass():
    band = retrieve_bandpass_model('megacampsf::g', average=True, radius=0)
    assert isinstance(band, sncosmo.bandpasses.AggregateBandpass)
