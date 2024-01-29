def binary_search(array, target):
 
  left = 0
  right = len(array) - 1

  while left <= right:
    mid = (left + right) // 2
    element = array[mid]

    if element == target:
      return mid
    elif element < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1



array = [1, 3, 5, 7, 9, 11,13,17,21,26]
target = 26

index = binary_search(array, target)

if index == -1:
  print("Target not found in the array")
else:
  print(f"Target found at index {index}")
