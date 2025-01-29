pole = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print("Původní pole:")
for radek in pole:
    print(radek)


pole[1][1] = 105


pole.append([100, 110, 120, 130])


for radek in pole:
    radek.append(0)


print("Upravené pole:")
for radek in pole:
    print(radek)
