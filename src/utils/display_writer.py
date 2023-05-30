import textwrap
import time
from epd7in5b import EPD
from PIL import Image, ImageDraw, ImageFont


class DisplayWriter:
    def __init__(self):
        self.font_file = "Palatino.ttf"
        self.epd: EPD = EPD()
        self.epd.init()

    def write_message_to_display_font_30(self, message: str):
        display = Image.new("1", (self.epd.width, self.epd.height), 255)
        draw = ImageDraw.Draw(display)
        font24 = ImageFont.truetype(self.font_file, 30)

        lines_to_display = textwrap.wrap(
            message, width=58, max_lines=15, placeholder="..."
        )

        y = 0
        for line in lines_to_display:
            draw.text((10, y), line, font=font24, fill=0)
            y += 32

        self.epd.display(self.epd.getbuffer(display))

    def write_message_to_display_font_48(self, message: str):
        display = Image.new("1", (self.epd.width, self.epd.height), 255)
        draw = ImageDraw.Draw(display)
        font48 = ImageFont.truetype(self.font_file, 48)

        lines_to_display = textwrap.wrap(
            message, width=35, max_lines=9, placeholder="..."
        )

        y = 0
        for line in lines_to_display:
            draw.text((10, y), line, font=font48, fill=0)
            y += 53

        self.epd.display(self.epd.getbuffer(display))

    def write_message_to_display_font_64(self, message: str):
        display = Image.new("1", (self.epd.width, self.epd.height), 255)
        draw = ImageDraw.Draw(display)
        font64 = ImageFont.truetype(self.font_file, 64)

        lines_to_display = textwrap.wrap(
            message, width=26, max_lines=7, placeholder="..."
        )

        y = 0
        for line in lines_to_display:
            draw.text((10, y), line, font=font64, fill=0)
            y += 68

        self.epd.display(self.epd.getbuffer(display))

    def write_message_to_display_font_96(self, message: str):
        display = Image.new("1", (self.epd.width, self.epd.height), 255)
        draw = ImageDraw.Draw(display)
        font64 = ImageFont.truetype(self.font_file, 96)

        lines_to_display = textwrap.wrap(
            message, width=16, max_lines=5, placeholder="..."
        )

        y = 0
        for line in lines_to_display:
            draw.text((10, y), line, font=font64, fill=0)
            y += 100

        self.epd.display(self.epd.getbuffer(display))

    def clear_display(self):
        buf = [0x00] * (int(self.width / 8) * self.height)
        self.epd.send_command(0x10)
        self.epd.send_data(buf)
        self.epd.send_data(0x13)
        self.epd.send_data(buf)
        self.epd.send_data(0x12)
