def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

    return unsorted_list

if __name__ == '__main__':
    unsorted_list = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Unsorted List {unsorted_list}")
    print(f"Sorted List {bubble_sort(unsorted_list)}")
