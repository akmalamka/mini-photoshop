# File : setup.py 

from distutils.core import setup, Extension 
#name of module 
name = "image"

#version of module 
version = "1.0"

# specify the name of the extension and source files 
# required to compile this 
ext_modules = Extension(name='_image',sources=["image.i", "image.cpp"], swig_opts=['-c++']) 

setup(name=name, 
	version=version, 
	ext_modules=[ext_modules]) 
