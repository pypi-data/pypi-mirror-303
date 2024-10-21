# pylint: disable = missing-module-docstring, wrong-import-position, invalid-name
import os
import sys
import numpy as np
from scipy.signal import convolve

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path+'/../src/')

from TRXASprefitpack import dmp_osc_conv_pvoigt, dmp_osc_conv_gau, dmp_osc_conv_cauchy
from TRXASprefitpack import voigt
from TRXASprefitpack import gau_irf, cauchy_irf
from TRXASprefitpack import calc_fwhm
from TRXASprefitpack import calc_eta


def dmp_osc(t, k, T, phi):
    return np.exp(-k*t)*np.cos(2*np.pi/T*t+phi)*np.heaviside(t, 1)


def test_dmp_osc_conv_gau():
    fwhm_G = 0.15
    tau = 0.5
    T = 0.3
    phi = np.pi/3
    N_ref = 50000
    N_sample = 100
    t = np.linspace(-2, 2, N_ref)
    t_sample = np.linspace(-1, 1, N_sample)
    sample_idx = np.searchsorted(t, t_sample)
    gau_ref = gau_irf(t, fwhm_G)
    dmp_osc_ref = dmp_osc(t, 1/tau, T, phi)
    ref = convolve(gau_ref, dmp_osc_ref, mode='same')*4/N_ref
    tst = dmp_osc_conv_gau(t_sample, fwhm_G, 1/tau, T, phi)
    max_rel_err = np.max(np.abs(ref[sample_idx]-tst))/np.max(ref)
    assert max_rel_err < 1e-3


def test_dmp_osc_conv_cauchy():
    fwhm_L = 0.15
    tau = 0.5
    T = 0.3
    phi = np.pi/3
    N_ref = 500000
    N_sample = 100
    t = np.linspace(-2, 2, N_ref)
    t_sample = np.linspace(-1, 1, N_sample)
    sample_idx = np.searchsorted(t, t_sample)
    cauchy_ref = cauchy_irf(t, fwhm_L)
    dmp_osc_ref = dmp_osc(t, 1/tau, T, phi)
    ref = convolve(cauchy_ref, dmp_osc_ref, mode='same')*4/N_ref
    tst = dmp_osc_conv_cauchy(t_sample, fwhm_L, 1/tau, T, phi)
    max_rel_err = np.max(np.abs(ref[sample_idx]-tst))/np.max(ref)
    assert max_rel_err < 1e-3


def test_dmp_osc_conv_pvoigt():
    fwhm_L = 0.05
    fwhm_G = 0.15
    tau = 0.5
    T = 0.3
    phi = np.pi/3
    fwhm = calc_fwhm(fwhm_G, fwhm_L)
    eta = calc_eta(fwhm_G, fwhm_L)
    N_ref = 5000
    N_sample = 100
    t = np.linspace(-2, 2, N_ref)
    t_sample = np.linspace(-1, 1, N_sample)
    sample_idx = np.searchsorted(t, t_sample)
    voigt_ref = voigt(t, fwhm_G, fwhm_L)
    dmp_osc_ref = dmp_osc(t, 1/tau, T, phi)
    ref = convolve(voigt_ref, dmp_osc_ref, mode='same')*4/N_ref
    tst = dmp_osc_conv_pvoigt(t_sample, fwhm, eta, 1/tau, T, phi)
    max_rel_err = np.max(np.abs(ref[sample_idx]-tst))/np.max(ref)
    assert max_rel_err < 2e-2
