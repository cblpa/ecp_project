# -*- coding: utf-8 -*-
import os
import search_module as sm

my_key = r"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Crypto " \
         r"Pro\Settings\Users\S-1-5-21-2348035228-4019040522-1569804633-5959\Keys"
folder = r"C:\Users\syrovatskij_dk\ecp_project"
file_extension = ".reg"
search = sm.search_file(file_extension, folder)

for file in search:
    os.system(file)

print(search)
