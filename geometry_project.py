import math
import os
import tkinter.colorchooser
from tkinter import *
from tkinter import messagebox as mb

# import key_base


version = 'v0.6'

try:
    file = open('File_Setting.txt', 'r')

    color_text = file.read().lower().split()

    check_none = 'none'

    if any(word in check_none for word in color_text):
        first_color = '#60493C'

        second_color = '#B2A7A0'

        third_color = '#D1C4BA'

        fourth_color = '#FFC98F'

        fifth_color = '#C38152'

    else:

        first_color = color_text[0]  # Цвет фона

        second_color = color_text[1]  # Цвет заголовка

        third_color = color_text[2]  # Цвет обычного текста

        fourth_color = color_text[3]  # Цвет кнопки

        fifth_color = color_text[4]  # Цвет фигур

    file.close()
except FileNotFoundError as ex:
    print(ex.strerror)
    first_color = '#60493C'

    second_color = '#B2A7A0'

    third_color = '#D1C4BA'

    fourth_color = '#FFC98F'

    fifth_color = '#C38152'


def visible_choose_subject_func():  # Показ окна с выбором предмета
    # Всё, что показываем:
    choose_subject_window.deiconify()
    # Всё, что скрываем:
    greet_window.withdraw()
    choose_geometry_window.withdraw()


def visible_geometry_window_func():  # Показ окна с геометрией
    # Всё, что показываем:
    choose_geometry_window.deiconify()
    # Всё, что скрываем:
    choose_subject_window.withdraw()
    choose_figure_window.withdraw()
    figure_window.withdraw()
    perevod_ed_window.withdraw()


def visible_choose_figure_window_func():  # Показ окна с выбором фигур
    # Всё, что показываем:
    choose_figure_window.deiconify()
    # Всё, что скрываем:
    choose_geometry_window.withdraw()
    axioms_window.withdraw()
    theorems_window.withdraw()
    figure_window.withdraw()
    calculate_triangle_window.withdraw()


def visible_greet_window_func():  # Показ главного окна
    # Всё, что показываем:
    greet_window.deiconify()
    # Всё, что скрываем:
    choose_subject_window.withdraw()
    choose_geometry_window.withdraw()


def visible_perevod_ed_window_func():
    # Всё, что показываем:
    perevod_ed_window.deiconify()
    # Всё, что скрываем:
    choose_geometry_window.withdraw()


def visible_calculate_triangle_window_func():  # Открытие окна c расётами треугольника
    # Всё, что показываем:
    calculate_triangle_window.deiconify()
    figure_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()


def visible_calculate_square_window():  # показ окна с расчётами прямоугольника
    # Всё, что показываем:
    calculate_square_window.deiconify()
    figure_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()


def visible_calculate_rectangle_window_func():  # показ окна с расчётами квадрата
    # Всё, что показываем
    calculate_rectangle_window.deiconify()
    figure_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()


def visible_triangle_window_event_func(event):  # Открытие окна с треугольником через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    theorems_window.withdraw()
    axioms_window.withdraw()

    formuls_window.withdraw()
    calculate_triangle_window.withdraw()
    # Всё что создаём
    figure_window.title('Треугольник')

    definition_figure_label.config(text='Треугольник - это геометрическая фигура, \n образованная тремя пересекающимися прямыми, \n образующими три внутренних угла')

    calculations_figure_button.config(text='Калькулятор треугольника', command=visible_calculate_triangle_window_func)

    axioms_figure_button.config(text='Аксиомы треугольника', command=visible_axioms_triangle_window_func)

    theorems_figure_button.config(text='Теоремы треугольника', command=visible_theorems_triangle_window_first_func)

    formulas_figure_button.config(text='Формулы треугольника', command=visible_formuls_triangle_func)


def visible_theorems_triangle_window_first_func():  # 1 стр аксиом треугольника
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()

    # Всё, что создаём
    title_theorem_label.config(text='Теоремы треугольника: 1 стр.')

    first_theorem_label.config(text='1.Сумма углов треугольника равна 180 градусам.')

    second_theorem_label.config(text='2.В треугольнике: \n1) против большей стороны лежит больший угол; \n2) обратно, против большего угла лежит большая сторона.')

    third_theorem_label.config(text='3.В прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов катетов.')

    fourth_theorem_label.config(text='4.Если квадрат одной стороны треугольника равен сумме квадратов двух \nдругих сторон, то треугольник прямоугольный.')

    fifth_theorem_label.config(text='5.Высоты треугольника (или их продолжения) пересекаются в одной точке.')

    sixth_theorem_label.config(text='6.Площадь треугольника равна половине произведения двух его сторон на синус угла \nмежду ними.')

    seventh_theorem_label.config(text='7.Стороны треугольника пропорциональны синусам противолежащих углов.')

    eight_theorem_label.config(text='8.Квадрат стороны треугольника равен сумме квадратов двух других сторон минус \nудвоенное произведение этих сторон, умноженное на косинус угла между ними.')

    first_theorems_page_button.config(command=visible_theorems_triangle_window_first_func)
    second_theorems_page_button.config(command=visible_theorems_triangle_window_second_func)
    second_theorems_page_button.place(x=320, y=460)

    first_theorem_label.grid()
    second_theorem_label.grid()
    third_theorem_label.grid()
    fourth_theorem_label.grid()
    fifth_theorem_label.grid()
    sixth_theorem_label.grid()
    seventh_theorem_label.grid()
    eight_theorem_label.grid()

    back_triangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_triangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_triangle_theorems_button.bind('<Button-1>', visible_triangle_window_event_func)


def visible_theorems_triangle_window_second_func():  # 2 стр аксиом треугольника
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()

    # Всё, что создаём
    title_theorem_label.config(text='Теоремы треугольника: 2 стр.')

    first_theorem_label.config(text='9.Если две стороны и угол между ними одного треугольника соответственно равны двум \nсторонам и углу между ними другого треугольника, то такие треугольники равны.')

    second_theorem_label.config(text='10.Если сторона и два прилежащих угла одного треугольника соответственно равны стороне\nи двум прилежащим углам другого треугольника, то такие треугольники равны.')

    third_theorem_label.config(text='11.Если три стороны одного треугольника соответственно равны трем сторонам другого \nтреугольника, то такие треугольники равны.')

    fourth_theorem_label.config(text='12.Внешний угол треугольника равен сумме двух углов треугольника, не смежных с ним.')

    fifth_theorem_label.config(text='13.В равнобедренном треугольнике биссектриса, проведённая к основанию,\nявляется медианой и высотой.')

    sixth_theorem_label.config(text='14.Если в треугольнике два угла равны, то треугольник равнобедренный.')

    seventh_theorem_label.config(text='15.Если в треугольнике высота является медианой или биссектрисой, то треугольник \nравнобедренный.')

    eight_theorem_label.grid_remove()

    back_triangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_triangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_triangle_theorems_button.bind('<Button-1>', visible_triangle_window_event_func)


