#!/bin/sh

echo "Create the images..."
./create_png.py

echo "Copy reserved unicode chars..."
cp reserved_unicode_chars/* .

echo "Create the bcfnt file..."
./bcfnt.py -cf code.bcfnt

echo "Convert the bcfnt file into a romfs..."

rm romfs -rf;
mkdir romfs;
./../common/lz_compress.py code.bcfnt romfs/cbf_std.bcfnt.lz;

echo "Cleanups..."
rm code.bcfnt;
rm code_sheet*;

echo "Done"
