# Study Assistant

* Данный проект делается, чтобы помогать людям любых возрастов в обучении. Поддерживается или будет поддерживаться русский язык, литература, физика, химия, геометрия, информатика, биология, история, английский язык.

### Использовать в проекте

* Python 3 или выше - [python.off.site]

* Любой удобный Вам IDE

## Модули

* Tkinter - [tkinter.docs]

* Math - [math.docs]

* MessageBox - [mb.docs]

* ColorChooser - [cc.docs]

* Os - [os.docs]

* FileDialog - [fd.docs]

* DateTime - [dt.docs]

## Документация

**Если Вы добавляете функцию в проект, то пишите про неё в документацию в соответствующий пункт**

**Если Вы добавляете окно в проект, то пишите про него в документацию в соответствующий пункт**

### Весь проект можно разбить на блоки:

1. Подгрузка файлов

2. Все функции(они в самом верху и занимают большую часть)

3. Окна приложений(они идут сразу после функций)

4. Изменение окон(они идут сразу после окон приложения)

### Название фигур:
1. Triangle - треугольник

2. Square - прямоугольник

3. Rectangle - квадрат

4. Circle - круг

5. Ellipse - эллипс

6. Oval - овал

7. Trapezium - трапеция

8. Rhombus - ромб

9. Parallelogram - параллелограмм

### Название окон и их нумерация(в комментариях в коде есть):

1. `greet_window` - Главное окно, которое встречает пользователя(1 окно)

2. `choose_subject_window` - Окно с выбором предмета, на данном окне перечислены все предметы проекта(2 окно)

3. `choose_geometry_window` - Окно, которое выходит после выбора геометрии(3 окно)

4. `choose_figure` - Окно на котором находятся все фигуры геометрии(4 окно)

5. `figure_window` - Универсальное окно, на котором выводятся все фигуры(5 окно)

6. `axioms_window` - Универсальное окно, на котором выводятся аксиомы всех фигур(6 окно)

7. `theorems_window` - Универсальное окно, на котором выводятся теоремы всех фигур(7 окно)

8. `calculate_triangle_window` - Окно, на котором выполняются все расчёты треугольника(8 окно)

9. `formuls_window` - Универсальное окно, на котором выводятся формулы всех фигур(9 окно)

10. `calculate_square_window` - Окно, на котором выполняются все расчёты прямоугольника(10 окно)

11. `calculate_rectangle_window` - Окно, на котором выполняются все расчёты квадрата(11 окно)

12. `perevod_ed_window` -  Окно, на котором выполняются все переводы единиц(12 окно)

13. `calculate_trapezium_window` - Окно, на котором выполняются все расчёты трапеции(13 окно)

14. `calculate_rhombus_window` - Окно, на котором выполняются все расчёты ромба(14 окно)

15. `calculate_parallelogram_window` - Окно, на котором выполняются все расчёты параллелограмма(15 окно)

16. `calculate_circle_window` - Окно, на котором выполняются все расчёты круга(16 окно)

### Название функций и что они делают:

1. `visible_choose_subject_func` - Отркыть окно с выбором предмета

2. `visible_geometry_window_func` - Открыть окно с выбором раздела геометрии

3. `visible_choose_figure_window_func` - Открыть окно с выбором фигур

4. `visible_greet_window_func` - Открыть главное окно

5. `visible_perevod_ed_window_func`  - Открыть окно с переводчиком

6. `visible_calculate_triangle_window_func` - Открыть окно с расчётами треугольника

7. `visible_calculate_square_window` - Открыть окно с расчётами прямоугольника

8. `visible_calculate_rectangle_window_func` - Открыть окно с расчётами квадрата

9. `visible_triangle_window_event_func`  - Открыть окно с треугольником

10. `visible_theorems_triangle_window_first_func` - Показать первую страницу с теоремами треугольника

11. `visible_theorems_triangle_window_second_func` - Показать вторую страницу с теоремами треугольника

12. `visible_axioms_triangle_window_func` - Показать окно с аксиомами трегольника

13. `visible_formuls_triangle_func` - Показать формулы треугольника

14. `visible_square_window_event_func` - Открыть окно с прямоугольником

15. `visible_theorems_square_window_first_func` - Показать теоремы прямоугольника

16. `visible_axioms_square_window_func` - Показать аксиомы прямоугольника

17. `visible_formuls_square_func` - Показать формулы прямоугольника

18. `visible_rectangle_window_event_func` - Открыть окно с квадратом

19. `visible_theorems_rectangle_window_func` - Показать теоремы квадрата

20. `visible_axioms_rectangle_window_func` - Показать аксиомы квадрата

21. `visible_formuls_rectangle_func` - Показать формулы квадрата

22. `visible_rhombus_window_event_func` - Открыть окно с ромбом

