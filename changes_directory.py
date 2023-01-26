import os


def create_directory():
    if os.path.exists('database/tel_directory.txt') is not True:
        temp = open('database/tel_directory.txt', "w", encoding="utf-8")
        # temp.writelines(first_line)
        temp.close()


def view_entry():
    """
    Просмотр записей справочника
    """
    temp_lst = []
    with open(r"database/tel_directory.txt", 'r', encoding="utf-8") as file:
        for line_numb, line in enumerate(file, start=1):
            temp_lst.append(str(line_numb) + '. ' + line[:(-1)])
    return line_numb, temp_lst


def add_entry(add_str=str):
    """
    Добавление записи справочника
    """
    with open(r"database/tel_directory.txt", "a", encoding="utf-8") as file:
        file.write(add_str)
    return


def find_entry(find_str=str):
    result_find = []
    with open(r"database/tel_directory.txt", 'r', encoding="utf-8") as file:
        for line_numb, line in enumerate(file, start=1):
            if find_str in line:
                result_find.append(str(line_numb) + '. ' + line[:(-1)])
    return result_find


def del_entry(del_line=int):
    """
    Удаление записи справочника
    """
    with open(r"database/tel_directory.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    del lines[del_line - 1]
    with open(r"database/tel_directory.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)
    pass
