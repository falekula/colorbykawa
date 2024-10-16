## ColorByKawa

```
ColorByKawa — это Python-класс для удобного форматирования текста с использованием ANSI-цветов в терминале. Он поддерживает стандартные цвета, расширенные 256-цветовые палитры, а также пользовательские цвета в форматах HEX и RGB.
```
## Установка
```
Вы можете установить пакет ColorByKawa с помощью pip. Введите следующую команду в терминале:
```

```bash

pip install colorlibx
```

## Пример использования

```python
Импортируйте библиотку:


import colorbykawa
```

## Теперь, чтобы использовать цветные маркеры в строках, достаточно просто использовать print как обычно:

## Стандартные цвета:

```python

print('{k.Red}This is red text{k.RESET} and {k.Green}this is green text{k.RESET}.')
```

## Цвет в формате HEX:

```python

print('{k.HEX(#FF5733)}This is HEX color text{k.RESET}.')
```

## Цвет в формате RGB:
```python

print('{k.RGB(75,0,130)}This is RGB color text{k.RESET}.')
```

## Примеры использования:

```python

import colorbykawa


# Стандартные цвета
print('{k.Red}This is red text{k.RESET}')

# HEX цвет
print('{k.HEX(#00FF00)}This is HEX green text{k.RESET}')

# RGB цвет
print('{k.RGB(0,0,255)}This is RGB blue text{k.RESET}')
```
## Предопределенные цвета
```
ColorByKawa поддерживает следующие группы цветов:
Стандартные цвета:

    Black
    Red
    Green
    Yellow
    Blue
    Magenta
    Cyan
    White
    Gray
    RedLight
    GreenLight
    YellowLight
    BlueLight
    MagentaLight
    CyanLight
    WhiteLight
    BlackBright
    RedBright
    GreenBright
    YellowBright
    BlueBright
    MagentaBright
    CyanBright
    WhiteBright
```

## Цвета из палитры 256 цветов:
```
    Orange
    Purple
    Turquoise
    Brown
    Pink
    LightGray
    DarkGray
    LightRed
    LightGreen
    LightYellow
    LightBlue
    LightMagenta
    LightCyan
    LightWhite
    DarkRed
    DarkGreen
    DarkYellow
    DarkBlue
    DarkMagenta
    DarkCyan
    DarkWhite
    SkyBlue
    SeaGreen
    Indigo
    Coral
    Beige
    Lime
    Cherry
    Salmon
    Olive
    Tan
    IndigoBlue
    Wheat
    Honeydew
    Mint
    Rose
    Moccasin
    Caramel
    Lavender
    Mauve
    Goldenrod
    Ivory
    Aquamarine
    Raspberry
    Cantaloupe
    Ash
    Chocolate
    Emerald
    Ruby
    TerraCotta
    MintGreen
    Blush
    Tangerine
    Auburn
    Coffee
    Papaya
    CherryRed
    Cinnamon
    Daffodil
    MossGreen
    Aubergine
    Lilac
    MoonYellow
    Eggplant
    PapayaWhip
    Granite
    Khaki
    Sunflower
    MauveTaupe
    Fuchsia
```

## Примечание
```
Цвета отображаются корректно только в терминалах, которые поддерживают ANSI-коды. Если ваш терминал не поддерживает ANSI-коды, текст может не окрашиваться должным образом.
```

## Исключения
```
    ValueError: Поднимается при использовании некорректного формата HEX или RGB значений.
```

## Замечания
```
    Убедитесь, что ваш терминал поддерживает ANSI-коды для правильного отображения цветов.
```

## Лицензия
```
Этот проект распространяется под лицензией MIT. См. LICENSE для подробной информации.
```
