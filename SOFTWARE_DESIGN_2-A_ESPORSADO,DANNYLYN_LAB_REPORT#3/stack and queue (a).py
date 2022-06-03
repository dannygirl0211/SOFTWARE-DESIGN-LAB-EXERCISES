
def is_empty(stk):
    if stk==[]:
        return True
    else:
        return False


def Push(stk,item):
    stk.append(item)
    top=len(stk)-1


def Pop(stk):
    if is_empty(stk):
        print("Underflow")
    else:
        item = stk.pop()
        if len(stk)==0:
            top = None
        else:
            top = len(stk)
            print("Popped item is "+str(item))


def Display(stk):
    if is_empty(stk):
      print("Stack is empty")
    else:
        top=len(stk)-1
        print("Elements in the stack are: ")
        for i in range(top,-1,-1):
            print(str(stk[i]))


if __name__ == "__main__":
    stk = []
    top = None
    Push(stk,1)
    Push(stk,2)
    Push(stk,3)
    Push(stk,4)
    Push(stk,5)
    Push(stk,6)
    Push(stk,7)
    Push(stk,8)
    Push(stk,9)
    Push(stk,10)
    Pop(stk)
    Display(stk)
