""" 
Created on : 04/12/22 5:22 AM
@author : ds  
"""

# https://edabit.com/challenge/ifDM26p25bqS8EsFu
# Having gotten rather sick of always being paired together in science literature, Alice and Bob
# have decided to finally settle their differences with a magical duel.
# They'll each learn some skills and then battle it out.
# Your job is to write the class Player which will handle all the combat mechanics.

class Player:

    def __init__(self, name, health, energy, armor):
        self.name = name
        self.__hp = health
        self.__maxHp = 1000
        self.__en = energy
        self.__maxEn = 1000
        self.armor = armor

    def set_hp(self, value):
        if 0 < value < self.__maxHp:
            self.__hp = value
        else:
            return "Unexpected health levels"

    def get_hp(self):
        return self.__hp

    def set_en(self, value):
        if 0 < value < self.__maxEn:
            self.__en = value
        else:
            return "Unexpected energy levels"

    def get_en(self):
        return self.__en

    def get_hpPerc(self):
        return round(self.__hp / self.__maxHp * 100, 2)









