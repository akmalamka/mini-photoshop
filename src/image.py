# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _image
else:
    import _image

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def new_mat(width, height):
    return _image.new_mat(width, height)

def mat(arr, width, height):
    return _image.mat(arr, width, height)

def freeAll(arr, width, height):
    return _image.freeAll(arr, width, height)

def free(arr, width, height):
    return _image.free(arr, width, height)

def get(arr, i, j, k):
    return _image.get(arr, i, j, k)

def set(arr, i, j, k, value):
    return _image.set(arr, i, j, k, value)
class Image(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    width = property(_image.Image_width_get, _image.Image_width_set)
    height = property(_image.Image_height_get, _image.Image_height_set)
    grayLevel = property(_image.Image_grayLevel_get, _image.Image_grayLevel_set)
    pixels = property(_image.Image_pixels_get, _image.Image_pixels_set)

    def __init__(self, *args):
        _image.Image_swiginit(self, _image.new_Image(*args))
    __swig_destroy__ = _image.delete_Image

    def __sub__(self, image):
        return _image.Image___sub__(self, image)

    def __add__(self, *args):
        return _image.Image___add__(self, *args)

    def __mul__(self, scalar):
        return _image.Image___mul__(self, scalar)

    def __and__(self, image):
        return _image.Image___and__(self, image)

    def __or__(self, image):
        return _image.Image___or__(self, image)

    def __xor__(self, image):
        return _image.Image___xor__(self, image)

    def negative(self):
        return _image.Image_negative(self)

    def grayscale(self):
        return _image.Image_grayscale(self)

    def translate(self, x, y):
        return _image.Image_translate(self, x, y)

    def rotate(self, isClockwise):
        return _image.Image_rotate(self, isClockwise)

    def flip(self, isVertical):
        return _image.Image_flip(self, isVertical)

    def zoom(self):
        return _image.Image_zoom(self)

    def contrastStrech(self, min, max):
        return _image.Image_contrastStrech(self, min, max)

    def logTransform(self, c):
        return _image.Image_logTransform(self, c)

    def inverseLogTransform(self, c):
        return _image.Image_inverseLogTransform(self, c)

    def powerTransform(self, c):
        return _image.Image_powerTransform(self, c)

    def grayLevelSlice(self, min, max):
        return _image.Image_grayLevelSlice(self, min, max)

    def bitPlaneSlice(self, n):
        return _image.Image_bitPlaneSlice(self, n)

# Register Image in _image:
_image.Image_swigregister(Image)


