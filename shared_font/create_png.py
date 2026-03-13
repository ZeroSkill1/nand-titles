#!/usr/bin/env python3

import PIL.ImageDraw
import PIL.ImageFont
import PIL.Image
import json
import sys
import os

ascii_font = PIL.ImageFont.truetype("Montserrat-Regular.otf", 22)
unifont = PIL.ImageFont.truetype("unifont-10.0.05.ttf", 22)
reservedchar_font = PIL.ImageFont.truetype("LibreCTR-Resources.ttf", 20)

chars = dict()
with open(sys.argv[1],'r') as f:
    manifest = json.load(f)
    glyphmap = manifest['glyphMap']
    chars= {y:x for x,y in glyphmap.items()}

rows = manifest["textureInfo"]["sheetInfo"]["rows"]
cols = manifest["textureInfo"]["sheetInfo"]["cols"]
sheetCount = manifest["textureInfo"]["sheetCount"]
width = manifest["textureInfo"]["sheetInfo"]["width"]
height = manifest["textureInfo"]["sheetInfo"]["height"]

x_start_offset = 0
y_start_offset = 1
x_offset = manifest["textureInfo"]["glyph"]["width"] + 1
y_offset = manifest["textureInfo"]["glyph"]["height"]

current_char = 0
for sheet in range(sheetCount):
    img = PIL.Image.new("RGBA", (width, height))
    draw = PIL.ImageDraw.Draw(img)
    pos_y = y_start_offset
    for row in range(rows):
        pos_x = x_start_offset
        for col in range(cols):
            if (current_char in chars.keys()):
                actual_char = ord(chars[current_char])

                if actual_char <= 127:
                    sel_font = ascii_font
                else:
                    if actual_char >= 0xE000 and actual_char <= 0xE07F:
                        sel_font = reservedchar_font
                    else:
                        sel_font = unifont

                point = pos_x, pos_y if sel_font != reservedchar_font else pos_x + 5, pos_y + 20
                draw.text((pos_x, pos_y), chars[current_char], "#FFF", font=sel_font)
            current_char += 1
            pos_x += x_offset
        pos_y += y_offset
    img.save(os.path.join(sys.argv[2], f"code_sheet{sheet}.png"), "PNG")
