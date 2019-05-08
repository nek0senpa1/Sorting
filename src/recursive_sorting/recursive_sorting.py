# TO-DO: complete the helpe function below to merge 2 sorted arrays
stuff = [1,2,2,3,46,74968,4,984,64,3,63510351,85,435,4,8543,8543,613,2,1]
stuff2 = [11,12,2,13,146,74968,14,984,164,13,63510351,85,1435,114,8543,8543,613,21,11]


def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    thing1 = 0
    thing2 = 0
    # print(merged_arr)
    for i in range(0, elements):
        if thing1 >= len(arrA):
            merged_arr[i] = arrB[thing2]
            thing2 = thing2+1
        
        elif thing2 >= len(arrB):
            merged_arr[i] = arrA[thing1]


    return merged_arr

print(merge(stuff,stuff2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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
