from .wheeltools import InWheelCtx
from .condatools import InCondaPkgCtx


def InGenericPkgCtx(in_path, out_path=None):    
    if in_path.endswith('.whl'):
        return InWheelCtx(in_path, out_path)
    if in_path.endswith('.tar.bz2'):
        if out_path is not None:
            raise NotImplementedError()
        return InCondaPkgCtx(in_path)

    raise ValueError(in_path)
