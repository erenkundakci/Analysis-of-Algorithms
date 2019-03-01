

```python
import ctypes
from pympler import asizeof

class DynamicArray:
    def getsize(self):
        import sys
        return sys.getsizeof(self._A)
    
    def ToString(self):
        for i in self._A:
            print(i," ")
            
    def getLength(self):
        return len(self._A)
    
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k <self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity: #kapasite yeterli degilse, kapasiteyi 2'ye katla.
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1
        
    def _resize(self, c): # nonpublic utitity
        print("şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, ta")
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A=B # use the bigger array
        self._capacity = c
        
    def _make_array(self, c): # nonpublic utitity
        return(c*ctypes.py_object)()
```


```python
c=DynamicArray()
for i in range(33):
    c.append(" add an  item "+str(i))
    print(str(i)+" eklendi, dizi boyutu: "+str(c.getLength()))
```

    0 eklendi, dizi boyutu: 1
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak
    1 eklendi, dizi boyutu: 2
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak
    2 eklendi, dizi boyutu: 4
    3 eklendi, dizi boyutu: 4
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak
    4 eklendi, dizi boyutu: 8
    5 eklendi, dizi boyutu: 8
    6 eklendi, dizi boyutu: 8
    7 eklendi, dizi boyutu: 8
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak
    8 eklendi, dizi boyutu: 16
    9 eklendi, dizi boyutu: 16
    10 eklendi, dizi boyutu: 16
    11 eklendi, dizi boyutu: 16
    12 eklendi, dizi boyutu: 16
    13 eklendi, dizi boyutu: 16
    14 eklendi, dizi boyutu: 16
    15 eklendi, dizi boyutu: 16
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak
    16 eklendi, dizi boyutu: 32
    17 eklendi, dizi boyutu: 32
    18 eklendi, dizi boyutu: 32
    19 eklendi, dizi boyutu: 32
    20 eklendi, dizi boyutu: 32
    21 eklendi, dizi boyutu: 32
    22 eklendi, dizi boyutu: 32
    23 eklendi, dizi boyutu: 32
    24 eklendi, dizi boyutu: 32
    25 eklendi, dizi boyutu: 32
    26 eklendi, dizi boyutu: 32
    27 eklendi, dizi boyutu: 32
    28 eklendi, dizi boyutu: 32
    29 eklendi, dizi boyutu: 32
    30 eklendi, dizi boyutu: 32
    31 eklendi, dizi boyutu: 32
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak
    32 eklendi, dizi boyutu: 64
    


```python

```


```python

```
