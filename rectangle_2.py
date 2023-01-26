from rectangle_1 import Rectangle, Square, Circle

# создаем два прямоугольника
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

# создаем два квадрата:
square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

# создаем два круга:
circle_1 = Circle(6)
circle_2 = Circle(9)

print(circle_1.get_area_circle(),
      circle_2.get_area_circle())

#  все объекты переносим в единую коллекцию - figures
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

# Далее пройдемся по циклу for и применим функцию isinstance,
# поддерживающую наследование. Она проверяет, является ли аргумент
# объекта экземпляром класса или экземпляром класса из кортежа:
for figure in figures:
      if isinstance(figure,Square):
# Если экземпляр класса figure является квадратом, то вызываем метод get_area_square():
            print('Площадь квадрата: ', figure.get_area_square())
      elif isinstance(figure,Circle):
            print('Площадь круга: ', figure.get_area_circle())
      else:
            print('Площадь прямоугольника: ', figure.get_area())


