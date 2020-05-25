import math
import os
import tkinter.colorchooser
from tkinter import *
from tkinter import messagebox as mb

# import key_base


version = 'v0.1.5'

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
except FileNotFoundError:
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


def visible_geometry_window_func():  # Показ окна с геометрией
    # Всё, что показываем:
    choose_geometry_window.deiconify()
    # Всё, что скрываем:
    choose_subject_window.withdraw()


def visible_choose_figure_window_func():  # Показ окна с выбором фигур
    # Всё, что показываем:
    choose_figure_window.deiconify()
    # Всё, что скрываем:
    choose_geometry_window.withdraw()
    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    figure_window.withdraw()
    calculate_triangle_window.withdraw()


def visible_triangle_window_func():  # Показ окна с треугольником
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:

    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    calculate_triangle_window.withdraw()


def visible_greet_window_func():  # Показ главного окна
    # Всё, что показываем:
    greet_window.deiconify()
    # Всё, что скрываем:
    choose_subject_window.withdraw()
    choose_geometry_window.withdraw()

    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    figure_window.withdraw()


def visible_theorems_triangle_window_func():  # Показ окна с теоремами треугольника
    # Всё, что показываем:
    theorems_triangle_window.deiconify()

    title_theorem_triangle_label = Label(theorems_triangle_window, text='Теоремы треугольника: ', font='Oswald 15', bg=first_color, fg=second_color, justify=LEFT)  # Надпись аксиомы треугольника
    title_theorem_triangle_label.grid(row=0, column=0, padx=10, sticky=W, pady=15)  # Надпись аксиомы треугольника расположение

    first_theorem_triangle_label = Label(theorems_triangle_window, text='1.Сумма углов треугольника равна 180 градусам.',
                                         font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    first_theorem_triangle_label.grid(row=1, column=0, padx=10, columnspan=9, sticky=W)  # Надпись аксиомы 1 расположение1.

    second_theorem_triangle_label = Label(theorems_triangle_window, text='2.В треугольнике: \n  1) против большей стороны лежит больший угол; \n  2) обратно, против большего угла лежит большая сторона.',
                                          font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    second_theorem_triangle_label.grid(row=2, column=0, padx=10, columnspan=9, sticky=W, pady=15)  # Надпись аксиомы 1 расположение

    third_theorem_triangle_label = Label(theorems_triangle_window, text='3.В прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов катетов.',
                                         font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    third_theorem_triangle_label.grid(row=3, column=0, padx=10, columnspan=9, sticky=W)  # Надпись аксиомы 1 расположение

    fourth_theorem_triangle_label = Label(theorems_triangle_window, text='4.Если квадрат одной стороны треугольника равен сумме квадратов двух \n   других сторон, то треугольник прямоугольный.',
                                          font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    fourth_theorem_triangle_label.grid(row=4, column=0, padx=10, columnspan=9, sticky=W, pady=15)  # Надпись аксиомы 1 расположение

    fifth_theorem_triangle_label = Label(theorems_triangle_window, text='5.Высоты треугольника (или их продолжения) пересекаются в одной точке.',
                                         font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    fifth_theorem_triangle_label.grid(row=5, column=0, padx=10, columnspan=9, sticky=W)  # Надпись аксиомы 1 расположение

    sixth_theorem_triangle_label = Label(theorems_triangle_window, text='6.Площадь треугольника равна половине произведения двух его сторон на синус угла \n    между ними.',
                                         font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    sixth_theorem_triangle_label.grid(row=6, column=0, padx=10, columnspan=9, sticky=W, pady=15)  # Надпись аксиомы 1 расположение

    seventh_theorem_triangle_label = Label(theorems_triangle_window, text='7.Стороны треугольника пропорциональны синусам противолежащих углов.',
                                           font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    seventh_theorem_triangle_label.grid(row=7, column=0, padx=10, columnspan=9, sticky=W)  # Надпись аксиомы 1 расположение

    eight_theorem_triangle_label = Label(theorems_triangle_window,
                                         text='8.Квадрат стороны треугольника равен сумме квадратов двух других сторон минус \n   удвоенное произведение этих сторон, умноженное на косинус угла между ними.',
                                         font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    eight_theorem_triangle_label.grid(row=8, column=0, padx=10, columnspan=9, sticky=W, pady=15)  # Надпись аксиомы 1 расположение

    back_button = Button(theorems_triangle_window, text='Назад', command=visible_triangle_window_func, bg=first_color, fg=fourth_color)  # Кнопка назад
    back_button.place(x=10, y=460)  # Кнопка назад
    # Всё, что скрываем:
    choose_figure_window.withdraw()


def visible_axioms_window_func():  # Показ окна с аксиомами треугольника
    # Всё, что показываем:
    aksioma_triangle_window.deiconify()
    # Всё, что скрываем:
    choose_figure_window.withdraw()
    # Всё что создаём
    title_aksioma_triangle_label = Label(aksioma_triangle_window, text='Аксиомы треугольника: ', font='Oswald 15', bg=first_color, fg=second_color, justify=LEFT)  # Надпись аксиомы треугольника
    title_aksioma_triangle_label.grid(row=0, column=0, padx=10, sticky=W, pady=15)  # Надпись аксиомы треугольника расположение

    first_aksioma_triangle_label = Label(aksioma_triangle_window, text='1.Каков бы ни был треугольник, существует равный ему треугольник в заданном \n  расположении относительно данной полупрямой.',
                                         font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    first_aksioma_triangle_label.grid(row=1, column=0, columnspan=9, padx=10, sticky=W)  # Надпись аксиомы 1 расположение

    back_button = Button(aksioma_triangle_window, text='Назад', command=visible_triangle_window_func, bg=first_color, fg=fourth_color)  # Кнопка назад
    back_button.place(x=10, y=460)  # Кнопка назад


def visible_triangle_formul_func():
    # Всё, что показываем
    formul_window.deiconify()
    # Всё, что скрываем
    choose_figure_window.withdraw()
    # Всё что создаём
    title_formul_triangle_label = Label(formul_window, text='Формулы треугольника: ', font='Oswald 15', bg=first_color, fg=second_color, justify=LEFT)  # Надпись аксиомы треугольника
    title_formul_triangle_label.grid(row=0, column=0, padx=10, sticky=W, pady=15)  # Надпись аксиомы треугольника расположение

    first_formul_triangle_label = Label(formul_window, text='Формулы для нахождения площади: \n а)S=½bh, \n б)S=½ab⋅sin(α) \n в)S=√(p·(p-a)·(p-b)·(p-c))',
                                        font='Oswald 12', bg=first_color, fg=third_color, justify=LEFT)  # Надпись аксиомы 1
    first_formul_triangle_label.grid(row=1, column=0, columnspan=9, padx=10, sticky=W)  # Надпись аксиомы 1 расположение

    back_button = Button(aksioma_triangle_window, text='Назад', command=visible_triangle_window_func, bg=first_color, fg=fourth_color)  # Кнопка назад
    back_button.place(x=10, y=460)  # Кнопка назад


def visible_triangle_window_event_func(event):  # Открытие окна с треугольником через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    theorems_triangle_window.withdraw()
    aksioma_triangle_window.withdraw()
    # Всё что создаём
    figure_window.title('Треугольник')

    definition_label = Label(figure_window, text='Треугольник - это геометрическая фигура, \n образованная тремя пересекающимися прямыми, \n образующими ''три внутренних угла', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы треугольника', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы треугольника', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы треугольника', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_square_window_event_func(event):  # Открытие окна с прямоугольником через event
    # Всё, что показываем
    figure_window.deiconify()
    # Всё, что скрываем:
    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    # Всё что создаём
    figure_window.title('Четырёхугольник')
    definition_label = Label(figure_window, text='Четырёхугольник', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы четырёхугольника', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы четырёхугольника', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы четырёхугольника', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_rectangle_window_event_func(event):  # Открытие окна с квадратом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    # Всё, что создаём
    figure_window.title('Квадрат')

    definition_label = Label(figure_window, text='Квадрат', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы квадрата', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы квадрата', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы квадрата', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_rhombus_window_event_func(event):  # Открытие окна с ромбом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    theorems_triangle_window.withdraw()
    aksioma_triangle_window.withdraw()
    # Всё что создаём
    figure_window.title('Ромб')

    definition_label = Label(figure_window, text='Ромб', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы ромба', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы ромба', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы ромба', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_parallelogram_window_event_func(event):  # Открытие окна с параллелограммом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    # Всё, что создаём
    figure_window.title('Параллелограмм')

    definition_label = Label(figure_window, text='Параллелограмм', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы параллелограмма', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы параллелограмма', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы параллелограмма', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_trapezium_window_event_func(event):  # Открытие окна с трапецией через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    # Всё, что создаём
    figure_window.title('Трапеция')

    definition_label = Label(figure_window, text='Трапеция', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы трапеции', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы трапеции', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы трапеции', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_circle_window_event_func(event):  # Открытие окна с кругом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    # Всё, что создаём
    figure_window.title('Круг')

    definition_label = Label(figure_window, text='Круг', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы круга', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы круга', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы круга', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_oval_window_event_func(event):  # Открытие окна с овалом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    # Всё, что создаём
    figure_window.title('Овал')

    definition_label = Label(figure_window, text='Овал', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы овала', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы овала', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы овала', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_ellipse_window_event_func(event):  # Открытие окна с эллипсом через event
    # Всё, что показываем:
    figure_window.deiconify()
    # Всё, что скрываем:
    theorems_triangle_window.withdraw()
    aksioma_triangle_window.withdraw()
    # Всё, что создаём
    figure_window.title('Эллипс')

    definition_label = Label(figure_window, text='Эллипс', font='Oswald 10',
                             bg=first_color,
                             fg=third_color, width=42)  # Надпись определение треугольника
    definition_label.grid(row=1, column=1, sticky=S, pady=15)  # Надпись определение треугольника расположение

    calculations_for_triangle_button = Button(figure_window, text='Приложение для расчёта сторон и углов', command=visible_calculate_triangle_window_func, bg=first_color, fg=fourth_color, width=32,
                                              font='Oswald 10')  # Кнопка перехода на окно с расчётами треугольника
    calculations_for_triangle_button.grid(row=2, column=1)  # Кнопка перехода на окно с расчётами треугольника расположение

    axioms_triangle_button = Button(figure_window, text='Аксиомы эллипса', command=visible_axioms_window_func, bg=first_color, fg=fourth_color, width=32,
                                    font='Oswald 10')  # Кнопка аксиомы треугольника
    axioms_triangle_button.grid(row=3, column=1, pady=15)  # Кнопка аксиомы треугольника расположение

    theorems_triangle_button = Button(figure_window, text='Теоремы эллипса', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_theorems_triangle_window_func)
    theorems_triangle_button.grid(row=4, column=1)

    formulas_triangle_button = Button(figure_window, text='Формулы эллипса', font='Oswald 10', bg=first_color, fg=fourth_color, width=32, command=visible_triangle_formul_func)
    formulas_triangle_button.grid(row=5, column=1, pady=15)

    back_button = Button(figure_window, text='Назад', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=32, font='Oswald 10')  # Кнопка назад
    back_button.grid(row=6, column=1)  # Кнопка назад расположение


def visible_calculate_triangle_window_func():  # Открытие окна c вычислением треугольника
    # Всё, что показываем:
    calculate_triangle_window.deiconify()
    figure_window.deiconify()
    # Всё, что скрываем:
    aksioma_triangle_window.withdraw()
    theorems_triangle_window.withdraw()
    choose_figure_window.withdraw()


def exit_error_func():  # Показываение ошибки при попытки закрытия важных окон
    mb.showerror('Ошибка', 'Это окно закрывается кнопкой "Назад"')


def exit_project_func():  # Полностью закрытие проекта
    sys.exit()


def write_change_theme_func():  # Создание файла с темой
    first_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для фона')

    second_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для заголовков')

    third_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для обычного текста')

    fourth_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для кнопок')

    fifth_color_choose = tkinter.colorchooser.askcolor(title='Выбор цвета для заливки фигур')

    file = open('File_Setting.txt', 'w')
    file.write(str(first_color_choose[1]) + ' ' + str(second_color_choose[1]) + ' ' + str(third_color_choose[1]) + ' ' + str(fourth_color_choose[1]) + ' ' + str(fifth_color_choose[1]))
    file.close()
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
    if a_entry.get() != '' and b_entry.get() != '' and c_entry.get() != '':
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        a_corner_entry['state'] = DISABLED
        b_corner_entry['state'] = DISABLED
        y_corner_entry['state'] = DISABLED
        if (a + b > c) and (a + c > b) and (b + c > a):

            a = float(a_entry.get())
            print(a)
            b = float(b_entry.get())
            print(b)
            c = float(c_entry.get())
            print(c)

            print(a, b, c)
            alpha = round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))
            print(f'Альфа = {alpha} гр')
            betta = round(math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))))
            print(f'Бетта = {betta} гр')
            gamma = round(180 - (alpha + betta))
            print(f'Гамма = {gamma} гр')
            p = round(a + b + c, 2)  # Периметр
            print(f'P = {p}')
            p_polu = (a + b + c) / 2  # Полупериметр
            s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)  # Площадь
            print(f'S = {s}')

        else:
            mb.showerror(title='Ошибка', message='Такого треугольника не существует')
    elif a_entry.get() != '' and c_entry.get() != '' and a_corner_entry.get() != '':
        b_entry['state'] = DISABLED
        b_corner_entry['state'] = DISABLED
        y_corner_entry['state'] = DISABLED
        a = float(a_entry.get())  # a
        c = float(c_entry.get())  # b
        alpha = float(a_corner_entry.get())  # y

        print(f'A = {a}')
        print(f'C = {c}')
        print(f'Alpha = {alpha}')

        b = round(math.sqrt((a ** 2 + c ** 2) - (2 * a * c * (math.cos(math.radians(alpha))))), 2)  # c
        print(f'Сторона B = {b}')

        betta = round(math.degrees(math.acos((c ** 2 + b ** 2 - a ** 2) / (2 * c * b))))  # a
        print(f'Betta = {betta}')

        gamma = round(180 - betta - alpha)
        print(f'Gamma = {gamma}')

        p = round(a + c + b, 2)
        print(f'P = {p}')

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)
        print(f'S = {s}')

    elif a_entry.get() != '' and b_entry.get() != '' and y_corner_entry.get() != '':
        c_entry['state'] = DISABLED
        a_corner_entry['state'] = DISABLED
        b_corner_entry['state'] = DISABLED
        a = float(a_entry.get())  # a
        b = float(b_entry.get())  # b
        gamma = float(y_corner_entry.get())  # y

        print(f'A = {a}')
        print(f'B = {b}')
        print(f'Gamma = {gamma}')

        c = round(math.sqrt((a ** 2 + b ** 2) - (2 * a * b * (math.cos(math.radians(gamma))))), 2)  # c
        print(f'Сторона C = {c}')

        betta = round(math.degrees(math.acos((c ** 2 + b ** 2 - a ** 2) / (2 * c * b))))  # a
        print(f'Betta = {betta}')

        betta = round(180 - gamma - betta)
        print(f'Alpha = {betta}')

        p = round(a + c + b, 2)
        print(f'P = {p}')

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)
        print(f'S = {s}')
    elif b_entry.get() != '' and c_entry.get() != '' and b_corner_entry.get() != '':
        a_entry['state'] = DISABLED
        a_corner_entry['state'] = DISABLED
        y_corner_entry['state'] = DISABLED

        b = float(b_entry.get())  # a
        c = float(c_entry.get())  # b
        betta = float(b_corner_entry.get())  # y

        print(f'B = {b}')
        print(f'C = {c}')
        print(f'Betta = {betta}')

        a = round(math.sqrt((b ** 2 + c ** 2) - (2 * b * c * (math.cos(math.radians(betta))))), 2)  # c
        print(f'Сторона A = {a}')

        alpha = round(math.degrees(math.acos((c ** 2 + a ** 2 - b ** 2) / (2 * c * a))))
        print(f'Alpha = {alpha}')

        gamma = round(180 - alpha - betta)
        print(f'Gamma = {gamma}')

        p = round(a + c + b, 2)
        print(f'P = {p}')

        p_polu = (a + b + c) / 2  # Полупериметр
        s = round(math.sqrt(p_polu * (p_polu - a) * (p_polu - b) * (p_polu - c)), 2)
        print(f'S = {s}')

    else:
        print('bullshit')


def calculate_triangle_2_func():
    if a_entry.get() != '' and c_entry.get() != '' and b_corner_entry.get() != '':
        b_entry['state'] = DISABLED
        a_corner_entry['state'] = DISABLED
        y_corner_entry['state'] = DISABLED

        a = float(a_entry.get())  # b
        c = float(c_entry.get())  # c
        b = float(b_corner_entry.get())  # betta

        gamma = c / a * math.sin(b)
        print(f'Gamma = {gamma}')
    else:
        print('Chest')


def reset_func():
    a_entry.delete(0, END)
    b_entry.delete(0, END)
    c_entry.delete(0, END)
    a_corner_entry.delete(0, END)
    b_corner_entry.delete(0, END)
    y_corner_entry.delete(0, END)
    a_entry.config(state=NORMAL)
    b_entry.config(state=NORMAL)
    c_entry['state'] = NORMAL
    a_corner_entry['state'] = NORMAL
    b_corner_entry['state'] = NORMAL
    y_corner_entry['state'] = NORMAL


# Окно формул начинается тут(9 окно)
formul_window = Tk()  # Окно треугольника
formul_window.title('Формулы')  # Заголовок окна треугольника
formul_window['bg'] = first_color

formul_window.withdraw()  # Скрытие окна треугольника
# Окно формул заканчивается тут(9 окно)

# Окно калькулятора начинается тут(8 окно)
calculate_triangle_window = Tk()  # Окно треугольника
calculate_triangle_window.title('Калькулятор')  # Заголовок окна треугольника
calculate_triangle_window['bg'] = first_color

calculate_triangle_window.withdraw()  # Скрытие окна треугольника

definition_label = Label(calculate_triangle_window, text='Калькулятор', font='Oswald 15',
                         bg=first_color,
                         fg=third_color)  # Надпись определение треугольника
definition_label.grid(row=1, column=8, pady=15, padx=15)  # Надпись определение треугольника расположение

a_label = Label(calculate_triangle_window, text='A = ', font='Oswald 15', bg=first_color, fg=second_color, width=5)
a_label.grid(row=2, column=1, padx=15, pady=15)

a_entry = Entry(calculate_triangle_window, width=5, font='Oswald 10', bg=fifth_color)
a_entry.grid(row=2, column=2)

b_label = Label(calculate_triangle_window, text='B = ', font='Oswald 15', bg=first_color, fg=second_color, width=5)
b_label.grid(row=3, column=1, padx=15)

b_entry = Entry(calculate_triangle_window, width=5, font='Oswald 10', bg=fifth_color)
b_entry.grid(row=3, column=2)

c_label = Label(calculate_triangle_window, text='C = ', font='Oswald 15', bg=first_color, fg=second_color, width=5)
c_label.grid(row=4, column=1, padx=15, pady=15)

c_entry = Entry(calculate_triangle_window, width=5, font='Oswald 10', bg=fifth_color)
c_entry.grid(row=4, column=2)

a_corner_label = Label(calculate_triangle_window, text='⦟α = ', font='Oswald 15', bg=first_color, fg=second_color, width=5)
a_corner_label.grid(row=5, column=1, padx=15)

a_corner_entry = Entry(calculate_triangle_window, width=5, font='Oswald 10', bg=fifth_color)
a_corner_entry.grid(row=5, column=2)

b_corner_label = Label(calculate_triangle_window, text='⦟β = ', font='Oswald 15', bg=first_color, fg=second_color, width=5)
b_corner_label.grid(row=6, column=1, padx=15, pady=15)

b_corner_entry = Entry(calculate_triangle_window, width=5, font='Oswald 10', bg=fifth_color)
b_corner_entry.grid(row=6, column=2)

y_corner_label = Label(calculate_triangle_window, text='⦟γ = ', font='Oswald 15', bg=first_color, fg=second_color, width=5)
y_corner_label.grid(row=7, column=1, padx=15)

y_corner_entry = Entry(calculate_triangle_window, width=5, font='Oswald 10', bg=fifth_color)
y_corner_entry.grid(row=7, column=2)

triangle_canvas = Canvas(calculate_triangle_window, width=180, height=160, bg=first_color, highlightthickness=0)
create_figure = triangle_canvas.create_polygon((40, 30), (10, 140), (150, 140), fill=fifth_color)
triangle_canvas.create_text(155, 140, text="β", font="Oswald 15", fill=third_color)
triangle_canvas.create_text(5, 140, text="α", font="Oswald 15", fill=third_color)
triangle_canvas.create_text(40, 15, text="γ", font="Oswald 15", fill=third_color)
triangle_canvas.create_text(10, 80, text="A", font="Oswald 15", fill=third_color)
triangle_canvas.create_text(80, 152, text="C", font="Oswald 15", fill=third_color)
triangle_canvas.create_text(110, 80, text="B", font="Oswald 15", fill=third_color)
triangle_canvas.place(x=350, y=80)

calculate_triangle_button = Button(calculate_triangle_window, text='Расчитать треугольник 3 стороны', bg=first_color, fg=fourth_color, font='Oswald 10', command=calculate_triangle_func)
calculate_triangle_button.grid(row=9, column=8, padx=15)
calculate_triangle_button = Button(calculate_triangle_window, text='Расчитать треугольник 2 стороны и угол', bg=first_color, fg=fourth_color, font='Oswald 10', command=calculate_triangle_2_func)
calculate_triangle_button.grid(row=9, column=9, padx=15)

back_button = Button(calculate_triangle_window, text='Сбросить', command=reset_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_button.grid(row=9, column=3, pady=15, padx=15)  # Кнопка назад расположение

back_button = Button(calculate_triangle_window, text='Назад', command=visible_triangle_window_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
back_button.grid(row=9, column=2, pady=15, padx=15)  # Кнопка назад расположение

exit_button = Button(calculate_triangle_window, text='Выход', command=exit_project_func, bg=first_color, fg=fourth_color, font='Oswald 10')  # Кнопка назад
exit_button.grid(row=9, column=1, pady=15, padx=15)  # Кнопка назад расположение
# Окно эллипс заканчивается тут(8 окно)


# Окно теорем треугольника начинается тут(7 окно)
theorems_triangle_window = Tk()  # Создание окна с аксиомами треугольника
theorems_triangle_window.title('Теоремы треугольника')  # Заголовок окна с аксиомами треугольника
theorems_triangle_window['bg'] = first_color  # Цвет фона окна с аксиомами

theorems_triangle_window.withdraw()  # Скрытие окна с аксиомами

# Окно теорем треугольника заканчивается тут(7 окно)

# Окно аксиом треугольника начинается тут(6 окно)
aksioma_triangle_window = Tk()  # Создание окна с аксиомами треугольника
aksioma_triangle_window.title('Аксиомы треугольника')  # Заголовок окна с аксиомами треугольника
aksioma_triangle_window['bg'] = first_color  # Цвет фона окна с аксиомами

aksioma_triangle_window.withdraw()  # Скрытие окна с аксиомами

# Окно аксиом треугольника заканчивается тут(6 окно)

# Окно треугольника начинается тут(5 окно)
figure_window = Tk()  # Окно треугольника
figure_window.geometry('335x690')  # Размер окна треугольника
figure_window['bg'] = first_color

figure_window.withdraw()  # Скрытие окна треугольника

# Окно треугольника заканчивается тут(5 окно)

# Окно выбора фигур начинается тут(4 окно)
choose_figure_window = Tk()  # Окно выбора фигуры
choose_figure_window.title('Фигуры')  # Заголовок окна выбора фигуры
choose_figure_window['bg'] = first_color

choose_figure_window.withdraw()  # Скрываем окно выбора фигуры

choose_figure_label = Label(choose_figure_window, text='Выберите фигуру', font='Oswald 15', bg=first_color, fg=second_color)  # Надпись выберите фигуру
choose_figure_label.grid(row=1, column=1, padx=15)  # Надпись выберите фигуру расположение

# Рисование треугольника
triangle_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = triangle_canvas.create_polygon((80, 20), (10, 140), (150, 140), fill=fifth_color)
triangle_canvas.create_text(40, 10, text="Треугольник", font="Oswald 10", fill=third_color)
triangle_canvas.tag_bind(create_figure, '<Button-1>', visible_triangle_window_event_func)
triangle_canvas.grid(row=2, column=1)
# Рисование четырёхугольника
square_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = square_canvas.create_rectangle((10, 30), (150, 120), fill=fifth_color)
square_canvas.tag_bind(create_figure, '<Button-1>', visible_square_window_event_func)
square_canvas.create_text(60, 10, text="Четырёхугольник", font="Oswald 10", fill=third_color)
square_canvas.grid(row=3, column=1)
# Рисование квадрата
rectangle_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = rectangle_canvas.create_rectangle((20, 30), (140, 140), fill=fifth_color)
rectangle_canvas.tag_bind(create_figure, '<Button-1>', visible_rectangle_window_event_func)
rectangle_canvas.create_text(30, 10, text="Квадрат", font="Oswald 10", fill=third_color)
rectangle_canvas.grid(row=4, column=1)
# Рисование ромба
rhombus_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = rhombus_canvas.create_polygon((80, 20), (120, 80), (80, 140), (40, 80), fill=fifth_color)
rhombus_canvas.tag_bind(create_figure, '<Button-1>', visible_rhombus_window_event_func)
rhombus_canvas.create_text(20, 10, text="Ромб", font="Oswald 10", fill=third_color)
rhombus_canvas.grid(row=2, column=2, padx=80)
# Рисование параллелограмма
parallelogram_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = parallelogram_canvas.create_polygon((50, 50), (150, 50), (110, 120), (10, 120), fill=fifth_color)
parallelogram_canvas.tag_bind(create_figure, '<Button-1>', visible_parallelogram_window_event_func)
parallelogram_canvas.create_text(55, 10, text="Параллелограмм", font="Oswald 10", fill=third_color)
parallelogram_canvas.grid(row=3, column=2)
# Рисование трапеции
trapezium_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = trapezium_canvas.create_polygon((40, 40), (120, 40), (150, 110), (10, 110), fill=fifth_color)
trapezium_canvas.tag_bind(create_figure, '<Button-1>', visible_trapezium_window_event_func)
trapezium_canvas.create_text(33, 10, text="Трапеция", font="Oswald 10", fill=third_color)
trapezium_canvas.grid(row=4, column=2)
# Рисование круга
circle_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = circle_canvas.create_oval(15, 10, 150, 140, fill=fifth_color)
circle_canvas.tag_bind(create_figure, '<Button-1>', visible_circle_window_event_func)
circle_canvas.create_text(18, 10, text="Круг", font="Oswald 10", fill=third_color)
circle_canvas.grid(row=2, column=3)
# Рисование овала
oval_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = oval_canvas.create_oval(15, 30, 150, 140, fill=fifth_color)
oval_canvas.tag_bind(create_figure, '<Button-1>', visible_oval_window_event_func)
oval_canvas.create_text(18, 10, text="Овал", font="Oswald 10", fill=third_color)
oval_canvas.grid(row=3, column=3)
# Рисование эллипса
ellipse_canvas = Canvas(choose_figure_window, width=160, height=150, bg=first_color, highlightthickness=0)
create_figure = ellipse_canvas.create_oval(10, 50, 150, 110, fill=fifth_color)
ellipse_canvas.tag_bind(create_figure, '<Button-1>', visible_ellipse_window_event_func)
ellipse_canvas.create_text(24, 10, text="Эллипс", font="Oswald 10", fill=third_color)
ellipse_canvas.grid(row=4, column=3)

back_button = Button(choose_figure_window, text='Назад', fg=fourth_color, bg=first_color, command=visible_geometry_window_func)  # Кнопка назад
back_button.grid(row=1, column=3)  # Кнопка назад расположение
# Окно выбора фигур заканчивается тут(4 окно)
# Окно раздела геометрии начинается тут(3 окно)
choose_geometry_window = Tk()  # Окно разделов геометрии
choose_geometry_window.title('Геометрия')  # Заголовок окна разделов геометрии
choose_geometry_window['bg'] = first_color

choose_geometry_window.withdraw()  # Скрытие окна разделов геометрии

empty_label = Label(choose_geometry_window, bg=first_color)
empty_label.grid(row=3, column=5, pady=53)

figures_button = Button(choose_geometry_window, text='Фигуры', font='Oswald 15', command=visible_choose_figure_window_func, bg=first_color, fg=fourth_color, width=25)  # Кнопка перехода на выбор фигур
figures_button.grid(row=4, column=5, padx=200, pady=25)  # Кнопка фигур расположение

add_material_button = Button(choose_geometry_window, text='Дополнительный материал', font='Oswald 15', bg=first_color, fg=fourth_color, width=25)  # Кнопка перехода на доп. материал
add_material_button.grid(row=5, column=5)  # Кнопка доп. материал расположение

back_button = Button(choose_geometry_window, text='Назад', command=visible_choose_subject_func, bg=first_color, fg=fourth_color, width=25,
                     font='Oswald 15')  # Кнопка назад, процедура используется такая же как и у смены главного на геометрию
back_button.grid(row=6, column=5, pady=25)  # Кнопка назад расположение
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

back_button = Button(choose_subject_window, text='Назад', font='Oswald 12', command=visible_greet_window_func, bg=first_color, fg=fourth_color, width=12)
back_button.grid(row=5, column=3, sticky=W, padx=60)
# Окно выбора предмета заканчивается тут(2 окно)

# Окно приветсвия начинается тут(1 окно)
greet_window = Tk()  # Создание главного окна
greet_window.geometry('700x500')  # Размер главного окна
greet_window.title(version)  # Заголовок главного окна
greet_window['bg'] = first_color
# greet_window.iconbitmap('D:\\pythoncube\\untitled\\ProjectForPythonCube\\12.ico')

greet_label = Label(greet_window, text='Добро пожаловать', font='Oswald 20', bg=first_color, fg=second_color)  # Надпись добро пожаловать
greet_label.grid(row=1, column=3, padx=230, pady=10)  # Надпись Добро пожаловать расположение

greet_label2 = Label(greet_window, text='в наше приложение', font='Oswald 20', bg=first_color, fg=third_color)  # Надпись в наше приложение
greet_label2.grid(row=2, column=3)  # Надпись в наше приложение расположение

name_project_label = Label(greet_window, text='pump your brain', font='Oswald 20', bg=first_color, fg=third_color)  # Надпись pump your brain
name_project_label.grid(row=3, column=3, pady=10)  # Надпись pump your brain расположение

continue_button = Button(greet_window, text='Перейти к выбору предмета', font='Oswald 15', command=visible_choose_subject_func, bg=first_color, fg=fourth_color, width=25)  # Кнопка продолжения
continue_button.grid(row=4, column=3, pady=25)  # Кнопка продолжения расположение

change_theme_button = Button(greet_window, text='Создать тему', font='Oswald 15', command=write_change_theme_func, bg=first_color, fg=fourth_color, width=25)
change_theme_button.grid(row=5, column=3)

change_theme_button = Button(greet_window, text='Удалить тему', font='Oswald 15', command=delete_custom_theme_func, bg=first_color, fg=fourth_color, width=25)
change_theme_button.grid(row=6, column=3, pady=25)

exit_button = Button(greet_window, text='Выход', font='Oswald 15', command=exit_project_func, bg=first_color, fg=fourth_color, width=25)
exit_button.grid(row=7, column=3)

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
aksioma_triangle_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
theorems_triangle_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
formul_window.geometry('{}x{}+{}+{}'.format(width_window_large, height_window_large, x_window_large, y_window_large))
# Треугольник поверх всех окно
figure_window.lift()
figure_window.attributes('-topmost', True)
figure_window.after_idle(figure_window.attributes, '-topmost', True)
figure_window.protocol('WM_DELETE_WINDOW', exit_error_func)
figure_window.resizable(False, False)

# Аксиомы поверх всех окно
aksioma_triangle_window.lift()
aksioma_triangle_window.attributes('-topmost', True)
aksioma_triangle_window.after_idle(aksioma_triangle_window.attributes, '-topmost', True)
aksioma_triangle_window.protocol('WM_DELETE_WINDOW', exit_error_func)
aksioma_triangle_window.resizable(False, False)

formul_window.lift()
formul_window.attributes('-topmost', True)
formul_window.after_idle(formul_window.attributes, '-topmost', True)
formul_window.protocol('WM_DELETE_WINDOW', exit_error_func)
formul_window.resizable(False, False)
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
theorems_triangle_window.protocol('WM_DELETE_WINDOW', exit_error_func)
theorems_triangle_window.resizable(False, False)
theorems_triangle_window.lift()
theorems_triangle_window.attributes('-topmost', True)
theorems_triangle_window.after_idle(theorems_triangle_window.attributes, '-topmost', True)

# Расчёт вертикальных окон
figure_window.update_idletasks()  #
width_window_small = figure_window.winfo_width()
height_window_small = figure_window.winfo_height()
x_window_small = (figure_window.winfo_screenwidth() // 2) - (width_window_small // 2)
y_window_small = (figure_window.winfo_screenheight() // 2) - (height_window_small // 2)
# Сделать левее вертикальные окна
figure_window.geometry('{}x{}+{}+{}'.format(width_window_small, height_window_small, 200, y_window_small))

# Запуск главного окна
greet_window.mainloop()

# TODO Алексей заполняет: ромб, круг, квадрат, четырёхугольник;
# TODO Никита заполняет: параллелограмм, эллипс, трапецию, овал. Нужно заполнить аксиомы, теоремы, формулы. Всё по анологии с треугольником. В коммите пишет, что сделали.
