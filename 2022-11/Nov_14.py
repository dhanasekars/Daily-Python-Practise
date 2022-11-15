""" 
Created on : 13/11/22 6:00 AM
@author : ds  
"""

# continue with Nov_13
# Fix unit tests
# find ways to delete all the instances of a class
import gc


class Composer:
    count = 0
    instances = []

    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1

    def __del__(self):
        print(f"deleted {self}")
        Composer.count -= 1


print(Composer.count)
c = Composer("Ludvig van Beethoven", 1770, "Germany")
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

# Learning the objects instances are destroyed automatically,
# this was found after I added a print statement in the __del__ method
# So there is no test file created for this exercise.
