def isInt(value):
    '''
    :param value:
    :return: True if it is an int
    '''
    if int(value) == value:
        return True
    else:
        raise ValueError("The value is not an int!")
def isIntGZero(value):
    '''
    :param value:
    :return: True if the value is int>0
    '''
    if int(value) == value and value >= 1:
        return True
    else:
        raise ValueError("You didn't type an int >0!")


def isNumber(value):
    '''
    :param value:
    :return: True if the value is an int or a float
    '''
    if int(value) == value or float(value) == value:
        return True
    else:
        raise ValueError("You didn't type a number!")