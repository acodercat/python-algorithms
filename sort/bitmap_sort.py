
def bitmap_sort(arr):
    bit = []
    for i in range(len(arr) + 1):
        bit.append(False)
    for i in arr:
        bit[i] = True
    for  index,item in enumerate(bit):
        if item:
            print(index)


bitmap_sort([11, 10, 9, 7, 0, 2, 3, 4, 5, 6, 1, 0])
