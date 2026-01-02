import warnings

warnings.warn(
    "shade-privacy is deprecated and has been renamed to veil-privacy. "
    "Please install and use 'veil-privacy' instead.",
    DeprecationWarning,
    stacklevel=2
)

# Keep original imports if you want
from .original_module import *
