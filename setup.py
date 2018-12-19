"""
Installation file for python vtki module
"""
from setuptools import setup
from io import open as io_open
import os
import sys
import warnings

package_name = 'vtki'

__version__ = None
filepath = os.path.dirname(__file__)
version_file = os.path.join(filepath, package_name, '_version.py')
with io_open(version_file, mode='r') as fd:
    exec(fd.read())

# pre-compiled vtk available for python3
install_requires = ['numpy',
                    'imageio']

# add vtk if not windows and 2.7
if os.name == 'nt' and int(sys.version[0]) < 3:
    warnings.warn('Will need to install VTK manually')
elif os.environ.get('READTHEDOCS') == 'True':
    # don't install for readthedocs
    pass
else:
    install_requires.append(['vtk'])


readme_file = os.path.join(filepath, 'README.rst')

setup(
    name=package_name,
    packages=[package_name, 'vtki.examples'],
    version=__version__,
    description='Easier Pythonic interface to VTK',
    long_description=open(readme_file).read(),
    author='Alex Kaszynski',
    author_email='akascap@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    url='https://github.com/akaszynski/vtki',
    keywords='vtk numpy plotting mesh',
    package_data={'vtki.examples': ['airplane.ply', 'ant.ply',
                                    'hexbeam.vtk', 'sphere.ply',
                                    'uniform.vtk', 'rectilinear.vtk']},
    install_requires=install_requires,
)
