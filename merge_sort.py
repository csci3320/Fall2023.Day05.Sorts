import math

def mergeRecurse(list, startIndex, stopIndex):
  diff = stopIndex - startIndex
  if diff <= 0:
    return list
  halfwayIndex = math.floor((stopIndex + startIndex)/2)
  firstHalf = mergeRecurse(list.copy(), startIndex, halfwayIndex)
  secondHalf = mergeRecurse(list.copy(), halfwayIndex+1, stopIndex)
  newList = list.copy()

  firstIndex = startIndex
  secondIndex = halfwayIndex+1
  for i in range(startIndex, stopIndex+1):
    if firstIndex > halfwayIndex:
      list[i] = secondHalf[secondIndex]
      secondIndex += 1
      continue
    if(secondIndex > stopIndex):
      list[i] = firstHalf[firstIndex]
      firstIndex += 1
      continue

    if firstHalf[firstIndex] < secondHalf[secondIndex]:
      newList[i] = firstHalf[firstIndex]
      firstIndex+=1
    else:
      newList[i] = secondHalf[secondIndex]
      secondIndex+=1
  return newList

def mergeSort(list):
  
  result = mergeRecurse(list, 0, len(list)-1)

  return result