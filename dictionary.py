
#dictionary

cities = {
    'antalya': '07', 
    'istanbul': '34',
    'izmir' : '36'
    }

cities['izmir'] = '35'
cities.update({"ankara":"06"})

print(cities)
print(cities['antalya'])
###
#Student Infos
students = {
    101: {
        "Name": "Jack",
        "Surname": "Jackson",
        "Years": 2010,
        "Notes": (80,90,100)
    },
    102: {
        "Name": "Jack1",
        "Surname": "Jackson1",
        "Years": 2011,
        "Notes": (90,90,100)
    }
}

print(f"{students[101]}")