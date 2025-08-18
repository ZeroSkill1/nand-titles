#!/usr/bin/env python3

import sys, os, struct

sys.path.append('../')
from common.lz_compress import compressLz
from io import BytesIO

if len(sys.argv) != 2:
    sys.exit("usage: {} <output directory>".format(sys.argv[0]))

# Since this is a fake EULA, we don't necessarily need full language support.
LANG_BIN_DATA = [ ("English", "I Accept", "Later") ]

with open(os.path.join(sys.argv[1], 'language.bin'), "wb") as output:
    for langname, accept_text, later_text in LANG_BIN_DATA:
        output.write(langname.encode('utf-16-le').ljust(0x40, b'\x00'))
        output.write(accept_text.encode('utf-16-le').ljust(0x40, b'\x00'))
        output.write(later_text.encode('utf-16-le').ljust(0x40, b'\x00'))
        
COUNTRY_IDS = [
    1  , 8  , 9  , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 ,
    26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 ,
    45 , 46 , 47 , 48 , 49 , 50 , 51 , 52 , 64 , 65 , 66 , 67 , 68 , 69 , 70 , 71 , 72 , 73 , 74 ,
    75 , 76 , 77 , 78 , 79 , 80 , 81 , 82 , 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 91 , 92 , 93 ,
    94 , 95 , 96 , 97 , 98 , 99 , 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
    113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 136, 144, 145,
    152, 153, 154, 155, 156, 160, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 184, 185, 186
]

with open(os.path.join(sys.argv[1], 'country.bin'), "wb") as output:
    output.write(len(COUNTRY_IDS).to_bytes(4, "little") + b'\x00' * 0xC)
    for i in range(len(COUNTRY_IDS)):
        output.write(struct.pack("<BBHI4B", COUNTRY_IDS[i], 1, 0xFFFF, 0, 0, 0, 0, 0))
        
eula_text_path = os.path.join(sys.argv[1], '0_LZ.bin')
        
with BytesIO() as uncompressed:
    uncompressed.write(("\nMikage Emulator" + "\n" * 50).encode('utf-16-le'))
    with open(eula_text_path, "wb") as output:
        compressLz(eula_text_path, uncompressed.getvalue(), output)
    