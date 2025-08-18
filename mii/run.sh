#!/bin/sh

echo "Create mii resource romfs..."

rm romfs -rf;
mkdir -p romfs;
./mii.py custom romfs;

echo "Done"
