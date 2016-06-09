def isFull(l):
    for x in l: 
        if x == "":
            return False
    return True
 
def firstEmpty(l):
    for a in range(0, 9):
        if l[a] == "":
            return a
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
    
def main():
    token = "x"
    curr = [["","","","","","","","",""]]
    while not isFull(curr[0]):
        print("lol")
        for each in curr:
            next = []
            for i,box in enumerate(each):
              if  box == "":
                  clone = list(each)
                  clone[i] = token
                    clone[index] = token 
                    if prune(clone):
                        next.append(clone)
        if token == "x":
            token = "o"
        elif token == "o":
            token = "x"
        else:
            print("whoops")
        
        curr = next
        next = []
        print(curr[0])

    print(curr)
    
main()