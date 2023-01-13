# Global Scope
health = 1

def drink_potion():
    health = 3
    
drink_potion()

print(health) # will print 1 because the health variable inside the function is a completely new variable

# Modifying Global Scope
def drink_potion():
    global health # it is not recommended to modify variable with global scope
    health = 3
    
drink_potion()

print(health) # will print 3 now

# There is no block scope in python
# if, while, for blocks do not have scope
enemies = ["Skeleton","Zombie","Alien"]
game_level = 3

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # will print skeleton

# A function will have a local scope though
def create():
    if game_level < 5:
        new_enemy_1 = enemies[0]

print(new_enemy_1) # now we can not access this variable, function local scope

URL = "https://www.google.com" # constants
