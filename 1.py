my_id = "privet_Petia"
try:
    test_file = open("test.reg", "w")
    with open(r"09.02.21 RR Your Choice Berezhnoy.reg", encoding='utf_16', errors='replace') as file:
        user_id = ""
        for i, line in enumerate(file, 1):
            # print(i, ": ", line)
            if i == 3:
                for j, word in enumerate(line, 1):
                    if 67 < j < 114:
                        user_id += word
                    # print(j, ":", word)
                line = line.replace(user_id, my_id)
                print(line)
            test_file.writelines(line)
    test_file.close()
except IOError:
    print('Error')

print(user_id)

