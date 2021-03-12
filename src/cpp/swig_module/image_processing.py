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
    from . import _image_processing
else:
    import _image_processing

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


BLACKANDWHITE = _image_processing.BLACKANDWHITE
GRAYSCALE = _image_processing.GRAYSCALE
RGB = _image_processing.RGB
class Image(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    imageType = property(_image_processing.Image_imageType_get, _image_processing.Image_imageType_set)
    height = property(_image_processing.Image_height_get, _image_processing.Image_height_set)
    width = property(_image_processing.Image_width_get, _image_processing.Image_width_set)

    def __init__(self, *args):
        _image_processing.Image_swiginit(self, _image_processing.new_Image(*args))
    __swig_destroy__ = _image_processing.delete_Image

    @staticmethod
    def loadImage(filename):
        return _image_processing.Image_loadImage(filename)

    def set_pixel(self, row, col, px):
        return _image_processing.Image_set_pixel(self, row, col, px)

    def get_pixel(self, row, col):
        return _image_processing.Image_get_pixel(self, row, col)

# Register Image in _image_processing:
_image_processing.Image_swigregister(Image)

def Image_loadImage(filename):
    return _image_processing.Image_loadImage(filename)

class pixel(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    len = property(_image_processing.pixel_len_get, _image_processing.pixel_len_set)
    alpha = property(_image_processing.pixel_alpha_get, _image_processing.pixel_alpha_set)
    _in = property(_image_processing.pixel__in_get, _image_processing.pixel__in_set)

    def __init__(self, *args):
        _image_processing.pixel_swiginit(self, _image_processing.new_pixel(*args))
    __swig_destroy__ = _image_processing.delete_pixel

# Register pixel in _image_processing:
_image_processing.pixel_swigregister(pixel)


def isNumber(c):
    return _image_processing.isNumber(c)

def isWhitespace(c):
    return _image_processing.isWhitespace(c)

def isNewline(c):
    return _image_processing.isNewline(c)

def isSpace(c):
    return _image_processing.isSpace(c)

def isComment(c):
    return _image_processing.isComment(c)

def isPrintableCharacter(c):
    return _image_processing.isPrintableCharacter(c)

def nextInt(bytes, size, pointer):
    return _image_processing.nextInt(bytes, size, pointer)

def nextString(bytes, size, pointer):
    return _image_processing.nextString(bytes, size, pointer)

def nextInt16(bytes, size, pointer):
    return _image_processing.nextInt16(bytes, size, pointer)

def nextInt32(bytes, size, pointer):
    return _image_processing.nextInt32(bytes, size, pointer)

def hasEnding(fullString, ending):
    return _image_processing.hasEnding(fullString, ending)


