from typing import Union
import numpy as np
from scipy.optimize import minimize_scalar
import numpy.typing as npt 

def P0_P(M:Union[npt.NDArray,float],gamma:float=1.4) -> float:
    """Computes the ratio P0/Ps

    Args:
        M (Union[npt.NDArray,float]): Mach Number
        gamma (float): specific heat ratio. Defaults to 1.4

    Returns:
        float: P0/P ratio 
    """
    return np.power((1+(gamma-1)/2.0 * M*M),gamma/(gamma-1))


def FindMachP0P(P0_P:npt.NDArray,gamma:float=1.4) -> float:
    """Finds the mach number given a P0/P ratio

    Args:
        P0_P (Union[npt.NDArray,float]): ratio of total to static pressure
        gamma (float): specific heat ratio. Defaults to 1.4

    Returns:
        float: [description]
    """
    n = (gamma-1)/gamma
    c = 2.0/(gamma-1) * (np.power(P0_P,n) - 1.0)

    M = np.sqrt(c)
    return M # Subsonic and supersonic solution
    


def T0_T(M:npt.NDArray,gamma:float=1.4) -> float:
    """Computes T0/Ts

    Args:
        M (Union[npt.NDArray,float]): _description_
        gamma (float): specific heat ratio. Defaults to 1.4

    Returns:
        float: Ratio of T0/Ts
    """
    return (1.0+(gamma-1.0)/2.0 *M*M)


def A_As(M:npt.NDArray,gamma:float=1.4) -> float:
    """Computes the ratio of Area to Throat Area give a given mach number and gamma 

    Args:
        M (Union[npt.NDArray,float]): Mach Number
        gamma (float): specific heat ratio. Defaults to 1.4

    Returns:
        float: Area to throat area ratio 
    """
    a = (gamma+1.0)/(2.0*(gamma-1.0))
    temp1 = np.power((gamma+1.0)/2.0,-a)
    temp2 = np.power((1+(gamma-1)/2*M*M),a)/M
    return temp1*temp2

def findMachAAs(AAs:float,gamma:float=1.4,IsSupersonic:bool=True) -> float:
    def func(M,gamma):
        return abs(A_As(M,gamma) - AAs)
    
    if IsSupersonic:
        res = minimize_scalar(func,bounds=[1.01,6],args=(gamma))
    else:
        res = minimize_scalar(func,bounds=[0.05,0.99],args=(gamma))
    return res.x 

def Massflow(P0:float,T0:float,A:float,M:float,gamma:float=1.4,R:float=287):
    """Massflow rate calculation
    
    Args:
        P0 (float): Inlet Total Pressure (Pa)
        T0 (float): Inlet Total Temperature (K)
        A (float): Area (m^2)
        M (float): Mach Number 
        gamma (float): specific heat ratio. Defaults to 1.4
        R (float): Ideal Gas Constant. Defaults to 287 J/(KgK).

    Returns:
        float: Nusselt Number
    """
    mdot = A * P0/np.sqrt(T0) * np.sqrt(gamma/R) * M \
        *np.power(1.0+(gamma-1.0)/2.0 * M*M, -(gamma+1.0)/(2.0*(gamma-1.0)))
    
    return mdot