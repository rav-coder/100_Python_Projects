
empty_dict = {} # use it to initialize or also wipe a dictionary

new_dict = {
    "name":"John",
    "amount":0
}

new_dict["address"] = "Checking"

print(new_dict["amount"])

new_dict["address"] = "Testing"

for smth in new_dict:
    print(smth)
    print(new_dict[smth])

print(new_dict)

####################

student_scores = {
    "Aaron": 81,
    "Barry": 64,
    "Harr": 94,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds expectation"
    else:
        student_grades[key] = "Acceptable"

print(student_grades)

############### Nesting
 
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": {
        "cities_visited":["Paris","Lille"],
        "total_visits": 2,
    },
    "Germany": {
        "cities_visited":["Berlin","Hamburg"],
        "total_visits": 3,
    }
}

travel_log_list = [
    {
        "country":"France",
        "cities_visited":["Paris","Lille"],
        "visits": 2,
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg"],
        "visits": 5,
    },
]

def add_new_country(country,visits,cities):
    new_dict = {}

    new_dict["country"] = country
    new_dict["cities_visited"] = cities
    new_dict["visits"] = visits

    travel_log_list.append(new_dict)

add_new_country("Russia",2,["Moscow","Saint"])

print(travel_log_list)
