
def enqueue(data):
    queue.insert(0,data)


def dequeue():
    if len(queue)>0:
        return queue.pop()
    return ("Queue Empty!")


def display():
    print("Elements on queue are:");
    for i in range(len(queue)):
        print(queue[i])


if __name__=="__main__":
    queue=[]
    enqueue(8)
    enqueue(10)
    enqueue(6)
    enqueue(2)
    enqueue(5)
    print("Popped Element is: "+str(dequeue()))
    display()
