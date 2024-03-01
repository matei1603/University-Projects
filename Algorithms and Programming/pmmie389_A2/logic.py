def add(score_list,value):
    '''

    :param score_list: The initial list
    :param value: The value we want to add at the end of the list
    :return: We return the new list
    '''
    score_list.append(value)
    return score_list
def test_add():
    score_list = [15, 20, 50, 60, 70]
    assert add(score_list, 75) == [15, 20, 50, 60, 70, 75]
    assert add(score_list, 40.6) == [15, 20, 50, 60, 70, 75, 40, 6]
    assert add(score_list, 10) == [15, 20, 50, 60, 70, 75, 40.6, 10]
    assert add(score_list, 85) == [15, 20, 50, 60, 70, 75, 40.6, 10, 85]

def insert(score_list, index, value):
    '''

    :param score_list: The initial list
    :param index: The index when we want to add a value
    :param value: The value we want to add the the specified index
    :return: We return the new list
    '''
    if index>= 0 and index <len(score_list):
        score_list.insert(index, value)
    return score_list

def test_insert():
    score_list = [85, 63, 74, 55, 87]
    assert insert(score_list, 2, 56) == [85, 63, 56, 74, 55, 87]
    assert insert(score_list, 5, 17) == [85, 63, 56, 74, 55, 17, 87]
    assert insert(score_list, 2, 11) == [85, 63, 11, 56, 74, 55, 17, 87]
    assert insert(score_list, 10, 9) == [85, 63, 11, 56, 74, 55, 17, 87]


def remove(score_list, index):
    '''

    :param score_list: The initial list
    :param index: The index of the element that we want to delete
    :return: The new list
    '''
    del(score_list[index])
    return score_list
def test_remove():
    score_list = [61, 28, 66, 77, 45]
    assert remove(score_list, 1) == [61, 66, 77, 45]
    assert remove(score_list, 0) == [66, 77, 45]
    assert remove(score_list, 3) == [66, 77, 45]

def remove2 (score_list,from_index,to_index):
    '''

    :param score_list:The initial list
    :param from_index: The first index of the interval
    :param to_index: The last index of the interval
    :return: The new list
    '''
    if from_index >=0 and from_index < len(score_list) and to_index >=0 and to_index<len(score_list):
        del(score_list[from_index:to_index+1])
    return score_list
def test_remove2():
    score_list = [78, 36, 45, 85, 74, 63, 14, 25, 80, 17, 57]
    assert remove2(score_list, 2, 5) == [78, 36, 14, 25, 80, 17, 57]
    assert remove2(score_list, 0, 2) == [25, 80, 17, 57]
    assert remove2(score_list, 3, 1) == [25, 80, 17, 57]
    assert remove2(score_list, 2, 20) == [25, 80, 17, 57]
    assert remove2(score_list, 0, 3) == []

def replace(score_list,index,new_value):
    '''

    :param score_list: The initial list
    :param index: The index of the element that we want to replace with a new_value
    :param new_value: The value that we want to replace on index
    :return: The new list
    '''
    if new_value<=100:
        score_list[index]=new_value
    return score_list
def test_replace():
    score_list = [85, 74, 36, 24, 55]
    assert replace(score_list, 2, 25) == [85, 74, 25, 24, 55]
    assert replace(score_list, 0, 18) == [18, 74, 25, 24, 55]
    assert replace(score_list, 8, 67) == [18, 74, 25, 24, 55]
    assert replace(score_list, 2, 79.5) == [18, 74, 25, 24, 79.5]

def less(score_list,value):
    '''

    :param score_list: The initial list
    :param value: The value
    :return: The new list with the participants with scores less than the value
    '''
    i=0
    score_list1=[]
    while i<len(score_list):
        if score_list[i]<value:
            score_list1.append(i)
        i+=1
    return score_list1
def test_less():
    score_list = [75, 35, 74, 25, 98, 17, 58]
    assert less(score_list, 30) == [25]
    assert less(score_list, 10) == []

def sorted(score_list):
    '''

    :param score_list: The initial list
    :return: The sorted list
    '''
    l=[x for x in enumerate(score_list)]
    l.sort(key=lambda x:x[1])
    return [i for i, nr in(l)]


def test_sorted():
    score_list = [75, 25, 36, 10, 95, 55, 82]
    assert sorted(score_list) == [(3, 10), (1, 25), (2, 36), (5, 55), (0, 75), (6, 82), (4, 95)]


