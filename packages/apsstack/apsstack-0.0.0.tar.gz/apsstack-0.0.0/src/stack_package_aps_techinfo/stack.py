l=''
def push(e):
    global l
    l=e
    sen=str(e)+' is sucessfully pushed into stack'
    return sen.upper()
def pop():
    if len(l)!=0 or l==None:
       sen=str(l[-1])+' is sucessfully removed from stack'
       po= l.pop()
       
       return po
    else:
        return 'Stack is Empty'
def peek():
    if len(l)!=0 or l==None:
        p=l[-1]
        return p
    else:
        return 'Stack is Empty'
def length():
    return len(l)
    

