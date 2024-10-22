from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [
    Extension("skcomm.cython_mods.rx_cython", ["src/skcomm/cython_mods/rx_cython.pyx"])]

try:
    setup(name="scikit-comm",    
        ext_modules=cythonize(extensions, annotate=True, language_level = "3"),
        zip_safe=False,
    )
except:
    setup(name="scikit-comm"
    )
