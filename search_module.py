import os


def search_file(file_extension, folder):
    '''
    Функция поиска файлов в директиории folder и во вложенных папках, по расширению файла file_extension.
    :param file_extension: расширение фалй с точкой. Пример: .rar
    :param folder: Путь до директории
    :return: лист с найденными фалами в формает полного пути до файла.
    '''
    result = []
    for path, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(file_extension):
                result.append("\"" + os.path.join(path, file) + "\"")
    return result
