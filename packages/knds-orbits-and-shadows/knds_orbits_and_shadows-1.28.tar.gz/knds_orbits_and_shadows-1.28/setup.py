from setuptools import setup, find_packages

VERSION = '1.28' 
DESCRIPTION = 'Python3 package drawing orbits and shadows of Kerr--Newman--(anti) de Sitter black holes'
with open("README.md", "r") as fh: 
    LONG_DESCRIPTION = fh.read() 

setup(
        name="knds_orbits_and_shadows", 
        version=VERSION,
        author="Arthur Garnier",
        author_email="<arthur.garnier@math.cnrs.fr>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license_files={'LICENSE.txt'},
        python_requires='>=3.10',
        packages=find_packages(),
        install_requires=['opencv-python>=4.10','imageio>=2.36'],
        url='https://github.com/arthur-garnier/knds_orbits_and_shadows-python',

        keywords=['python', 'knds', 'kerr', 'kerr-newman', 'deSitter', 'cosmology', 'black hole', 'orbit', 'black hole shadowing', 'accretion disk', 'backward ray-tracing', 'gif'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ],
)
