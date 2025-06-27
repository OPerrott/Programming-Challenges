from data import *

def dis(_Line):
    print(_Line[1])
    
def sub(_Line):
    # Try parsing first argument
    try:
        var1 = int(_Line[1].strip(','))
    except ValueError:
        key = _Line[1].strip(',')
        if key in Data.variables:
            var1 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    # Try parsing second argument
    try:
        var2 = int(_Line[2].strip(','))
    except ValueError:
        key = _Line[2].strip(',')
        if key in Data.variables:
            var2 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    result = var1 - var2
    print(result)  # Or return result
    return result
    
def add(_Line): 
    # Try parsing first argument
    try:
        var1 = int(_Line[1].strip(','))
    except ValueError:
        key = _Line[1].strip(',')
        if key in Data.variables:
            var1 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    # Try parsing second argument
    try:
        var2 = int(_Line[2].strip(','))
    except ValueError:
        key = _Line[2].strip(',')
        if key in Data.variables:
            var2 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    result = var1 + var2
    print(result)  # Or return result
    return result


def mul(_Line): 
    # Try parsing first argument
    try:
        var1 = int(_Line[1].strip(','))
    except ValueError:
        key = _Line[1].strip(',')
        if key in Data.variables:
            var1 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    # Try parsing second argument
    try:
        var2 = int(_Line[2].strip(','))
    except ValueError:
        key = _Line[2].strip(',')
        if key in Data.variables:
            var2 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    result = var1 * var2
    print(result)  # Or return result
    return result

def div(_Line): 
    # Try parsing first argument
    try:
        var1 = int(_Line[1].strip(','))
    except ValueError:
        key = _Line[1].strip(',')
        if key in Data.variables:
            var1 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    # Try parsing second argument
    try:
        var2 = int(_Line[2].strip(','))
    except ValueError:
        key = _Line[2].strip(',')
        if key in Data.variables:
            var2 = int(Data.variables[key])
        else:
            print(f"[ERROR] {key} is not a valid variable!")
            return

    result = var1 / var2
    print(result)  # Or return result
    return result