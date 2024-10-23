from typing import Union
import numpy.typing as npt
import numpy as np 

def M2(M1:Union[float,npt.NDArray],gam:float=1.4) -> Union[float,npt.NDArray]:
    """Returns the mach number after the shock 

    Args:
        M1 (Union[float,npt.NDArray]): Mach before shock
        gam (float, optional): cp/cv. Defaults to 1.4.

    Returns:
        Union[float,npt.NDArray]: mach after the shock
    """
    return np.sqrt(((gam-1)*M1**2+2) / (2*gam*M1**2-(gam-1)))

def P2_P1(M1:Union[float,npt.NDArray],gam:float=1.4) -> Union[float,npt.NDArray]:
    """Returns the ratio of P2/P1

    Args:
        M1 (Union[float,npt.NDArray][float,npt.NDArray]): Mach 1 before shock
        gam (float, optional): cp/cv. Defaults to 1.4.

    Returns:
        Union[float,npt.NDArray]: ratio of P2/P1
    """
    return 1+2*gam/(gam+1)*(M1**2-1)

def rho2_rho1(M1:Union[float,npt.NDArray],gam:float=1.4) -> Union[float,npt.NDArray]:
    """Returns ratio of density rho2/rho1 which is same as u2/u1

    Args:
        M1 (Union[float,npt.NDArray]): mach number before shock 
        gam (float, optional): cp/cv. Defaults to 1.4.

    Returns:
        Union[float,npt.NDArray]: Returns ratio of density rho2/rho1
    """
    return (gam+1)*M1**2 / (2+(gam-1)*M1**2) 

def T2_T1(M1:Union[float,npt.NDArray],gam:float=1.4) -> Union[float,npt.NDArray]:
    """Returns ratio of T2/T1 

    Args:
        M1 (Union[float,npt.NDArray]): mach number before shock 
        gam (float, optional): cp/cv. Defaults to 1.4.

    Returns:
        Union[float,npt.NDArray]: Returns ratio of T2/T1 
    """
    return (1+2*gam/(gam+1)*(M1**2-1)) * (2+(gam-1)*M1**2)/((gam+1)*M1**2)

def P02_P01(M1:Union[float,npt.NDArray],gam:float=1.4) -> Union[float,npt.NDArray]:
    """Returns the ratio of total pressure after a shock 

    Args:
        M1 (Union[float,npt.NDArray]): Mach number before shock 
        gam (float, optional): Ratio of specific heats. Defaults to 1.4.

    Returns:
        Union[float,npt.NDArray]: ratio of P02/P01 where P02 is after shock, P01 is
    """
    a = (gam+1)*M1**2 / ((gam-1)*M1**2+2)
    b = (gam+1)/(2*gam*M1**2-(gam-1))
    return a ** (gam/(gam-1)) * b**(1/(gam-1))
if __name__ == "__main__":
    from isentropic import T0_T
    
    P2 = P2_P1(3,1.4)
    print(f"P2 = {P2:0.3f}")
    
    mach2 = M2(3,1.4)
    print(f"M2 = {mach2:0.3f}")
    
    T0_T = T0_T(3,1.4)
    print(f"T0_T = {T0_T:0.3f}")
    
    T2 = 288*T2_T1(3,1.4)
    print(f"T2 = {T2:0.3f}")
  