23. `visible_theorems_rhombus_window_func` - Показать аксиомы ромба

24. `visible_axioms_rhombus_window_func` - Показать аксиомы ромба

25. `visible_formuls_rhombus_func` - Показать формулы ромба

26. `visible_parallelogram_window_event_func` - Открыть окно с параллелограммом

27. `visible_theorems_parallelogram_window_first_func` - Показать первую страницу с теоремами параллограмма

28. `visible_theorems_parallelogram_window_second_func` - Показать вторую страницу с теоремами параллелограмма

29. `visible_axioms_parallelogram_window_func` - Показать аксиомы параллелограмма

30. `visible_formuls_parallelogram_func` - Показать формулы параллелограмма

31. `visible_trapezium_window_event_func` - Открыть окно с трапецией

32. `visible_theorems_trapezium_window_first_func` - Показать первую страницу с теоремами трапеции

33. `visible_theorems_trapezium_window_second_func` - Показать вторую страницу с теоремами трапеции

34. `visible_axioms_trapezium_window_func` - Показать аксиомы трапеции

35. `visible_formuls_trapezium_func` - Показать формулы трапеции

36. `visible_circle_window_event_func` - Показать окно с кругом

37. `visible_theorems_circle_window_func` - Показать теоремы круга

38. `visible_axioms_circle_window_func` - Показать аксиомы круга

39. `visible_formuls_circle_func` - Показать формулы круга

40. `visible_ellipse_window_event_func` - Открыть окно с главным меню эллипса

41. `visible_theorems_ellipse_window_func` - Показать теоремы эллипса

42. `visible_axioms_ellipse_window_func` - Показать аксиомы эллипса

43. `visible_formuls_ellipse_func` - Показать формулы эллипса

44. `exit_error_func` -  Показать mb при нажатии на окна, которые нельзя закрывать при помощи крестика

45. `exit_project_func` - Закрыть приложение

46. `development_func` - Показать mb с уведомлением о разработке

47. `write_change_theme_func` - Создать файл с данными кастомной темы

48. `delete_custom_theme_func` - Удалить файл с данными кастомной темы

49. `calculate_triangle_func` - Просчёт треугольника

50. `reset_triangle_calculate_func` - Сброс всех entry и label на окне с расчётами треугольника

51. `calculate_square_func` - Просчёт прямоугольника

52. `reset_square_calculate_func` - Сброс всех entry и label на окне с расчётами прямоугольника

53. `calculate_rectangle_func` - Просчёт квадрата

54. `reset_rectangle_calculate_func` - Сброс всех entry и label на окне с расчётами квадрата

55. `perevod_func` - Перевести единицы

56. `reset_perevod_func` - Очистка всех entry на окне переводчика

57. `calculate_trapezium_func` - Просчитать трапецию

58. `reset_trapezium_calculate_func` - Очистить и сделать активными entry and label

59. `visible_calculate_trapezuim_calculate_window_func` - Показывать окно с калькулятором трапеции

60. `visible_calculate_rhombus_window_func` - Показывать окно с калькулятором ромба

61. `reset_rhombus_calculate_func` - Очищать и сделать активными entry and label

62. `calculate_rhombus_func` - Просчёт ромба

63. `visible_calculate_parallelogram_window_func` - Показывать окно с калькулятором параллелограмма

64. `reset_parallelogram_calculate_func` - Очищать и сделать активными entry and label

65. `calculate_parallelogram_func` - Просчёт параллелограмма

66. `save_result_perevod_ed_func` - Сохранить результат перевода

67. `visible_calculate_circle_window_func` - Показать окно с калькулятором круга

68. `reset_circle_calculate_func` - Очищать и сделать активными entry and label

69. `calculate_circle_func` - Просчёт круга

### Про кастомную тему:

**Кастомная тема принимает 5 цветов:**

1. `first_color` - цвет заднего фона

2. `second_color` - цвет заголовков

3. `third_color` - цвет обычного текста

4. `fourth_color` - цвет текста у кнопок

5. `fifth_color` - цвет фигур

## Разработчики

#### Криштопа Денис
________________________________________________________________________________________________

#### Дмитренко Никита

#### Константинов Алексей


## Куратор

#### Горьев Александр Викторович


[python.off.site]: https://www.python.org/

[tkinter.docs]: https://docs.python.org/3/library/tk.html

[math.docs]: https://docs.python.org/3/library/math.html

[mb.docs]: https://docs.python.org/3/library/tkinter.html?highlight=messagebox

[cc.docs]: https://docs.python.org/3/library/tkinter.html?highlight=colorchooser

[os.docs]: https://docs.python.org/3/whatsnew/3.8.html#os

[fd.docs]: https://docs.python.org/3.10/library/dialog.html

[dt.docs]: https://docs.python.org/3.10/library/datetime.html?highlight=datetime#module-datetime