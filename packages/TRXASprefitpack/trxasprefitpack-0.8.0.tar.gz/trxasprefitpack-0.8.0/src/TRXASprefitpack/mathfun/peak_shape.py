'''
peak_shape:
submodule for the mathematical functions for
peak shape function

:copyright: 2021-2022 by pistack (Junho Lee).
:license: LGPL3.
'''
from typing import Union, Optional
import numpy as np
from scipy.special import erf, wofz


def edge_gaussian(e: Union[float, np.ndarray], fwhm_G: float) -> np.ndarray:
    '''
    Gaussian type edge function :math:(\\frac{1}{2}\\left(1+{erf}\\left(\\frac{x}{\\sigma\\sqrt{2}}\\right)\\right))

    Args:
     e: energy
     fwhm_G: full width at half maximum

    Returns:
     gaussian type edge shape function
    '''

    return (1+erf(2*np.sqrt(np.log(2))*e/fwhm_G))/2


def edge_lorenzian(e: Union[float, np.ndarray], fwhm_L: float) -> np.ndarray:
    '''
    Lorenzian type edge function :math:(0.5+\\frac{1}{\\pi}{arctan}\\left(\\frac{x}{\\gamma}\\right))

    Args:
     e: energy
     fwhm_L: full width at half maximum

    Returns:
     lorenzian type edge shape function
    '''

    return 0.5+np.arctan(2*e/fwhm_L)/np.pi


def voigt(e: Union[float, np.ndarray], fwhm_G: float, fwhm_L: float) -> Union[float, np.ndarray]:
    '''
    voigt: evaluates voigt profile function with full width at half maximum of gaussian part is fwhm_G and
    full width at half maximum of lorenzian part is fwhm_L

    Args:
     e: energy
     fwhm_G: full width at half maximum of gaussian part :math:`(2\\sqrt{2\\log(2)}\\sigma)`
     fwhm_L: full width at half maximum of lorenzian part :math:`(2\\gamma)`

    Returns:
     voigt profile

    Note:
     * if fwhm_G is (<1e-8) it returns normalized lorenzian shape
     * if fwhm_L is (<1e-8) it returns normalized gaussian shape
    '''
    sigma = fwhm_G/(2*np.sqrt(2*np.log(2)))

    if fwhm_G < 1e-8:
        return fwhm_L/2/np.pi/(e**2+fwhm_L**2/4)

    if fwhm_L < 1e-8:
        return np.exp(-(e/sigma)**2/2)/(sigma*np.sqrt(2*np.pi))

    z = (e+complex(0, fwhm_L/2))/(sigma*np.sqrt(2))
    return wofz(z).real/(sigma*np.sqrt(2*np.pi))


def voigt_thy(e: np.ndarray, thy_peak: np.ndarray,
              fwhm_G: float, fwhm_L: float,
              peak_factor: Union[float, np.ndarray],
              policy: Optional[str] = 'shift') -> np.ndarray:
    '''
    Calculates normalized
    voigt broadened theoretically calculated lineshape spectrum

    Args:
        e: energy
        thy_peak: theoretical calculated peak position and intensity
        fwhm_G: full width at half maximum of gaussian shape
        fwhm_L: full width at half maximum of lorenzian shape
        peak_factor: Peak factor, its behavior depends on policy.
        policy ({'shift', 'scale', 'both'}): Policy to match discrepency
         between experimental data and theoretical spectrum.

         * 'shift' : Default option, shift peak position by peak_factor
         * 'scale' : scale peak position by peak_factor
         * 'both' : both shift and scale peak postition.

         `peak_factor` should be equal to the pair of `shift_factor` and `scale_factor`.

    Returns:
      normalized voigt broadened theoritical lineshape spectrum
    '''

    v_matrix = np.empty((e.size, thy_peak.shape[0]))
    peak_copy = np.copy(thy_peak[:, 0])
    if policy == 'shift':
        peak_copy = peak_copy + peak_factor
    elif policy == 'scale':
        peak_copy = peak_factor*peak_copy
    else:
        peak_copy = peak_factor[1]*peak_copy + peak_factor[0]
    for i in range(peak_copy.size):
        v_matrix[:, i] = voigt(e-peak_copy[i], fwhm_G, fwhm_L)

    broadened_theory = v_matrix @ thy_peak[:, 1].reshape((peak_copy.size, 1))

    return broadened_theory.flatten()


