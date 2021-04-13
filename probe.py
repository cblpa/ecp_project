import os
from pprint import pprint


def search_file(file_extension, folder):
    '''
    Функция поиска файлов в директиории folder и во вложенных папках, по расширению файла file_extension.
    :param file_extension: расширение фалй с точкой. Пример: .rar
    :param folder: Путь до директории
    :return: лист с найденными фалами в формает полного пути до файла.
    '''
    result = {}
    for path, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(file_extension):
                result[file] = path + "\\"
    return result

folder = r"C:\Users\syrovatskij_dk\ecp_project\1"
files = search_file(".reg", folder)
my_id = 'S-1-5-21-2348035228-4019040522-1569804633-5959'
finish_file = []


for i, file in enumerate(files.keys(), 1):
    new_file = folder + "\\" + str(i) + ".reg"
    new_line = ""
    with open(files[file] + file, encoding='UTF-16') as f:
        for line in f:
            if r"HKEY_LOCAL_MACHINE\SOFTWARE" in line:
                user_id = line.split("\\")[6]
                if user_id != my_id:
                    line = line.replace(user_id, my_id)
            new_line += line
    with open(folder + "\\" + str(i) + ".reg", 'w') as ff:
        for line in new_line:
            ff.writelines(line)
        finish_file.append(new_file)
pprint(finish_file)
for file in finish_file:
    os.system(file)
