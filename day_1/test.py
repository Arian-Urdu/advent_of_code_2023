s = "8ninejseven"

letter_to_num = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
}

def getnumbers(s):
    # will add all found nums in list
    nums = []
    
    for i in range(0,len(s)):
        # is a digit -> just add to list
        if s[i].isdigit(): nums.append(s[i])
        else:
            word = ""
            for j in range(0,5):
                try:
                    word += s[i + j]
                except IndexError as ie:
                    do_nothing1 = ie    
                try:
                    nums.append(letter_to_num[word])
                except  KeyError as ke:
                    do_nothing2 = ke
    return nums  


sum = 0
linenums = getnumbers(s)
result = linenums[0] + linenums[-1]
sum += int(result)
print(sum) 