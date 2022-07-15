from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf=8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

pattern = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
number = r"+7(\2)\3-\4-\5\6\7"

def filter():
  dirty_list = []
  clean_list = []
  for item in contacts_list:
    full_name = ' '.join(item[:3]).split(' ')
    result = [full_name[0], full_name[1], full_name[2], item[3], item[4], re.sub(pattern, number, item[5]), item[6]]
    dirty_list.append(result)
  for trash in dirty_list:
    for words in trash:
      if len(words) == 0:
        trash.remove(words)
    clean_list.append(trash)
  return clean_list


#print(filter())

def duplicates(employees_list):
  phone_book = dict()
  for contacts in employees_list:
    if contacts[0] in phone_book:
      contact_value = phone_book[contacts[0]]
      for i in range(len(contact_value)):
        if contacts[i]:
          contact_value[i] = contacts[i]
    else:
      phone_book[contacts[0]] = contacts
  return list(phone_book.values())

pprint(duplicates(filter()))


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

with open("phonebook_clear.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  #Вместо contacts_list подставьте свой список
  datawriter.writerows(duplicates(filter()))  