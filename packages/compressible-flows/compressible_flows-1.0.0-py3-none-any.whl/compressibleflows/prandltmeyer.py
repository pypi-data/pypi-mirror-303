from typing import Tuple
import numpy.typing as npt
import numpy as np 
from scipy.optimize import minimize_scalar

def prandlt(M:Tuple[float,npt.NDArray], gam:float=1.4):
    """Prandlt Meyer Angle

    Args:
        M (Tuple[float,npt.NDArray]): Incoming mach number
        gam (float): ratio of specific heats. Defaults to 1.4

    Returns:
        Tuple containing
        float or NDArray: Prandlt Meyer Angle, mach angle
        
    """
    nu = np.sqrt((gam+1)/(gam-1)) * np.atan(np.sqrt((gam-1)/(gam+1)*(M**2-1))) - np.atan(np.sqrt(M**2-1))
    mu = np.asin(1/M)
    return np.degrees(nu),mu
    
def prandltM(nu:float,gam:float=1.4) -> float :
    """Get the mach number from prandlt meyer expansion

    Args:
        nu (float): Incoming mach number
        gam (float): ratio of specific heats. Defaults to 1.4
    
    Returns:
        (float): Mach number
    """
    
    assert "Prandlt Meyer angle Nu has to be smaller than pi/2*(sqrt((gamma+1)/(gamma-1))-1)",nu>np.pi/2*(np.sqrt((gam+1)/(gam-1))-1) 
    
    # Solve for prandlt meyer angle
    def pr(M):
        return abs(prandlt(M,gam)[0] - nu)
    res = minimize_scalar(pr,bounds = [1.05,6])
    return res.x 