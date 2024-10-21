from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'anndatavis'
LONG_DESCRIPTION = 'AnnData interactive visualization widget for Jupyter NB/lab'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="anndatavis",
        version=VERSION,
        author="Yochay Tzur",
        author_email="yochaytzur@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['anndata', 'plotly'], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'anndata', 'single cell RNA'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
