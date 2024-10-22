from scipy._lib._array_api import array_namespace as array_namespace
from scipy._typing import Untyped

def dctn(
    x: Untyped,
    type: int = 2,
    s: Untyped | None = None,
    axes: Untyped | None = None,
    norm: Untyped | None = None,
    overwrite_x: bool = False,
    workers: Untyped | None = None,
    *,
    orthogonalize: Untyped | None = None,
) -> Untyped: ...
def idctn(
    x: Untyped,
    type: int = 2,
    s: Untyped | None = None,
    axes: Untyped | None = None,
    norm: Untyped | None = None,
    overwrite_x: bool = False,
    workers: Untyped | None = None,
    *,
    orthogonalize: Untyped | None = None,
) -> Untyped: ...
def dstn(
    x: Untyped,
    type: int = 2,
    s: Untyped | None = None,
    axes: Untyped | None = None,
    norm: Untyped | None = None,
    overwrite_x: bool = False,
    workers: Untyped | None = None,
    orthogonalize: Untyped | None = None,
) -> Untyped: ...
def idstn(
    x: Untyped,
    type: int = 2,
    s: Untyped | None = None,
    axes: Untyped | None = None,
    norm: Untyped | None = None,
    overwrite_x: bool = False,
    workers: Untyped | None = None,
    *,
    orthogonalize: Untyped | None = None,
) -> Untyped: ...
def dct(
    x: Untyped,
    type: int = 2,
    n: Untyped | None = None,
    axis: int = -1,
    norm: Untyped | None = None,
    overwrite_x: bool = False,
    workers: Untyped | None = None,
    orthogonalize: Untyped | None = None,
) -> Untyped: ...
def idct(
    x: Untyped,
    type: int = 2,
    n: Untyped | None = None,
    axis: int = -1,
    norm: Untyped | None = None,
    overwrite_x: bool = False,
    workers: Untyped | None = None,
    orthogonalize: Untyped | None = None,
) -> Untyped: ...
def dst(
    x: Untyped,
    type: int = 2,
    n: Untyped | None = None,
    axis: int = -1,
    norm: Untyped | None = None,
    overwrite_x: bool = False,
    workers: Untyped | None = None,
    orthogonalize: Untyped | None = None,
) -> Untyped: ...
def idst(
    x: Untyped,
    type: int = 2,
    n: Untyped | None = None,
    axis: int = -1,
    norm: Untyped | None = None,
    overwrite_x: bool = False,
    workers: Untyped | None = None,
    orthogonalize: Untyped | None = None,
) -> Untyped: ...
