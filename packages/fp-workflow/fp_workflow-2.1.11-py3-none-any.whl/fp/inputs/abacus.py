#region: Modules.
from fp.schedulers.scheduler import JobProcDesc
from typing import List, Sequence
import numpy as np 
#endregion

#region: Variables.
#endregion

#region: Functions.
#endregion

#region: Classes.
class AbacusInput:
    def __init__(
        self,
        calculation: str,
        ecut:float,
        kdim: Sequence[int], 
        job_desc: JobProcDesc,
        basis_type: str='lcao',
        extra_args: str=None,
    ):
        self.calculation: str = calculation
        self.ecut: float = ecut
        self.kdim: np.ndarray = np.array(kdim, dtype='i4')
        self.job_desc: JobProcDesc = job_desc
        self.basis_type: str = basis_type
        self.extra_args: str = extra_args
        
#endregion
