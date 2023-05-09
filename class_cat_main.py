from class_cat import Cat
cats = [
    {
    "name": "Барон",
    "gender": "мальчик",
    "age": 2,
    },
    {
    "name": "Сэм",
    "gender": "мальчик",
    "age": 2,
    }
]
print('----------------------------------------')
print('Животное  -  Имя  -  Пол  -  Возраст')
num = 0
for cat in cats:
    num=num+1
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)

    print('----------------------------------------')
    print(num,'. Кот  -  ',cat_obj.name,'  -  ',cat_obj.gender,'  -  ',cat_obj.age)