def deriv_edge_gaussian(e: Union[float, np.ndarray], fwhm_G: float) -> np.ndarray:
    '''
    derivative of gaussian type edge

    Args:
     e: energy
     fwhm_G: full width at half maximum

    Returns:
     first derivative of gaussian edge function

    Note:

     * 1st column: df/de
     * 2nd column: df/d(fwhm_G)
    '''
    tmp = np.exp(-4*np.log(2)*(e/fwhm_G)**2)/np.sqrt(np.pi)

    grad_e = 2*np.sqrt(np.log(2))/fwhm_G*tmp
    grad_fwhm_G = -2*np.sqrt(np.log(2))*e/fwhm_G/fwhm_G*tmp

    if isinstance(e, np.ndarray):
        grad = np.empty((e.size, 2))
        grad[:, 0] = grad_e
        grad[:, 1] = grad_fwhm_G
    else:
        grad = np.empty(2)
        grad[0] = grad_e
        grad[1] = grad_fwhm_G

    return grad


def deriv_edge_lorenzian(e: Union[float, np.ndarray], fwhm_L: float) -> np.ndarray:
    '''
    derivative of lorenzian type edge

    Args:
     e: energy
     fwhm_G: full width at half maximum

    Returns:
     first derivative of lorenzian type function

    Note:

     * 1st column: df/de
     * 2nd column: df/d(fwhm_L)
    '''
    tmp = 1/np.pi/(e**2+fwhm_L**2/4)
    grad_e = fwhm_L*tmp/2
    grad_fwhm_L = -e*tmp/2

    if isinstance(e, np.ndarray):
        grad = np.empty((e.size, 2))
        grad[:, 0] = grad_e
        grad[:, 1] = grad_fwhm_L
    else:
        grad = np.empty(2)
        grad[0] = grad_e
        grad[1] = grad_fwhm_L

    return grad


def deriv_voigt(e: Union[float, np.ndarray], fwhm_G: float, fwhm_L: float) -> np.ndarray:
    '''
    deriv_voigt: derivative of voigt profile with respect to (e, fwhm_G, fwhm_L)

    Args:
     e: energy
     fwhm_G: full width at half maximum of gaussian part :math:(2\\sqrt{2\\log(2)}\\sigma)
     fwhm_L: full width at half maximum of lorenzian part :math:(2\\gamma)

    Returns:
     first derivative of voigt profile

    Note:

     * 1st column: df/de
     * 2nd column: df/d(fwhm_G)
     * 3rd column: df/d(fwhm_L)

     if `fwhm_G` is (<1e-8) then,

     * 1st column: dl/de
     * 2nd column: 0
     * 3rd column: dL/d(fwhm_L)

     L means normalized lorenzian shape with full width at half maximum parameter: `fwhm_L`

     if `fwhm_L` is (<1e-8) it returns

     * 1st column: dg/de
     * 2nd column: dg/d(fwhm_G)
     * 3rd column: 0

     g means normalized gaussian shape with full width at half maximum parameter: `fwhm_G`
    '''

    if fwhm_G < 1e-8:
        tmp = fwhm_L/2/np.pi/(e**2+fwhm_L**2/4)**2
        if isinstance(e, np.ndarray):
            grad = np.empty((e.size, 3))
            grad[:, 0] = - 2*e*tmp
            grad[:, 1] = 0
            grad[:, 2] = (1/np.pi/(e**2+fwhm_L**2/4)-fwhm_L*tmp)/2
        else:
            grad = np.empty(3)
            grad[0] = -2*e*tmp
            grad[1] = 0
            grad[2] = (1/np.pi/(e**2+fwhm_L**2/4)-fwhm_L*tmp)/2
        return grad

    sigma = fwhm_G/(2*np.sqrt(2*np.log(2)))
    if fwhm_L < 1e-8:
        tmp = np.exp(-(e/sigma)**2/2)/(sigma*np.sqrt(2*np.pi))
        if isinstance(e, np.ndarray):
            grad = np.empty((e.size, 3))
            grad[:, 0] = -e/sigma**2*tmp
            grad[:, 1] = ((e/sigma)**2-1)/fwhm_G*tmp
            grad[:, 2] = 0
        else:
            grad = np.empty(3)
            grad[0] = -e/sigma**2*tmp
            grad[1] = ((e/sigma)**2-1)/sigma*tmp
            grad[2] = 0
        return grad

    z = (e+complex(0, fwhm_L/2))/(sigma*np.sqrt(2))
    f = wofz(z)/(sigma*np.sqrt(2*np.pi))
    f_z = complex(0, np.sqrt(2)/(np.pi*sigma))-2*z*f
    if isinstance(e, np.ndarray):
        grad = np.empty((e.size, 3))
        grad[:, 0] = f_z.real/(sigma*np.sqrt(2))
        grad[:, 1] = (-f/sigma-z/sigma*f_z).real/(2*np.sqrt(2*np.log(2)))
        grad[:, 2] = -f_z.imag/(2*np.sqrt(2)*sigma)
    else:
        grad = np.empty(3)
        grad[0] = f_z.real/(sigma*np.sqrt(2))
        grad[1] = (-f/sigma-z/sigma*f_z).real/(2*np.sqrt(2*np.log(2)))
        grad[2] = -f_z.imag/(2*np.sqrt(2)*sigma)
    return grad


