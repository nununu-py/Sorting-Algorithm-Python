from native_sorting import selection_sort, bubble_sort

my_number = [13, 1, 7, 3, 2, 3, 12, 4]
my_string = ["nunu", "rajes", "denis", "jek", "bayu"]

# selection sort
print("Data before Sorting", my_number)
print("Data before Sorting", my_string)

selection_sort(my_number, "asc")
selection_sort(my_string, "desc")

print("Selection Sort Result Ascending : ", my_number)
print("Selection Sort Result Descending: ", my_string)

print()

# bubble sort
my_number = [13, 1, 7, 3, 2, 3, 12, 4]
my_string = ["nunu", "rajes", "denis", "jek", "bayu"]

print("Data before Sorting", my_number)
print("Data before Sorting", my_string)

bubble_sort(my_number, "asc")
bubble_sort(my_string, "desc")

print("Bubble Sort Result Ascending : ", my_number)
print("Bubble Sort Result Desending : ", my_string)
