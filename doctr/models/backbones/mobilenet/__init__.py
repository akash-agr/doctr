from doctr import is_tf_available

if is_tf_available():
    from .tensorflow import *