def deriv_voigt_thy(e: np.ndarray, thy_peak: np.ndarray,
                    fwhm_G: float, fwhm_L: float,
                    peak_factor: Union[float, np.ndarray],
                    policy: Optional[str] = 'shift') -> np.ndarray:
    '''
    Calculates derivative of normalized
    voigt broadened theoretically calculated lineshape spectrum

    Args:
        e: energy
        thy_peak: theoretical calculated peak position and intensity
        fwhm_G: full width at half maximum of gaussian shape
        fwhm_L: full width at half maximum of lorenzian shape
        peak_factor: Peak factor, its behavior depends on policy.
        policy ({'shift', 'scale', 'both'}): Policy to match discrepency
         between experimental data and theoretical spectrum.

         * 'shift' : Default option, shift peak position by peak_factor
         * 'scale' : scale peak position by peak_factor
         * 'both' : both shift and scale peak postition.

         `peak_factor` should be equal to the pair of `shift_factor` and `scale_factor`.

    Returns:
      derivative of normalized voigt broadened theoritical lineshape spectrum

    Note:
     * 1st column: df/d(fwhm_G)
     * 2nd column: df/d(fwhm_L)

     if policy is `shift` or `scale`,

     * 3rd column: df/d(peak_factor)

     if policy is `both`

     * 3rd column: df/d(peak_factor[0]), peak_factor[0]: shift factor
     * 4th column: df/d(peak_factor[1]), peak_factor[1]: scale factor
    '''

    deriv_voigt_tensor = np.empty((e.size, 3, thy_peak.shape[0]))
    peak_copy = np.copy(thy_peak[:, 0])
    if policy == 'shift':
        peak_copy = peak_copy + peak_factor
    elif policy == 'scale':
        peak_copy = peak_factor*peak_copy
    else:
        peak_copy = peak_factor[1]*peak_copy + peak_factor[0]
    for i in range(peak_copy.size):
        deriv_voigt_tensor[:, :, i] = deriv_voigt(
            e-peak_copy[i], fwhm_G, fwhm_L)

    if policy in ['shift', 'scale']:
        grad = np.empty((e.size, 3))
    else:
        grad = np.empty((e.size, 4))

    grad[:, 0] = deriv_voigt_tensor[:, 1, :] @ thy_peak[:, 1]
    grad[:, 1] = deriv_voigt_tensor[:, 2, :] @ thy_peak[:, 1]

    if policy == 'shift':
        grad[:, 2] = -deriv_voigt_tensor[:, 0, :] @ thy_peak[:, 1]
    elif policy == 'scale':
        grad[:, 2] = -deriv_voigt_tensor[:, 0, :] @ \
            (thy_peak[:, 0]*thy_peak[:, 1])
    else:
        grad[:, 2] = -deriv_voigt_tensor[:, 0, :] @ thy_peak[:, 1]
        grad[:, 3] = -deriv_voigt_tensor[:, 0, :] @ \
            (thy_peak[:, 0]*thy_peak[:, 1])

    return grad

