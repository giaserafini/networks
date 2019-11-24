def insertion_sort_d(sorted_list):
    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        j = i - 1
        while j >= 0 and key > sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = key
        return sorted_list
    sorted_list = insertion_sort_d()
    # print('\nThe sorted list is: \t', sorted_list)
    # sorted_list.reverse()
    # print('\nThe sorted list: \t', sorted_list)
    # print('\n')



listad = []
size = int(input("\nEnter size of the list: \t"))

for i in range(size):
    elements = int(input("Enter the element: \t"))
    listad.append(elements)

insertion_sort_d(listad)