def visible_axioms_triangle_window_func():  # Показ окна с аксиомами треугольника
    # Всё, что показываем:
    axioms_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём
    title_axioms_label.config(text='Аксиомы треугольника: ')

    first_axioms_label.config(text='1.Каков бы ни был треугольник, существует равный ему треугольник в заданном \n  расположении относительно данной полупрямой.')

    back_triangle_axioms_button = Button(axioms_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_triangle_axioms_button.place(x=10, y=460)  # Кнопка назад
    back_triangle_axioms_button.bind('<Button-1>', visible_triangle_window_event_func)


def visible_formuls_triangle_func():  # Показ окна с формулами треугольника
    # Всё, что показываем
    formuls_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём

    title_formulas_label.config(text='Формулы треугольника: ')

    first_formulas_label.config(text='Формулы для нахождения площади:\n   S = ½bh, \n   S = ½ab ⋅ sin(α)\n   S=√(p·(p-a)·(p-b)·(p-c))')

    second_formulas_label.config(text='Формула для нахождения суммы углов:\n   α + β + γ = 180°')

    third_formulas_label.config(text='Синусы:\n   a / sin α = b / sin β = c / sin γ = 2R')

    fourth_formulas_label.config(text='Косинус:\n   a² = b² + с² - 2ab * cos α\n   b² = a² + c² - 2ac * cos β\n   c² = a² + b² - 2ab * cos γ')

    fifth_formulas_label.config(text='Формула для нахождения периметра:\n   P = a + b + c')

    first_formulas_label.grid()
    second_formulas_label.grid()
    third_formulas_label.grid()
    fourth_formulas_label.grid()
    fifth_formulas_label.grid()

    back_formulas_triangle_button = Button(formuls_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_formulas_triangle_button.place(x=10, y=460)  # Кнопка назад
    back_formulas_triangle_button.bind('<Button-1>', visible_triangle_window_event_func)


def visible_square_window_event_func(event):  # Открытие окна с прямоугольником через event
    # Всё, что показываем
    figure_window.deiconify()
    # Всё, что скрываем:
    axioms_window.withdraw()
    theorems_window.withdraw()
    formuls_window.withdraw()
    calculate_square_window.withdraw()

    # Всё что создаём
    figure_window.title('Прямоугольник')

    definition_figure_label.config(text='Прямоугольник — четырехугольник, \nу которого все углы прямые (равны 90 градусам)')
    calculations_figure_button.config(text='Калькулятор прямоугольника', command=visible_calculate_square_window)

    axioms_figure_button.config(text='Аксиомы прямоугольника', command=visible_axioms_square_window_func)

    theorems_figure_button.config(text='Теоремы прямоугольника', command=visible_theorems_square_window_first_func)

    formulas_figure_button.config(text='Формулы прямоугольника', command=visible_formuls_square_func)


def visible_theorems_square_window_first_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()

    # Всё, что создаём

    title_theorem_label.config(text='Теоремы прямоугольника: ')

    first_theorem_label.config(text='1.Диагонали прямоугольника равны.')
    second_theorem_label.config(text='2.Если в четырехугольнике диагонали равны и точкой пересечения делятся пополам, \nто такой четырехугольник является прямоугольником.')
    third_theorem_label.config(text='3.Диаметр описанной около прямоугольника окружности равен его диагонали.\nПлощадь прямоугольника')
    fourth_theorem_label.config(text='4.Площадь прямоугольника равна половине произведения квадрата диагонали и \nсинуса угла между диагоналями.')

    first_theorem_label.grid()
    second_theorem_label.grid()
    third_theorem_label.grid()
    fourth_theorem_label.grid()

    fifth_theorem_label.grid_remove()
    sixth_theorem_label.grid_remove()
    seventh_theorem_label.grid_remove()
    eight_theorem_label.grid_remove()

    first_theorems_page_button.config(command=visible_theorems_square_window_first_func)
    second_theorems_page_button.place_forget()

    back_square_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_square_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_square_theorems_button.bind('<Button-1>', visible_square_window_event_func)


def visible_axioms_square_window_func():
    # Всё, что показываем:
    axioms_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём

    title_axioms_label.config(text='Аксиомы прямоугольника: ')

    first_axioms_label.config(text='Отсутствуют')

    back_square_axioms_button = Button(axioms_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_square_axioms_button.place(x=10, y=460)  # Кнопка назад
    back_square_axioms_button.bind('<Button-1>', visible_square_window_event_func)


def visible_formuls_square_func():
    # Всё, что показываем
    formuls_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём
    title_formulas_label.config(text='Формулы прямоугольника: ')

    first_formulas_label.config(text=' Формула стороны прямоугольника через диагональ и другую сторону:\n    a = √d² - b²\n    b = √d² - a²')

    second_formulas_label.config(text='Формула стороны прямоугольника через площадь и другую сторону:\n    a = S / b\n    b = S / a')

    third_formulas_label.config(text='Формула стороны прямоугольника через периметр и другую сторону:\n    a = (P-2b) / 2\n    b = (P-2a) / 2')

    fourth_formulas_label.config(text='Формула стороны прямоугольника через диаметр и угол α:\n    a = d * sin(a)\n    b = d * cos(a)')

    fifth_formulas_label.config(text='Формула стороны прямоугольника через диаметр и угол β:\n    a = d * sin(β / 2)\n    b = d * cos(β / 2)')

    first_formulas_label.grid()
    second_formulas_label.grid()
    third_formulas_label.grid()
    fourth_formulas_label.grid()
    fifth_formulas_label.grid()

    back_formulas_square_button = Button(formuls_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_formulas_square_button.place(x=10, y=460)  # Кнопка назад
    back_formulas_square_button.bind('<Button-1>', visible_square_window_event_func)


def visible_rectangle_window_event_func(event):  # Открытие окна с квадратом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    axioms_window.withdraw()
    theorems_window.withdraw()
    formuls_window.withdraw()
    calculate_rectangle_window.withdraw()
    # Всё, что создаём
    figure_window.title('Квадрат')

    definition_figure_label.config(text='Квадрат - правильный четырёхугольник, \nто есть четырёхугольник, у которого все \nуглы равны и все стороны равны')

    calculations_figure_button.config(text='Калькулятор квадрата', command=visible_calculate_rectangle_window_func)

    axioms_figure_button.config(text='Аксиомы квадрата', command=visible_axioms_rectangle_window_func)

    theorems_figure_button.config(text='Теоремы квадрата', command=visible_theorems_rectangle_window_func)

    formulas_figure_button.config(text='Формулы квадрата', command=visible_formuls_rectangle_func)


def visible_theorems_rectangle_window_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё, что создаём
    title_theorem_label.config(text='Теоремы квадрата: ')

    first_theorem_label.config(text='1.Площадь квадрата равна квадрату стороны или половине квадрата его диагонали')
    second_theorem_label.config(text='2.Если диагонали прямоугольника пересекаются под прямым углом, \nэтот прямоугольник - квадрат.')
    third_theorem_label.config(text='3.Если один из углов ромба прямой, этот ромб - квадрат.')

    fourth_theorem_label.grid_remove()
    fifth_theorem_label.grid_remove()
    sixth_theorem_label.grid_remove()
    seventh_theorem_label.grid_remove()
    eight_theorem_label.grid_remove()

    first_theorems_page_button.config(command=visible_theorems_rectangle_window_func)
    second_theorems_page_button.place_forget()

    back_rectangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_theorems_button.bind('<Button-1>', visible_rectangle_window_event_func)


def visible_axioms_rectangle_window_func():
    # Всё, что показываем:
    axioms_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём
    title_axioms_label.config(text='Аксиомы квадрата: ')

    first_axioms_label.config(text='Отсутствуют')

    back_rectangle_axioms_button = Button(axioms_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_axioms_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_axioms_button.bind('<Button-1>', visible_rectangle_window_event_func)


def visible_formuls_rectangle_func():
    # Всё, что показываем
    formuls_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём
    title_formulas_label.config(text='Формулы квадарата: ')

    first_formulas_label.config(text='Формулы для нахождения площади:\n    S = a * a\n    S = P² / 16\n    S = D² / 2')

    second_formulas_label.config(text='Формулы для нахождения периметра:\n    P = 4 * a\n    P = 2 * D * √2\n    P = 4 * √S')

    third_formulas_label.config(text='Формулы для нахождения диагонали:\n    D = a * √2\n    D = √(2 * S)\n    D = P / 2 * √2')

    fourth_formulas_label.grid_remove()
    fifth_formulas_label.grid_remove()

    back_formulas_rectangle_button = Button(formuls_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_formulas_rectangle_button.place(x=10, y=460)  # Кнопка назад
    back_formulas_rectangle_button.bind('<Button-1>', visible_rectangle_window_event_func)


def visible_rhombus_window_event_func(event):  # Открытие окна с ромбом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    theorems_window.withdraw()
    axioms_window.withdraw()
    formuls_window.withdraw()
    # Всё что создаём
    figure_window.title('Ромб')
    definition_figure_label.config(text='Ромб - это параллелограмм,\n у которого все стороны равны')
    calculations_figure_button.config(text='Калькулятор ромба', command=development_func)
    axioms_figure_button.config(text='Аксиомы ромба', command=visible_axioms_rhombus_window_func)

    theorems_figure_button.config(text='Теоремы ромба', command=visible_theorems_rhombus_window_func)

    formulas_figure_button.config(text='Формулы ромба', command=visible_formuls_rhombus_func)


def visible_theorems_rhombus_window_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё, что создаём

    title_theorem_label.config(text='Теоремы ромба: ')

    first_theorem_label.config(text='1.Диагонали ромба пересекаются под прямым углом.')
    second_theorem_label.config(text='2.Диагонали ромба являются биссектрисами его углов.')
    third_theorem_label.config(text='3.Если диагонали параллелограмма перпендикулярны, то параллелограмм – ромб.')
    fourth_theorem_label.config(text='4.Если диагональ параллелограмма является биссектрисой его угла, то \nпараллелограмм – ромб.')

    first_theorem_label.grid()
    second_theorem_label.grid()
    third_theorem_label.grid()
    fourth_theorem_label.grid()

    fifth_theorem_label.grid_remove()
    sixth_theorem_label.grid_remove()
    seventh_theorem_label.grid_remove()
    eight_theorem_label.grid_remove()

    first_theorems_page_button.config(command=visible_theorems_rhombus_window_func)
    second_theorems_page_button.place_forget()

    back_rectangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_theorems_button.bind('<Button-1>', visible_rhombus_window_event_func)


def visible_axioms_rhombus_window_func():
    # Всё, что показываем:
    axioms_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём
    title_axioms_label.config(text='Аксиомы ромба: ')

    first_axioms_label.config(text='Отсутствуют')

    back_rectangle_axioms_button = Button(axioms_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_axioms_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_axioms_button.bind('<Button-1>', visible_rhombus_window_event_func)


def visible_formuls_rhombus_func():
    # Всё, что показываем
    formuls_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём
    title_formulas_label.config(text='Формулы ромба: ')

    first_formulas_label.config(text='Формулы определения длины стороны ромба:\n    a = S / h\n    a = √S / √sin(a)\n    a = S / 2 * r')

    second_formulas_label.config(text='Формулы определения длины диагонали ромба:\n    D = a * √2 - 2 * cos(β)\n    D = a * √2 + 2 * cos(α)\n    D₁ = 2 * S / D₂')

    third_formulas_label.config(text='Формула определения длины периметра ромба:\n    P = 4 * a')

    fourth_theorem_label.config(text='Формулы определения площади ромба:\n    S = a * h\n    S = a² * sin(α)\n    S = 2 * a * r')

    fifth_formulas_label.config(text='Формулы определения радиуса круга вписанного в ромб:\n    r = h/2\n    r = S / 2 * a\n    r = √(S * sin(α) / 2')

    first_formulas_label.grid()
    second_formulas_label.grid()
    third_formulas_label.grid()
    fourth_formulas_label.grid()
    fifth_formulas_label.grid()

    back_formulas_rectangle_button = Button(formuls_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_formulas_rectangle_button.place(x=10, y=460)  # Кнопка назад
    back_formulas_rectangle_button.bind('<Button-1>', visible_rhombus_window_event_func)


def visible_parallelogram_window_event_func(event):  # Открытие окна с параллелограммом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    axioms_window.withdraw()
    formuls_window.withdraw()
    theorems_window.withdraw()
    # Всё, что создаём
    figure_window.title('Параллелограмм')
    definition_figure_label.config(text='Параллелограмм - это четырёхугольник, \nу которого противоположные стороны \nпопарно параллельны, то есть \nлежат на параллельных прямых')

    calculations_figure_button.config(text='Калькулятор параллелограмма', command=development_func)

    axioms_figure_button.config(text='Аксиомы параллелограмма', command=visible_axioms_parallelogram_window_func)

    theorems_figure_button.config(text='Теоремы параллелограмма', command=visible_theorems_parallelogram_window_first_func)

    formulas_figure_button.config(text='Формулы параллелограмма', command=visible_formuls_parallelogram_func)


def visible_theorems_parallelogram_window_first_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё, что создаём

    title_theorem_label.config(text='Теоремы параллелограма: 1 стр.')

    first_theorem_label.config(text='1.Противоположные стороны параллелограма равны.')
    second_theorem_label.config(text='2.Противоположные углы параллелограмма равны.')
    third_theorem_label.config(text='3.Соседние углы параллелограмма, т.е. углы, прилежащие к одной стороне, составляют \nв сумме 180 градусов.')
    fourth_theorem_label.config(text='4.Диагонали параллелограмма делят друг друга в точке их пересечения пополам.')
    fifth_theorem_label.config(text='5.Если противоположные стороны четырехугольника попарно равны, то он \nявляется параллелограммом.')
    sixth_theorem_label.config(text='6.Если противоположные углы четырехугольника попарно равны, то он \nявляется параллелограммом.')
    seventh_theorem_label.config(text='7.Если соседние углы четырехугольника, т.е. углы, прилежащие к одной стороне, \nсоставляют в сумме 180 градусов, то он является параллелограммом.')
    eight_theorem_label.config(text='8.Если диагонали четырехугольника взаимно делятся в точке пересечения пополам, \nто четырехугольник - параллелограмм.')

    first_theorem_label.grid()
    second_theorem_label.grid()
    third_theorem_label.grid()
    fourth_theorem_label.grid()
    fifth_theorem_label.grid()
    sixth_theorem_label.grid()
    seventh_theorem_label.grid()
    eight_theorem_label.grid()

    first_theorems_page_button.config(command=visible_theorems_parallelogram_window_first_func)
    second_theorems_page_button.config(command=visible_theorems_parallelogram_window_second_func)
    second_theorems_page_button.place(x=320, y=460)

    back_rectangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_theorems_button.bind('<Button-1>', visible_parallelogram_window_event_func)


def visible_theorems_parallelogram_window_second_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()

    # Всё, что создаём
    title_theorem_label.config(text='Теоремы параллелограма: 2 стр.')

    first_theorem_label.config(text='9.Если четырехугольник имеет пару равных, параллельных между собой сторон, то \nон является параллелограммом.')

    second_theorem_label.config(text='10.Площадь параллелограмма равна произведению стоны и проведенную к ней высоту.')

    third_theorem_label.config(text='11.Площадь параллелограмма равна произведению двух смежных сторон и синуса \nугла между ними.')

    fourth_theorem_label.config(text='12.Площадь параллелограмма равна половине произведения диагоналей и синуса \nугла между ними.')

    fifth_theorem_label.grid_remove()
    sixth_theorem_label.grid_remove()
    seventh_theorem_label.grid_remove()
    eight_theorem_label.grid_remove()

    back_triangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_triangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_triangle_theorems_button.bind('<Button-1>', visible_parallelogram_window_event_func)


def visible_axioms_parallelogram_window_func():
    # Всё, что показываем:
    axioms_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём
    title_axioms_label.config(text='Аксиомы параллелограмма: ')

    first_axioms_label.config(text='Отсутствуют')

    back_rectangle_axioms_button = Button(axioms_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_axioms_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_axioms_button.bind('<Button-1>', visible_parallelogram_window_event_func)


def visible_formuls_parallelogram_func():
    # Всё, что показываем
    formuls_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём
    title_formulas_label.config(text='Формулы параллелограмма: ')

    first_formulas_label.config(text='Формулы определения длин сторон параллелограмма:\n    b = h₁ / sin(α)\n    a = h₂ / sin(α)\n    a = S / h₁\n    b = S / h₂')

    second_formulas_label.config(text='Формулы определения длины диагонали параллелограмма:\n    D₁ = √(2 * a² + 2 * b² + 2 * a * b * cos(α))\n    D₂ = √(2 * a² + 2 * b² - 2 * a * b * cos(α))')

    third_formulas_label.config(text='Формулы определения длины периметра параллелограмма:\n    P = 2 * a + 2 * b\n    P = 2 * a + √(2 * D₁² + 2 * D₂² - 4 * a²)\n    P = 2 * b + √(2 * D₁² + 2 * D₂² - 4 * b²)')

    fourth_formulas_label.config(text='Формулы определения площади параллелограмма:\n    S = a * h₁\n    S = b * h₂\n    S = a * b * sin(α)')

    first_formulas_label.grid()
    second_formulas_label.grid()
    third_formulas_label.grid()
    fourth_formulas_label.grid()

    fifth_formulas_label.grid_remove()

    back_formulas_rectangle_button = Button(formuls_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_formulas_rectangle_button.place(x=10, y=460)  # Кнопка назад
    back_formulas_rectangle_button.bind('<Button-1>', visible_parallelogram_window_event_func)


def visible_trapezium_window_event_func(event):  # Открытие окна с трапецией через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    axioms_window.withdraw()
    theorems_window.withdraw()
    formuls_window.withdraw()
    calculate_trapezium_window.withdraw()
    # Всё, что создаём
    figure_window.title('Трапеция')
    definition_figure_label.config(text='Трапеция — четырехугольник, у которого \nдве стороны параллельны, а две \nстороны не параллельны')
    calculations_figure_button.config(text='Калькулятор трапеции', command=development_func)
    axioms_figure_button.config(text='Аксиомы трапеции', command=visible_axioms_trapezium_window_func)
    theorems_figure_button.config(text='Теоремы трапеции', command=visible_theorems_trapezium_window_first_func)
    formulas_figure_button.config(text='Формулы трапеции', command=visible_formuls_trapezium_func)


def visible_theorems_trapezium_window_first_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё, что создаём

    title_theorem_label.config(text='Теоремы трапеции: 1 стр.')

    first_theorem_label.config(text='1.Средняя линия трапеции параллельна основаниям и равна их полусумме.')
    second_theorem_label.config(text='2.Диагонали делят трапецию на четыре части, две из которых, прилежащие к \nбоковым сторонам, равовелики.')
    third_theorem_label.config(text='3.В трапеции середины оснований и точка пересечения диагоналей лежат на одной прямой.')
    fourth_theorem_label.config(text='4.Углы, прилежащие к каждому из оснований равнобокой трапеции, равны.')
    fifth_theorem_label.config(text='5.Диагонали равнобокой трапеции равны.')
    sixth_theorem_label.config(text='6.Если продолжить стороны равнобочной трапеции до их пересечения, то вместе с \nбольшим основанием трапеции они образуют равнобедренный треугольник.')
    seventh_theorem_label.config(text='7.Диагонали равнобедренной трапеции точкой пересечения делятся на \nсоответственно равные отрезки.')
    eight_theorem_label.config(text='8.Ось сисмметрии равнобокой трапеции перпендикулярна её основаниям.')

    first_theorem_label.grid()
    second_theorem_label.grid()
    third_theorem_label.grid()
    fourth_theorem_label.grid()
    fifth_theorem_label.grid()
    sixth_theorem_label.grid()
    seventh_theorem_label.grid()
    eight_theorem_label.grid()

    first_theorems_page_button.config(command=visible_theorems_trapezium_window_first_func)
    second_theorems_page_button.config(command=visible_theorems_trapezium_window_second_func)
    second_theorems_page_button.place(x=320, y=460)

    back_rectangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_theorems_button.bind('<Button-1>', visible_trapezium_window_event_func)


def visible_theorems_trapezium_window_second_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё, что создаём

    title_theorem_label.config(text='Теоремы трапеции: 2 стр.')

    first_theorem_label.config(text='9.Если углы, прилежищие к одному из оснований трапеции, равны, то трапеция равнобокая.')
    second_theorem_label.config(text='10.Если диагонали трапеции равны, то трапеция равнобокая.')
    third_theorem_label.config(text='11.Если продолженные до пересечения боковые стороны трапеции образуют вместе \nи её большим основанием равнобедренный треугольник, то трапеция равнобокая.')
    fourth_theorem_label.config(text='12.Если трапецию можно вписать в окружность, то она равнобокая.')
    fifth_theorem_label.config(text='13.Радиус вписанной в трапецию окружности равен половине высоты основания.')
    sixth_theorem_label.config(text='14.Площадь трапеции равна произведению полусуммы оснований и высоты оснований.')

    first_theorem_label.grid()
    second_theorem_label.grid()
    third_theorem_label.grid()
    fourth_theorem_label.grid()
    fifth_theorem_label.grid()
    sixth_theorem_label.grid()

    seventh_theorem_label.grid_remove()
    eight_theorem_label.grid_remove()

    first_theorems_page_button.config(command=visible_theorems_trapezium_window_first_func)
    second_theorems_page_button.config(command=visible_theorems_trapezium_window_second_func)
    second_theorems_page_button.place(x=320, y=460)

    back_rectangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_theorems_button.bind('<Button-1>', visible_trapezium_window_event_func)


def visible_axioms_trapezium_window_func():
    # Всё, что показываем:
    axioms_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём
    title_axioms_label.config(text='Аксиомы трапеции: ')

    first_axioms_label.config(text='Отсутствуют')

    back_rectangle_axioms_button = Button(axioms_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_axioms_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_axioms_button.bind('<Button-1>', visible_trapezium_window_event_func)


def visible_formuls_trapezium_func():
    # Всё, что показываем
    formuls_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём
    title_formulas_label.config(text='Формулы трапеции: ')

    first_formulas_label.config(text='Формулы определения длин сторон трапеции:\n    a = a * m - b\n    b = 2 * m - a\n    a = b + h * (ctg(α) + ctg(β))')

    second_formulas_label.config(text='Формулы определения длины средней линии трапеции:\n    m = (a + b) / 2\n    m = S / h')

    third_formulas_label.config(text='Формулы определения длины высоты трапеции:\n    h = c * sin(α)\n    α = D * sin(β)')

    fourth_formulas_label.config(text='Формулы определения длины диагоналей трапеции:\n    D₁ = √(a² + D₂ - 2 * a * d * cos(β))\n    D₂ = √(a² + c² - 2 * a * c * cos(β))')

    fifth_formulas_label.config(text='Формулы определения площади трапеции:\n    S = ((a + b)/2) / h\n    S = m * h')

    first_formulas_label.grid()
    second_formulas_label.grid()
    third_formulas_label.grid()
    fourth_formulas_label.grid()
    fifth_formulas_label.grid()

    back_formulas_rectangle_button = Button(formuls_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_formulas_rectangle_button.place(x=10, y=460)  # Кнопка назад
    back_formulas_rectangle_button.bind('<Button-1>', visible_trapezium_window_event_func)


def visible_circle_window_event_func(event):  # Открытие окна с кругом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    axioms_window.withdraw()
    theorems_window.withdraw()
    formuls_window.withdraw()
    # Всё, что создаём
    figure_window.title('Круг')
    definition_figure_label.config(text='Круг - часть плоскости,\n лежащая внутри окружности')

    calculations_figure_button.config(text='Калькулятор круга', command=development_func)

    axioms_figure_button.config(text='Аксиомы круга', command=visible_axioms_circle_window_func)

    theorems_figure_button.config(text='Теоремы круга', command=visible_theorems_circle_window_func)

    formulas_figure_button.config(text='Формулы круга', command=visible_formuls_circle_func)


def visible_theorems_circle_window_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё, что создаём
    title_theorem_label.config(text='Теоремы круга: 1 стр.')

    first_theorem_label.config(text='1.Перпендикуляр, опущенный на хорду из центра окружности, делит эту хорду пополам.')
    second_theorem_label.config(text='2.Угол, вписанный в окружность, равен половине соответствующего центрального угла.')
    third_theorem_label.config(text='3.Вписанные углы, опирающиеся на равные дуги, равны.')
    fourth_theorem_label.config(text='4.Величина угла с вершиной внутри круга равна полусумме угловых величин дуг, \nзаключенных между его сторонами и их продолжениями.')
    fifth_theorem_label.config(
        text='5.Величина угла, образованного двумя секущими с вершиной вне круга, стороны \nкоторого пересекают этот круг, равна полуразности угловых величин большей и меньшей дуг, \nзаключенных между его сторонами.')
    sixth_theorem_label.config(text='6.При пересечении хорды делятся на отрезки, произведения которых равны.')
    seventh_theorem_label.config(text='7.Радиус, проведенный в точку касания окружности, перпендикулярен касательной.')
    eight_theorem_label.config(text='8.Хорда, имеющая те же концевые точки, что и дуга, называется хордой, \nстягивающей эту дугу.')

    first_theorem_label.grid()
    second_theorem_label.grid()
    third_theorem_label.grid()
    fourth_theorem_label.grid()
    fifth_theorem_label.grid()
    sixth_theorem_label.grid()
    seventh_theorem_label.grid()
    eight_theorem_label.grid()

    first_theorems_page_button.config(command=visible_theorems_circle_window_func)
    second_theorems_page_button.place_forget()

    back_rectangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_theorems_button.bind('<Button-1>', visible_circle_window_event_func)


def visible_axioms_circle_window_func():
    # Всё, что показываем:
    axioms_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём
    title_axioms_label.config(text='Аксиомы круга: ')

    first_axioms_label.config(text='Отсутствуют')

    back_rectangle_axioms_button = Button(axioms_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_axioms_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_axioms_button.bind('<Button-1>', visible_circle_window_event_func)


def visible_formuls_circle_func():
    # Всё, что показываем
    formuls_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём
    title_formulas_label.config(text='Формулы трапеции: ')

    first_formulas_label.config(text='Формулы определения площади круга:\n    S = pi * r²')
    second_formulas_label.config(text='Формулы определения периметра круга:\n    P = 2 * pi * r')
    third_formulas_label.config(text='Длину окружности можно вычислить по формуле:\n    l = 2 * pi * r')

    first_formulas_label.grid()
    second_formulas_label.grid()

    fourth_formulas_label.grid_remove()
    fifth_formulas_label.grid_remove()

    back_formulas_rectangle_button = Button(formuls_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_formulas_rectangle_button.place(x=10, y=460)  # Кнопка назад
    back_formulas_rectangle_button.bind('<Button-1>', visible_trapezium_window_event_func)


def visible_ellipse_window_event_func(event):  # Открытие окна с эллипсом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    theorems_window.withdraw()
    axioms_window.withdraw()
    formuls_window.withdraw()
    # Всё, что создаём
    figure_window.title('Эллипс')
    definition_figure_label.config(text='Эллипс — это замкнутая плоская кривая, \nсумма расстояний от каждой точки \nкоторой до двух точек F1 и F2 \nравна постоянной величине')
    calculations_figure_button.config(text='Калькулятор эллипса', command=visible_calculate_triangle_window_func)
    axioms_figure_button.config(text='Аксиомы эллипса', command=visible_axioms_ellipse_window_func)

    theorems_figure_button.config(text='Теоремы эллипса', command=visible_theorems_ellipse_window_func)

    formulas_figure_button.config(text='Формулы эллипса', command=visible_formuls_ellipse_func)


def visible_theorems_ellipse_window_func():
    # Всё, что показываем:
    theorems_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё, что создаём
    title_theorem_label.config(text='Теоремы эллипса: 1 стр.')

    first_theorem_label.config(text='1.Угол между касательной к эллипсу и фокальным радиусом r₁ равен углу между \nкасательной и фокальным радиусом r₂')
    second_theorem_label.config(
        text='2.Если эллипс пересекается двумя параллельными прямыми, то отрезок, соединяющий \nсередины отрезков образовавшихся при пересечении прямых и эллипса, всегда \nбудет проходить '
             'через центр эллипсa. \n(Это свойство дает возможность построением с помощью циркуля и линейки \nполучить центр эллипса.)')
    third_theorem_label.config(text='3.Эволютой эллипсa есть астероида, что растянута вдоль короткой оси.')

    first_theorem_label.grid()
    second_theorem_label.grid()
    third_theorem_label.grid()

    fourth_formulas_label.grid_remove()
    fifth_formulas_label.grid_remove()
    sixth_theorem_label.grid_remove()
    seventh_theorem_label.grid_remove()
    eight_theorem_label.grid_remove()

    first_theorems_page_button.config(command=visible_theorems_ellipse_window_func)
    second_theorems_page_button.place_forget()

    back_rectangle_theorems_button = Button(theorems_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_theorems_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_theorems_button.bind('<Button-1>', visible_ellipse_window_event_func)


def visible_axioms_ellipse_window_func():
    # Всё, что показываем:
    axioms_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём
    title_axioms_label.config(text='Аксиомы эллипса: ')

    first_axioms_label.config(text='Отсутствуют')

    back_rectangle_axioms_button = Button(axioms_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_rectangle_axioms_button.place(x=10, y=460)  # Кнопка назад
    back_rectangle_axioms_button.bind('<Button-1>', visible_ellipse_window_event_func)


def visible_formuls_ellipse_func():
    # Всё, что показываем
    formuls_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём
    title_formulas_label.config(text='Формулы эллипса: ')

    first_formulas_label.config(text='Формула определение площади эллипсa:\n    S = pi * a * b')

    first_formulas_label.grid()

    second_formulas_label.grid_remove()
    third_formulas_label.grid_remove()
    fourth_formulas_label.grid_remove()
    fifth_formulas_label.grid_remove()

    back_formulas_rectangle_button = Button(formuls_window, text='Назад', bg=first_color, fg=fourth_color)  # Кнопка назад
    back_formulas_rectangle_button.place(x=10, y=460)  # Кнопка назад
    back_formulas_rectangle_button.bind('<Button-1>', visible_ellipse_window_event_func)


def exit_error_func():  # Показываение ошибки при попытки закрытия важных окон
    mb.showerror('Ошибка', 'Это окно закрывается кнопкой "Назад"')


def exit_project_func():  # Полностью закрытие проекта
    sys.exit()


def development_func():
    mb.showinfo(title='Уведомление', message='На стадии разработки')


def write_change_theme_func():  # Создание файла с темой
    first_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для фона')

    second_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для заголовков')

    third_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для обычного текста')

    fourth_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для кнопок')

    fifth_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для заливки фигур')

    create__theme_file = open('File_Setting.txt', 'w')
    create__theme_file.write(str(first_color_choose[1]) + ' ' + str(second_color_choose[1]) + ' ' + str(third_color_choose[1]) + ' ' + str(fourth_color_choose[1]) + ' ' + str(fifth_color_choose[1]))
    create__theme_file.close()
    mb.showwarning(title='Уведомелние', message='Тема поменяется после перезагрузки приложения')
    sys.exit()


def delete_custom_theme_func():
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'File_Setting.txt')
        os.remove(path)
        mb.showinfo(title='Информация', message='Тема успешно удалена, перезагрузите программу, чтобы тема сбросилась')
        sys.exit()
    except FileNotFoundError:
        mb.showwarning(title='Предупреждение', message='У вас не создана кастомная тема')


def calculate_triangle_func():
    if a_triangle_entry.get() != '' and b_triangle_entry.get() != '' and c_triangle_entry.get() != '':  # проверено работает
        a = float(a_triangle_entry.get())
        b = float(b_triangle_entry.get())
        c = float(c_triangle_entry.get())
        alpha_corner_triangle_entry['state'] = DISABLED
        betta_corner_triangle_entry['state'] = DISABLED
        gamma_corner_triangle_entry['state'] = DISABLED
        if (a + b > c) and (a + c > b) and (b + c > a):

            a = float(a_triangle_entry.get())

            b = float(b_triangle_entry.get())

            c = float(c_triangle_entry.get())

            alpha = round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))

            betta = round(math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))))

            gamma = round(180 - (alpha + betta))

            p = round(a + b + c, 2)  # Периметр

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)  # Площадь

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    elif a_triangle_entry.get() != '' and c_triangle_entry.get() != '' and alpha_corner_triangle_entry.get() != '' and alpha_corner_triangle_entry.get() != '90':  # проверено работает
        b_triangle_entry['state'] = DISABLED
        betta_corner_triangle_entry['state'] = DISABLED
        gamma_corner_triangle_entry['state'] = DISABLED
        a = float(a_triangle_entry.get())  # a
        c = float(c_triangle_entry.get())  # b
        alpha = float(alpha_corner_triangle_entry.get())  # y

        b = round(math.sqrt((a ** 2 + c ** 2) - (2 * a * c * (math.cos(math.radians(alpha))))), 2)  # c

        betta = round(math.degrees(math.acos((c ** 2 + b ** 2 - a ** 2) / (2 * c * b))))  # a

        gamma = round(180 - betta - alpha)

        p = round(a + c + b, 2)

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

        a_result_triangle_label.config(text=a)
        b_result_triangle_label.config(text=b)
        c_result_triangle_label.config(text=c)
        alpha_result_triangle_label.config(text=alpha)
        betta_result_triangle_label.config(text=betta)
        gamma_result_triangle_label.config(text=gamma)
        p_result_triangle_label.config(text=p)
        s_result_triangle_label.config(text=s)

    elif a_triangle_entry.get() != '' and b_triangle_entry.get() != '' and gamma_corner_triangle_entry.get() != '' and gamma_corner_triangle_entry.get() != '90':  # проверено работает
        c_triangle_entry['state'] = DISABLED
        alpha_corner_triangle_entry['state'] = DISABLED
        betta_corner_triangle_entry['state'] = DISABLED
        a = float(a_triangle_entry.get())  # a
        b = float(b_triangle_entry.get())  # b
        gamma = float(gamma_corner_triangle_entry.get())  # y

        c = round(math.sqrt((a ** 2 + b ** 2) - (2 * a * b * (math.cos(math.radians(gamma))))), 2)  # c

        betta = round(math.degrees(math.acos((c ** 2 + b ** 2 - a ** 2) / (2 * c * b))))  # a

        alpha = round(180 - gamma - betta)

        p = round(a + c + b, 2)

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

        a_result_triangle_label.config(text=a)
        b_result_triangle_label.config(text=b)
        c_result_triangle_label.config(text=c)
        alpha_result_triangle_label.config(text=alpha)
        betta_result_triangle_label.config(text=betta)
        gamma_result_triangle_label.config(text=gamma)
        p_result_triangle_label.config(text=p)
        s_result_triangle_label.config(text=s)
    elif b_triangle_entry.get() != '' and c_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '90':  # проверено работает
        a_triangle_entry['state'] = DISABLED
        alpha_corner_triangle_entry['state'] = DISABLED
        gamma_corner_triangle_entry['state'] = DISABLED

        b = float(b_triangle_entry.get())  # a
        c = float(c_triangle_entry.get())  # b
        betta = float(betta_corner_triangle_entry.get())  # y

        a = round(math.sqrt((b ** 2 + c ** 2) - (2 * b * c * (math.cos(math.radians(betta))))), 2)  # c

        alpha = round(math.degrees(math.acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a))))

        gamma = round(180 - alpha - betta)

        p = round(a + c + b, 2)

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

        a_result_triangle_label.config(text=a)
        b_result_triangle_label.config(text=b)
        c_result_triangle_label.config(text=c)
        alpha_result_triangle_label.config(text=alpha)
        betta_result_triangle_label.config(text=betta)
        gamma_result_triangle_label.config(text=gamma)
        p_result_triangle_label.config(text=p)
        s_result_triangle_label.config(text=s)
    elif c_triangle_entry.get() != '' and alpha_corner_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '' and alpha_corner_triangle_entry.get() != '90' and betta_corner_triangle_entry.get() != '90':  # проверено работает
        a_triangle_entry['state'] = DISABLED
        b_triangle_entry['state'] = DISABLED
        gamma_corner_triangle_entry['state'] = DISABLED
        c = float(c_triangle_entry.get())
        alpha = float(alpha_corner_triangle_entry.get())
        betta = float(betta_corner_triangle_entry.get())

        if (alpha + betta) < 180:

            gamma = 180 - alpha - betta

            a = round(c * (math.sin(math.radians(betta)) / math.sin(math.radians(gamma))), 2)
            b = round(c * (math.sin(math.radians(alpha)) / math.sin(math.radians(gamma))), 2)

            p = round(a + c + b, 2)

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    elif a_triangle_entry.get() != '' and alpha_corner_triangle_entry.get() != '' and gamma_corner_triangle_entry.get() != '' and alpha_corner_triangle_entry.get() != '90' and gamma_corner_triangle_entry.get() != '90':  # проверено работает
        b_triangle_entry['state'] = DISABLED
        c_triangle_entry['state'] = DISABLED
        betta_corner_triangle_entry['state'] = DISABLED
        a = float(a_triangle_entry.get())
        alpha = float(alpha_corner_triangle_entry.get())
        gamma = float(gamma_corner_triangle_entry.get())
        if (alpha + gamma) < 180:

            betta = 180 - alpha - gamma

            b = round(a * (math.sin(math.radians(alpha)) / math.sin(math.radians(betta))), 2)
            c = round(a * (math.sin(math.radians(gamma)) / math.sin(math.radians(betta))), 2)

            p = round(a + c + b, 2)

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    elif b_triangle_entry.get() != '' and gamma_corner_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '' and gamma_corner_triangle_entry.get() != '90' and betta_corner_triangle_entry.get() != '90':  # проверено работает
        a_triangle_entry['state'] = DISABLED
        c_triangle_entry['state'] = DISABLED
        alpha_corner_triangle_entry['state'] = DISABLED
        b = float(b_triangle_entry.get())
        gamma = float(gamma_corner_triangle_entry.get())
        betta = float(betta_corner_triangle_entry.get())
        if (gamma + betta) < 180:

            alpha = 180 - gamma - betta
            print(f'Alpha = {alpha}')
            print(f'Betta = {betta}')
            print(f'Gamma = {gamma}')
            a = round(b * (math.sin(math.radians(betta)) / math.sin(math.radians(alpha))), 2)
            c = round(b * (math.sin(math.radians(gamma)) / math.sin(math.radians(alpha))), 2)
            print(f'A = {a}')
            print(f'B = {b}')
            print(f'C = {c}')

            p = round(a + c + b, 2)
            print(f'P = {p}')

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)
            print(f'S = {s}')

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    elif a_triangle_entry.get() != '' and c_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '90':  # проверено работает
        b_triangle_entry['state'] = DISABLED
        alpha_corner_triangle_entry['state'] = DISABLED
        gamma_corner_triangle_entry['state'] = DISABLED

        a = float(a_triangle_entry.get())  # b
        c = float(c_triangle_entry.get())  # c
        betta = float(betta_corner_triangle_entry.get())  # betta

        gamma = round(math.degrees(math.asin(c / a * (math.sin(math.radians(betta))))), 2)

        alpha = round(180 - betta - gamma, 2)

        b = round(a * (math.sin(math.radians(alpha)) / math.sin(math.radians(betta))), 2)

        p = round(a + c + b, 2)

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

        a_result_triangle_label.config(text=a)
        b_result_triangle_label.config(text=b)
        c_result_triangle_label.config(text=c)
        alpha_result_triangle_label.config(text=alpha)
        betta_result_triangle_label.config(text=betta)
        gamma_result_triangle_label.config(text=gamma)
        p_result_triangle_label.config(text=p)
        s_result_triangle_label.config(text=s)
    elif b_triangle_entry.get() != '' and c_triangle_entry.get() != '' and alpha_corner_triangle_entry.get() != '' and alpha_corner_triangle_entry.get() != '90':  # проверено работает

        a_triangle_entry['state'] = DISABLED
        betta_corner_triangle_entry['state'] = DISABLED
        gamma_corner_triangle_entry['state'] = DISABLED

        b = float(b_triangle_entry.get())
        c = float(c_triangle_entry.get())
        alpha = float(alpha_corner_triangle_entry.get())

        gamma = round(math.degrees(math.asin(c / b * (math.sin(math.radians(alpha))))), 2)

        betta = round(180 - alpha - gamma, 2)

        a = round(b * (math.sin(math.radians(betta)) / math.sin(math.radians(alpha))), 2)

        p = round(a + c + b, 2)

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

        a_result_triangle_label.config(text=a)
        b_result_triangle_label.config(text=b)
        c_result_triangle_label.config(text=c)
        alpha_result_triangle_label.config(text=alpha)
        betta_result_triangle_label.config(text=betta)
        gamma_result_triangle_label.config(text=gamma)
        p_result_triangle_label.config(text=p)
        s_result_triangle_label.config(text=s)

    elif a_triangle_entry.get() != '' and b_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '90':  # проверено работает
        c_triangle_entry['state'] = DISABLED
        alpha_corner_triangle_entry['state'] = DISABLED
        gamma_corner_triangle_entry['state'] = DISABLED

        a = float(a_triangle_entry.get())
        b = float(b_triangle_entry.get())
        betta = float(betta_corner_triangle_entry.get())

        alpha = round(math.degrees(math.asin(b / a * (math.sin(math.radians(betta))))), 2)

        gamma = round(180 - betta - alpha, 2)

        print('1')
        c = round(a * (math.sin(math.radians(gamma)) / math.sin(math.radians(betta))), 2)

        p = round(a + c + b, 2)

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

        a_result_triangle_label.config(text=a)
        b_result_triangle_label.config(text=b)
        c_result_triangle_label.config(text=c)
        alpha_result_triangle_label.config(text=alpha)
        betta_result_triangle_label.config(text=betta)
        gamma_result_triangle_label.config(text=gamma)
        p_result_triangle_label.config(text=p)
        s_result_triangle_label.config(text=s)
    elif alpha_corner_triangle_entry.get() == '90' and a_triangle_entry.get() != '' and c_triangle_entry.get() != '':  # проверено работает
        a = float(a_triangle_entry.get())
        c = float(c_triangle_entry.get())
        alpha = float(90)
        b = round(math.sqrt(a ** 2 + c ** 2), 2)

        betta = round(math.degrees(math.asin(a / b)), 2)
        gamma = round(math.degrees(math.asin(c / b)), 2)

        p = round(a + c + b, 2)

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

        a_result_triangle_label.config(text=a)
        b_result_triangle_label.config(text=b)
        c_result_triangle_label.config(text=c)
        alpha_result_triangle_label.config(text=alpha)
        betta_result_triangle_label.config(text=betta)
        gamma_result_triangle_label.config(text=gamma)
        p_result_triangle_label.config(text=p)
        s_result_triangle_label.config(text=s)
    elif alpha_corner_triangle_entry.get() == '90' and b_triangle_entry.get() != '' and c_triangle_entry.get() != '':  # проверено работает
        b = float(b_triangle_entry.get())
        c = float(c_triangle_entry.get())
        alpha = float(90)

        a = round(math.sqrt(b ** 2 - c ** 2), 2)

        betta = round(math.degrees(math.asin(a / b)), 2)
        gamma = round(math.degrees(math.asin(c / b)), 2)

        p = round(a + c + b, 2)

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

        a_result_triangle_label.config(text=a)
        b_result_triangle_label.config(text=b)
        c_result_triangle_label.config(text=c)
        alpha_result_triangle_label.config(text=alpha)
        betta_result_triangle_label.config(text=betta)
        gamma_result_triangle_label.config(text=gamma)
        p_result_triangle_label.config(text=p)
        s_result_triangle_label.config(text=s)
    elif alpha_corner_triangle_entry.get() == '90' and c_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '':  # проверено работает
        if float(betta_corner_triangle_entry.get()) < 90:
            gamma_corner_triangle_entry['state'] = DISABLED
            b_triangle_entry['state'] = DISABLED
            a_triangle_entry['state'] = DISABLED
            c = float(c_triangle_entry.get())  # b
            betta = float(betta_corner_triangle_entry.get())  # alpha
            alpha = float(90)  # gamma

            b = round(c / math.cos(math.radians(betta)), 2)  # c

            a = round(c * math.tan(math.radians(betta)), 2)

            gamma = round(90 - betta, 2)

            p = round(a + c + b, 2)

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    elif alpha_corner_triangle_entry.get() == '90' and a_triangle_entry.get() != '' and gamma_corner_triangle_entry.get() != '':  # проверено работает
        if float(gamma_corner_triangle_entry.get()) < 90:
            b_triangle_entry['state'] = DISABLED
            c_triangle_entry['state'] = DISABLED
            betta_corner_triangle_entry['state'] = DISABLED

            a = float(a_triangle_entry.get())  # b
            gamma = float(gamma_corner_triangle_entry.get())  # alpha
            alpha = float(90)  # gamma

            b = round(a / math.cos(math.radians(gamma)), 2)  # c

            c = round(a * math.tan(math.radians(gamma)), 2)

            betta = round(90 - gamma, 2)

            p = round(a + c + b, 2)

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')

    elif alpha_corner_triangle_entry.get() == '90' and c_triangle_entry.get() != '' and gamma_corner_triangle_entry.get() != '':  # проверено работает
        if float(gamma_corner_triangle_entry.get()) < 90:
            betta_corner_triangle_entry['state'] = DISABLED
            a_triangle_entry['state'] = DISABLED
            b_triangle_entry['state'] = DISABLED

            alpha = float(90)  # gamma
            c = float(c_triangle_entry.get())  # b
            gamma = float(gamma_corner_triangle_entry.get())  # betta

            b = round(c / math.sin(math.radians(gamma)), 2)

            a = round(math.sqrt(b ** 2 - c ** 2), 2)

            betta = round(90 - gamma, 2)

            p = round(a + c + b, 2)

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')

    elif alpha_corner_triangle_entry.get() == '90' and a_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '':  # проверено работает
        if float(betta_corner_triangle_entry.get()) < 90:
            gamma_corner_triangle_entry['state'] = DISABLED
            b_triangle_entry['state'] = DISABLED
            c_triangle_entry['state'] = DISABLED

            alpha = float(90)
            a = float(a_triangle_entry.get())
            betta = float(betta_corner_triangle_entry.get())

            gamma = round(90 - betta, 2)

            b = round(a / math.sin(math.radians(betta)), 2)

            c = round(b * math.sin(math.radians(gamma)), 2)

            p = round(a + c + b, 2)

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    elif alpha_corner_triangle_entry.get() == '90' and b_triangle_entry.get() != '' and betta_corner_triangle_entry.get() != '':  # проверено работает
        if float(betta_corner_triangle_entry.get()) < 90:

            gamma_corner_triangle_entry['state'] = DISABLED
            a_triangle_entry['state'] = DISABLED
            c_triangle_entry['state'] = DISABLED

            alpha = float(90)
            b = float(b_triangle_entry.get())
            betta = float(betta_corner_triangle_entry.get())

            gamma = round(90 - betta, 2)

            a = round(b * math.sin(math.radians(betta)), 2)
            c = round(b * math.sin(math.radians(gamma)), 2)

            p = round(a + c + b, 2)

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)

        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    elif alpha_corner_triangle_entry.get() == '90' and b_triangle_entry.get() != '' and gamma_corner_triangle_entry.get() != '':  # проверено работает
        if float(gamma_corner_triangle_entry.get()) < 90:
            a_triangle_entry['state'] = DISABLED
            c_triangle_entry['state'] = DISABLED
            betta_corner_triangle_entry['state'] = DISABLED

            alpha = float(90)
            b = float(b_triangle_entry.get())
            gamma = float(gamma_corner_triangle_entry.get())

            betta = round(90 - gamma, 2)

            c = round(b * math.sin(math.radians(gamma)), 2)
            a = round(b * math.cos(math.radians(gamma)), 2)

            p = round(a + c + b, 2)
            print(f'P = {p}')

            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)

            a_result_triangle_label.config(text=a)
            b_result_triangle_label.config(text=b)
            c_result_triangle_label.config(text=c)
            alpha_result_triangle_label.config(text=alpha)
            betta_result_triangle_label.config(text=betta)
            gamma_result_triangle_label.config(text=gamma)
            p_result_triangle_label.config(text=p)
            s_result_triangle_label.config(text=s)
        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    else:
        mb.showerror(title='Ошибка', message='Что-то пошло не так')


def reset_triangle_calculate_func():
    a_triangle_entry.delete(0, END)
    b_triangle_entry.delete(0, END)
    c_triangle_entry.delete(0, END)
    alpha_corner_triangle_entry.delete(0, END)
    betta_corner_triangle_entry.delete(0, END)
    gamma_corner_triangle_entry.delete(0, END)

    a_triangle_entry['state'] = NORMAL
    b_triangle_entry['state'] = NORMAL
    c_triangle_entry['state'] = NORMAL
    alpha_corner_triangle_entry['state'] = NORMAL
    betta_corner_triangle_entry['state'] = NORMAL
    gamma_corner_triangle_entry['state'] = NORMAL

    a_result_triangle_label.config(text='')
    b_result_triangle_label.config(text='')
    c_result_triangle_label.config(text='')
    alpha_result_triangle_label.config(text='')
    betta_result_triangle_label.config(text='')
    gamma_result_triangle_label.config(text='')
    p_result_triangle_label.config(text='')
    s_result_triangle_label.config(text='')


def calculate_square_func():
    if a_square_entry.get() != '' and b_square_entry.get() != '':
        d_square_entry['state'] = DISABLED
        alpha_corner_square_entry['state'] = DISABLED
        betta_corner_square_entry['state'] = DISABLED
        s_square_entry['state'] = DISABLED

        a = float(a_square_entry.get())
        b = float(b_square_entry.get())

        p = round(2 * (a + b), 2)

        s = round(a * b, 2)

        d = round(math.sqrt(a ** 2 + b ** 2), 2)

        gamma = round(math.degrees(math.atan(b / a)), 2)

        delta = round(math.degrees(math.atan(a / b)), 2)

        betta = round(2 * gamma, 2)

        alpha = round(2 * delta, 2)

        a_result_square_label.config(text=a)
        b_result_square_label.config(text=b)
        d_result_square_label.config(text=d)
        alpha_result_square_label.config(text=alpha)
        betta_result_square_label.config(text=betta)
        gamma_result_square_label.config(text=gamma)
        delta_result_square_label.config(text=delta)
        p_result_square_label.config(text=p)
        s_result_square_label.config(text=s)

    elif s_square_entry.get() != '' and a_square_entry.get() != '':
        b_square_entry['state'] = DISABLED
        d_square_entry['state'] = DISABLED
        alpha_corner_square_entry['state'] = DISABLED
        betta_corner_square_entry['state'] = DISABLED

        s = float(s_square_entry.get())
        a = float(a_square_entry.get())

        b = round(s / a, 2)

        p = round(2 * (a + b), 2)

        d = round(math.sqrt(a ** 2 + b ** 2), 2)

        gamma = round(math.degrees(math.atan(b / a)), 2)

        delta = round(math.degrees(math.atan(a / b)), 2)

        betta = round(2 * gamma, 2)

        alpha = round(2 * delta, 2)
        a_result_square_label.config(text=a)
        b_result_square_label.config(text=b)
        d_result_square_label.config(text=d)
        alpha_result_square_label.config(text=alpha)
        betta_result_square_label.config(text=betta)
        gamma_result_square_label.config(text=gamma)
        delta_result_square_label.config(text=delta)
        p_result_square_label.config(text=p)
        s_result_square_label.config(text=s)

    elif s_square_entry.get() != '' and b_square_entry.get() != '':
        a_square_entry['state'] = DISABLED
        d_square_entry['state'] = DISABLED
        alpha_corner_square_entry['state'] = DISABLED
        betta_corner_square_entry['state'] = DISABLED

        s = float(s_square_entry.get())
        b = float(b_square_entry.get())

        a = round(s / b, 2)

        p = round(2 * (a + b), 2)

        d = round(math.sqrt(a ** 2 + b ** 2), 2)

        gamma = round(math.degrees(math.atan(b / a)), 2)

        delta = round(math.degrees(math.atan(a / b)), 2)

        betta = round(2 * gamma, 2)

        alpha = round(2 * delta, 2)
        a_result_square_label.config(text=a)
        b_result_square_label.config(text=b)
        d_result_square_label.config(text=d)
        alpha_result_square_label.config(text=alpha)
        betta_result_square_label.config(text=betta)
        gamma_result_square_label.config(text=gamma)
        delta_result_square_label.config(text=delta)
        p_result_square_label.config(text=p)
        s_result_square_label.config(text=s)

    elif d_square_entry.get() != '' and a_square_entry.get() != '':
        b_square_entry['state'] = DISABLED
        alpha_corner_square_entry['state'] = DISABLED
        betta_corner_square_entry['state'] = DISABLED
        s_square_entry['state'] = DISABLED

        d = float(d_square_entry.get())
        a = float(a_square_entry.get())

        b = round(math.sqrt(d ** 2 - a ** 2), 2)

        p = round(2 * (a + b), 2)

        s = round(a * b, 2)

        gamma = round(math.degrees(math.atan(b / a)), 2)

        delta = round(math.degrees(math.atan(a / b)), 2)

        betta = round(2 * gamma, 2)

        alpha = round(2 * delta, 2)
        a_result_square_label.config(text=a)
        b_result_square_label.config(text=b)
        d_result_square_label.config(text=d)
        alpha_result_square_label.config(text=alpha)
        betta_result_square_label.config(text=betta)
        gamma_result_square_label.config(text=gamma)
        delta_result_square_label.config(text=delta)
        p_result_square_label.config(text=p)
        s_result_square_label.config(text=s)

    elif d_square_entry.get() != '' and b_square_entry.get() != '':
        a_square_entry['state'] = DISABLED
        alpha_corner_square_entry['state'] = DISABLED
        betta_corner_square_entry['state'] = DISABLED
        s_square_entry['state'] = DISABLED

        d = float(d_square_entry.get())
        b = float(b_square_entry.get())

        a = round(math.sqrt(d ** 2 - b ** 2), 2)

        p = round(2 * (a + b), 2)

        s = round(a * b, 2)

        gamma = round(math.degrees(math.atan(b / a)), 2)

        delta = round(math.degrees(math.atan(a / b)), 2)

        betta = round(2 * gamma, 2)

        alpha = round(2 * delta, 2)
        a_result_square_label.config(text=a)
        b_result_square_label.config(text=b)
        d_result_square_label.config(text=d)
        alpha_result_square_label.config(text=alpha)
        betta_result_square_label.config(text=betta)
        gamma_result_square_label.config(text=gamma)
        delta_result_square_label.config(text=delta)
        p_result_square_label.config(text=p)
        s_result_square_label.config(text=s)

    elif d_square_entry.get() != '' and alpha_corner_square_entry.get() != '':
        a_square_entry['state'] = DISABLED
        b_square_entry['state'] = DISABLED
        betta_corner_square_entry['state'] = DISABLED
        s_square_entry['state'] = DISABLED

        d = float(d_square_entry.get())
        alpha = float(alpha_corner_square_entry.get())

        b = round(d * math.cos(math.radians(alpha) / 2), 2)
        a = round(d * math.sin(math.radians(alpha) / 2), 2)
        betta = round((360 - alpha - alpha) / 2, 2)
        gamma = round(betta / 2, 2)
        delta = round(alpha / 2, 2)
        p = round(2 * (a + b), 2)
        s = round(a * b, 2)
        a_result_square_label.config(text=a)
        b_result_square_label.config(text=b)
        d_result_square_label.config(text=d)
        alpha_result_square_label.config(text=alpha)
        betta_result_square_label.config(text=betta)
        gamma_result_square_label.config(text=gamma)
        delta_result_square_label.config(text=delta)
        p_result_square_label.config(text=p)
        s_result_square_label.config(text=s)

    elif d_square_entry.get() != '' and betta_corner_square_entry.get() != '':
        a_square_entry['state'] = DISABLED
        b_square_entry['state'] = DISABLED
        alpha_corner_square_entry['state'] = DISABLED
        s_square_entry['state'] = DISABLED

        d = float(d_square_entry.get())
        betta = float(betta_corner_square_entry.get())

        b = round(d * math.cos(math.radians(betta) / 2), 2)
        a = round(d * math.sin(math.radians(betta) / 2), 2)
        alpha = round((360 - betta - betta) / 2, 2)
        gamma = round(alpha / 2, 2)
        delta = round(betta / 2, 2)
        p = round(2 * (a + b), 2)
        s = round(a * b, 2)
        a_result_square_label.config(text=a)
        b_result_square_label.config(text=b)
        d_result_square_label.config(text=d)
        alpha_result_square_label.config(text=alpha)
        betta_result_square_label.config(text=betta)
        gamma_result_square_label.config(text=gamma)
        delta_result_square_label.config(text=delta)
        p_result_square_label.config(text=p)
        s_result_square_label.config(text=s)

    else:
        mb.showerror(title='Ошибка', message='Что-то пошло не так')


def reset_square_calculate_func():
    a_square_entry.delete(0, END)
    b_square_entry.delete(0, END)
    d_square_entry.delete(0, END)
    alpha_corner_square_entry.delete(0, END)
    betta_corner_square_entry.delete(0, END)
    s_square_entry.delete(0, END)

    a_square_entry['state'] = NORMAL
    b_square_entry['state'] = NORMAL
    d_square_entry['state'] = NORMAL
    alpha_corner_square_entry['state'] = NORMAL
    betta_corner_square_entry['state'] = NORMAL
    s_square_entry['state'] = NORMAL

    a_result_square_label.config(text='')
    b_result_square_label.config(text='')
    d_result_square_label.config(text='')
    alpha_result_square_label.config(text='')
    betta_result_square_label.config(text='')
    gamma_result_square_label.config(text='')
    delta_result_square_label.config(text='')
    p_result_square_label.config(text='')
    s_result_square_label.config(text='')


def calculate_rectangle_func():
    if a_rectangle_entry.get() != '':
        d_rectangle_entry['state'] = DISABLED
        p_rectangle_entry['state'] = DISABLED
        s_rectangle_entry['state'] = DISABLED

        a = float(a_rectangle_entry.get())

        d = round(math.sqrt(2) * a, 2)
        p = round(4 * a, 2)
        s = round(a ** 2, 2)

        a_result_rectangle_label.config(text=a)
        d_result_rectangle_label.config(text=d)
        p_result_rectangle_label.config(text=p)
        s_result_rectangle_label.config(text=s)

    elif s_rectangle_entry.get() != '':
        a_rectangle_entry['state'] = DISABLED
        d_rectangle_entry['state'] = DISABLED
        p_rectangle_entry['state'] = DISABLED
        s = float(s_rectangle_entry.get())

        a = round(math.sqrt(s), 2)

        p = round(4 * a, 2)

        d = round(math.sqrt(2) * a, 2)

        a_result_rectangle_label.config(text=a)
        d_result_rectangle_label.config(text=d)
        p_result_rectangle_label.config(text=p)
        s_result_rectangle_label.config(text=s)
    elif d_rectangle_entry.get() != '':
        a_rectangle_entry['state'] = DISABLED
        p_rectangle_entry['state'] = DISABLED
        s_rectangle_entry['state'] = DISABLED
        d = float(d_rectangle_entry.get())

        a = round(d / math.sqrt(2), 2)

        p = round(4 * a, 2)

        s = round(a ** 2, 2)

        a_result_rectangle_label.config(text=a)
        d_result_rectangle_label.config(text=d)
        p_result_rectangle_label.config(text=p)
        s_result_rectangle_label.config(text=s)
    elif p_rectangle_entry.get() != '':
        a_rectangle_entry['state'] = DISABLED
        d_rectangle_entry['state'] = DISABLED
        s_rectangle_entry['state'] = DISABLED
        p = float(p_rectangle_entry.get())

        a = round(p / 4, 2)

        s = round(a ** 2, 2)

        d = round(math.sqrt(2) * a, 2)

        a_result_rectangle_label.config(text=a)
        d_result_rectangle_label.config(text=d)
        p_result_rectangle_label.config(text=p)
        s_result_rectangle_label.config(text=s)
    else:
        mb.showerror(title='Ошибка', message='Что-то пошло не так')


def reset_rectangle_calculate_func():
    a_rectangle_entry.delete(0, END)
    d_rectangle_entry.delete(0, END)
    p_rectangle_entry.delete(0, END)
    s_rectangle_entry.delete(0, END)

    a_rectangle_entry['state'] = NORMAL
    d_rectangle_entry['state'] = NORMAL
    p_rectangle_entry['state'] = NORMAL
    s_rectangle_entry['state'] = NORMAL

    a_result_rectangle_label.config(text='')
    d_result_rectangle_label.config(text='')
    p_result_rectangle_label.config(text='')
    s_result_rectangle_label.config(text='')


def perevod_func():
    if mm_entry.get() != '' and sm_entry.get() == '' and m_entry.get() == '':
        mm = float(mm_entry.get())

        sm = round(mm / 10, 2)

        m = round(mm / 1000, 4)

        sm_entry.insert(0, sm)
        m_entry.insert(0, m)

    elif sm_entry.get() != '' and mm_entry.get() == '' and m_entry.get() == '':
        sm = float(sm_entry.get())

        mm = round(sm * 10, 2)

        m = round(sm / 100, 2)

        mm_entry.insert(0, mm)
        m_entry.insert(0, m)

    elif m_entry.get() != '' and sm_entry.get() == '' and mm_entry.get() == '':
        m = float(m_entry.get())

        sm = round(m * 100, 2)

        mm = round(m * 1000, 2)

        mm_entry.insert(0, mm)
        sm_entry.insert(0, sm)

    elif min_entry.get() != '' and degres_entry.get() == '' and rad_entry.get() == '':
        min = float(min_entry.get())

        degres = round(min / 60, 2)

        rad = round(min * (math.pi / (60 * 180)), 4)

        degres_entry.insert(0, degres)
        rad_entry.insert(0, rad)

    elif degres_entry.get() != '' and rad_entry.get() == '' and min_entry.get() == '':
        degres = float(degres_entry.get())

        min = round(degres * 60, 2)
        rad = round(degres * (math.pi / 180), 2)

        min_entry.insert(0, min)
        rad_entry.insert(0, rad)

    elif rad_entry.get() != '' and min_entry.get() == '' and degres_entry.get() == '':
        rad = float(rad_entry.get())

        min = round(rad * ((60 * 180) / math.pi), 2)
        degres = round(rad * (180 / math.pi), 2)

        min_entry.insert(0, min)
        degres_entry.insert(0, degres)

    else:
        mb.showerror(title='Ошибка', message='Что-то пошло не так')


def reset_perevod_func():
    min_entry.delete(0, END)

    mm_entry.delete(0, END)

    m_entry.delete(0, END)

    sm_entry.delete(0, END)

    degres_entry.delete(0, END)

    rad_entry.delete(0, END)


def calculate_trapezium_func():
    if a_trapezium_entry.get() != '' and b_trapezium_entry.get() != '' and c_trapezium_entry.get() != '' and d_trapezium_entry.get() != '':
        h_trapezium_entry['state'] = DISABLED
        m_trapezium_entry['state'] = DISABLED
        a = float(a_trapezium_entry.get())
        b = float(b_trapezium_entry.get())
        c = float(c_trapezium_entry.get())
        d = float(d_trapezium_entry.get())

        p = round(a + b + c + d, 2)

        h = round(math.sqrt(a ** 2 - ((((d - b) ** 2) + a ** 2 - c ** 2) / (2 * (d - b))) ** 2), 2)

        m = round((b + d) / 2, 2)

        s = round(h * m, 2)

        d_1 = round(math.sqrt((c ** 2) + (d * b) - ((d * (c ** 2 - a ** 2)) / (d - b))), 2)

        d_2 = round(math.sqrt((a ** 2 + d * b) - (d * (a ** 2 - c ** 2)) / (d - b)), 2)

        a_result_trapezium_label.config(text=a)
        b_result_trapezium_label.config(text=b)
        c_result_trapezium_label.config(text=c)
        d_result_trapezium_label.config(text=d)
        m_result_trapezium_label.config(text=m)
        h_result_trapezium_label.config(text=h)
        s_result_trapezium_label.config(text=s)
        p_result_trapezium_label.config(text=p)
        d_1_result_trapezium_label.config(text=d_1)
        d_2_result_trapezium_label.config(text=d_2)

    elif b_trapezium_entry.get() != '' and d_trapezium_entry.get() != '' and h_trapezium_entry.get() != '':
        a_trapezium_entry['state'] = DISABLED
        c_trapezium_entry['state'] = DISABLED
        m_trapezium_entry['state'] = DISABLED
        b = float(b_trapezium_entry.get())
        d = float(d_trapezium_entry.get())
        h = float(h_trapezium_entry.get())

        d_1 = round(math.sqrt((h ** 2) + ((b + d) / 2) ** 2), 2)
        d_2 = d_1

        a = round(math.sqrt((d_1 ** 2) - (d * b)), 2)
        c = a

        m = round((b + d) / 2, 2)

        p = round(2 * a + b + d, 2)

        s = round(h * m, 2)

        a_result_trapezium_label.config(text=a)
        b_result_trapezium_label.config(text=b)
        c_result_trapezium_label.config(text=c)
        d_result_trapezium_label.config(text=d)
        m_result_trapezium_label.config(text=m)
        h_result_trapezium_label.config(text=h)
        s_result_trapezium_label.config(text=s)
        p_result_trapezium_label.config(text=p)
        d_1_result_trapezium_label.config(text=d_1)
        d_2_result_trapezium_label.config(text=d_2)
    elif h_trapezium_entry.get() != '' and m_trapezium_entry.get() != '':
        a_trapezium_entry['state'] = DISABLED
        b_trapezium_entry['state'] = DISABLED
        c_trapezium_entry['state'] = DISABLED
        d_trapezium_entry['state'] = DISABLED
        h = float(h_trapezium_entry.get())
        m = float(m_trapezium_entry.get())

        s = round(h * m, 2)
        d_1 = round(math.sqrt((h ** 2) + (m ** 2)), 2)
        d_2 = d_1

        a_result_trapezium_label.config(text='')
        b_result_trapezium_label.config(text='')
        c_result_trapezium_label.config(text='')
        d_result_trapezium_label.config(text='')
        m_result_trapezium_label.config(text=m)
        h_result_trapezium_label.config(text=h)
        s_result_trapezium_label.config(text=s)
        p_result_trapezium_label.config(text='')
        d_1_result_trapezium_label.config(text=d_1)
        d_2_result_trapezium_label.config(text=d_2)
    else:
        mb.showerror(title='Ошибка', message='Что-то пошло не так')


def reset_trapezium_calculate_func():
    a_trapezium_entry['state'] = NORMAL
    b_trapezium_entry['state'] = NORMAL
    c_trapezium_entry['state'] = NORMAL
    d_trapezium_entry['state'] = NORMAL
    m_trapezium_entry['state'] = NORMAL
    h_trapezium_entry['state'] = NORMAL

    a_trapezium_entry.delete(0, END)
    b_trapezium_entry.delete(0, END)
    c_trapezium_entry.delete(0, END)
    d_trapezium_entry.delete(0, END)
    m_trapezium_entry.delete(0, END)
    h_trapezium_entry.delete(0, END)

    a_result_trapezium_label.config(text='')
    b_result_trapezium_label.config(text='')
    c_result_trapezium_label.config(text='')
    d_result_trapezium_label.config(text='')
    m_result_trapezium_label.config(text='')
    h_result_trapezium_label.config(text='')
    s_result_trapezium_label.config(text='')
    p_result_trapezium_label.config(text='')
    d_1_result_trapezium_label.config(text='')
    d_2_result_trapezium_label.config(text='')


# Окно расчётов трапеции начинается тут(13 окно)
calculate_trapezium_window = Tk()
calculate_trapezium_window['bg'] = first_color
calculate_trapezium_window.title('Калькулатор трапеции')

calculate_trapezium_window.deiconify()

definition_label = Label(calculate_trapezium_window, text='Калькулятор', font='Oswald 15',
                         bg=first_color,
                         fg=third_color)  # Надпись определение треугольника
definition_label.grid(row=0, column=2, pady=15, padx=15)  # Надпись определение треугольника расположение

a_label = Label(calculate_trapezium_window, text='A = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
a_label.grid(row=1, column=1, padx=15, pady=5)

a_trapezium_entry = Entry(calculate_trapezium_window, width=4, font='Oswald 10', bg=fifth_color)
a_trapezium_entry.grid(row=1, column=2, padx=15)

b_label = Label(calculate_trapezium_window, text='B = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
b_label.grid(row=2, column=1, padx=15)

b_trapezium_entry = Entry(calculate_trapezium_window, width=4, font='Oswald 10', bg=fifth_color)
b_trapezium_entry.grid(row=2, column=2, padx=15)

c_label = Label(calculate_trapezium_window, text='C = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
c_label.grid(row=3, column=1, padx=15, pady=5)

c_trapezium_entry = Entry(calculate_trapezium_window, width=4, font='Oswald 10', bg=fifth_color)
c_trapezium_entry.grid(row=3, column=2, padx=15)

d_label = Label(calculate_trapezium_window, text='D = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
d_label.grid(row=4, column=1, padx=15)

d_trapezium_entry = Entry(calculate_trapezium_window, width=4, font='Oswald 10', bg=fifth_color)
d_trapezium_entry.grid(row=4, column=2, padx=15)

h_label = Label(calculate_trapezium_window, text='h = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
h_label.grid(row=5, column=1, padx=15, pady=5)

h_trapezium_entry = Entry(calculate_trapezium_window, width=4, font='Oswald 10', bg=fifth_color)
h_trapezium_entry.grid(row=5, column=2, padx=15)

m_label = Label(calculate_trapezium_window, text='m = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
m_label.grid(row=6, column=1, padx=15)

m_trapezium_entry = Entry(calculate_trapezium_window, width=4, font='Oswald 10', bg=fifth_color)
m_trapezium_entry.grid(row=6, column=2, padx=15)

d_first_label = Label(calculate_trapezium_window, text='d₁= ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
d_first_label.grid(row=7, column=1, padx=15, pady=5)

d_second_label = Label(calculate_trapezium_window, text='d₂= ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
d_second_label.grid(row=8, column=1, padx=15)

p_label = Label(calculate_trapezium_window, text='P = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
p_label.grid(row=9, column=1, pady=5)

s_label = Label(calculate_trapezium_window, text='S = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
s_label.grid(row=10, column=1)

# Виджеты для вывода данных
a_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
a_result_trapezium_label.place(x=60, y=65)

b_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
b_result_trapezium_label.place(x=60, y=97)

c_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
c_result_trapezium_label.place(x=60, y=130)

d_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
d_result_trapezium_label.place(x=60, y=165)

h_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
h_result_trapezium_label.place(x=60, y=200)

m_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
m_result_trapezium_label.place(x=60, y=235)

d_1_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color,
                                   width=5)
d_1_result_trapezium_label.place(x=60, y=267)

d_2_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color,
                                   width=5)
d_2_result_trapezium_label.place(x=60, y=303)

p_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color,
                                 width=5)
p_result_trapezium_label.place(x=60, y=336)

s_result_trapezium_label = Label(calculate_trapezium_window, text='', font='Oswald 15', bg=first_color, fg=third_color,
                                 width=5)
s_result_trapezium_label.place(x=60, y=369)

trapezium_first_canvas = Canvas(calculate_trapezium_window, width=160, height=150, bg=first_color, highlightthickness=0)
trapezium_first_canvas.create_polygon((40, 40), (120, 40), (150, 110), (10, 110), fill=fifth_color, outline=second_color)
trapezium_first_canvas.create_line((40, 40), (40, 110), fill=second_color)
trapezium_first_canvas.create_text(47, 65, text="h", font="Oswald 10", fill=third_color)
trapezium_first_canvas.create_text(15, 70, text="A", font="Oswald 10", fill=third_color)
trapezium_first_canvas.create_text(75, 30, text="B", font="Oswald 10", fill=third_color)
trapezium_first_canvas.create_text(145, 70, text="C", font="Oswald 10", fill=third_color)
trapezium_first_canvas.create_text(75, 125, text="D", font="Oswald 10", fill=third_color)
trapezium_first_canvas.create_line((40, 40), (150, 110), fill=second_color)
trapezium_first_canvas.create_text(67, 86, text="d₁", font="Oswald 10", fill=third_color)
trapezium_first_canvas.create_line((120, 40), (10, 110), fill=second_color)
trapezium_first_canvas.create_text(97, 86, text="d₂", font="Oswald 10", fill=third_color)
trapezium_first_canvas.create_line((25, 75), (135, 75), fill=second_color)
trapezium_first_canvas.create_text(103, 68, text="m", font="Oswald 10", fill=third_color)
trapezium_first_canvas.place(x=350, y=80)

calculate_square_button = Button(calculate_trapezium_window, text='Произвести расчёты', bg=first_color, fg=fourth_color, font='Oswald 10', command=calculate_trapezium_func)
calculate_square_button.grid(row=11, column=8, padx=15)

back_figure_button = Button(calculate_trapezium_window, text='Сбросить', command=reset_trapezium_calculate_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_figure_button.grid(row=11, column=3, pady=15, padx=15)  # Кнопка назад расположение

back_figure_button = Button(calculate_trapezium_window, text='Назад', bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_figure_button.grid(row=11, column=2, pady=15, padx=15)  # Кнопка назад расположение
back_figure_button.bind('<Button-1>', visible_trapezium_window_event_func)

exit_button = Button(calculate_trapezium_window, text='Выход', command=exit_project_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
exit_button.grid(row=11, column=1, pady=15, padx=15)  # Кнопка назад расположение
# Окно расчётов трапеции заканчивается тут(13 окно)

# Окно переводов начинается тут(12 окно)
perevod_ed_window = Tk()
perevod_ed_window['bg'] = first_color
perevod_ed_window.title('Переводчик')

perevod_ed_window.withdraw()
empty_label = Label(perevod_ed_window, fg=first_color, bg=first_color)
empty_label.grid(row=1, column=0, padx=5)

main_label = Label(perevod_ed_window, text='Переводчик', fg=third_color, bg=first_color, font='Oswald 15')
main_label.grid(row=0, column=1, sticky=W, padx=5, columnspan=3, pady=15)

mm_label = Label(perevod_ed_window, text='Мм = ', fg=second_color, bg=first_color, font='Oswald 15')
mm_label.grid(row=1, column=1, sticky=W, padx=5, pady=15)

mm_entry = Entry(perevod_ed_window, bg=fifth_color, font='Oswald 10', width=5)
mm_entry.grid(row=1, column=2, sticky=W)

sm_label = Label(perevod_ed_window, text='См = ', fg=second_color, bg=first_color, font='Oswald 15')
sm_label.grid(row=1, column=3, sticky=W, padx=5)

sm_entry = Entry(perevod_ed_window, bg=fifth_color, font='Oswald 10', width=5)
sm_entry.grid(row=1, column=4, sticky=W)

m_label = Label(perevod_ed_window, text='М = ', fg=second_color, bg=first_color, font='Oswald 15')
m_label.grid(row=1, column=5, sticky=W, padx=5)

m_entry = Entry(perevod_ed_window, bg=fifth_color, font='Oswald 10', width=5)
m_entry.grid(row=1, column=6, sticky=W)

min_label = Label(perevod_ed_window, text='Мин = ', fg=second_color, bg=first_color, font='Oswald 15')
min_label.grid(row=2, column=1, sticky=W, padx=5, pady=15)

min_entry = Entry(perevod_ed_window, bg=fifth_color, font='Oswald 10', width=5)
min_entry.grid(row=2, column=2, sticky=W)

degres_label = Label(perevod_ed_window, text='Гр° = ', fg=second_color, bg=first_color, font='Oswald 15')
degres_label.grid(row=2, column=3, sticky=W, padx=5)

degres_entry = Entry(perevod_ed_window, bg=fifth_color, font='Oswald 10', width=5)
degres_entry.grid(row=2, column=4, sticky=W)

rad_label = Label(perevod_ed_window, text='Рад = ', fg=second_color, bg=first_color, font='Oswald 15')
rad_label.grid(row=2, column=5, sticky=W, padx=5)

rad_entry = Entry(perevod_ed_window, bg=fifth_color, font='Oswald 10', width=5)
rad_entry.grid(row=2, column=6, sticky=W)

result_button = Button(perevod_ed_window, text='Перевести', fg=fourth_color, bg=first_color, font='Oswald 10', command=perevod_func)
result_button.grid(row=3, column=1, sticky=W, padx=5, pady=15, columnspan=2)

reset_button = Button(perevod_ed_window, text='Очистить', fg=fourth_color, bg=first_color, font='Oswald 10', command=reset_perevod_func)
reset_button.grid(row=3, column=2, sticky=W, padx=15, pady=15, columnspan=2)

back_button = Button(perevod_ed_window, text='Назад', bg=first_color, fg=fourth_color, command=visible_geometry_window_func)  # Кнопка назад
back_button.place(x=15, y=460)  # Кнопка назад

# Окно переводов заканчивается тут(12 окно)
# Окно расчётов квадрата начинается тут(11 окно)
calculate_rectangle_window = Tk()
calculate_rectangle_window['bg'] = first_color
calculate_rectangle_window.title('Калькулатор квадрата')

calculate_rectangle_window.withdraw()

definition_label = Label(calculate_rectangle_window, text='Калькулятор', font='Oswald 15',
                         bg=first_color,
                         fg=third_color)  # Надпись определение треугольника
definition_label.grid(row=1, column=2, pady=15, padx=15)  # Надпись определение треугольника расположение

a_label = Label(calculate_rectangle_window, text='A = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
a_label.grid(row=2, column=1, padx=15, pady=20)

a_rectangle_entry = Entry(calculate_rectangle_window, width=4, font='Oswald 10', bg=fifth_color)
a_rectangle_entry.grid(row=2, column=2, padx=15)

d_square_label = Label(calculate_rectangle_window, text='D = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
d_square_label.grid(row=3, column=1, padx=15)

d_rectangle_entry = Entry(calculate_rectangle_window, width=4, font='Oswald 10', bg=fifth_color)
d_rectangle_entry.grid(row=3, column=2, padx=15)

p_corner_label = Label(calculate_rectangle_window, text='P = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
p_corner_label.grid(row=4, column=1, pady=20)

p_rectangle_entry = Entry(calculate_rectangle_window, width=4, font='Oswald 10', bg=fifth_color)
p_rectangle_entry.grid(row=4, column=2, padx=15)

s_corner_label = Label(calculate_rectangle_window, text='S = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
s_corner_label.grid(row=5, column=1)

s_rectangle_entry = Entry(calculate_rectangle_window, width=4, font='Oswald 10', bg=fifth_color)
s_rectangle_entry.grid(row=5, column=2, padx=15)

# Виджеты для вывода данных
a_result_rectangle_label = Label(calculate_rectangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
a_result_rectangle_label.place(x=60, y=78)

d_result_rectangle_label = Label(calculate_rectangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
d_result_rectangle_label.place(x=60, y=128)

p_result_rectangle_label = Label(calculate_rectangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
p_result_rectangle_label.place(x=60, y=175)

s_result_rectangle_label = Label(calculate_rectangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
s_result_rectangle_label.place(x=60, y=225)

rectangle_canvas = Canvas(calculate_rectangle_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = rectangle_canvas.create_rectangle((20, 30), (140, 140), fill=fifth_color, outline=second_color)
rectangle_canvas.create_line(20, 30, 140, 140, fill=third_color)
rectangle_canvas.create_text(80, 20, text='A', font='Oswald 15', fill=third_color)
rectangle_canvas.create_text(80, 68, text='D', font='Oswald 15', fill=third_color)
rectangle_canvas.place(x=350, y=80)

calculate_rectangle_button = Button(calculate_rectangle_window, text='Произвести расчёты', bg=first_color, fg=fourth_color, font='Oswald 10', command=calculate_rectangle_func)
calculate_rectangle_button.grid(row=11, column=8, padx=15)

back_figure_button = Button(calculate_rectangle_window, text='Сбросить', command=reset_rectangle_calculate_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_figure_button.grid(row=11, column=3, pady=15, padx=15)  # Кнопка назад расположение

back_figure_button = Button(calculate_rectangle_window, text='Назад', bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_figure_button.grid(row=11, column=2, pady=15, padx=15)  # Кнопка назад расположение
back_figure_button.bind('<Button-1>', visible_rectangle_window_event_func)

exit_button = Button(calculate_rectangle_window, text='Выход', command=exit_project_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
exit_button.grid(row=11, column=1, pady=15, padx=15)  # Кнопка назад расположение
# Окно расчётов квадрата заканчивается тут(11 окно)


# Окно расчётов прямоугольника начинается тут(10 окно)
calculate_square_window = Tk()
calculate_square_window['bg'] = first_color
calculate_square_window.title('Калькулатор прямоугольника')

calculate_square_window.withdraw()

definition_label = Label(calculate_square_window, text='Калькулятор прямоугольника', font='Oswald 15',
                         bg=first_color,
                         fg=third_color)  # Надпись определение треугольника
definition_label.grid(row=1, column=2, pady=15, padx=15)  # Надпись определение треугольника расположение

a_label = Label(calculate_square_window, text='A = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
a_label.grid(row=2, column=1, padx=15, pady=10)

a_square_entry = Entry(calculate_square_window, width=4, font='Oswald 10', bg=fifth_color)
a_square_entry.grid(row=2, column=2, padx=15)

b_label = Label(calculate_square_window, text='B = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
b_label.grid(row=3, column=1, padx=15)

b_square_entry = Entry(calculate_square_window, width=4, font='Oswald 10', bg=fifth_color)
b_square_entry.grid(row=3, column=2, padx=15)

a_corner_label = Label(calculate_square_window, text='⦟α = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
a_corner_label.grid(row=4, column=1, padx=15, pady=10)

alpha_corner_square_entry = Entry(calculate_square_window, width=4, font='Oswald 10', bg=fifth_color)
alpha_corner_square_entry.grid(row=4, column=2, padx=15)

b_corner_label = Label(calculate_square_window, text='⦟β = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
b_corner_label.grid(row=5, column=1, padx=15)

betta_corner_square_entry = Entry(calculate_square_window, width=4, font='Oswald 10', bg=fifth_color)
betta_corner_square_entry.grid(row=5, column=2, padx=15)

y_corner_label = Label(calculate_square_window, text='⦟γ = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
y_corner_label.grid(row=6, column=1, padx=15, pady=10)

d_corner_label = Label(calculate_square_window, text='⦟δ = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
d_corner_label.grid(row=7, column=1, padx=15)

d_square_label = Label(calculate_square_window, text='D = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
d_square_label.grid(row=8, column=1, padx=15, pady=10)

d_square_entry = Entry(calculate_square_window, width=4, font='Oswald 10', bg=fifth_color)
d_square_entry.grid(row=8, column=2, padx=15)

p_corner_label = Label(calculate_square_window, text='P = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
p_corner_label.grid(row=9, column=1)

s_corner_label = Label(calculate_square_window, text='S = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
s_corner_label.grid(row=10, column=1, pady=10)

s_square_entry = Entry(calculate_square_window, width=4, font='Oswald 10', bg=fifth_color)
s_square_entry.grid(row=10, column=2, padx=15)

# Виджеты для вывода данных
a_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
a_result_square_label.place(x=60, y=68)

b_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
b_result_square_label.place(x=60, y=107)

alpha_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
alpha_result_square_label.place(x=60, y=146)

betta_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
betta_result_square_label.place(x=60, y=185)

gamma_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
gamma_result_square_label.place(x=60, y=224)

delta_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
delta_result_square_label.place(x=60, y=263)

d_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color,
                              width=5)
d_result_square_label.place(x=60, y=302)

p_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color,
                              width=5)
p_result_square_label.place(x=60, y=341)

s_result_square_label = Label(calculate_square_window, text='', font='Oswald 15', bg=first_color, fg=third_color,
                              width=5)
s_result_square_label.place(x=60, y=380)

square_canvas = Canvas(calculate_square_window, width=180, height=150, bg=first_color, highlightthickness=0)
square_canvas.create_rectangle((20, 30), (160, 120), fill=fifth_color, outline=second_color)
square_canvas.create_line(20, 30, 160, 120, fill=third_color)
square_canvas.create_line(160, 30, 20, 120, fill=third_color)
square_canvas.create_text(7, 75, text="A", font="Oswald 15", fill=third_color)
square_canvas.create_text(172, 75, text="A", font="Oswald 15", fill=third_color)
square_canvas.create_text(90, 15, text="B", font="Oswald 15", fill=third_color)
square_canvas.create_text(90, 135, text="B", font="Oswald 15", fill=third_color)
square_canvas.create_text(135, 65, text="D", font="Oswald 15", fill=third_color)
square_canvas.create_text(65, 73, text="α", font="Oswald 15", fill=third_color)
square_canvas.create_text(92, 57, text="β", font="Oswald 15", fill=third_color)
square_canvas.create_text(28, 96, text="γ", font="Oswald 15", fill=third_color)
square_canvas.create_text(50, 112, text="δ", font="Oswald 15", fill=third_color)
square_canvas.place(x=350, y=80)

calculate_square_button = Button(calculate_square_window, text='Произвести расчёты', bg=first_color, fg=fourth_color,
                                 font='Oswald 10', command=calculate_square_func)
calculate_square_button.grid(row=11, column=8, padx=15)

back_figure_button = Button(calculate_square_window, text='Сбросить', command=reset_square_calculate_func,
                            bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_figure_button.grid(row=11, column=3, pady=15, padx=15)  # Кнопка назад расположение

back_figure_button = Button(calculate_square_window, text='Назад', bg=first_color, fg=fourth_color,
                            font='Oswald 10')  # Кнопка назад
back_figure_button.grid(row=11, column=2, pady=15, padx=15)  # Кнопка назад расположение
back_figure_button.bind('<Button-1>', visible_square_window_event_func)

exit_button = Button(calculate_square_window, text='Выход', command=exit_project_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
exit_button.grid(row=11, column=1, pady=15, padx=15)  # Кнопка назад расположение
# Окно расчётов прямоугольника заканчивается тут(10 окно)

# Окно формул начинается тут(9 окно)
formuls_window = Tk()  # Окно треугольника
formuls_window.title('Формулы')  # Заголовок окна с формулами
formuls_window['bg'] = first_color

formuls_window.withdraw()  # Скрытие окна c формулами

title_formulas_label = Label(formuls_window, text='', font='Oswald 15', bg=first_color, fg=second_color, justify=LEFT)  # Надпись аксиомы треугольника
title_formulas_label.grid(row=0, column=0, padx=10, sticky=W, pady=15)  # Надпись аксиомы треугольника расположение

first_formulas_label = Label(formuls_window, text='',
                             font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
first_formulas_label.grid(row=1, column=0, columnspan=9, padx=10, sticky=W, pady=10)  # Надпись аксиомы 1 расположение

second_formulas_label = Label(formuls_window, text='', font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)
second_formulas_label.grid(row=2, column=0, columnspan=9, padx=10, sticky=W)

third_formulas_label = Label(formuls_window, text='', font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)
third_formulas_label.grid(row=3, column=0, columnspan=9, padx=10, sticky=W, pady=10)

fourth_formulas_label = Label(formuls_window, text='', font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)
fourth_formulas_label.grid(row=4, column=0, columnspan=9, padx=10, sticky=W)

fifth_formulas_label = Label(formuls_window, text='', font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)
fifth_formulas_label.grid(row=5, column=0, columnspan=9, padx=10, sticky=W, pady=10)
# Окно формул заканчивается тут(9 окно)

# Окно расчётов треугольника начинается тут(8 окно)
calculate_triangle_window = Tk()  # Окно треугольника
calculate_triangle_window.title('Калькулятор')  # Заголовок окна треугольника
calculate_triangle_window['bg'] = first_color

calculate_triangle_window.withdraw()  # Скрытие окна треугольника

definition_label = Label(calculate_triangle_window, text='Калькулятор треугольника', font='Oswald 15',
                         bg=first_color,
                         fg=third_color)  # Надпись определение треугольника
definition_label.grid(row=1, column=2, pady=15, padx=15)  # Надпись определение треугольника расположение

a_label = Label(calculate_triangle_window, text='A = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
a_label.grid(row=2, column=1, padx=15, pady=15)

a_triangle_entry = Entry(calculate_triangle_window, width=4, font='Oswald 10', bg=fifth_color)
a_triangle_entry.grid(row=2, column=2, padx=15)

b_label = Label(calculate_triangle_window, text='B = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
b_label.grid(row=3, column=1, padx=15)

b_triangle_entry = Entry(calculate_triangle_window, width=4, font='Oswald 10', bg=fifth_color)
b_triangle_entry.grid(row=3, column=2, padx=15)

c_label = Label(calculate_triangle_window, text='C = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
c_label.grid(row=4, column=1, padx=15, pady=15)

c_triangle_entry = Entry(calculate_triangle_window, width=4, font='Oswald 10', bg=fifth_color)
c_triangle_entry.grid(row=4, column=2, padx=15)

a_corner_label = Label(calculate_triangle_window, text='⦟α = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
a_corner_label.grid(row=5, column=1, padx=15)

alpha_corner_triangle_entry = Entry(calculate_triangle_window, width=4, font='Oswald 10', bg=fifth_color)
alpha_corner_triangle_entry.grid(row=5, column=2, padx=15)

b_corner_label = Label(calculate_triangle_window, text='⦟β = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
b_corner_label.grid(row=6, column=1, padx=15, pady=15)

betta_corner_triangle_entry = Entry(calculate_triangle_window, width=4, font='Oswald 10', bg=fifth_color)
betta_corner_triangle_entry.grid(row=6, column=2, padx=15)

y_corner_label = Label(calculate_triangle_window, text='⦟γ = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
y_corner_label.grid(row=7, column=1, padx=15)

gamma_corner_triangle_entry = Entry(calculate_triangle_window, width=4, font='Oswald 10', bg=fifth_color)
gamma_corner_triangle_entry.grid(row=7, column=2, padx=15)

p_corner_label = Label(calculate_triangle_window, text='P = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
p_corner_label.grid(row=8, column=1, pady=15)

s_corner_label = Label(calculate_triangle_window, text='S = ', font='Oswald 15', bg=first_color, fg=second_color, width=3)
s_corner_label.grid(row=9, column=1)

# Виджеты для вывода данных
a_result_triangle_label = Label(calculate_triangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
a_result_triangle_label.place(x=60, y=75)

b_result_triangle_label = Label(calculate_triangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
b_result_triangle_label.place(x=60, y=117)

c_result_triangle_label = Label(calculate_triangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
c_result_triangle_label.place(x=60, y=162)

alpha_result_triangle_label = Label(calculate_triangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
alpha_result_triangle_label.place(x=60, y=206)

betta_result_triangle_label = Label(calculate_triangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
betta_result_triangle_label.place(x=60, y=250)

gamma_result_triangle_label = Label(calculate_triangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
gamma_result_triangle_label.place(x=60, y=294)

p_result_triangle_label = Label(calculate_triangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
p_result_triangle_label.place(x=60, y=338)

s_result_triangle_label = Label(calculate_triangle_window, text='', font='Oswald 15', bg=first_color, fg=third_color, width=5)
s_result_triangle_label.place(x=60, y=381)

calculate_triangle_canvas = Canvas(calculate_triangle_window, width=180, height=160, bg=first_color, highlightthickness=0)
main_triangle = calculate_triangle_canvas.create_polygon((40, 30), (10, 140), (150, 140), fill=fifth_color, outline=second_color)
calculate_triangle_canvas.create_text(155, 140, text="β", font="Oswald 15", fill=third_color)
calculate_triangle_canvas.create_text(5, 140, text="α", font="Oswald 15", fill=third_color)
calculate_triangle_canvas.create_text(40, 15, text="γ", font="Oswald 15", fill=third_color)
calculate_triangle_canvas.create_text(10, 80, text="A", font="Oswald 15", fill=third_color)
calculate_triangle_canvas.create_text(80, 152, text="C", font="Oswald 15", fill=third_color)
calculate_triangle_canvas.create_text(110, 80, text="B", font="Oswald 15", fill=third_color)
calculate_triangle_canvas.place(x=350, y=80)

calculate_triangle_button = Button(calculate_triangle_window, text='Произвести расчёты', bg=first_color, fg=fourth_color, font='Oswald 10', command=calculate_triangle_func)
calculate_triangle_button.grid(row=10, column=8, padx=15)

back_figure_button = Button(calculate_triangle_window, text='Сбросить', command=reset_triangle_calculate_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_figure_button.grid(row=10, column=3, pady=15, padx=15)  # Кнопка назад расположение

back_figure_button = Button(calculate_triangle_window, text='Назад', bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_figure_button.grid(row=10, column=2, pady=15, padx=15)  # Кнопка назад расположение
back_figure_button.bind('<Button-1>', visible_triangle_window_event_func)

exit_button = Button(calculate_triangle_window, text='Выход', command=exit_project_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
exit_button.grid(row=10, column=1, pady=15, padx=15)  # Кнопка назад расположение
# Окно расчётов треугольника заканчивается тут(8 окно)


# Окно теорем треугольника начинается тут(7 окно)
theorems_window = Tk()  # Создание окна с аксиомами треугольника
theorems_window.title('Теоремы')  # Заголовок окна с аксиомами треугольника
theorems_window['bg'] = first_color  # Цвет фона окна с аксиомами

theorems_window.withdraw()  # Скрытие окна с аксиомами

title_theorem_label = Label(theorems_window, text='', font='Oswald 15', bg=first_color, fg=second_color, justify=LEFT)  # Надпись аксиомы треугольника
title_theorem_label.grid(row=0, column=0, padx=10, sticky=W, pady=15)  # Надпись аксиомы треугольника расположение

first_theorem_label = Label(theorems_window, text='',
                            font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
first_theorem_label.grid(row=1, column=0, padx=10, columnspan=9, sticky=W)  # Надпись аксиомы 1 расположение

second_theorem_label = Label(theorems_window, text='',
                             font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
second_theorem_label.grid(row=2, column=0, padx=10, columnspan=9, sticky=W, pady=15)  # Надпись аксиомы 1 расположение

third_theorem_label = Label(theorems_window, text='',
                            font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
third_theorem_label.grid(row=3, column=0, padx=10, columnspan=9, sticky=W)  # Надпись аксиомы 1 расположение

fourth_theorem_label = Label(theorems_window, text='',
                             font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
fourth_theorem_label.grid(row=4, column=0, padx=10, columnspan=9, sticky=W, pady=15)  # Надпись аксиомы 1 расположение

fifth_theorem_label = Label(theorems_window, text='',
                            font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
fifth_theorem_label.grid(row=5, column=0, padx=10, columnspan=9, sticky=W)  # Надпись аксиомы 1 расположение

sixth_theorem_label = Label(theorems_window, text='',
                            font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
sixth_theorem_label.grid(row=6, column=0, padx=10, columnspan=9, sticky=W, pady=15)  # Надпись аксиомы 1 расположение

seventh_theorem_label = Label(theorems_window, text='',
                              font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
seventh_theorem_label.grid(row=7, column=0, padx=10, columnspan=9, sticky=W)  # Надпись аксиомы 1 расположение

eight_theorem_label = Label(theorems_window,
                            text='',
                            font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
eight_theorem_label.grid(row=8, column=0, padx=10, columnspan=9, sticky=W, pady=15)  # Надпись аксиомы 1 расположение

first_theorems_page_button = Button(theorems_window, text='1', font='Oswald 12', bg=first_color, fg=fourth_color, justify=LEFT, width=3)
first_theorems_page_button.place(x=280, y=460)

second_theorems_page_button = Button(theorems_window, text='2', font='Oswald 12', bg=first_color, fg=fourth_color, justify=LEFT, width=3)
second_theorems_page_button.place(x=320, y=460)
# Окно теорем треугольника заканчивается тут(7 окно)


# Окно аксиом треугольника начинается тут(6 окно)
axioms_window = Tk()  # Создание окна с аксиомами треугольника
axioms_window.title('Аксиомы треугольника')  # Заголовок окна с аксиомами треугольника
axioms_window['bg'] = first_color  # Цвет фона окна с аксиомами

axioms_window.withdraw()  # Скрытие окна с аксиомами

title_axioms_label = Label(axioms_window, text='', font='Oswald 15', bg=first_color, fg=second_color, justify=LEFT)  # Надпись аксиомы треугольника
title_axioms_label.grid(row=0, column=0, padx=10, sticky=W, pady=15)  # Надпись аксиомы треугольника расположение

first_axioms_label = Label(axioms_window, text='',
                           font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
first_axioms_label.grid(row=1, column=0, columnspan=9, padx=10, sticky=W)  # Надпись аксиомы 1 расположение
# Окно аксиом треугольника заканчивается тут(6 окно)

# Окно фигур начинается тут(5 окно)
figure_window = Tk()  # Окно треугольника
figure_window.geometry('335x690')  # Размер окна треугольника
figure_window['bg'] = first_color

figure_window.withdraw()  # Скрытие окна треугольника

definition_figure_label = Label(figure_window, text='', font='Oswald 10', bg=first_color, fg=third_color, width=42)  # Надпись определение треугольника
definition_figure_label.grid(row=1, column=1, pady=15, sticky=N + S + W + E)  # Надпись определение треугольника расположение

calculations_figure_button = Button(figure_window, text='', bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
calculations_figure_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

axioms_figure_button = Button(figure_window, text='', bg=first_color, fg=fourth_color, width=32,
                              font='Oswald 10')  # Кнопка аксиомы треугольника
axioms_figure_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

theorems_figure_button = Button(figure_window, text='', font='Oswald 10', bg=first_color, fg=fourth_color, width=32)
theorems_figure_button.grid(row=4, column=1)

formulas_figure_button = Button(figure_window, text='', font='Oswald 10', bg=first_color, fg=fourth_color, width=32)
formulas_figure_button.grid(row=5, column=1, pady=15)

back_figure_button = Button(figure_window, text='Назад', bg=first_color, fg=fourth_color, width=32, font='Oswald 10', command=visible_choose_figure_window_func)  # Кнопка назад
back_figure_button.grid(row=6, column=1)  # Кнопка назад расположение
# Окно фигур заканчивается тут(5 окно)

# Окно выбора фигур начинается тут(4 окно)
choose_figure_window = Tk()  # Окно выбора фигуры
choose_figure_window.title('Фигуры')  # Заголовок окна выбора фигуры
choose_figure_window['bg'] = first_color

choose_figure_window.withdraw()  # Скрываем окно выбора фигуры

choose_figure_label = Label(choose_figure_window, text='Выберите фигуру', font='Oswald 15', bg=first_color, fg=second_color)  # Надпись выберите фигуру
choose_figure_label.grid(row=1, column=1, padx=15)  # Надпись выберите фигуру расположение

# Рисование треугольника
triangle_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
triangle_canvas.create_polygon((80, 20), (10, 140), (150, 140), fill=fifth_color, outline=first_color)
triangle_canvas.create_text(40, 10, text="Треугольник", font="Oswald 10", fill=third_color)
triangle_canvas.tag_bind(create_figure, '<Button-1>', visible_triangle_window_event_func)
triangle_canvas.grid(row=2, column=1)
# Рисование прямоугольника
square_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = square_canvas.create_rectangle((10, 30), (150, 120), fill=fifth_color, outline=first_color)
square_canvas.tag_bind(create_figure, '<Button-1>', visible_square_window_event_func)
square_canvas.create_text(60, 10, text="Прямоугольник", font="Oswald 10", fill=third_color)
square_canvas.grid(row=3, column=1)
# Рисование квадрата
rectangle_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = rectangle_canvas.create_rectangle((20, 30), (140, 140), fill=fifth_color, outline=first_color)
rectangle_canvas.tag_bind(create_figure, '<Button-1>', visible_rectangle_window_event_func)
rectangle_canvas.create_text(30, 10, text="Квадрат", font="Oswald 10", fill=third_color)
rectangle_canvas.grid(row=4, column=1)
# Рисование ромба
rhombus_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = rhombus_canvas.create_polygon((80, 20), (120, 80), (80, 140), (40, 80), fill=fifth_color, outline=first_color)
rhombus_canvas.tag_bind(create_figure, '<Button-1>', visible_rhombus_window_event_func)
rhombus_canvas.create_text(20, 10, text="Ромб", font="Oswald 10", fill=third_color)
rhombus_canvas.grid(row=2, column=2, padx=80)
# Рисование параллелограмма
parallelogram_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = parallelogram_canvas.create_polygon((50, 50), (150, 50), (110, 120), (10, 120), fill=fifth_color, outline=first_color)
parallelogram_canvas.tag_bind(create_figure, '<Button-1>', visible_parallelogram_window_event_func)
parallelogram_canvas.create_text(55, 10, text="Параллелограмм", font="Oswald 10", fill=third_color)
parallelogram_canvas.grid(row=3, column=2)
# Рисование трапеции
trapezium_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = trapezium_canvas.create_polygon((40, 40), (120, 40), (150, 110), (10, 110), fill=fifth_color, outline=first_color)
trapezium_canvas.tag_bind(create_figure, '<Button-1>', visible_trapezium_window_event_func)
trapezium_canvas.create_text(33, 10, text="Трапеция", font="Oswald 10", fill=third_color)
trapezium_canvas.grid(row=4, column=2)
# Рисование круга
circle_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = circle_canvas.create_oval(15, 10, 150, 140, fill=fifth_color, outline=first_color)
circle_canvas.tag_bind(create_figure, '<Button-1>', visible_circle_window_event_func)
circle_canvas.create_text(18, 10, text="Круг", font="Oswald 10", fill=third_color)
circle_canvas.grid(row=2, column=3)
# Рисование эллипса
ellipse_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = ellipse_canvas.create_oval(10, 50, 150, 110, fill=fifth_color, outline=first_color)
ellipse_canvas.tag_bind(create_figure, '<Button-1>', visible_ellipse_window_event_func)
ellipse_canvas.create_text(24, 10, text="Эллипс", font="Oswald 10", fill=third_color)
ellipse_canvas.grid(row=3, column=3)

back_figure_button = Button(choose_figure_window, text='Назад', fg=fourth_color, bg=first_color, command=visible_geometry_window_func)  # Кнопка назад
back_figure_button.grid(row=1, column=3)  # Кнопка назад расположение
# Окно выбора фигур заканчивается тут(4 окно)
# Окно раздела геометрии начинается тут(3 окно)
choose_geometry_window = Tk()  # Окно разделов геометрии
choose_geometry_window.title('Геометрия')  # Заголовок окна разделов геометрии
choose_geometry_window['bg'] = first_color

choose_geometry_window.withdraw()  # Скрытие окна разделов геометрии

empty_label = Label(choose_geometry_window, fg=first_color, bg=first_color)
empty_label.grid(column=0, pady=45)

figures_button = Button(choose_geometry_window, text='Фигуры', font='Oswald 15', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=25)  # Кнопка перехода на выбор фигур
figures_button.grid(row=4, column=0, pady=25, padx=200)  # Кнопка фигур расположение

add_material_button = Button(choose_geometry_window, text='Дополнительный материал', font='Oswald 15', bg=first_color, fg=fourth_color, width=25, command=development_func)  # Кнопка перехода на доп. материал
add_material_button.grid(row=5, column=0)  # Кнопка доп. материал расположение

perevodchik_button = Button(choose_geometry_window, text='Переводчик', font='Oswald 15', bg=first_color, fg=fourth_color, width=25, command=visible_perevod_ed_window_func)  # Кнопка перехода на доп. материал
perevodchik_button.grid(row=6, column=0, pady=25)  # Кнопка доп. материал расположение

back_figure_button = Button(choose_geometry_window, text='Назад', command=visible_choose_subject_func, bg=first_color, fg=fourth_color, width=25,
                            font='Oswald 15')  # Кнопка назад, процедура используется такая же как и у смены главного на геометрию
back_figure_button.grid(row=7, column=0)  # Кнопка назад расположение
# Окно раздела геометрии заканчивается тут(3 окно)


# Окно выбора предмета начинается тут(2 окно)
choose_subject_window = Tk()  # Окно выбора предмета
choose_subject_window.title(version)  # Заголовок окна выбора предмета
choose_subject_window['bg'] = first_color

choose_subject_window.withdraw()  # Скрытие окна выбора предмета

choose_subject_label = Label(choose_subject_window, text='Выбор предмета: ', font='Oswald 15', bg=first_color, fg=second_color, width=15)  # Надпись выбора предмета
choose_subject_label.grid(row=1, column=1, padx=30, pady=20)  # Надпись выбора предмета расположение

stuff_geometry_button = Button(choose_subject_window, text='Геометрия', font='Oswald 15', command=visible_geometry_window_func, bg=first_color, fg=fourth_color, width=15)  # Кнопка Геометрии
stuff_geometry_button.grid(row=2, column=1, pady=20, sticky=W, padx=30)  # Кнопка Геометрии расположение

stuff_russian_language_button = Button(choose_subject_window, text='Русский язык', font='Oswald 15', state=DISABLED, fg=fourth_color, bg=first_color, width=15)  # Кнопка Русского языка
stuff_russian_language_button.grid(row=3, column=1, pady=40, sticky=W, padx=30)  # Кнопка Русского языка расположение

stuff_literature_button = Button(choose_subject_window, text='Литература', font='Oswald 15', state=DISABLED, bg=first_color, fg=fourth_color, width=15)  # Кнопка Литературы
stuff_literature_button.grid(row=4, column=1, pady=40, sticky=W, padx=30)  # Кнопка Литературы расположение

stuff_informatics_button = Button(choose_subject_window, text='Информатика', font='Oswald 15', state=DISABLED, bg=first_color, fg=fourth_color, width=15)  # Кнопка Информатики
stuff_informatics_button.grid(row=2, column=3, sticky=W, padx=30)  # Кнопка Информатики расположение

stuff_biology_button = Button(choose_subject_window, text='Биология', font='Oswald 15', state=DISABLED, bg=first_color, fg=fourth_color, width=15)  # Кнопка Биологии
stuff_biology_button.grid(row=3, column=3, sticky=W, padx=30)  # Кнопка Биологии расположение

stuff_physic_button = Button(choose_subject_window, text='Физика', font='Oswald 15', state=DISABLED, bg=first_color, fg=fourth_color, width=15)  # Кнопка физики
stuff_physic_button.grid(row=4, column=3, sticky=W, padx=30)  # Кнопка Физики расположение

stuff_english_language_button = Button(choose_subject_window, text='Английский язык', font='Oswald 15', state=DISABLED, bg=first_color, fg=fourth_color, width=15)  # Кнопка Английского языка
stuff_english_language_button.grid(row=2, column=5, padx=30, sticky=W)  # Кнопка Английского языка расположение

stuff_chemistry_button = Button(choose_subject_window, text='Химия', font='Oswald 15', state=DISABLED, bg=first_color, fg=fourth_color, width=15)  # Кнопка Химии
stuff_chemistry_button.grid(row=3, column=5, sticky=W, padx=30)  # Кнопка Химии расположение

stuff_history_button = Button(choose_subject_window, text='История', font='Oswald 15', state=DISABLED, bg=first_color, fg=fourth_color, width=15)  # Кнопка Истории
stuff_history_button.grid(row=4, column=5, sticky=W, padx=30)  # Кнопка Истории расположение

back_figure_button = Button(choose_subject_window, text='Назад', font='Oswald 15', command=visible_greet_window_func, bg=first_color, fg=fourth_color, width=15)
back_figure_button.grid(row=5, column=3, sticky=W, padx=30)
# Окно выбора предмета заканчивается тут(2 окно)

# Окно приветсвия начинается тут(1 окно)
greet_window = Tk()  # Создание главного окна
greet_window.geometry('700x500')  # Размер главного окна
greet_window.title(version)  # Заголовок главного окна
greet_window['bg'] = first_color
# greet_window.iconbitmap('D:\\pythoncube\\untitled\\ProjectForPythonCube\\12.ico')

greet_label = Label(greet_window, text='Добро пожаловать', font='Oswald 20', bg=first_color, fg=second_color)  # Надпись добро пожаловать
greet_label.grid(row=1, column=3, padx=230, pady=10)  # Надпись Добро пожаловать расположение

greet_label2 = Label(greet_window, text='в наше приложение', font='Oswald 20', bg=first_color,
                     fg=third_color)  # Надпись в наше приложение
greet_label2.grid(row=2, column=3)  # Надпись в наше приложение расположение

name_project_label = Label(greet_window, text='Study Assistant', font='Oswald 20', bg=first_color,
                           fg=third_color)  # Надпись pump your brain
name_project_label.grid(row=3, column=3, pady=10)  # Надпись pump your brain расположение

continue_button = Button(greet_window, text='Перейти к выбору предмета', font='Oswald 15', command=visible_choose_subject_func, bg=first_color, fg=fourth_color, width=25)  # Кнопка продолжения
continue_button.grid(row=4, column=3, pady=15)  # Кнопка продолжения расположение

create_theme_button = Button(greet_window, text='Создать тему', font='Oswald 15', command=write_change_theme_func, bg=first_color, fg=fourth_color, width=25)
create_theme_button.grid(row=8, column=3)

delete_theme_button = Button(greet_window, text='Удалить тему', font='Oswald 15', command=delete_custom_theme_func, bg=first_color, fg=fourth_color, width=25)
delete_theme_button.grid(row=9, column=3, pady=15)

exit_button = Button(greet_window, text='Выход', font='Oswald 15', command=exit_project_func, bg=first_color, fg=fourth_color, width=25)
exit_button.grid(row=10, column=3)

# Окно приветсвия заканчивается тут(1 окно)

# Просчёт больших окон
greet_window.update_idletasks()  #
width_window_large = greet_window.winfo_width()
height_window_large = greet_window.winfo_height()
x_window_large = (greet_window.winfo_screenwidth() // 2) - (width_window_large // 2)
y_window_large = (greet_window.winfo_screenheight() // 2) - (height_window_large // 2)

# Центрирвоание всех окон больших окон
choose_subject_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
choose_geometry_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
choose_figure_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
greet_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
calculate_triangle_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
axioms_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
theorems_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
formuls_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
calculate_square_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
calculate_rectangle_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
perevod_ed_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
calculate_trapezium_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
# Треугольник поверх всех окно
figure_window.lift()
figure_window.attributes('-topmost', True)
figure_window.after_idle(figure_window.attributes, '-topmost', True)
figure_window.protocol('WM_DELETE_WINDOW', exit_error_func)
figure_window.resizable(False, False)

# Аксиомы поверх всех окно
axioms_window.lift()
axioms_window.attributes('-topmost', True)
axioms_window.after_idle(axioms_window.attributes, '-topmost', True)
axioms_window.protocol('WM_DELETE_WINDOW', exit_error_func)
axioms_window.resizable(False, False)

formuls_window.lift()
formuls_window.attributes('-topmost', True)
formuls_window.after_idle(formuls_window.attributes, '-topmost', True)
formuls_window.protocol('WM_DELETE_WINDOW', exit_error_func)
formuls_window.resizable(False, False)
# Главный экран не изменяет размер
greet_window.resizable(False, False)
# Окно с калькулятором сторон не изменяет размер
calculate_triangle_window.resizable(False, False)
calculate_triangle_window.protocol('WM_DELETE_WINDOW', exit_error_func)
calculate_triangle_window.lift()
calculate_triangle_window.attributes('-topmost', True)
calculate_triangle_window.after_idle(calculate_triangle_window.attributes, '-topmost', True)
# Экран выбора предмета не изменяет размер и не закрывается
choose_subject_window.resizable(False, False)

# Изменения связанные с окном выбора разделов геометрии
choose_geometry_window.protocol('WM_DELETE_WINDOW', exit_error_func)
choose_geometry_window.resizable(False, False)

# Изменения связанные с окном выбора фигур в геометрии
choose_figure_window.protocol('WM_DELETE_WINDOW', exit_error_func)
choose_figure_window.resizable(False, False)

# Изменения связанные с приветственным окном
greet_window.protocol('WM_DELETE_WINDOW', exit_project_func)

# Изменения связанные с окном выбора предмета
choose_subject_window.protocol('WM_DELETE_WINDOW', exit_project_func)

# Изменения связанные с окном теорем
theorems_window.protocol('WM_DELETE_WINDOW', exit_error_func)
theorems_window.resizable(False, False)
theorems_window.lift()
theorems_window.attributes('-topmost', True)
theorems_window.after_idle(theorems_window.attributes, '-topmost', True)

# Расчёт вертикальных окон
figure_window.update_idletasks()  #
width_window_small = figure_window.winfo_width()
height_window_small = figure_window.winfo_height()
x_window_small = (figure_window.winfo_screenwidth() // 2) - (width_window_small // 2)
y_window_small = (figure_window.winfo_screenheight() // 2) - (height_window_small // 2)
# Сделать левее вертикальные окна
figure_window.geometry('{}x{}+{}+{}'.format(width_window_small, height_window_small, 200, y_window_small))

calculate_square_window.lift()
calculate_square_window.attributes('-topmost', True)
calculate_square_window.after_idle(calculate_square_window.attributes, '-topmost', True)
calculate_square_window.protocol('WM_DELETE_WINDOW', exit_error_func)
calculate_square_window.resizable(False, False)

calculate_rectangle_window.lift()
calculate_rectangle_window.attributes('-topmost', True)
calculate_rectangle_window.after_idle(calculate_rectangle_window.attributes, '-topmost', True)
calculate_rectangle_window.protocol('WM_DELETE_WINDOW', exit_error_func)
calculate_rectangle_window.resizable(False, False)

perevod_ed_window.lift()
perevod_ed_window.attributes('-topmost', True)
perevod_ed_window.after_idle(perevod_ed_window.attributes, '-topmost', True)
perevod_ed_window.protocol('WM_DELETE_WINDOW', exit_error_func)
perevod_ed_window.resizable(False, False)

calculate_trapezium_window.lift()
calculate_trapezium_window.attributes('-topmost', True)
calculate_trapezium_window.after_idle(calculate_trapezium_window.attributes, '-topmost', True)
calculate_trapezium_window.protocol('WM_DELETE_WINDOW', exit_error_func)
calculate_trapezium_window.resizable(False, False)
# Запуск главного окна
greet_window.mainloop()

# © 2020 TheFox
# TODO Расширить Entry() в окне с переводом единиц
