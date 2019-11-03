def insertion_sort(sorted_list): #rosnaco
    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        j = i - 1
        while j >= 0 and key < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = key
    print('\nThe sorted list: \t', sorted_list)
    print('\n')
    sorted_list.reverse()
    print('\nThe sorted list: \t', sorted_list)
    print('\n')

#DZIALAAAAAAAA
