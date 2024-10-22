import unittest
import numpy as np
from numpy.testing import (
        assert_, assert_raises, assert_equal, assert_almost_equal, assert_warns,
        assert_no_warnings, assert_array_equal, assert_array_almost_equal,
        suppress_warnings
        )

from .. import utils
from .. import tx


class TestGenerateConstellation(unittest.TestCase):
    """
    Test class for generate_constellation
    """
    
    def test_completeness(self):
        # QPSK
        ref = set([-1.-1.j, -1.+1.j,  1.-1.j,  1.+1.j])
        const = utils.generate_constellation(format='QAM', order=4)
        assert_equal(len(ref.difference(const)), 0)
        # 16QAM
        ref = set([-3.-3.j, -3.-1.j, -3.+3.j, -3.+1.j, -1.-3.j, -1.-1.j, -1.+3.j,
                   -1.+1.j,  3.-3.j,  3.-1.j,  3.+3.j,  3.+1.j,  1.-3.j,  1.-1.j,
                   1.+3.j,  1.+1.j])
        const = utils.generate_constellation(format='QAM', order=16)
        assert_equal(len(ref.difference(const)), 0)
        # 32 QAM        
        ref = set([-3.-5.j, -1.-5.j, -3.+5.j, -1.+5.j, -5.-3.j, -5.-1.j, -5.+3.j,
                   -5.+1.j, -1.-3.j, -1.-1.j, -1.+3.j, -1.+1.j, -3.-3.j, -3.-1.j,
                   -3.+3.j, -3.+1.j,  3.-5.j,  1.-5.j,  3.+5.j,  1.+5.j,  5.-3.j,
                   5.-1.j,  5.+3.j,  5.+1.j,  1.-3.j,  1.-1.j,  1.+3.j,  1.+1.j,
                   3.-3.j,  3.-1.j,  3.+3.j,  3.+1.j])
        const = utils.generate_constellation(format='QAM', order=32)
        assert_equal(len(ref.difference(const)), 0)
        
    def test_errors(self):
        # verifies errors raised by function
        with assert_raises(TypeError):
            # order type
            utils.generate_constellation(order=4.)  
        with assert_raises(ValueError):
            # valid order numbers
            utils.generate_constellation(order=5)
            utils.generate_constellation(order=2)
            # valid modulation formats
            utils.generate_constellation(format='DPSK')
        
        
class TestTimeAxis(unittest.TestCase):
    """
    Test class for creat_time_axis
    """
    
    def test_length(self):
        l = 100
        t = utils.create_time_axis(sample_rate=1.0, n_samples=l)
        assert_equal(len(t), l)
        l = 101
        t = utils.create_time_axis(sample_rate=1.0, n_samples=l)
        assert_equal(len(t), l)
    
    def test_end_points_and_delta(self):
        l = 100
        sr = 10
        t = utils.create_time_axis(sample_rate=sr, n_samples=l)
        assert_equal(t[0], 0)
        assert_equal(t[-1], 1/sr*(l-1))
        assert_equal(t[1]-t[0], 1/sr)
        
        l = 101
        sr = 10
        t = utils.create_time_axis(sample_rate=sr, n_samples=l)
        assert_equal(t[0], 0)
        assert_equal(t[-1], 1/sr*(l-1))
        assert_equal(t[1]-t[0], 1/sr)
        
        
class TestBitsToDec(unittest.TestCase):
    """
    Test class for bits_to_dec
    """
    
    def test_errors(self):
        # test errors thrown by function
        with assert_raises(ValueError):
            # one-dimensionality
            utils.bits_to_dec(np.asarray([[True,False],[False,True]]),4)
            # n_bits is integer multiple of m
            utils.bits_to_dec(np.asarray([True,False,True,True]),3)
    
    def test_reconversion(self):
        # convert and reconvert bit sequence and test for equality
        dummy = tx.generate_bits(n_bits=20)
        dec_dummy = utils.bits_to_dec(dummy,4)
        bits = utils.dec_to_bits(dec_dummy,4)
        assert_equal(bits,dummy)
        
