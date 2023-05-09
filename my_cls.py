from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        key = record.name.value
        self.data[key] = record
        # print(f'key is {key}')

    # def search(self, search_string):
    #     search_result = []
    #     for record in self.data.values():
    #         if search_string in record.name.value:
    #             search_result.append(record)
    #         else:
    #             for phone in record.phones:
    #                 if search_string in phone.value:
    #                     search_result.append(record)
    #                     break
    #     return search_result


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value


class Name(Field):
    pass
    # def __init__(self, name):
    #     self.value = name
    #     self.name = name

    # def __str__(self) -> str:
    #     return self.name

    # def __repr__(self) -> str:
    #     return self.name


class Phone(Field):
    pass
    # def __init__(self, phone=None):
    #     self.phone = phone

    # def __str__(self) -> str:
    #     return f'{self.phone}'

    # def __repr__(self) -> str:
    #     return f'{self.phone}'


class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []

    def __str__(self) -> str:
        return f'User {self.name} have phone nymbers: {self.phones}'

    def __repr__(self) -> str:
        return f'{self.phones}'

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    # def get_name(self):
    #     return self.name.value

    # def get_phones(self):
    #     return [phone.value for phone in self._phones]


# phone1 = Phone('11')
# phone2 = Phone('67')
# phone3 = Phone('89')
# phone4 = Phone('00')
# name1 = Name('Angle')
# record1 = Record(name1)
# record1.add_phone(phone1)
# record1.add_phone(phone2)
# record1.add_phone(phone3)
# record1.edit_phone(phone1, phone4)

# address = AddressBook()
# address.add_record(record1)
# record1.edit_phone(phone2, phone4)
# print(f'-----------{type(phone2)}--------{type(phone4)}')
# address.add_record(record1)
# for tel in record1.phones:
#     print(type(tel), str(tel))
# print(record1)
# print(address)
