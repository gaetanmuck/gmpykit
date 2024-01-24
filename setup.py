from setuptools import setup, find_packages

setup(
    name="gmpykit",
    version="0.0.4",
    author='Gaétan Muck',
    author_email='gaetan.muck@gmail.com',
    description='Package with various python tools',
    long_description='Package with various python tools',
    packages=find_packages(),
    install_require=[
        "pandas==2.0.3", 
        "numpy==1.26.2",
        "yaml", 
        "jdcal==1.4.1", 
        "lxml==4.9.3",
        "plotly==5.18.0"
    ],
    keywords=['python', 'toolkit', 'utilities', 'utils', 'tools']
)