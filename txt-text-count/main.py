with open(r"txt-text-count\sample.txt","r") as f:
    data = f.read()

array = []

for i in data.split(" "):
    array.append(i)

print(len(array))

