data = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
data2 = data.split()
data3 = [len(word.rstrip('.,')) for word in data2]
print(data3)
