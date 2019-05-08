# TO-DO: complete the helpe function below to merge 2 sorted arrays
stuff = [1,2,3,4,5,6,7,8,9,10]
stuff2 = [1,2,3,4,5,6,7,8,9,10]


def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    thing1 = 0
    thing2 = 0
    # print(merged_arr)
    for i in range(0, elements):
        
        if arrA[thing1] < arrB[thing2]:
            merged_arr[i] = arrA[thing1]

            if thing1 < len(arrA)-1:
                thing1 = thing1 +1
                print('got to thing1a', merged_arr)

        elif arrB[thing2] <= arrA[thing1]:
            merged_arr[i] = arrB[thing2]

            if thing2 < len(arrB)-1:
                thing2 = thing2 +1
                print('got to thing2a', merged_arr)

        elif arrA[thing1] == arrB[thing2]:
            merged_arr[i] = arrB[thing2]

            if thing2 < len(arrB):
                thing2 = thing2 +1
                print('got to thing2a equaled!!', merged_arr)
        
        elif thing1 >= len(arrA):
            merged_arr[i] = arrB[thing2]
            thing2 = thing2+1
            print('got to thing2', thing2)
        
        elif thing2 >= len(arrB):
            merged_arr[i] = arrA[thing1]
            thing1 = thing1 +1
            print('got to thing1', thing1)

        


    return merged_arr

print(merge(stuff,stuff2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    mid = len(arr)//2

    if len(arr):
        right = merge_sort(arr[mid:])
        left = merge_sort(arr[:mid])
        arr = merge(left,right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
