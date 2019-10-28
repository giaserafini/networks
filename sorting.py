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
    print('\nThe sorted list: \t', reversed(sorted_list))
    print('\n')

lista = []
size = int(input("\nEnter the size of the list: \t"))

for i in range(size):
    elements = int(input("Enter the element: \t"))
    lista.append(elements)

insertion_sort(lista)

def insertion_sort_d(sorted_list_d): #why you don't want to work???
    for i in range(1, len(sorted_list_d)):
        key = sorted_list_d[i]
        j=i-1
        while j>=0 and key <sorted_list_d[j]:
            sorted_list_d[j + 1] = sorted_list_d[j]
            j -=1
        sorted_list_d[j+1] = key
    print('\nThe sorted list is: \t', sorted_list_d.reverse())
    print('\n')


listad = []
size = int(input("\nEnter the size of the list: \t"))

for i in range(size):
    elements = int(input("Enter the element: \t"))
    listad.append(elements)

insertion_sort(listad)

#wiem dlaczego to nie chce sortowac na odwrót  - z jakiegos powodu wywoluje 2 razy te 1 funkcje
#dalam w tej 1 2 wywlania i wywala jakis dziwny blad :(
