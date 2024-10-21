import os
import os as _os
import os.path as _path
from importlib import import_module as _import_module
from types import ModuleType as _ModuleType

from mavro.parser.lens import LensParser as _LensParser


def public__findService(module: str) -> _ModuleType:
    if not _path.exists(module):
        raise ImportError(f"Mavro module '{module}' not found in '{_os.getcwd()}'")
    from ..internal.build import build
    build(
        path=module,
        dist_path=module.removesuffix(".mav") + ".py",
        no_delete=True,
        line_loader=_LensParser.stdLoadLinesWithoutEntrypoint
    )
    module_literal: _ModuleType = _import_module(module.removesuffix(".mav"))
    os.remove(module.removesuffix(".mav") + ".py")
    return module_literal