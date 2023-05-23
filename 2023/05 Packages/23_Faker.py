""" 
Created on : 22/05/23 2:30 pm
@author : ds  
"""

from faker import Faker
from faker.providers import internet

faker = Faker()


print(faker.job())
print(faker.date_of_birth(minimum_age=18, maximum_age=65))


for _ in range(5):
    print(faker.name())
    # print(faker.pydict())


faker.add_provider(internet)

print(faker.ipv4_private())