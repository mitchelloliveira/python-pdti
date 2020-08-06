frutas = ["banana", "uva", "morango", "cajá", "maçã", "goiaba", "jaca", "laranja"]
legumes = ["ervilha", "cenoura", "batata"]
print(frutas)

for item in frutas:
    print(item)

frutas.sort()

print(frutas)

# -------------------------

frutas.extend(legumes)
print(frutas)