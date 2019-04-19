
# coding: utf-8

# In[22]:

#Dynamic programming - Knapsack problem
#Çantamızın ağırlık kapasitesi kadar kitap almak istiyoruz ama aldığımız kitapların toplam değeri en yüksek olmalı.
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total weight of a solution to the
    0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0][2] > avail:
        #Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem[2])
        withVal += nextItem[1]
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def getItems():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]

    items_a = [names[0],vals[0],weights[0]]
    items_b = [names[1],vals[1],weights[1]]
    items_c = [names[2],vals[2],weights[2]]
    items_d = [names[3],vals[3],weights[3]]

    items = [items_a, items_b, items_c, items_d]
    return items

getItems()


# In[23]:

items = getItems()
maxVal(items,10)


# In[ ]:



