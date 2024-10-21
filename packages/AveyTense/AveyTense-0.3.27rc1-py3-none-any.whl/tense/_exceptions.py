"""
**TensePy Exceptions**

\\@since 0.3.27a1 \\
© 2024-Present Aveyzan // License: MIT
```
module tense._exceptions
```
Exception classes for TensePy
"""
class MissingValueError(Exception):
    """
    \\@since 0.3.19
    ```
    in module tense.types_collection
    # 0.3.26b3 - 0.3.26c3 in module tense.tcs
    # to 0.3.26b3 in module tense.primary
    ```
    Missing value (empty parameter)
    """
    ...
class IncorrectValueError(Exception):
    """
    \\@since 0.3.19
    ```
    in module tense.types_collection
    # 0.3.26b3 - 0.3.26c3 in module tense.tcs
    # to 0.3.26b3 in module tense.primary
    ```
    Incorrect value of a parameter, having correct type
    """
    ...
class NotInitializedError(Exception):
    """
    \\@since 0.3.25
    ```
    in module tense.types_collection
    # 0.3.26b3 - 0.3.26c3 in module tense.tcs
    # to 0.3.26b3 in module tense.primary
    ```
    Class was not instantiated
    """
    ...
class InitializedError(Exception):
    """
    \\@since 0.3.26b3
    ```
    in module tense.types_collection
    ```
    Class was instantiated
    """
    ...
class NotReassignableError(Exception):
    """
    \\@since 0.3.26b3
    ```
    in module tense.types_collection
    ```
    Attempt to re-assign a value
    """
    ...
class NotComparableError(Exception):
    """
    \\@since 0.3.26rc1
    ```
    in module tense.types_collection
    ```
    Attempt to compare a value with another one
    """
    ...
class NotIterableError(Exception):
    """
    \\@since 0.3.26rc1
    ```
    in module tense.types_collection
    ```
    Attempt to iterate
    """
    ...
class NotInvocableError(Exception):
    """
    \\@since 0.3.26rc1
    ```
    in module tense.types_collection
    ```
    Attempt to call an object
    """
    ...
    
class SubclassedError(Exception):
    """
    \\@since 0.3.27rc1
    ```
    in module tense.types_collection
    ```
    Class has been inherited by the other class
    """
    ...

class ErrorHandler:
    """
    \\@since 0.3.26rc1
    ```
    in module tense.types_collection
    ```
    Internal class for error handling

    - `100` - cannot modify a final variable (`any`)
    - `101` - cannot use comparison operators on type which doesn't support them + ...
    - `102` - cannot assign a new value or re-assign a value with any of augmented \\
    assignment operators on type which doesn't support them + ...
    - `103` - object is not iterable (`any`)
    - `104` - attempt to initialize an abstract class + ...
    - `105` - class (`any`) was not initialized
    - `106` - could not compare types - at least one of them does not support comparison \\
    operators
    - `107` - object cannot be called
    - `108` - object cannot use any of unary operators: '+', '-', '~', cannot be called nor be value \\
    of `abs()` in-built function
    - `109` - object cannot use unary +|- operator
    - `110` - object cannot use bitwise NOT operator '~'
    - `111` - this file is not for compiling, moreover, this file does not have a complete \\
    TensePy declarations collection. Consider importing module `tense` instead
    - any other - unknown error occured
    """
    def __new__(cls, code: int, *args: str):
        _arg0 = "" if len(args) == 0 else args[0]
        _arg1 = "" if len(args) == 1 else args[1]
        if code == 100:
            err, s = (NotReassignableError, "cannot modify a final variable '{}'".format(_arg0) if _arg0 not in (None, "") else "cannot modify a final variable")
        elif code == 101:
            err, s = (NotComparableError, "cannot use comparison operators on type which doesn't support them" + _arg0)
        elif code == 102:
            err, s = (NotReassignableError, "cannot assign a new value or re-assign" + _arg0)
        elif code == 103:
            err, s = (NotIterableError, "object is not iterable ('{}')".format(_arg0) if _arg0 not in (None, "") else "cannot modify a final variable")
        elif code == 104:
            err, s = (InitializedError, "attempt to initialize an abstract class " + _arg0)
        elif code == 105:
            err, s = (NotInitializedError, "class '{}' was not initalized".format(_arg0))
        elif code == 106:
            err, s = (NotComparableError, "could not compare types - at least one of them does not support comparison operators")
        elif code == 107:
            err, s = (NotInvocableError, f"class {_arg0} cannot be called")
        elif code == 108:
            err, s = (TypeError, "object cannot use any of unary operators: '+', '-', '~', cannot be called nor be value of abs() in-built function")
        elif code == 109:
            err, s = (TypeError, "object cannot use unary '{}' operator".format(_arg0))
        elif code == 110:
            err, s = (TypeError, "object cannot use bitwise NOT operator '~'")
        elif code == 111:
            err, s = (RuntimeError, "this file is not for compiling, moreover, this file does not have a complete TensePy declarations collection. Consider importing module 'tense' instead.")
        elif code == 112:
            err, s = (AttributeError, "cannot modify a final attribute {}".format(_arg0))
        elif code == 113:
            err, s = (SubclassedError, "attempt to subclass a final class {}".format(_arg0))
        elif code == 114:
            err, s = (TypeError, "{} cannot be used on {}".format(_arg0, _arg1))
        elif code == 115:
            err, s = (TypeError, "cannot inspect because class {} is abstract".format(_arg0))
        elif code == 116:
            err, s = (TypeError, "cannot inspect because class {} is final".format(_arg0))
        elif code == 117:
            err, s = (AttributeError, "attempt to delete item {}".format(_arg0))
        elif code == 118:
            err, s = (AttributeError, "attempt to reassign item {}".format(_arg0))
        elif code == 119:
            err, s = (AttributeError, "cannot modify any fields in class {}".format(_arg0))
        else:
            err, s = (RuntimeError, "unknown error occured")
        raise err(s)
