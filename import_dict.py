import os


def import_file():
    if os.path.exists("import_file/import_file.txt") is True:
        with open("import_file/import_file.txt", 'r', encoding="utf-8") as file_dict:
            line_temp = file_dict.readlines()
            # print(line_temp)
            # print(type(line_temp))
            if str(line_temp[0]).find('*') != -1:
                import_dict_1(line_temp)
            elif '\n' in line_temp:
                import_dict_2(line_temp)
            else:
                print("\nВложите файл в требуемом формате")
    else:
        print("\nВложите импортируемый файл в папку /import_file")


def import_dict_1(import_line):
    str_imp_line = ''
    for i in range(len(import_line)):
        str_imp_line += ' '.join(import_line[i][:-1].split(" *** ")) + '\n'
    with open("database/tel_directory.txt", 'a', encoding="utf-8") as dict_database:
        dict_database.write(str_imp_line)
    print("Импорт данных выполнен")
    return


def import_dict_2(import_line):
    str_imp_line = ''
    for i in range(len(import_line)):
        if import_line[i] == '\n':
            str_imp_line += (import_line[i])
        else:
            str_imp_line += (import_line[i][:-1]) + ' '
    # print(str_imp_line)
    with open("database/tel_directory.txt", 'a', encoding="utf-8") as dict_database:
        dict_database.write(str_imp_line + '\n')
        print("Импорт данных выполнен")
    return
