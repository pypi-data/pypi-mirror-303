import os
import types
from typing import cast
import importlib


def import_submodule(mod: types.ModuleType):
    for filename in sorted(os.listdir(os.path.dirname(cast(str, mod.__file__)))):
        if filename.endswith(".py") and filename[0] != "_":
            importlib.import_module(f"{mod.__name__}.{filename[:-3]}")
        elif filename.endswith(".so"):
            importlib.import_module(f"{mod.__name__}.{filename.split('.')[0]}")
