'''
res:
subpackage for resdiual function for
fitting time delay scan data or static spectrum data

:copyright: 2021-2022 by pistack (Junho Lee).
:license: LGPL3.
'''
from .parm_bound import set_bound_t0, set_bound_tau
from .parm_bound import set_bound_e0
from .res_decay import residual_decay, res_grad_decay, res_hess_decay
from .res_decay import residual_decay_same_t0, res_grad_decay_same_t0
from .res_decay import res_hess_decay_same_t0
from .res_raise import residual_raise, res_grad_raise, res_hess_raise
from .res_raise import residual_raise_same_t0, res_grad_raise_same_t0
from .res_raise import res_hess_raise_same_t0 
from .res_osc import residual_dmp_osc, res_grad_dmp_osc
from .res_osc import residual_dmp_osc_same_t0, res_grad_dmp_osc_same_t0
from .res_both import residual_both, res_grad_both
from .res_both import residual_both_same_t0, res_grad_both_same_t0
from .res_voigt import residual_voigt, res_grad_voigt, res_hess_voigt
from .res_thy import residual_thy, res_grad_thy

__all__ = ['set_bound_t0', 'set_bound_tau',
           'set_bound_e0',
           'residual_decay', 'res_grad_decay', 'res_hess_decay',
           'residual_raise', 'res_grad_raise', 'res_hess_raise',
           'residual_dmp_osc', 'res_grad_dmp_osc',
           'residual_both', 'res_grad_both',
           'residual_decay_same_t0', 'res_grad_decay_same_t0',
           'res_hess_decay_same_t0',
           'residual_raise_same_t0', 'res_grad_raise_same_t0',
           'res_hess_raise_same_t0',
           'residual_dmp_osc_same_t0', 'res_grad_dmp_osc_same_t0',
           'residual_both_same_t0', 'res_grad_both_same_t0',
           'residual_voigt', 'res_grad_voigt', 'res_hess_voigt',
           'residual_thy', 'res_grad_thy']
