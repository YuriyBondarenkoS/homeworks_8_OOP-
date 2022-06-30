from operator import indexOf
from pprint import pprint
import os

file_name_1 = "C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/list_files_task_3/1.txt"
file_name_2 = "C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/list_files_task_3/2.txt"
file_name_3 = "C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/list_files_task_3/3.txt"


def recipe_list_processing(file_1: str, file_2: str, file_3: str) -> dict:

    dic_file_1 = reading_file(file_1)
    dic_file_2 = reading_file(file_2)
    dic_file_3 = reading_file(file_3)

    final_dic = {}
    final_dic[dic_file_1['count_line']] = dic_file_1
    final_dic[dic_file_2['count_line']] = dic_file_2
    final_dic[dic_file_3['count_line']] = dic_file_3

    sorted_list = sorted(final_dic.keys())

    record_from_dic(final_dic, sorted_list)


def record_from_dic(final_dic, sorted_list):

    path_final_file = "C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/list_files_task_3/final_file.txt"
    final_file = open(path_final_file, "w+")
    final_file.write(f"\n")
    index = 0

    while index < len(sorted_list):

        dic_item = final_dic[sorted_list[index]]
        final_file = open(path_final_file, "a+")
        final_file.write(f"{dic_item['name']}\n")
        final_file.write(f"{dic_item['count_line']}\n")
        index_line = 1

        for index_line in range(dic_item['count_line']):
            final_file.write(f"{dic_item[(index_line + 1)]}\n")
            index_line += 1
        index += 1

    final_file.close()


def reading_file(file_name) -> dict:

    with open(file_name, "r", encoding="utf-8") as file:
        count_line = sum(1 for line in file)
        dic_file = {}
        dic_file['count_line'] = count_line
        name = os.path.basename(file_name)
        dic_file['name'] = name

    with open(file_name, "r", encoding="utf-8") as file_1:
        index_line = 1
        for line in file_1:
            dic_file[index_line] = line.replace("\n", "")
            index_line += 1

    return dic_file


recipe_list_processing(file_name_1, file_name_2, file_name_3)
