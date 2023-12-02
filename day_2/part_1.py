import re


def get_rgb(s):
    rgbs = []
    # remove game
    no_game = s.split(":")[1]

    for i in no_game.split(";"):
        # [red,green,blue]
        array = []

        red = re.search(r"\d+?(?=\s?red?\b)",i)
        if red:
            array.append(int(red.group()))
        else:
            array.append(0) 

        green = re.search(r"\d+?(?=\s?green?\b)",i)
        if green:
            array.append(int(green.group()))
        else:
            array.append(0) 

        blue = re.search(r"\d+?(?=\s?blue?\b)",i)
        if blue:
            array.append(int(blue.group()))
        else:
            array.append(0)     

        rgbs.append(array)   

    return rgbs

red_cubes = 12
green_cubes = 13
blue_cubes = 14

input = open("input.txt")

input_clean = []
possible_games = 0
id_sum = 0

for games in input:
    input_clean.append(get_rgb(games))

for i, one_game in enumerate(input_clean):
    valid = False

    for pull in one_game:
        if pull[0] <= red_cubes and pull[1] <= green_cubes and pull[2] <= blue_cubes: 
            valid = True
        else: 
            valid = False
            break

    if valid: 
        possible_games += 1  
        id_sum += (i+1)


print(possible_games)    
print(id_sum)    
    