import random
def shuffle(array): 
  m = len(array)
  t = None
  i = None

  while m:

    i = int(random.random() * m)
    m -= 1 
    t = array[m]
    array[m] = array[i]
    array[i] = t
  

  return array
# print shuffle([1,2,3,4,5,6,7,8,9,10])
