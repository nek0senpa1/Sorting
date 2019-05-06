stuff = [1,2,2,3,46,74968,4,984,64,3,63510351,85,435,4,8543,8543,613,2,1]



# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for k in range(cur_index, len(arr)):
            if arr[k] < arr[smallest_index]:
                smallest_index = k

        newPlace = arr[smallest_index]

        arr[smallest_index] =arr[cur_index]
             
        arr[cur_index] = newPlace

        # TO-DO: swap

    return arr

print(selection_sort(stuff))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr