def selectionSort(list):
  ticks = 0
  for i in range(len(list)):
    lowestIndex = -1
    lowestValue = 1000000
    for j in range(i, len(list)):
      ticks += 1
      if list[j] < lowestValue:
        lowestIndex = j
        lowestValue = list[j]
    temp = list[i]
    list[i] = list[lowestIndex]
    list[lowestIndex] = temp
  print(ticks)
  return list