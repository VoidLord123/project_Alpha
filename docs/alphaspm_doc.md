# .alphaspm
#### Расшифровывается как alpha sprite map

## Описание формата
Первая строка "groups:" открывающий тег для создания групп.

Далее идет первый уровень отступов и информационные теги вида "group-name: group_type"

Далее на 0ом уровне отступов идет открывающий тег sprites

Затем на первом уровне отступа идут теги вида "sprite-name:" вместо sprite-name может писаться не только имя спрайта, но и ключевое слово no-name которое означает что спрайт не имеет выделенного имени и не сохраняется в поле named_sprites.

Затем идут на втором уровне отступа теги "x: float", "y: float", "vx: float", "vy: float", а также "state: int" указывающий на начальное состояние спрайта. Координаты по x и y а так же скорости относительно x и y. Идут названия групп. Должна быть одно группа. Группа all_sprites в указании не нуждается. 

Не рекомендуется к использованию с input_sprite т.к. он обладает особыми свойствами 