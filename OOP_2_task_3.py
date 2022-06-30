
from pprint import pprint
import os


def recipe_list_processing(list_files: str) -> dict:

    final_dic = {}

    for item_file in list_files:

        with open(item_file, "r", encoding="utf-8") as file:
            count_line = sum(1 for line in file)
            dic_file = {}
            dic_file['count_line'] = count_line
            name = os.path.basename(item_file)
            dic_file['name'] = name

        with open(item_file, "r", encoding="utf-8") as file_1:
            index_line = 1
            for line in file_1:
                dic_file[index_line] = line.replace("\n", "")
                index_line += 1

        final_dic[dic_file['count_line']] = dic_file

    sorted_list = sorted(final_dic.keys())

    record_from_dic(final_dic, sorted_list)


def record_from_dic(final_dic, sorted_list):

    path_final_file = "C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/final_file.txt"
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


if __name__ == '__main__':
    list_files = ["C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/list_files_task_3/1.txt",
                  "C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/list_files_task_3/2.txt",
                  "C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/list_files_task_3/3.txt"]

    recipe_list_processing(list_files)
