def insertionSort(list):
  ticks = 0
  for i in range(1, len(list)):
    for j in range(i, 0, -1):
      before = list[j-1]
      current = list[j]
      if current < before:
        temp = list[j]
        list[j] = list[j-1]
        list[j-1] = temp
  print(ticks)
  return list