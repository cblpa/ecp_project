def replace_server(file_rdp, server_name):
    '''
    Редактирование ярлыка РДП, меняем имя сервера в двух местах
    :param file_rdp: рпд ярлык
    :param server_name: на что меняем
    :return: ничего не возвращает, перезаписывает открытый файл
    '''
    with open(file_rdp) as file:
        nsx = "nsx-lb1.mof.local"
        new_line = []
        for line in file:
            if nsx in line:
                line = line.replace(nsx, server_name)
            new_line.append(line)
    with open(file_rdp, "w") as file:
        for line in new_line:
            file.writelines(line)

my_id = "S-1-5-21-2348035228-4019040522-1569804633-5959"
with open(r"test_file.reg", encoding="UTF-16") as file:
    new_line = ""
    user_id = ""
    for line in file:
        if "[HKEY" in line:
            for i, word in enumerate(line, 1):
                if 67 < i and i != '"\"':
                    user_id += word
            print(user_id)
            line = line.replace(user_id, my_id)
        new_line += line
with open(r"test_file.reg", "w") as file:
    for line in new_line:
        file.writelines(line)