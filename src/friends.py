def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            return True
    return False

def add_friend(person, new_friend):
    person["friends"].append(new_friend)

def remove_friend(person, old_friend):
    person["friends"].remove(old_friend)

def total_money(people):
    total_money = 0
    for person in people:
        total_money += person["monies"]
    return total_money
    
def lend_money(person_1, person_2, amount):
    person_1["monies"] -= amount
    person_2["monies"] += amount

def all_favourite_foods(people):
    foods = []
    for person in people:
        foods += person["favourites"]["snacks"]
    return foods

def find_no_friends(people):
    no_friends = []
    for person in people:
        if len(person["friends"]) == 0:
            no_friends.append(person)
    return no_friends

