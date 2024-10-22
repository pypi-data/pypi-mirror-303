from setuptools import setup, find_packages

VERSION = '1.23' 
DESCRIPTION = 'Python3 package drawing orbits and shadows of Kerr--Newman--(anti) de Sitter black holes'
with open("README.md", "r") as fh: 
    LONG_DESCRIPTION = fh.read() 

###'This is a package for Python 3.10, loaded with Opencv 4.10 and Imageio 2.36, to compute and draw (animated) shadows of a KNdS black hole (i.e. a charged rotating black hole inside a cosmological universe), possibly equipped with a thin Keplerian accretion disk, radiating as a blackbody. This code also allows to draw (massive or null) orbits in a KNdS space-time, using different integration methods of the geodesic equation.'

# Setting up
setup(
        name="knds_orbits_and_shadows", 
        version=VERSION,
        author="Arthur Garnier",
        author_email="<arthur.garnier@math.cnrs.fr>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license_files={'LICENSE.txt'},
        packages=find_packages(),
        install_requires=['opencv-python','imageio'],
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
