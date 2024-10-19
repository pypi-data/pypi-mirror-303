from distutils.core import  setup
import setuptools
packages = ['jackal_report']# 唯一的包名，自己取名
setup(name='jackal_report',
    version='1.0',
    author='gazi',
    packages=packages, 
    package_dir={'requests': 'requests'},)

