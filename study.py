import random



locked = { 
    (1,1) : (0,0,0), 
    (1,2) : (0,255,255)  
}


try:
    del locked[ ( 1,1 ) ]
except:
    print("not deleted")


a = { (1,2):(0,0,1), (2,4):(0,3,1), (3,9):(0,4,1), (4,2):(0,1,1) }
print(a)
for i in sorted( list(a), key = lambda x:x[0] )[::-1]:
    print( i )


