from distutils.core import setup, Extension
from Cython.Build import cythonize
import sys
import numpy
import os

sys.argv = ['setup.py', 'build_ext', '--inplace']


conda_base = os.getenv('CONDA_PREFIX')
lib_path = os.path.join(conda_base, 'lib')
rdkit_include_path = os.path.join(conda_base, 'include', 'rdkit')


# Define the Cython extension
extensions = [
    Extension(
        name="bitset_block_range",
        sources=["bitset_block_range.pyx"],  # Replace with your actual Cython file name
        extra_compile_args=[
            '-O3',
            '-fopenmp',
        ],
        extra_link_args=[
            '-fopenmp'
        ],
        include_dirs=[
            numpy.get_include(),
            rdkit_include_path,
            # boost_include,
        ],
        library_dirs=[
            lib_path,
        ],
        libraries=[
            "RDKitRDGeneral",
            "RDKitDataStructs",
            # "boost_numpy310",
            "boost_python310",
        ],
        language="c++",
    ),
]

# Setup
setup(
    name="bitset_block_range",
    ext_modules=cythonize(extensions, language_level = "3str"),
)

from bitset_block_range import *

check_unsigned_long_size()
test_bitvec_to_numpy()
test_bitvec_arr_to_numpy()
benchmark_bitvec_arr_to_numpy()