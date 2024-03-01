import helper

def sortByLastName(a,b):
    '''
    :param a:
    :param b:
    :return:
    '''
    if a.getLastName() > b.getLastName():
        return True
    return False

def sortByLen(a,b):
    '''
    :param a: list
    :param b: list
    :return:
    '''
    if len(a.getListOfPassengers()) > len(b.getListOfPassengers()):
        return True
    return False

def sortByStartingSubstring(a,b,sString):
    '''

    :param a: plane object
    :param b: plane object
    :return:
    '''
    result = 0
    for i in range(len(a.getListOfPassengers())):
        if a.getListOfPassengers()[i].getFirstName()[0:len(sString)] == sString:
            result += 1
    result1 = 0
    for i in range(len(b.getListOfPassengers())):
        if b.getListOfPassengers()[i].getFirstName()[0:len(sString)] == sString:
            result1 += 1
    if result > result1:
        return True
    return False

def sortByConcatenation(a,b):
    '''
    :param a:
    :param b:
    :param help:
    :return:
    '''
    String = str(len(a.getListOfPassengers())) + a.getDestination()
    String1 = str(len(b.getListOfPassengers())) + b.getDestination()
    if String > String1:
        return True
    return False

def findByFirst3(a):
    '''
    :param a:object
    :param help:
    :return:
    '''
    for i in range(len(a.getListOfPassengers()) - 1):
        for j in range(i + 1, len(a.getListOfPassengers())):
            myList1 =helper.makeIntList(a.getListOfPassengers()[i].getPassNumber())
            myList2 =helper.makeIntList(a.getListOfPassengers()[j].getPassNumber())
            if myList2[0:3] == myList1[0:3]:
                return True
    return False

def findByString(a, sString):
    '''
    :param a:  object
    :param sString: string
    :return:
    '''
    if sString in a.getFirstName() or sString in a.getLastName():
        return True
    return False

def findByName(a, name):
    '''
    :param a: plane object
    :param name: string
    :return:
    '''
    name = name.split()
    for elem in a.getListOfPassengers():
        if elem.getFirstName() == name[0] and elem.getLastName() == name[1]:
            return True
    return False