# Recall in 5.2.4 Worked Example 1, we gave you the code for
# merge_sort. You may copy that code into this problem and
# modify it. Change it such that instead of sorting from
# lowest to highest, it sorts from highest to lowest.
#
# Name your function sort_with_merge(). For example, if you call
# merge_sort([5, 3, 1, 2, 4]), you would get [5, 4, 3, 2, 1].
#
# Do not use Python's sort or reverse methods to complete
# this.


# Write your code below!
def sort_with_merge(arr):
    if arr and len(arr) > 1:
        mid = len(arr) // 2
        l_arr = sort_with_merge(arr[:mid])
        r_arr = sort_with_merge(arr[mid:])

        sorted_arr = []
        while l_arr and r_arr:
            victim_arr = l_arr if l_arr[0] > r_arr[0] else r_arr
            sorted_arr.append(victim_arr[0])
            victim_arr.pop(0)

        sorted_arr.extend(l_arr)
        sorted_arr.extend(r_arr)

        return sorted_arr
    else:
        return arr


# The code below will test your function. If it works, this
# will print [5, 3, 1, -1, -3, -5].
print(sort_with_merge([1, 3, -1, -3, -5, 5]))
print(sort_with_merge([1, 3, -1, -3, -5, -3, 5]))
print(sort_with_merge([1, -3]))
print(sort_with_merge([1, 3]))
print(sort_with_merge([1]))
print(sort_with_merge([]))
print(sort_with_merge([1, -3, 3]))
