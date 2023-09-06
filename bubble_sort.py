def bubbleSort(list):
  ticks = 0
  for i in range(len(list)):
    for j in range(len(list)-1-i):
      ticks += 1
      if list[j+1] < list[j]:
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp
  print(ticks)
  return list