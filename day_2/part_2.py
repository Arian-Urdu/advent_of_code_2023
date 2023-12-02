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



input = open("input.txt")

input_clean = []

for games in input:
    input_clean.append(get_rgb(games))


red_cubes = 0
green_cubes = 0
blue_cubes = 0
power = 0
sum = 0

for i, one_game in enumerate(input_clean):
    
    red_cubes = 0
    green_cubes = 0
    blue_cubes = 0
    power = 0

    for pull in one_game:
        if pull[0] > red_cubes: 
            red_cubes = pull[0]

        if pull[1] > green_cubes: 
            green_cubes = pull[1]

        if pull[2] > blue_cubes: 
            blue_cubes = pull[2]

    power = red_cubes * blue_cubes * green_cubes
    sum += power
   
print(sum)    
    