def hess_edge_gaussian(e: Union[float, np.ndarray], fwhm_G: float) -> np.ndarray:
    '''
    hessian of gaussian type edge

    Args:
     e: energy
     fwhm_G: full width at half maximum

    Returns:
     hessian of gaussian edge function

    Note:

     * 1st column: d^2f/de^2
     * 2nd column: df/de d(fwhm_G)
     * 3rd column: d^2 f / d(fwhm_G)
    '''

    tmp = 2*np.sqrt(np.log(2))/(fwhm_G*np.sqrt(np.pi))*\
    np.exp(-4*np.log(2)*(e/fwhm_G)**2)

    if isinstance(e, np.ndarray):
        hess = np.empty((e.size, 3))
        hess[:, 0] = -8*np.log(2)/fwhm_G*(e/fwhm_G)*tmp
        hess[:, 1] = (8*np.log(2)*(e/fwhm_G)**2-1)*(tmp/fwhm_G)
        hess[:, 2] = (1-4*np.log(2)*(e/fwhm_G)**2)*(2*e/fwhm_G/fwhm_G*tmp)
    else:
        hess = np.empty(3)
        hess[0] = -8*np.log(2)/fwhm_G*(e/fwhm_G)*tmp
        hess[1] = (8*np.log(2)*(e/fwhm_G)**2-1)*(tmp/fwhm_G)
        hess[2] = (1-4*np.log(2)*(e/fwhm_G)**2)*(2*e/fwhm_G/fwhm_G*tmp)

    return hess


def hess_edge_lorenzian(e: Union[float, np.ndarray], fwhm_L: float) -> np.ndarray:
    '''
    derivative of lorenzian type edge

    Args:
     e: energy
     fwhm_L: full width at half maximum

    Returns:
     hessian of lorenzian type function

    Note:

     * 1st column: d^2f/de^2
     * 2nd column: d^2f/ded(fwhm_L)
     * 3rd column: d^2f/d(fwhm_L)^2
    '''
    fp = fwhm_L/(2*np.pi)/(e**2+(fwhm_L/2)**2)

    if isinstance(e, np.ndarray):
        hess = np.empty((e.size, 3))
        hess[:, 0] = -4*(np.pi/fwhm_L)*e*fp**2
        hess[:, 1] = -(fp+e*hess[:, 0])/fwhm_L
        hess[:, 2] = 2/fwhm_L*(e/fwhm_L)*fp+(e/fwhm_L)**2*hess[:, 0]

    else:
        hess = np.empty((3))
        hess[0] = -4*(np.pi/fwhm_L)*e*fp**2
        hess[1] = -(fp+e*hess[0])/fwhm_L
        hess[2] = 2/fwhm_L*(e/fwhm_L)*fp+(e/fwhm_L)**2*hess[0]

    return hess