def sorted2 (score_list, value):
    '''

    :param score_list: The initial list
    :param value: The value
    :return: The new list with participants with scores higher than value sorted
    '''
    l = [x for x in enumerate(score_list) if x[1]>value]
    l.sort(key=lambda x: x[1])
    return [i for i, nr in (l)]

def test_sorted2():
    score_list = [49, 26, 54, 25, 92, 100, 27]
    assert sorted2(score_list, 50) == [(2, 54), (6, 27), (4, 92), (5, 100)]
    assert sorted2(score_list, 100) == []

def avg(score_list,from_index,to_index):
    '''

    :param score_list: The initial list
    :param from_index: The first index of the interval
    :param to_index: The last index of the interval
    :return: The average of the scores between the 2 indexes
    '''
    nl=score_list[from_index:to_index+1]
    s=0
    if from_index >=0 and from_index < len(score_list) and to_index >= 0 and to_index < len(score_list):
        for i in range (len(nl)):
            s+=nl[i]

    average=s/len(nl)
    return average

def test_avg():
    score_list = [20, 30, 40, 58, 36, 75, 25, 11, 33, 78, 25]
    assert avg(score_list, 0, 2) == 30
    assert avg(score_list, 5, 2) == 0
    assert avg(score_list, 0, 9) == 53.8


def min(score_list,from_index,to_index):
    '''

    :param score_list: The initial list
    :param from_index: The first index of the interval
    :param to_index: The last index of the interval
    :return: The minimum element between the 2 indexes
    '''
    nl = score_list[from_index:to_index + 1]
    minn=0
    if from_index >=0 and from_index < len(score_list) and to_index >= 0 and to_index < len(score_list):
        minn=nl[0]
        for i in range(len(nl)):
            if nl[i]<minn:
                minn=nl[i]
    return minn

def test_min():
    score_list = [25, 66, 75, 55, 53, 78, 25, 36, 11, 10, 8]
    assert min(score_list, 0, 2) == 25
    assert min(score_list, 10, 7) == 0
    assert min(score_list, 0, 5) == 25

def mul(score_list,value,from_index,to_index):
    '''

    :param score_list: The initial list
    :param value: The value
    :param from_index: The first index of the interval
    :param to_index: The last index of the interval
    :return: The new list with the  participants with scores multiple of value
    '''
    mul=[]
    if from_index >=0 and from_index < len(score_list) and to_index >= 0 and to_index < len(score_list):
        i=0
        while i< len(score_list):
            if value % score_list[i]==0:
                mul.append(score_list[i])
            i+=1
    return mul
def test_mul():
    score_list = [36, 45, 66, 75, 20, 30, 70, 25, 78, 61, 73]
    assert mul(score_list, 0, 1, 10) == []
    assert mul(score_list, 30, 6, 2) == []
    assert mul(score_list, 10, 0 , 6) == [20, 30, 70]
def filter_mul(score_list,value):
    '''
    :param score_list: The initial list
    :param value: The value
    :return: The new list with the participants with scores multiple of value
    '''
    i=0
    while i<len(score_list):
        if score_list[i] % value !=0:
            del(score_list[i])
            i-=1
        i=i+1
    return score_list

def test_filter_mul():
    score_list = [56, 33, 45, 25, 78, 25, 45, 36, 14, 88]
    assert filter_mul(score_list, 5) == [(2, 45), (3, 25), (5, 25), (6, 45)]
    assert filter_mul(score_list, 90) == []
    assert filter_mul(score_list, 88) == [(9,88)]


def filter_greater(score_list,value):
    '''

    :param score_list: The initial list
    :param value: The value
    :return: The new list with the participants with scores higher than value
    '''
    i=0
    while i<len(score_list):
        if score_list[i] <=value:
            del(score_list[i])
        i=i+1
    return score_list
def test_filter_greater():
    score_list = [56, 45, 25, 75, 36, 75, 44, 33, 78, 100]
    assert filter_greater(score_list, 75) == [(8, 78), (9, 100)]
    assert filter_greater(score_list, 100) == []
    assert filter_greater(score_list, 74) == [(3, 75), (5, 75), (8, 78), (9, 100)]
def undo(score_list):
    '''

    :param score_list: The list with operations
    :return: The undo of the last operation made
    '''
    return score_list[len(score_list)-1]