from setuptools import setup, find_packages
  
setup( 
    name='bindcurve', 
    version='0.1.0-alpha1', 
    description='A Python package for fitting and plotting of binding curves.', 
    author='choutkaj',  
    packages=find_packages(), 
    install_requires=[ 
        'numpy', 
        'pandas',
        'matplotlib',
        'lmfit',
    ], 
) 