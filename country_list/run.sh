#!/bin/sh

echo "Create country list romfs..."

rm romfs -rf;
mkdir -p romfs;
./country-archive.py country.json romfs;

echo "Done"
