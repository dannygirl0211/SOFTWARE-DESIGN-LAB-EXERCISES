
def max_min(data,n):
    if n == 1:
        return data[0],data[0]
    else:
        x,y = max_min(data, n - 1)
        return data[n - 1] if (data[n - 1] > x) else x, data[n - 1] if (data[n - 1] <y) else y


data = [10,20,30,40,50,60,70,80,90,100]
m,n = max_min(data,10)
print(m,n)