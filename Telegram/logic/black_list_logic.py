from typing import List

import Telegram.bd_functions.db_user_info as bui

def add_users(tg_id, tg_id_persons: list):
    data = bui.get_line_userinfo(tg_id)
    black_list = str(data[3]).split('.')
    # black_list = []
    for i in tg_id_persons:
        ans = str(i)
        if i not in black_list:
            black_list.append(str(i))
    print(black_list)
    # black_list = '.'.join(black_list)
    # print(black_list)
    try:
        black_list.remove("NOT")
    except:
        pass
    print(black_list)
    bui.update_line_userinfo(tg_id, data[2], black_list)
    return True


def delete_users(tg_id, tg_id_persons):
    data = bui.get_line_userinfo(tg_id)
    black_list = str(data[3]).split('.')

    for tg_id_person in tg_id_persons:
        try:
            black_list.remove(str(tg_id_person))
            bui.delete_line_userinfo(tg_id_person)
        except:
            pass
    return True
def is_check_user_BL(tg_id: int, tg_id_person: int):
    data = bui.get_line_userinfo(tg_id)
    try:
        black_list = str(data[3]).split('.')
        if str(tg_id_person) in black_list:
            return False
        else:
            return True
    except:
        return True
def get_black_list(tg_id: int) -> List:
    return str(bui.get_line_userinfo(tg_id)[3]).split('.')
def is_username_in_list(username: str) -> bool:
    try:
        data = bui.get_line_userinfo_username(username)[2]
        return True
    except Exception as e:
        print("error from 'is_username_in_list': "+str(e))
        return False
def get_tgid(username: str):
    data = bui.get_line_userinfo_username(username)[1]
    return data

# bui.create_row_userinfo(1783918240, '@rm1238g', 1, '132453415.12341234')
# print(bui.get_line_userinfo(1783918240))
# add_users(1783918240, [13451345, '12351324511', 21342134])
# print(bui.get_line_userinfo(1783918240))