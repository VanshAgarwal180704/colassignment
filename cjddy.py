def xor(a,b):
    return ((a or b)and not(a and b))
def hfadder(a,b):
    return ((a or b)and not(a and b), a and b)
print(hfadder(True,True))
def add(a,b,c):
    vv=(xor(xor(a,b),c),(a or b)and(b or c)and (a or c))
    return vv

#print(add(True,True,False)[1])

#print(f"vv([0])")


'''abcd
   edfg
   
   add d g =l k
   add l c f =ui
   add u b d =pl
   add p a e = ki'''

def add4(a0,a1,a2,a3,  b0,b1,b2,b3, c):
    return (add(a0,b0,c)[0],add(add(a0,b0,c)[1],a1,b1)[0],add(add(add(a0,b0,c)[1],a1,b1)[1],a2,b2)[0],add(add(add(add(a0,b0,c)[1],a1,b1)[1],a2,b2)[1],a3,b3)[0],add(add(add(add(a0,b0,c)[1],a1,b1)[1],a2,b2)[1],a3,b3)[1])
 
print(add4(False,True,True,False, True,True,True,True, True))


'''add(a0,b0,c))



     =(s1,s2)
     add(s2,a1,b1)
     =(s3,s4)
     '''

def comp(a0,a1,a2,a3,  b0,b1,b2,b3):
    x=8*a3+4*a2+2*a1+a0
    y=8*b3+4*b2+2*b1+b0
    if x>y:
        return True
    else:
        return False



print(comp(False,True,True,False, True,True,True,True))
