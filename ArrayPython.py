def commonPre():
 arr = ['11', '18', 19, 21,23]
 length = len(arr)
 print(length)
 middle_index = length // 4
 print(middle_index)
 first_half = arr[:middle_index]
 print(first_half)
 second_half = arr[middle_index:]
 print(second_half)
 for i in first_half:
     second_half.append(i)
 print(second_half)
commonPre()
#   inp=["flower","flow","flight"]
#   out=split(inp, 1)
#   print(out[1])
#   print(out[2])

