import textwrap
import sys
import os
import epd7in5_V2
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

font_file = "Palatino.ttf"


def write_message_to_display_font_30(epd: epd7in5_V2.EPD, message: str):
    display = Image.new("1", (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(display)
    font24 = ImageFont.truetype(font_file, 30)

    lines_to_display = textwrap.wrap(message, width=58, max_lines=15, placeholder="...")

    y = 0
    for line in lines_to_display:
        draw.text((10, y), line, font=font24, fill=0)
        y += 32

    epd.display(epd.getbuffer(display))


def write_message_to_display_font_48(epd: epd7in5_V2.EPD, message: str):
    display = Image.new("1", (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(display)
    font48 = ImageFont.truetype(font_file, 48)

    lines_to_display = textwrap.wrap(message, width=35, max_lines=9, placeholder="...")

    y = 0
    for line in lines_to_display:
        draw.text((10, y), line, font=font48, fill=0)
        y += 53

    epd.display(epd.getbuffer(display))


def write_message_to_display_font_64(epd: epd7in5_V2.EPD, message: str):
    display = Image.new("1", (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(display)
    font64 = ImageFont.truetype(font_file, 64)

    lines_to_display = textwrap.wrap(message, width=26, max_lines=7, placeholder="...")

    y = 0
    for line in lines_to_display:
        draw.text((10, y), line, font=font64, fill=0)
        y += 68

    epd.display(epd.getbuffer(display))


def write_message_to_display_font_96(epd: epd7in5_V2.EPD, message: str):
    display = Image.new("1", (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(display)
    font64 = ImageFont.truetype(font_file, 96)

    lines_to_display = textwrap.wrap(message, width=16, max_lines=5, placeholder="...")

    y = 0
    for line in lines_to_display:
        draw.text((10, y), line, font=font64, fill=0)
        y += 100

    epd.display(epd.getbuffer(display))


def clear_display(epd: epd7in5_V2):
    epd.Clear()


if __name__ == "__main__":
    epd = epd7in5_V2.EPD()
    epd.init()

    if message_repository.is_image():
        image_name = message_repository.get_message_string()
        image = Image.open(os.path.join(pic_dir, image_name))
        epd.display(epd.getbuffer(image))
    else:
        font_size_function = {
            30: write_message_to_display_font_30,
            48: write_message_to_display_font_48,
            64: write_message_to_display_font_64,
            96: write_message_to_display_font_96,
        }

        message = message_repository.get_message_string()
        if message == "clear":
            clear_display(epd)
            sys.exit(0)

        fontsize = message_repository.get_font_size()
        try:
            font_size_function[int(fontsize)](epd, message)
        except KeyError or TypeError:
            print("Invalid font-size given:", fontsize)
