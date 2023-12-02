# Part 1
def getnumbers(s):
    nums = []
    for i in s:
        if i.isdigit(): nums.append((i))
    return nums        

data = open("calibration_doc.txt")

sum = 0
for line in data:
    linenums = getnumbers(line)
    result = linenums[0] + linenums[-1]
    sum += int(result)
print(sum)   