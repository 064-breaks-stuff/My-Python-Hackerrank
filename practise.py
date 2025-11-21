numbers, modulo = map(int, input("").split())
lister = []

while numbers:
    count, listed = input('').split(' ',1)
    lister.append(listed)
    numbers -= 1

lister = [x.split() for x in lister]

lister = [list(map(int, sublist)) for sublist in lister]
output = 0

for i in lister:
    inter = max(i)
    inter = inter**2
    output += inter
    print(output)

#print(output)
output %= modulo
print(output)