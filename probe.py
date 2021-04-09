import os
old_line = ""

with open(r"27.02.21_rrr_matveev_depozitarniy.reg", "r") as reg_file:
    for line in reg_file:
        print(line)
#134 - 227
# old_id = ""
# for i in range(135, 227):
#     old_id += old_line[i]
# print(old_id)
#
# new_id = "S-1-5-21"
# with open(r"27.02.21_rrr_matveev_depozitarniy.reg", "w") as reg_file:
#     for line in reg_file:
#         if len(line) > 200:
#             line.replace(old_id, new_id)
#             print(line)