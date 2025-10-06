# tal1 = float(input("Ange det första talet: "))
# tal2 = float(input("Ange det andra talet: "))

# Beräkna medelvärdet
# medelvärde = (tal1 + tal2) / 2

# Skriv ut medelvärdet avrundat till 2 decimaler
# print(f"Medelvärdet är: {round(medelvärde, 2)}")


# age = int(input('Hej och välkomen till mitt program. '
# 'Var snäll och skriv din ålder:\n'))


# if age <= 0:
#     print('Var snäll och skriv i rätt format!')
    
# elif age < 13:
#     print('Du är ugn')
# elif age < 18:
#     print('Du är tonåriing!')
# elif age > 18:
#     print('Du är vuxen!')
# elif age <= 64:
#     print('Du är vuxen!')
# else:
    # print('Du är pansionär!')


# age = int(input('Hej och välkommen till mitt program. '
#                 'Var snäll och skriv din ålder:\n'))

# if age <= 0:
#     print('Var snäll och skriv i rätt format!')
# elif age < 13:
#     print('Du är ung!')
# elif age < 18:
#     print('Du är tonåring!')
# elif age <= 64:
#     print('Du är vuxen!')
# else:
#     print('Du är pansionär!')


superheroes = [
    "Spider-Man",
    "Wonder Woman",
    "Batman",
    "Iron Man",
    "Captain America",
    "Black Panther",
    "Hulk",
    "Thor",
    "Flash",
    "Superman"
]

powers = [
    "Super strength, agility, spider-sense",
    "Super strength, flight, combat skills",
    "Genius intellect, martial arts, gadgets",
    "Genius intellect, powered armor suit",
    "Enhanced strength, agility, shield mastery",
    "Enhanced strength, agility, advanced technology",
    "Super strength, invulnerability, regeneration",
    "Godly strength, lightning manipulation, flight",
    "Super speed, time manipulation",
    "Super strength, flight, heat vision, invulnerability"
]

for powers in range(len(superheroes)):
    print(powers, superheroes[powers])