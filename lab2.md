

```python
sayac=0

def power_recursive(x,y):
    global sayac
    sayac = sayac+1
    if(y==0): return 1
    if(y==1): return x
    if(y%2==0):
        return power_recursive(x*x,int(y/2))
    if(y%2==1):
        return power_recursive(x*x,int(y/2))*x
    
test = power_recursive(2,10)
print(test)
```

    1024
    


```python
def power_recursive_helper(x,y):
    global sayac
    sayac = 0
    result = (power_recursive(x,y),sayac)
    return result

print(power_recursive_helper(2,11))
```

    (2048, 4)
    


```python
def power(x,y):
    t=1
    global sayac
    for i in range(y):
        sayac = sayac+1
        t=t*x
    return (t,sayac)

power(2,5)
```




    (32, 59)




```python
def power_helper(x,y):
    global sayac
    sayac = 0
    r = power(x,y)
    print(x," uzeri ",y," degeri :",r[0]," cagrim sayisi: ",r[1])
    
print(power_helper(2,10))
```

    2  uzeri  10  degeri : 1024  cagrim sayisi:  10
    None
    


```python

```


```python
def selectionSort(alist):
    for fillSlot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillSlot+1):
            if(alist[location]>alist[positionOfMax]):
                positionOfMax = location       
        t = alist[fillSlot]
        alist[fillSlot] = alist[positionOfMax]
        alist[positionOfMax] = t
    return alist
        
list = [42,99,40,3,0,27,998,1024,1453,2023,456456,23438,234243,84,5935,53]
print("Normal list:",list)
sortedList = selectionSort(list)
print("Sorted list:",sortedList)
```

    Normal list: [42, 99, 40, 3, 0, 27, 998, 1024, 1453, 2023, 456456, 23438, 234243, 84, 5935, 53]
    Sorted list: [0, 3, 27, 40, 42, 53, 84, 99, 998, 1024, 1453, 2023, 5935, 23438, 234243, 456456]
    


```python

```
