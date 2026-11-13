# https://www.youtube.com/watch?v=X6pp6MZiKAM
# How Does Python Generate A Random Name?
import random
firsts = ["John", "Jane", "Zaphod", "Terry", "Trillian", "Sarah", "David", "Olivia"]
lasts = ["Spooner", "Johnson", "Chu", "Brown", "Jones", "Cooper", "Davis", "Garcia"]
# Use a function to build 
#  a random name
def build_name():
    first = random.choice(firsts)
    last = random.choice(lasts)
    middle = random.choice(["A", "B", "C", "D", "E", "F", "G"])
    random_name = first + " " + middle + ". " + last
    return random_name
for _ in range(3):
    print(build_name())
# What if we want to generate 
#  100 random names 
#  with no duplicates?
# The set data structure 
#  is perfect for this.
# It prevents duplicates, 
#  and it is very fast.
names = set()
names_count = 100
while True:
    name = build_name()
    # print(name)
    names.add(name)
    if len(names) == names_count:
        break
print(f"We generated {len(names)} unique names.")
