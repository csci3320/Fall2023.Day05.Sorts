import math

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

sortAlgorithms = [bubble_sort, selection_sort, insertion_sort, merge_sort]

l1 = (1,2)
l2 = (2,1)
l3 = ()

lists = [l1, l2, l3]

def isSorted(tuple):
  for i in range(len(tuple)-1):
    if tuple[i+1] <= tuple[i]:
      return False
  return True

for j in range(len(sortAlgorithms)):
  algorithmName = str(sortAlgorithms[j].__name__)
  for i in range(len(lists)):
    result = sortAlgorithms[j](lists[i])
    sorted = isSorted(result)
    if not sorted:
      print(str(sortAlgorithms[j].__name__) + " didn't sort correctly on: " + str(lists[i]))
      print("Incorrect result: " + str(result))
