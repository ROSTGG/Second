# import json
#
# import requests
# token = "UF3yBZifIs2ysssxEQc9CBknkGU5FWsi"
# # def update_row(**kwargs):
# #     print("hhhfhhfhhf")
# #     print(kwargs)
# #     print(f"id = {str(kwargs['id'])}")
# #     print(f"name = {str(kwargs['name'])}")
# #     res = requests.patch(
# #     f"https://api.baserow.io/api/database/rows/table/251052/{kwargs['id']}/?user_field_names=true",
# #     headers={
# #         "Authorization": f"Token {token}",
# #         "Content-Type": "application/json"
# #     },
# #     json={
# #         "tg_id": str(kwargs['tg_id']),
# #         "name": str(kwargs['name']),
# #         "find": str(kwargs['find']),
# #         "city": str(kwargs['city']),
# #         "isFind": bool(kwargs['isFind']),
# #         "link": str(kwargs['link']),
# #         "description": str(kwargs['description']),
# #         "loality": 0,
# #         "condit": "No",
# #         "status": int(kwargs['status']["id"])
# #     })
# #     print(f"fff{res}")
# #     print(f"ffft{res.text}")
# def update_row(**kwargs):
#     print("hhhfhhfhhf")
#     print(kwargs)
#     print(f"id = {str(kwargs['id'])}")
#     print(f"name = {str(kwargs['name'])}")
#     try:
#         status = kwargs['status_id']
#     except:
#         status = kwargs['status']['id']
#     res = requests.patch(
#     "https://api.baserow.io/api/database/rows/table/251052/batch/?user_field_names=true",
#     headers={
#         "Authorization": f"Token {token}",
#         "Content-Type": "application/json"
#     },
#     json={
#         "items": [
#             {
#                 "id": int(kwargs['id']),
#                 "id_tg": str(kwargs['id_tg']),
#                 "name": str(kwargs['name']),
#                 "find": str(kwargs['find']),
#                 "city": str(kwargs['city']),
#                 "isFind": bool(kwargs['isFind']),
#                 "link": str(kwargs['link']),
#                 "description": str(kwargs['description']),
#                 "loality": 0,
#                 "condit": "No",
#                 "status": int(status)
#             }
#         ]
#     })
#     return res
#
# def get_one_str(num: int):
#     up = requests.get(
#         f"https://api.baserow.io/api/database/rows/table/250967/{num}/?user_field_names=true",
#         headers={
#             "Authorization": f"Token {token}"
#         }
#     )
#     list = json.loads(up.text)
#     print(f"ID: {list['id']}, chat_id: {list['chat_id']}, first_name: {list['first_name']}, last_name: {list['last_name']}, username: {list['username']}")
# def get_all_str(id_user: str):
#     response1 = requests.get(
#         f"https://api.baserow.io/api/database/rows/table/251052/?user_field_names=true",
#         headers={
#             "Authorization": f"Token {token}"
#         }
#     )
#     list = json.loads(response1.text)
#     for i in range(list["count"]):
#         if str(list['results'][i]["id_tg"]) == str(id_user):
#             return (True, list['results'][i])
#     return (False, list)
# def get_all_bd():
#     response1 = requests.get(
#         f"https://api.baserow.io/api/database/rows/table/251052/?user_field_names=true",
#         headers={
#             "Authorization": f"Token {token}"
#         }
#     )
#     list = json.loads(response1.text)
#     return (True, list)
#     # for i in range(list["count"]):
#     #     print(f"ID: {list['results'][i]['id']}, chat_id: {list['results'][i]['chat_id']}, first_name: {list['results'][i]['first_name']}, last_name: {list['results'][i]['last_name']}, username: {list['results'][i]['username']}")
# def is_id_bool(id_user: str):
#     response1 = requests.get(
#         f"https://api.baserow.io/api/database/rows/table/251052/?user_field_names=true",
#         headers={
#             "Authorization": f"Token {token}"
#         }
#     )
#     list = json.loads(response1.text)
#     for i in range(list["count"]):
#         if str(list['results'][i]["id_tg"]) == str(id_user):
#             return (True, i, list['results'][i])
#     return (False, i, list)
#
# def new_str(tg_id: str, name: str, find: str, city: str, isFind: bool, description: str, link: str, status: int):
#     res = requests.post(
#         "https://api.baserow.io/api/database/rows/table/251052/?user_field_names=true",
#         headers={
#             "Authorization": f"Token {token}",
#             "Content-Type": "application/json"
#         },
#         json={
#             "id_tg": tg_id,
#             "name": name,
#             "find": find,
#             "city": city,
#             "isFind": isFind,
#             "link": link,
#             "description": description,
#             "loality": 0,
#             "condit": "No",
#             "status": status
#         }
#     )
#     return res
#     # print(json.loads(res.text))
#     # print(res)
# def del_str(id: int):
#     res = requests.post(
#     "https://api.baserow.io/api/database/rows/table/251052/batch-delete/",
#     headers={
#         "Authorization": f"Token {token}",
#         "Content-Type": "application/json"
#     },
#     json={
#         "items": [
#             id
#         ]
#     })
# def reg_user(mes):
#     response = requests.get(
#         f"https://api.baserow.io/api/database/rows/table/251719/?user_field_names=true",
#         headers={
#             "Authorization": f"Token {token}"
#         }
#     )
#     list = json.loads(response.text)
#     for i in range(list["count"]):
#         if str(list['results'][i]["user_id"]) == str(mes.chat.id):
#             return "None"
#     response = requests.post(
#         "https://api.baserow.io/api/database/rows/table/251719/?user_field_names=true",
#         headers={
#             "Authorization": f"Token {token}",
#             "Content-Type": "application/json"
#         },
#         json={
#             "user_id": mes.chat.id,
#             "first_name": mes.from_user.first_name,
#             "last_name": mes.from_user.last_name,
#             "username": mes.from_user.username
#         }
#     )
#     return response
#
# # add_user_bd(1651098098, "stas", "smol559", "stassmol25")
# # update_row(1651098098, "stas", "smol559", "stassmol2567", 4)
# # get_all_str()
# # get_one_str(4)
# # new_str(61850779809, "vladislav", "mansurov", "vladhero3000")
# # del_str(11)
#
# # Код ошибки	Имя	                            Описание
# # 200	        ОК	Запрос успешно выполнен.
# # 400	        Неверный запрос	                Запрос содержит недопустимые значения или JSON не удалось разобрать.
# # 401	        Несанкционированный доступ	    При попытке получить доступ к конечной точке без действительного токена базы данных.
# # 404	        Не найдено	                    Строка или таблица не найдены.
# # 413	        Объект запроса слишком большой	Запрос превысил максимально допустимый размер полезной нагрузки.
# # 500	        Внутренняя ошибка сервера	    Сервер столкнулся с непредвиденным состоянием.
# # 502	        Плохой шлюз	                    Baserow перезапускается или происходит непредвиденный сбой.
# # 503	        Сервис недоступен	            Серверу не удалось вовремя обработать ваш запрос.