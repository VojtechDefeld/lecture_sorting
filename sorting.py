import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data


def selection_sort(list):
    for i in range(len(list)):
        min_ind = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_ind]:
                min_ind = j
        (list[i], list[min_ind]) = (list[min_ind], list[i])

    return list


def bubble_sort(list):
    for i in range(0, len(list)-1):
        for j in range(len(list)-1):
            if (list[j]>list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list


def insertion_sort(list):
    if (n := len(list)) <= 1:
        return
    for i in range(1, n):
        key = list[i]
        j = i-1
        while j >=0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

    return list



def main():
  my_data = read_data("numbers.csv")
  column = my_data["series_3"]
  print(insertion_sort(column))



if __name__ == '__main__':
    main()
