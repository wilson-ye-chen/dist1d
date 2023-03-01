from setuptools import setup

setup(
    name='dist1d',
    version='0.1',
    description='Numerical pdf, cdf, and ppf for an unnormalised density',
    url='https://github.com/wilson-ye-chen/dist1d',
    author='Wilson Ye Chen',
    license='MIT',
    packages=['dist1d'],
    install_requires=['numpy', 'scipy']
    )
