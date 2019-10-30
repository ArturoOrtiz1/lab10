#This program will be the same as "sort(myList)"
def byFreq(pair):
    return pair[1]

def count(myList,x):
    num=0
    #look through the list
    for i in myList:
        if i == x:
            num=num+1
    return num
    

def isin(myList,x):
    for i in myList:
        if i==x:
            return True
        
    return False
    
#numbers()




def index(myList,x):
    
    for i in range(len(myList)):
        #return position
        if x==myList[i]:
            return i
        
    return None

print (index([1,2,1,1,3,4],3))
