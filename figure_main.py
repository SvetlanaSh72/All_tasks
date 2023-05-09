from figures import Rectangle,Сircle

# прямоугольники
rect_1 = Rectangle(5,10)
rect_2 = Rectangle(50,100)
print('===============================')
print('прямоугольник_1 имеет Р (периметр) =',rect_1.get_perim_rect())
print('прямоугольник_2 имеет Р (периметр) =',rect_2.get_perim_rect())
print('===============================')


# два круга
circl_1 = Сircle(10)
circl_2 = Сircle(20)
print('длина окружности_1 L =',int(circl_1.get_circle_l()))
print('длина окружности_2 L =',int(circl_2.get_circle_l()))
print('===============================')

#выведем атрибуты
rect = [rect_1.width, rect_1.height,rect_2.width, rect_2.height]
circl = [circl_1.radius, circl_2.radius]

print('Rectangle:')
print(', '.join(map(str, rect)))
print('Сircle:')
print(', '.join(map(str, circl)))
