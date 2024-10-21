# pylint: disable = missing-module-docstring, wrong-import-position, invalid-name
import os
import sys
import numpy as np

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path+'/../src/')

from TRXASprefitpack import solve_seq_model, solve_l_model


def test_solve_seq_1():
    tau1 = 1
    tau2 = 10
    A = np.array([[-1/tau1, 0, 0],
    [1/tau1, -1/tau2, 0],
    [0, 1/tau2, 0]])
    eigval_ref = np.array([-1/tau1, -1/tau2, 0])
    y0 = np.array([1, 0, 0])
    eigval_tst, V_tst, c_tst = solve_seq_model(np.array([tau1, tau2]), y0)
    lV_tst = np.einsum('j,ij->ij', eigval_ref, V_tst)

    assert np.allclose(eigval_ref, eigval_tst)
    assert np.allclose(V_tst@c_tst, y0)
    assert np.allclose(A@V_tst, lV_tst)

def test_solve_seq_2():
    tau1 = 1
    tau2 = 10
    tau3 = 100
    A = np.array([[-1/tau1, 0, 0, 0],
    [1/tau1, -1/tau2, 0, 0],
    [0, 1/tau2, -1/tau3, 0],
    [0, 0, 1/tau3, 0]])
    eigval_ref = np.array([-1/tau1, -1/tau2, -1/tau3, 0])
    y0 = np.array([0.6, 0.1, 0.25, 0.05])
    eigval_tst, V_tst, c_tst = solve_seq_model(np.array([tau1, tau2, tau3]), y0)
    lV_tst = np.einsum('j,ij->ij', eigval_ref, V_tst)

    assert np.allclose(eigval_ref, eigval_tst)
    assert np.allclose(V_tst@c_tst, y0)
    assert np.allclose(A@V_tst, lV_tst)

def test_solve_l_1():
    tau1 = 1
    tau2 = 0.5
    A = np.array([[-(1/tau1+1/tau2), 0, 0],
    [1/tau1, 0, 0],
    [1/tau2, 0, 0]])
    eigval_ref = np.array([-(1/tau1+1/tau2), 0, 0])
    y0 = np.array([0.5, 0.3, 0.2])
    eigval_tst, V_tst, c_tst = solve_l_model(A, y0)
    lV_tst = np.einsum('j,ij->ij', eigval_ref, V_tst)

    assert np.allclose(eigval_ref, eigval_tst)
    assert np.allclose(V_tst@c_tst, y0)
    assert np.allclose(A@V_tst, lV_tst)

def test_solve_l_2():
    tau1 = 1
    tau2 = 0.5
    A = np.array([[-1/tau1, 0, 0, 0],
    [1/tau1, 0, 0, 0],
    [0, 0, -1/tau2, 0],
    [0, 0, 1/tau2, 0]])
    eigval_ref = np.array([-1/tau1, 0, -1/tau2, 0])
    y0 = np.array([0.5, 0, 0.5, 0])
    eigval_tst, V_tst, c_tst = solve_l_model(A, y0)
    lV_tst = np.einsum('j,ij->ij', eigval_ref, V_tst)

    assert np.allclose(eigval_ref, eigval_tst)
    assert np.allclose(V_tst@c_tst, y0)
    assert np.allclose(A@V_tst, lV_tst)

def test_solve_l_3():
    tau1 = 1
    tau2 = 0.5
    tau3 = 250
    A = np.array([[-(1/tau1+1/tau2), 0, 0],
    [1/tau1, 0, 0],
    [1/tau3, 0, -1/tau3]])
    eigval_ref = np.array([-(1/tau1+1/tau2), 0, -1/tau3])
    y0 = np.array([0.6, 0.3, 0.1])
    eigval_tst, V_tst, c_tst = solve_l_model(A, y0)
    lV_tst = np.einsum('j,ij->ij', eigval_ref, V_tst)

    assert np.allclose(eigval_ref, eigval_tst)
    assert np.allclose(V_tst@c_tst, y0)
    assert np.allclose(A@V_tst, lV_tst)

def test_solve_l_4():
    tau1 = 1
    tau2 = 0.5
    tau3 = 250
    tau4 = 500

    A = np.array([[-(1/tau1+1/tau2), 0, 0],
    [1/tau1, -1/tau3, 0],
    [1/tau2, 0, -1/tau4]])
    eigval_ref = np.array([-(1/tau1+1/tau2), -1/tau3, -1/tau4])
    y0 = np.array([0.6, 0.3, 0.1])
    eigval_tst, V_tst, c_tst = solve_l_model(A, y0)
    lV_tst = np.einsum('j,ij->ij', eigval_ref, V_tst)

    assert np.allclose(eigval_ref, eigval_tst)
    assert np.allclose(V_tst@c_tst, y0)
    assert np.allclose(A@V_tst, lV_tst)




