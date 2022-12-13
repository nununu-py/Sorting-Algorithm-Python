
# selection sort

def selection_sort(list_data: list, order: str):

    if order.lower() == "asc":

        for i in range(len(list_data)-1):

            first_num = list_data[i]

            for j in range(i + 1, len(list_data)):

                if first_num > list_data[j]:

                    first_num, list_data[j] = list_data[j], first_num

            list_data[i] = first_num

    elif order.lower() == "desc":

        for i in range(len(list_data)-1):

            first_num = list_data[i]

            for j in range(i + 1, len(list_data)):

                if first_num < list_data[j]:

                    first_num, list_data[j] = list_data[j], first_num

            list_data[i] = first_num

    else:

        list_data


# bubble sort

def bubble_sort(list_data: list, order: str):

    stop_iter = True

    if order.lower() == "asc":

        for i in range(len(list_data)-1):

            for j in range(len(list_data)-1):

                if list_data[j] > list_data[j + 1]:

                    stop_iter = False

                    list_data[j], list_data[j +
                                            1] = list_data[j + 1], list_data[j]

            if stop_iter:

                break

    elif order.lower() == "desc":

        for i in range(len(list_data)-1):

            for j in range(len(list_data)-1):

                if list_data[j] < list_data[j + 1]:

                    stop_iter = False

                    list_data[j], list_data[j +
                                            1] = list_data[j + 1], list_data[j]

            if stop_iter:

                break

    else:

        list_data
