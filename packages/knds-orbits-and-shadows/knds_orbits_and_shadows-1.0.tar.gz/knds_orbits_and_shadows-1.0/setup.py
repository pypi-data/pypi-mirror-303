from setuptools import setup, find_packages

VERSION = '1.0' 
DESCRIPTION = 'Python3 package drawing orbits and shadows of Kerr--Newman--(anti) de Sitter black holes'
LONG_DESCRIPTION = 'This is a package for Python 3.10, loaded with Opencv 4.10 and Imageio 2.36, to compute and draw (animated) shadows of a KNdS black hole (i.e. a charged rotating black hole inside a cosmological universe), possibly equipped with a thin Keplerian accretion disk, radiating as a blackbody. This code also allows to draw (massive or null) orbits in a KNdS space-time, using different integration methods of the geodesic equation.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="knds_orbits_and_shadows", 
        version=VERSION,
        author="Arthur Garnier",
        author_email="<arthur.garnier@math.cnrs.fr>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        #packages=find_packages(),
        install_requires=['opencv-python','imageio'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'knds', 'black hole', 'orbit', 'black hole shadowing', 'accretion disk'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ],
        packages=find_packages()
        #package_dir = {"": "src"},
        #packages = find_packages(where="src"),
)
