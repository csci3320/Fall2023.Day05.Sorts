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


l1 = [9,8,7,6,5,4,3,2,1,0]

print(l1)
print(insertionSort(l1))