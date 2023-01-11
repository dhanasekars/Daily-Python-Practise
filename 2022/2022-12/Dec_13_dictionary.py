""" 
Created on : 13/12/22 4:58 AM
@author : ds

"""


class DictionaryClass:

    def __init__(self):
        self.keytocheck = None
        self.dict_in = None
        self.result = {}
        pass

    def set_input(self, dict_in: dict, keytocheck):
        self.dict_in = dict_in
        self.keytocheck = keytocheck

    def get_details(self):
        return self.dict_in, self.keytocheck

    def has_key(self):
        # https://edabit.com/challenge/zdo6JCL6Z5d2fT8JB
        return self.keytocheck in self.dict_in

    def swap_dict(self):
        # https://edabit.com/challenge/JgD9KHBYrDnKrGJ7a
        for key, value in self.dict_in.items():
            self.result.setdefault(value, []).append(key)
        return self.result
