import ctypes as ct
from ctypes import *
import typing

import os
import h5py

# is there a more elegant way to do this? Molule load error --> OSError: [WinError 126] The specified module could not be found
# seems like having trouble load a dependency file?
os.chdir('libs')

h5lib = ct.cdll.LoadLibrary("TwH5Dll.dll")

os.chdir('../')


# Return values from C functions
TwDaqRecNotRunning      = 0
TwAcquisitionActive     = 1
TwNoActiveAcquisition   = 2
TwFileNotFound          = 3
TwSuccess               = 4
TwError                 = 5
TwOutOfBounds           = 6
TwNoData                = 7
TwTimeout               = 8
TwValueAdjusted         = 9
TwInvalidParameter      = 10
TwInvalidValue          = 11
TwAborted               = 12


# The function `close` is a Python wrapper for the C function with prototype of:
#
# int _TwCloseH5(char* filename);
#
# Args:
#     filename: full path of the h5 file to close
#
# Returns:
#     result: with possible values listed between lines 9 and 21


def close(filename: str) -> int:
    """
    This function is called to close an opened h5 file. There is no 'open'
    function that opens a h5 file, if any of the functions below are called
    on a h5 file, the h5 file is implicitly opened, and you need to close it
    afterwards.

    Args:
        filename: full path of the h5 file to close
    
    Returns:
        result: return value from C function _TwCloseH5
    """
    status = h5lib._TwCloseH5(c_char_p(bytes(filename, 'utf-8')))
    return status

# The function `get_int_attribute` is a Python wrapper for the C function with prototype of:
#
# int _TwGetIntAttributeFromH5(char* filename, char* location, char* name, int* attribute);
#
# Args:
#     filename: full path of the h5 file
#     location: location of the group or datset the attribute is attached to
#     name: attribute name
#     attribute: output for the attribute
#
# Returns:
#     result: with possible values listed between lines 9 and 21


def get_int_attribute(filename: str, location: str, name: str) -> typing.Tuple[int, int]:
    """
    This function is called to get a 32-bit integer attribute from a h5 file.

    Args:
        filename: full path of the h5 file
        location: location of the group or datset the attribute is attached to
        name: attribute name

    Returns:
        result: `tuple` of len 2:
            * return value from C function _TwGetIntAttributeFromH5
            * the attribute value
    """
    attribute_value = int(h5py.File(filename, 'r')[location].attrs[name])
    
    char_star_filename = c_char_p(bytes(filename, 'utf-8'))
    char_star_location = c_char_p(bytes(location, 'utf-8'))
    char_star_name = c_char_p(bytes(name, 'utf-8'))
    attribute_value_location = hex(id(attribute_value))

    c_function_return = h5lib._TwGetIntAttributeFromH5(char_star_filename, char_star_location, char_star_name, attribute_value_location)
    
    int_attribute = (c_function_return, attribute_value)
    return int_attribute


# The function `get_float_attribute` is a Python wrapper for the C function with prototype of:
#
# int _TwGetFloatAttributeFromH5(char* filename, char* location, char* name, int64_t* attribute);
#
# Args:
#     filename: full path of the h5 file
#     location: location of the group or datset the attribute is attached to
#     name: attribute name
#     attribute: output for the attribute
#
# Returns:
#     result: with possible values listed between lines 9 and 21


def get_float_attribute(filename: str, location: str, name: str) -> typing.Tuple[int, float]:
    """
    This function is called to get a 32-bit float attribute from a h5 file.

    Args:
        filename: full path of the h5 file
        location: location of the group or datset the attribute is attached to
        name: attribute name

    Returns:
        result: `tuple` of len 2:
            * return value from C function _TwGetFloatAttributeFromH5
            * the attribute value
    """
    attribute_value = float(h5py.File(filename, 'r')[location].attrs[name])

    char_star_filename = c_char_p(bytes(filename, 'utf-8'))
    char_star_location = c_char_p(bytes(location, 'utf-8'))
    char_star_name = c_char_p(bytes(name, 'utf-8'))
    attribute_value_location = hex(id(attribute_value))

    c_function_return = h5lib._TwGetFloatAttributeFromH5(char_star_filename, char_star_location, char_star_name, attribute_value_location)

    float_attribute = (c_function_return, attribute_value)
    return float_attribute


# The function `get_str_attribute` is a Python wrapper for the C function with prototype of:
#
# int _TwGetStringAttributeFromH5(char* filename, char* location, char* name, char* attribute);
#
# Args:
#     filename: full path of the h5 file
#     location: location of the group or datset the attribute is attached to
#     name: attribute name
#     attribute: output for the attribute, with max length of 256
#
# Returns:
#     result: with possible values listed between lines 9 and 21


def get_str_attribute(filename: str, location: str, name: str) -> typing.Tuple[int, str]:
    """
    This function is called to get a string attribute from a h5 file.

    Args:
        filename: full path of the h5 file
        location: location of the group or datset the attribute is attached to
        name: attribute name

    Returns:
        result: `tuple` of len 2:
            * return value from C function _TwGetStringAttributeFromH5
            * the attribute value
    """
    attribute_value = h5py.File(filename, 'r')[location].attrs[name]
    tw_string_function_return = h5lib._TwGetStringAttributeFromH5(c_char_p(bytes(filename, 'utf-8')), c_char_p(bytes(location, 'utf-8')), c_char_p(bytes(name, 'utf-8')), c_char_p(attribute_value))

    string_attribute = (tw_string_function_return, attribute_value)
    return string_attribute
