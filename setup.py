from setuptools import setup, find_packages

setup(
     name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/exclusivedollar/Team_5_analyse',
    author='TeamAnalyse',
    author_email='lesedi10madumo@gmail.com'
)