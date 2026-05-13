from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height = ["array", 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height = ""
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height = [2.71, 1.15, 1, 56]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height = [2.71, 1.15, 1.56]
weight = [165.3, 38.4, 56.3]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, "cucu"))

height = [2.71, 1.15, 1.56]
weight = [165.3, 38.4, 56.3]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 25))
