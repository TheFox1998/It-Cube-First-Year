# Study Assistant

* Данный проект делается, чтобы помогать людям любых возрастов в обучении. Поддерживается или будет поддерживаться русский язык, литература, физика, химия, геометрия, информатика, биология, история, английский язык.

### Использовать в проекте

* Python 3 или выше - https://www.python.org/

* Любой удобный Вам IDE

## Модули

* Tkinter

* Math

* MessageBox

* ColorChooser

* Os

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

### Название функций и что они делают:

1. `visible_choose_subject_func` - переход с главного окна на выбор предмета

2. `visible_geometry_window_func` - переход с окна выбора предмета на окно геометрии

3. `visible_choose_figure_window_func` - переход с окна геометрии на окно с фигурами

4. `visible_greet_window_func` - переход с любого окна на главное окно

5. `visible_perevod_ed_window_func`  - показ окна с переводчиком

6. `visible_calculate_triangle_window_func` -  показ окна с расчётами треугольника

7. `visible_calculate_square_window` - показ окна с расчётами прямоугольника

8. `visible_calculate_rectangle_window_func` -  показ окна с расчётами квадрата

9. `visible_triangle_window_event_func`  -  показ окна треугольника

10. `visible_theorems_triangle_window_first_func` - показ окна с теоремами треугольника(1 стр)

11. `visible_theorems_triangle_window_second_func` - показ окна с теоремами треугольника(2 стр)

12. `visible_axioms_triangle_window_func` - показ окна с аксиомами треугольника

13. `visible_formuls_triangle_func` - показ окна с формулами треугольника

14. `visible_square_window_event_func` - показ окна прямоугольника

15. `visible_theorems_square_window_first_func` - показ окна с теоремами прямоугольника

16. `visible_axioms_square_window_func` -  показ окна с аксиомами прямоугольника

17. `visible_formuls_square_func` -  показ окна с формулами прямоугольника

18. `visible_rectangle_window_event_func` -  показ окна с квадратом

19. `visible_theorems_rectangle_window_func` -  показ окна с теоремами квадрата

20. `visible_axioms_rectangle_window_func` -  показ окна с аксиомами квадрата

21. `visible_formuls_rectangle_func` -  показ окна с формулами квадрата

22. `visible_rhombus_window_event_func` -  показ окна с ромбом

23. `visible_theorems_rhombus_window_func` -  показ окна с теоремами ромба

24. `visible_axioms_rhombus_window_func` -  показ окна с аксиомами ромба

25. `visible_formuls_rhombus_func` -  показ окна с формулами ромба

26. `visible_parallelogram_window_event_func` -  показ окна с параллелограммом

27. `visible_theorems_parallelogram_window_first_func` -  показ окна с теоремами параллелограмма(1 стр)

28. `visible_theorems_parallelogram_window_second_func` -  показ окна с теоремами параллелограмма(2 стр)

29. `visible_axioms_parallelogram_window_func` -  показ окна с аксиомами параллелограмма

30. `visible_formuls_parallelogram_func` -  показ окна с формулами параллелограмма

31. `visible_trapezium_window_event_func` - показ окна с трапецией

32. `visible_theorems_trapezium_window_first_func` - показ окна с теоремами трапеции(1 стр)

33. `visible_theorems_trapezium_window_second_func` - показ окна с теоремами трапеции(2 стр)

34. `visible_axioms_trapezium_window_func` - показ окна с аксиомами трапеции

35. `visible_formuls_trapezium_func` - показ окна с формулами трапеции

36. `visible_circle_window_event_func` - показ окна круга

37. `visible_theorems_circle_window_func` - показ окна с теоремами круга

38. `visible_axioms_circle_window_func` - показ окна с аксиомами круга

39. `visible_formuls_circle_func` - показ окна с формулами круга

40. `visible_ellipse_window_event_func` - показ окна эллипса

41. `visible_theorems_ellipse_window_func` - показ окна с теоремами эллипса

42. `visible_axioms_ellipse_window_func` - показ окна с аксиомами эллипса

43. `visible_formuls_ellipse_func` - показ окна с формулами эллипса

44. `exit_error_func` -  показ ошибки при закрытия окна

45. `exit_project_func` - полное закрытие программы

46. `development_func` - показ уведомления с информацией о разработке

47. `write_change_theme_func` - запись файла с кастомной темой

48. `delete_custom_theme_func` - удаления файла с кастомной темой

49. `calculate_triangle_func` - просчёт треугольника

50. `reset_triangle_calculate_func` - сброс всех entry и label на окне с расчётами треугольника

51. `calculate_square_func` - просчёт прямоугольника

52. `reset_square_calculate_func` - сброс всех entry и label на окне с расчётами прямоугольника

53. `calculate_rectangle_func` - просчёт квадрата

54. `reset_rectangle_calculate_func` - сброс всех entry и label на окне с расчётами квадрата

55. `perevod_func` - функция перевода единиц и последующий вывод их на экран

56. `reset_perevod_func` - очистка всех entry на окне переводчика

57. `calculate_trapezium_func` - просчитать трапецию

58. `reset_trapezium_calculate_func` - очистить и сделать активными entry and label

59. `visible_calculate_trapezuim_calculate_window_func` - показывать окно с калькулятором трапеции

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