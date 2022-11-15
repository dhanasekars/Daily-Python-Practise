"""
Created on : 12/11/22 6:02 AM
@author : ds
"""

# https://edabit.com/challenge/TkbgxTEn7rxd9hmx7
import gc


class Composer:
    count = 0

    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1

    def __del__(self):
        Composer.count -= 1


print(Composer.count)
c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
c2 = Composer("Ludvig van Beethoven", 1770, "Germany")
c3 = Composer("Ludvig van Beethoven", 1770, "Germany")
c4 = Composer("Ludvig van Beethoven", 1770, "Germany")
c5 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.count)
c6 = Composer("Ludvig van Beethoven", 1770, "Germany")
c7 = Composer("Ludvig van Beethoven", 1770, "Germany")
c8 = Composer("Ludvig van Beethoven", 1770, "Germany")
c9 = Composer("Ludvig van Beethoven", 1770, "Germany")
c10 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.count)

print(type(c5))


del c10, c9, c8, c7, c6, c5, c4, c3, c2, c1
for obj in gc.get_objects():
    if isinstance(obj, Composer):
        print(obj)
        del obj


print(Composer.count)
