

def export_directory_1():
    """
    Тут нужна функция (создающая и копирующая)/(перезаписвающая) записи
    из database/telephone_directory.txt в /export/export_telephone_directory_v1.txt
    в файле на одной строке хранится одна часть записи, пустая строка - разделитель
    Фамилия_1
    Имя_1
    Телефон_1
    Описание_1
    <пустая строка>
    Фамилия_2
    Имя_2
    Телефон_2
    Описание_2
    <пустая строка>
    и т.д.
    """
    with open(r"database/tel_directory.txt", 'r', encoding="utf-8") as file_dict:
        file_export = open("export_file/dict_export_ver1.txt", 'w', encoding="utf-8")
        line_temp = file_dict.readline()
        while line_temp:
            lst_temp = line_temp.split()
            line = str(lst_temp[0] + '\n'
                       + lst_temp[1] + '\n'
                       + lst_temp[2] + '\n'
                       + lst_temp[3] + '\n' + '\n')
            file_export.write(line)
            line_temp = file_dict.readline()
        file_export.close()
    return


def export_directory_2():
    """
    Тут нужна функция (создающая и копирующая)/(перезаписвающая) записи
    из database/telephone_directory.txt в /export/export_telephone_directory_v2.txt
    или в файле на одной строке хранится все записи, символ разделитель - *;***
    .
    Фамилия_1,Имя_1,Телефон_1,Описание_1
    Фамилия_2,Имя_2,Телефон_2,Описание_2
    и т.д.
    """
    with open(r"database/tel_directory.txt", 'r', encoding="utf-8") as file_dict:
        file_export = open("export_file/dict_export_ver2.txt", 'w', encoding="utf-8")
        line_temp = file_dict.readline()
        while line_temp:
            lst_temp = line_temp.split()
            line = str(lst_temp[0] + ' *** '
                       + lst_temp[1] + ' *** '
                       + lst_temp[2] + ' *** '
                       + lst_temp[3] + '\n')
            file_export.write(line)
            line_temp = file_dict.readline()
        file_export.close()
    return
