def readList(score_list):
    n=int(input("The nr. of elements:"))
    for i in range(0,n):
        element=int(input("Your element is:"))
        score_list.append(element)