class TestEstimateSnrSpectrum(unittest.TestCase):
    """
    Test class for estimate_snr_spectrum
    """
    
    def test_correct_snr(self):
        
        x = np.arange(-10, 11, 1)
        # noise = 0.5
        y = np.ones_like(x) * 0.5
        #  signal + noise = 6
        y[int(x.size/2)-1:int(x.size/2)+2] = 6
        noise_range = np.asarray([-4.2, -8.0, 4.1, 8.4])
        sig_range = np.asarray([-0.9, 0.6])
        noise_bw = 1
        order = 1

        snr = utils.estimate_snr_spectrum(x, y, sig_range, noise_range, 
                                               order=order, noise_bw=noise_bw, 
                                               scaling='lin', fit_lin=False, 
                                               plotting=False)["snr_dB"]
        
        assert_almost_equal(snr, 10.0, decimal=10)
        
        snr = utils.estimate_snr_spectrum(x, y, sig_range, noise_range, 
                                               order=order, noise_bw=noise_bw, 
                                               scaling='lin', fit_lin=True, 
                                               plotting=False)["snr_dB"]
        
        assert_almost_equal(snr, 10.0, decimal=10)

class TestFindLag(unittest.TestCase):
    """
    Test class for find_lag
    """

    def test_correct_estimated_lag(self):
        """
        find correct estimated lag in samples
        """
        rng = np.random.default_rng(seed=1)
        sample_size = int(1000)

        samples_ref = rng.uniform(-1,1,size=sample_size) + 1j*rng.uniform(-1,1,size=sample_size)
        # positive lag
        lag = 11
        samples_lagged = np.roll(samples_ref, shift=lag)
        lag_est = utils.find_lag(samples=samples_lagged, samples_ref=samples_ref, period_length=None, detrend=False, debug=False)['estimated_lag']
        assert_equal(lag_est, lag)
        lag_est = utils.find_lag(samples=samples_lagged, samples_ref=samples_ref, period_length=None, detrend=True, debug=False)['estimated_lag']
        assert_equal(lag_est, lag)
        # negative lag
        lag = -25
        samples_lagged = np.roll(samples_ref, shift=lag)
        lag_est = utils.find_lag(samples=samples_lagged, samples_ref=samples_ref, period_length=None, detrend=False, debug=False)['estimated_lag']
        assert_equal(lag_est, lag)
        lag_est = utils.find_lag(samples=samples_lagged, samples_ref=samples_ref, period_length=None, detrend=True, debug=False)['estimated_lag']
        assert_equal(lag_est, lag)
    
    def test_correct_estimated_lag_with_sequence_length(self):
        """
        find correct estimated lag in samples when considering periodic signals
        """
        
        rng = np.random.default_rng(seed=1)
        sample_size = int(1000)

        samples_ref = rng.uniform(-1,1,size=sample_size) + 1j*rng.uniform(-1,1,size=sample_size)
        samples_ref = np.tile(samples_ref, 3)
        # positive lag
        lag = 1001
        samples_lagged = np.roll(samples_ref, shift=lag)
        lag_est = utils.find_lag(samples=samples_lagged, samples_ref=samples_ref, period_length=sample_size, detrend=False, debug=False)['estimated_lag']
        assert_equal(lag_est, lag-sample_size)
        lag_est = utils.find_lag(samples=samples_lagged, samples_ref=samples_ref, period_length=sample_size, detrend=True, debug=False)['estimated_lag']
        assert_equal(lag_est, lag-sample_size)
        # negative lag
        lag = -1500
        samples_lagged = np.roll(samples_ref, shift=lag)
        lag_est = utils.find_lag(samples=samples_lagged, samples_ref=samples_ref, period_length=sample_size, detrend=False, debug=False)['estimated_lag']
        assert_equal(lag_est, lag+sample_size)
        lag_est = utils.find_lag(samples=samples_lagged, samples_ref=samples_ref, period_length=sample_size, detrend=True, debug=False)['estimated_lag']
        assert_equal(lag_est, lag+sample_size)