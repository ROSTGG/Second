import Telegram.bd_functions.db_user_info as bui

def add_users(tg_id, tg_id_persons: list):
    data = bui.get_line_userinfo(tg_id)
    black_list = str(data[4]).split('.')
    for i in tg_id_persons:
        ans = str(i)
        if i not in black_list:
            black_list.append(str(i))
    black_list = '.'.join(black_list)
    print(black_list)
    bui.update_line_userinfo(tg_id, data[2], data[3], black_list)
    return True


def delete_users(tg_id, tg_id_persons):
    data = bui.get_line_userinfo(tg_id)
    black_list = str(data[3]).split('.')

    for tg_id_person in tg_id_persons:
        try:
            black_list.remove(str(tg_id_person))
        except:
            pass
    return True
def is_check_user_BL(tg_id, tg_id_person):
    data = bui.get_line_userinfo(tg_id)
    try:
        black_list = str(data[3]).split('.')
        if str(tg_id_person) in black_list:
            return False
        else:
            return True
    except:
        return True


bui.create_row_userinfo(1783918240, '@rm1238g', 1, '132453415.12341234')
print(bui.get_line_userinfo(1783918240))
add_users(1783918240, [13451345, '12351324511', 21342134])
print(bui.get_line_userinfo(1783918240))