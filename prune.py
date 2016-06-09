def isFull(l):
    for x in l: 
        if x == "":
            return False
    return True
    
def prune(l):
    for a in range(0, 2):
        if l[0+a] == l[3+a] == l[6+a] == "x":
            return False
        if l[3*a + 0] == l[3*a + 1] == l[3*a+ 2] == "x":
            return False 
    if l[0] == l[4] == l[8] == "x":
        return False
    if l[2] == l[4] == l[6] == "x":
        return False 
    return True 