# pylint: disable = missing-module-docstring,wrong-import-position,invalid-name,multiple-statements
import os
import sys
import numpy as np

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path+'/../src/')

from TRXASprefitpack import calc_eta, calc_fwhm
from TRXASprefitpack import solve_seq_model, rate_eq_conv
from TRXASprefitpack import fit_transient_raise
from TRXASprefitpack import save_TransientResult, load_TransientResult

def test_driver_transient_raise_3():
    tau_1 = 0.2
    tau_2 = 2
    tau_3 = 10
    fwhm_G = 0.100
    fwhm_L = 0.05
    fwhm = calc_fwhm(fwhm_G, fwhm_L)
    eta = calc_eta(fwhm_G, fwhm_L)
    # initial condition
    y0 = np.array([1, 0, 0, 0])

    # set time range (mixed step)
    t_seq1 = np.arange(-2, -1, 0.2)
    t_seq2 = np.arange(-1, 2, 0.02)
    t_seq3 = np.arange(2, 5, 0.2)
    t_seq4 = np.arange(5, 10, 1)
    t_seq5 = np.arange(10, 100, 10)
    t_seq6 = np.arange(100, 1000, 100)
    t_seq7 = np.linspace(1000, 5000, 5)

    t_seq = np.hstack((t_seq1, t_seq2, t_seq3, t_seq4, t_seq5, t_seq6, t_seq7))
    eigval_seq, V_seq, c_seq = solve_seq_model(np.array([tau_1, tau_2, tau_3]), y0)

    # Now generates measured transient signal
    # Last element is ground state
    abs_1 = [0, 1, 1, 0.2]
    abs_2 = [0, 0.8, 0.2, -0.05]
    abs_3 = [0, 0.7, 0.9, 0.03]
    abs_4 = [0, 0.3, -1, 0.25]

    t0 = np.random.uniform(-0.2, 0.2, 4) # perturb time zero of each scan

    # generate measured data
    y_obs_1 = rate_eq_conv(t_seq-t0[0], fwhm, abs_1, eigval_seq, V_seq, c_seq, 
    irf='pv', eta=eta)
    y_obs_2 = rate_eq_conv(t_seq-t0[1], fwhm, abs_2, eigval_seq, V_seq, c_seq, 
    irf='pv', eta=eta)
    y_obs_3 = rate_eq_conv(t_seq-t0[2], fwhm, abs_3, eigval_seq, V_seq, c_seq, 
    irf='pv', eta=eta)
    y_obs_4 = rate_eq_conv(t_seq-t0[3], fwhm, abs_4, eigval_seq, V_seq, c_seq, 
    irf='pv', eta=eta)

    eps_obs_1 = np.ones_like(y_obs_1)/1000
    eps_obs_2 = np.ones_like(y_obs_2)/1000
    eps_obs_3 = np.ones_like(y_obs_3)/1000
    eps_obs_4 = np.ones_like(y_obs_4)/1000

    # generate measured intensity
    i_obs_1 = y_obs_1
    i_obs_2 = y_obs_2
    i_obs_3 = y_obs_3
    i_obs_4 = y_obs_4

    t = [t_seq]
    intensity = [np.vstack((i_obs_1, i_obs_2, i_obs_3, i_obs_4)).T]
    eps = [np.vstack((eps_obs_1, eps_obs_2, eps_obs_3, eps_obs_4)).T]

    ans = np.array([fwhm_G, fwhm_L, t0[0], t0[1], t0[2], t0[3],
    tau_1, tau_2, tau_3])

    bound_fwhm = [(0.05, 0.2), (0.025, 0.1)]
    bound_t0 = [(-0.4, 0.4), (-0.4, 0.4), (-0.4, 0.4), (-0.4, 0.4)]
    bound_tau = [(0.1, 1), (1, 5), (5, 100)]
    fwhm_init = np.array([np.random.uniform(0.05, 0.2),
    np.random.uniform(0.025, 0.1)])
    t0_init = np.random.uniform(-0.4, 0.4, 4)
    tau_init = np.array([np.random.uniform(0.1, 1),
    np.random.uniform(1, 5), np.random.uniform(5, 100)])


    result_ampgo = fit_transient_raise('pv', fwhm_init, t0_init, tau_init, True,
    method_glb='ampgo', bound_fwhm=bound_fwhm, bound_t0=bound_t0, bound_tau=bound_tau,
    t=t, intensity=intensity, eps=eps)

    save_TransientResult(result_ampgo, 'test_driver_transient_raise_3')
    load_result_ampgo = load_TransientResult('test_driver_transient_raise_3')
    os.remove('test_driver_transient_raise_3.h5')

    assert np.allclose(result_ampgo['x'], ans)
    assert str(result_ampgo) == str(load_result_ampgo)

if __name__ == '__main__':
    test_driver_transient_raise_3()


