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


def replase_user(file_reg, id):
    with open(file_reg, encoding="UTF-16") as file:
        new_line = ""
        for line in file:
            if r"[HKEY_LOCAL_MACHINE" in line:
                user_id = line.split("\\")[6]
                line = line.replace(user_id, id)
            new_line += line
    with open(file_reg, "w", encoding='cp1251') as file:
        for line in new_line:
            file.writelines(line)
