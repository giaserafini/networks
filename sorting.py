def insertion_sort(sorted_list):
    for i in range(1, len(sorted_list)):
        key = sorted_list[i]
        j = i - 1
        while j >= 0 and key < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = key
    print('\nThe sorted list: \t', sorted_list)
    print('\n')

lista = []
size = int(input("\nEnter size of the list: \t"))

for i in range(size):
    elements = int(input("Enter the element: \t"))
    lista.append(elements)

insertion_sort(lista)



