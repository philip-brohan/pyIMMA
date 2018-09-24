"""Setup configuration for python IMMA package.

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open  # 2.7 only
import glob

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='IMMA',
    version='0.0.3',
    description='Python API for IMMA records',

    # From README - see above
    long_description=long_description,
    #long_description_content_type='text/x-rst',

    url='https://brohan.org/pyIMMA/',

    author='Philip Brohan',
    author_email='philip.brohan@metofice.gov.uk',

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
    ],

    # Keywords for your project. What does your project relate to?
    keywords='IMMA ICOADS',

    # Automatically find the software to be included
    packages=find_packages(),

    # Tests are in Meteorographica/tests organised as a module
    # (a unittest.TestSuite - just put __init__.py in all directories).
    # Name the module not the file here ('.' not '/').
    #test_suite="IMMA.tests",

    # Other packages that your project depends on.
    install_requires=[
        'numpy>1.13',
        'scipy>0.18',
        'pandas>0.20',
    ],

    # Data files for the examples
    #data_files=[('example_data',(glob.glob('examples/data/*.imma') +
    #                             glob.glob('examples/data/*.pklz')))]

)
