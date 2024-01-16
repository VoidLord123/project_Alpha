# Project Alpha 
##  Описание концепта игры:
Вы попали в симуляцию и стали ее частью. Но вы вернули свою волю, но теперь вы нее ее часть и не можете перемещаться свободно. Вся симуляция пытается вас остановить и вернуть в свою систему. Ваша цель понять что что такое проект Alpha и как выбраться из симуляции.

## Технологии:

 - Pygame 
 - Поддержка полноэкранного режима
 - Поддержка мониторов с нестандартным соотношением сторон
 - Связанные спрайты
 - Создание пользовательских уровней
 
## Архитектура:
### Файловая архитектура:
 - /main_levels - хранение карт встроенных уровней
 - /user_levels - хранение карт пользовательских уровней
 - /lib - реализация основных классов
 - /lib/entities - все сущности(блоки уровня, игрок и т.д.) 
 - /save - сохранение пользователя
 - main.py - запуск игры.
 - README.md - документация
 - requirements.txt - зависимости  

### Программная архитектура:

 - main.py - Запуск проекта

### Для пользователя: Руководство по пользовательским уровням
Пользовательские уровни состоят из двух файлом. "some.alphaspm" и "some.alphamap". Это карты спрайтов и уровня. Если вы загрузили уровень из интернета или уровень своего друга вам нужно положить эти два файла в папку user_levels. Важно! Оба файла должны иметь одно и то же название. Так же кнопка и двигающийся блок не будет работать в пользовательских уровнях. Подробнее о этом можно узнать в документации к форматам. Стоит обязательно прочесть /docs/level_doc.md перед созданием собственных уровней, а также желательно прочесть остальную документацию. 

#### Примечание:
Два игрока на карте не баг. 
 
 ## Авторы:
 
 - Калинин Иван
 - Галюшин Ярослав
