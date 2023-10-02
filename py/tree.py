def insert_element(lst, position, element):
    lst.insert(position, element)

def find_element_index(lst, element):
    try:
        index = lst.index(element)
        return index
    except ValueError:
        return -1

def remove_element(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)

def get_previous_and_next_elements(lst, index):
    previous_element = None
    next_element = None
    if 0 <= index < len(lst):
        if index > 0:
            previous_element = lst[index - 1]
        if index < len(lst) - 1:
            next_element = lst[index + 1]
    return previous_element, next_element

def merge_lists(list1, list2):
    return list1 + list2

def sort_list(lst):
    lst.sort()  

def merge_sorted_lists(list1, list2):
    merged_list = []
    a = 0
    b = 0

    while a < len(list1) and b < len(list2):
        if list1[a] < list2[b]:
            merged_list.append(list1[a])
            a += 1
        else:
            merged_list.append(list2[b])
            b += 1

    merged_list.extend(list1[a:])
    merged_list.extend(list2[b:])
    return merged_list

my_list = [1, 2, 3, 4, 5]
insert_element(my_list, 2, 6)
print(my_list)  

element_index = find_element_index(my_list, 3)
print(f"Елемент 3 має індекс {element_index}")

remove_element(my_list, 1)
print(my_list) 

prev, next = get_previous_and_next_elements(my_list, 2)
print(f"Попередній елемент: {prev}, Наступний елемент: {next}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print(merged_list)  
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sort_list(my_list)
print(my_list)  

sorted_list1 = [1, 3, 5, 7]
sorted_list2 = [2, 4, 6, 8]
merged_sorted_list = merge_sorted_lists(sorted_list1, sorted_list2)
print(merged_sorted_list)  