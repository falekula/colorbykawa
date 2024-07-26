ColorByKawa

colorbykawa — это библиотека для окрашивания текста в терминале с использованием ANSI-цветов. Библиотека предоставляет класс ColorByKawa, который содержит константы для различных цветов, а также методы для использования цветов в формате HEX и RGB.
Установка

Для установки библиотеки используйте pip:

```bash

pip install colorbykawa
```
## Инициализация

```python

import colorbykawa
# col можно заменить на любое другое название
col = colorbykawa.ColorByKawa()
```

## Примеры использования

Вы можете использовать константы класса ColorByKawa для окрашивания текста в терминале. Вот несколько примеров:

```python

import colorbykawa

a = colorbykawa.ColorByKawa()

print(a.col('Red', "This is red text"))
print(a.col('Green', "This is green text"))
print(a.col('Blue', "This is blue text"))

# Использование HEX-кода
print(a.hcol('#ff5733', "This is custom HEX color text"))

# Использование RGB значений
print(a.rgb(255, 87, 51, "This is RGB color text"))
```
## Доступные цвета
```
Класс ColorByKawa предоставляет следующие константы:

    Red: Красный
    Green: Зеленый
    Yellow: Желтый
    Blue: Синий
    Magenta: Магентовый
    Cyan: Циан
    Reset: Сброс (возвращает цвет текста в исходное состояние)
    White: Белый
    LightGray: Светло-серый
    LightRed: Светло-красный
    LightGreen: Светло-зеленый
    LightYellow: Светло-желтый
    LightBlue: Светло-синий
    LightMagenta: Светло-магентовый
    LightCyan: Светло-циан
    LightWhite: Светло-белый
    Black: Черный
    Orange: Оранжевый
    Coral: Кораловый
    Pink: Розовый
    LightPink: Светло-розовый
    LightCoral: Светло-коралловый
    Salmon: Лососевый
    Peach: Персиковый
    Apricot: Абрикосовый
    LightApricot: Светло-абрикосовый
    Beige: Бежевый
    Cream: Кремовый
    Milk: Молочный
    Ivory: Слоновая кость
    Lemon: Лимонный
    LightLemon: Светло-лимонный
    Canary: Канареечный
    LightCanary: Светло-канареечный
    Salad: Салатный
    LightSalad: Светло-салатный
    Apple: Яблочный
    LightApple: Светло-яблочный
    Lime: Лаймовый
    LightLime: Светло-лаймовый
    Mint: Мятный
    LightMint: Светло-мятный
    Emerald: Изумрудный
    LightEmerald: Светло-изумрудный
    Turquoise: Бирюзовый
    LightTurquoise: Светло-бирюзовый
    Aquamarine: Аквамариновый
    LightAquamarine: Светло-аквамариновый
    Azure: Лазурный
    LightAzure: Светло-лазурный
    SkyBlue: Небесно-голубой
```
## Методы
```
## Метод col
col(color_name, text)

Окрашивает text в цвет, указанный в color_name, используя заранее определенные цвета.

## Метод hcol
hcol(hex_code, text)

Окрашивает text в цвет, указанный в hex_code, используя цвет в формате HEX (#RRGGBB).

## Метод rgb
rgb(r, g, b, text)

Окрашивает text в цвет, указанный в RGB значениях (r, g, b), где каждый параметр может быть в диапазоне от 0 до 255.
```
## Примечание

Цвета отображаются корректно только в терминалах, которые поддерживают ANSI-коды. Если ваш терминал не поддерживает ANSI-коды, текст может не окрашиваться должным образом.

##Лицензия

Этот проект лицензирован под лицензией MIT. См. файл LICENSE для получения подробной информации.
