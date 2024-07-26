import re

class ColorByKawa:

    def __init__(self):
        self.Reset = "\033[0m"
        self.Black = "\033[30m"
        self.Red = "\033[31m"
        self.Green = "\033[32m"
        self.Yellow = "\033[33m"
        self.Blue = "\033[34m"
        self.Magenta = "\033[35m"
        self.Cyan = "\033[36m"
        self.White = "\033[37m"
        self.Gray = "\033[90m"
        self.RedLight = "\033[91m"
        self.GreenLight = "\033[92m"
        self.YellowLight = "\033[93m"
        self.BlueLight = "\033[94m"
        self.MagentaLight = "\033[95m"
        self.CyanLight = "\033[96m"
        self.WhiteLight = "\033[97m"
        self.BlackBright = "\033[30;1m"
        self.RedBright = "\033[31;1m"
        self.GreenBright = "\033[32;1m"
        self.YellowBright = "\033[33;1m"
        self.BlueBright = "\033[34;1m"
        self.MagentaBright = "\033[35;1m"
        self.CyanBright = "\033[36;1m"
        self.WhiteBright = "\033[37;1m"
        self.Orange = "\033[38;5;208m"
        self.Purple = "\033[38;5;128m"
        self.Turquoise = "\033[38;5;48m"
        self.Brown = "\033[38;5;94m"
        self.Pink = "\033[38;5;205m"
        self.LightGray = "\033[38;5;250m"
        self.DarkGray = "\033[38;5;235m"
        self.LightRed = "\033[38;5;9m"
        self.LightGreen = "\033[38;5;10m"
        self.LightYellow = "\033[38;5;11m"
        self.LightBlue = "\033[38;5;12m"
        self.LightMagenta = "\033[38;5;13m"
        self.LightCyan = "\033[38;5;14m"
        self.LightWhite = "\033[38;5;15m"
        self.DarkRed = "\033[38;5;88m"
        self.DarkGreen = "\033[38;5;22m"
        self.DarkYellow = "\033[38;5;136m"
        self.DarkBlue = "\033[38;5;24m"
        self.DarkMagenta = "\033[38;5;54m"
        self.DarkCyan = "\033[38;5;6m"
        self.DarkWhite = "\033[38;5;7m"
        self.SkyBlue = "\033[38;5;39m"
        self.SeaGreen = "\033[38;5;36m"
        self.Indigo = "\033[38;5;54m"
        self.Coral = "\033[38;5;204m"
        self.Beige = "\033[38;5;230m"
        self.Lime = "\033[38;5;10m"
        self.Cherry = "\033[38;5;196m"
        self.Salmon = "\033[38;5;209m"
        self.Olive = "\033[38;5;58m"
        self.Tan = "\033[38;5;180m"
        self.IndigoBlue = "\033[38;5;69m"
        self.Wheat = "\033[38;5;229m"
        self.Honeydew = "\033[38;5;152m"
        self.Mint = "\033[38;5;159m"
        self.Rose = "\033[38;5;201m"
        self.Moccasin = "\033[38;5;230m"
        self.Caramel = "\033[38;5;130m"
        self.Lavender = "\033[38;5;207m"
        self.Mauve = "\033[38;5;171m"
        self.Goldenrod = "\033[38;5;220m"
        self.Ivory = "\033[38;5;230m"
        self.Aquamarine = "\033[38;5;80m"
        self.Raspberry = "\033[38;5;125m"
        self.Cantaloupe = "\033[38;5;214m"
        self.Ash = "\033[38;5;246m"
        self.Chocolate = "\033[38;5;94m"
        self.Emerald = "\033[38;5;2m"
        self.Ruby = "\033[38;5;124m"
        self.TerraCotta = "\033[38;5;174m"
        self.MintGreen = "\033[38;5;119m"
        self.Blush = "\033[38;5;217m"
        self.Tangerine = "\033[38;5;208m"
        self.Auburn = "\033[38;5;52m"
        self.Coffee = "\033[38;5;94m"
        self.Papaya = "\033[38;5;215m"
        self.CherryRed = "\033[38;5;196m"
        self.Cinnamon = "\033[38;5;130m"
        self.Daffodil = "\033[38;5;226m"
        self.MossGreen = "\033[38;5;28m"
        self.Aubergine = "\033[38;5;54m"
        self.Lilac = "\033[38;5;138m"
        self.MoonYellow = "\033[38;5;220m"
        self.Eggplant = "\033[38;5;55m"
        self.PapayaWhip = "\033[38;5;229m"
        self.Granite = "\033[38;5;236m"
        self.Khaki = "\033[38;5;143m"
        self.Sunflower = "\033[38;5;226m"
        self.MauveTaupe = "\033[38;5;153m"
        self.Fuchsia = "\033[38;5;201m"

    def col(self, color_name, text):
        if hasattr(self, color_name):
            return f"{getattr(self, color_name)}{text}{self.Reset}"
        return text

    def hcol(self, hex_code, text):
        # Убедимся, что HEX-код корректный
        if not re.match(r'^#[0-9A-Fa-f]{6}$', hex_code):
            raise ValueError("Invalid HEX code format. Use #RRGGBB.")
        
        # Преобразуем HEX-код в RGB
        hex_code = hex_code.lstrip('#')
        r = int(hex_code[0:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:6], 16)
        
        # Генерируем ANSI-код для 24-битных цветов
        return f"\033[38;2;{r};{g};{b}m{text}{self.Reset}"
    
    def rgb(self, r, g, b, text):
        # Убедимся, что значения RGB корректные
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("RGB values must be between 0 and 255.")
        
        # Генерируем ANSI-код для 24-битных цветов
        return f"\033[38;2;{r};{g};{b}m{text}{self.Reset}"

# Пример использования
#color = ColorByKawa()
#print(color.col('Red', 'This is red text'))
#print(color.hcol('#9100ff', 'This is custom color text'))
#print(color.rgb(135,206,235, 'This is RGB color text'))

