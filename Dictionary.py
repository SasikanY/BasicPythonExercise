scores = {'james': 1828, 'thomas': 3628, 'danny': 9310}
scores['bobby'] = 4401
numbers = {1: 'One', 2: 'Two', 3: 'Three'}
print(scores)
print(numbers)
print(scores["thomas"]) #ปริ้นบางตัว

# การอ่านข้อมูลทั้งหมดใน dictionary
for key, value in scores.items():
    print(key, value)

# อ่านเฉพาะ value อย่างเดียว
for value in scores.values():
    print(value)

# อ่านเฉพาะ key อย่างเดียว
for key in scores.keys():
    print(key)






