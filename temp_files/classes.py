# from temp_files.baserow import *
#
#
# class Client():
#     def __init__(self, *args, **kwargs):
#         self.data = kwargs
#         self.add = args
#         self.data['condid'] = self.find()[-1]
#
#
#     def find(self, search: str = 'None'):
#         list = self.data
#         cs = []
#         oppsite_list = get_all_bd()[-1]["results"]
#         listr = []
#         print(oppsite_list)
#         for i in oppsite_list:
#             if i['city'] == list['city']:
#                 cs.append(i['id_tg'])
#                 listr.append(i)
#             if i['find'] == list['find']:
#                 self.data['condid'] = i['id_tg']
#                 cs.append(i['id_tg'])
#                 listr.append(i)
#             if i['find'] == search:
#                 self.data['condid'] = i['id_tg']
#                 cs.append(i['id_tg'])
#                 listr.append(i)
#         if len(cs) != 0:
#             return ('200', cs, listr)
#
#         if len(cs) != 0:
#             i = []
#             for l in cs:
#                 i.append(l['id_tg'])
#                 listr.append(i)
#             self.data['condid'] = ", ".join(i)
#             return ('201', cs ,listr)
#         else:
#             return ('404', 'No coincidence', ["error"])
#
#     def search(self, search: str = 'None'):
#         list = self.data
#         cs = []
#         oppsite_list = get_all_bd()[-1]["results"]
#         listr = []
#         print(oppsite_list)
#         for i in oppsite_list:
#             if i['find'] == search:
#                 self.data['condid'] = i['id_tg']
#                 if i["isFind"] == True:
#                     cs.append(i['id_tg'])
#                     listr.append(i)
#         if len(listr) != 0:
#             return ('200', cs, listr)
#         else:
#             return ('404', 'No coincidence', ["error"])
#
#     def get_info(self):
#         return f"Имя - {self.data['name']}\nИнструмент - {self.data['find']}\nГород - {self.data['city']}\nСайт - {self.data['link']}\nОписание - {self.data['description']}\nЛояльность - {self.data['loality']}\n{(lambda a, b, c: a if c else b)('Аккаунт активен ( для заморозки пропишите /isfind )', 'Аккаунт заморожен( для разморозки пропишите /isfind )', self.data['isFind']) }\n"
#
#
#     def reset(self, *args, **kwargs):
#         self.data = kwargs
#         self.add = args
#
#     def upload(self):
#         return self.data
#
