#!/bin/sh

echo "Creating EULA files..."

rm romfs -rf;
mkdir -p romfs;
./eula.py romfs;

echo "Done"