def hess_voigt(e: Union[float, np.ndarray], fwhm_G: float, fwhm_L: float) -> np.ndarray:
    '''
    hess_voigt: Hessian of voigt profile with respect to (e, fwhm_G, fwhm_L)

    Args:
     e: energy
     fwhm_G: full width at half maximum of gaussian part :math:(2\\sqrt{2\\log(2)}\\sigma)
     fwhm_L: full width at half maximum of lorenzian part :math:(2\\gamma)

    Returns:
     Hessian derivative of voigt profile

    Note:

     * 1st column: d^2f/de^2
     * 2nd column: d^2f/ded(fwhm_G)
     * 3rd column: d^2f/ded(fwhm_L)
     * 4th column: d^2f/d(fwhm_G)^2
     * 5th column: d^2f/d(fwhm_G)d(fwhm_L)
     * 6th column: d^2f/d(fwhm_L)^2

     if `fwhm_G` is (<1e-8) then, It assume fwhm_G = 0 => lorenzian profile
     if `fwhm_L` is (<1e-8) then, It assume fwhm_L = 0 => gaussian profile
    '''

    if fwhm_G < 1e-8:
        tmp = 1/(e**2+(fwhm_L/2)**2)
        if isinstance(e, np.ndarray):
            hess = np.zeros((e.size, 6))
            hess[:, 0] = (4*e*(e*tmp)-1)*(fwhm_L/np.pi)*tmp*tmp
            hess[:, 2] = -(e*tmp)*((e**2-3*(fwhm_L/2)**2)*tmp*tmp)/np.pi
            hess[:, 5] = (fwhm_L*(fwhm_L**2*tmp)-3*fwhm_L)*tmp*tmp/(4*np.pi)
        else:
            hess = np.zeros(6)
            hess[0] = (4*e*(e*tmp)-1)*(fwhm_L/np.pi)*tmp*tmp
            hess[2] = -(e*tmp)*((e**2-3*(fwhm_L/2)**2)*tmp*tmp)/np.pi
            hess[5] = (fwhm_L*(fwhm_L**2*tmp)-3*fwhm_L)*tmp*tmp/(4*np.pi)
        return hess 

    sigma = fwhm_G/(2*np.sqrt(2*np.log(2)))
    if fwhm_L < 1e-8:
        tmp = np.exp(-(e/sigma)**2/2)/(sigma*np.sqrt(2*np.pi))/sigma/sigma
        if isinstance(e, np.ndarray):
            hess = np.zeros((e.size, 6))
            hess[:, 0] = tmp*((e/sigma)**2-1)
            hess[:, 1] = -tmp*(e/sigma)*((e/sigma)**2-3)/(2*np.sqrt(2*np.log(2)))
            hess[:, 3] = tmp*((e/sigma)**2*((e/sigma)**2-5)+2)/(8*np.log(2))
        else:
            hess = np.zeros(6)
            hess[0] = tmp*((e/sigma)**2-1)
            hess[1] = -tmp*(e/sigma)*((e/sigma)**2-3)/(2*np.sqrt(2*np.log(2)))
            hess[3] = tmp*((e/sigma)**2*((e/sigma)**2-5)+2)/(8*np.log(2))
        return hess 

    z = (e+complex(0, fwhm_L/2))/(sigma*np.sqrt(2))
    f = wofz(z); fp = complex(0, 2/np.sqrt(np.pi))-2*z*f
    fpp = -2*(f+z*fp)
    if isinstance(e, np.ndarray):
        hess = np.empty((e.size, 6))
        hess[:, 0] = fpp.real/(2*np.sqrt(2*np.pi)*sigma**3)
        hess[:, 1] = -(fp+z*fpp/2).real/(np.sqrt(np.pi)*sigma**3)/(2*np.sqrt(2*np.log(2)))
        hess[:, 2] = -fpp.imag/(2*np.sqrt(2*np.pi)*sigma**3)/2
        hess[:, 3] = (2*f+4*z*fp+z*(z*fpp)).real/(np.sqrt(2*np.pi)*sigma**3)/(8*np.log(2))
        hess[:, 4] = (fp+z*fpp/2).imag/(np.sqrt(np.pi)*sigma**3)/(4*np.sqrt(2*np.log(2)))
        hess[:, 5] = -hess[:, 0]/4
    else:
        hess = np.empty(6)
        hess[0] = fpp.real/(2*np.sqrt(2*np.pi)*sigma**3)
        hess[1] = -(fp+z*fpp/2).real/(np.sqrt(np.pi)*sigma**3)/(2*np.sqrt(2*np.log(2)))
        hess[2] = -fpp.imag/(2*np.sqrt(2*np.pi)*sigma**3)/2
        hess[3] = (2*f+4*z*fp+z*(z*fpp)).real/(np.sqrt(2*np.pi)*sigma**3)/(8*np.log(2))
        hess[4] = (fp+z*fpp/2).imag/(np.sqrt(np.pi)*sigma**3)/(4*np.sqrt(2*np.log(2)))
        hess[5] = -hess[0]/4
    return hess 