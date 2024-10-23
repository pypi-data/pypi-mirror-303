import numpy as np
import os

def import_mirror_sep(path, number_of_bands):
    t = np.arange(0,number_of_bands,1)
    p = np.poly1d(np.load(path))
    mirror_sep = p(t)
    if np.max(mirror_sep) > 100e-6:
        mirror_sep = mirror_sep*1e-6
    return mirror_sep
