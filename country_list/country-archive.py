#!/usr/bin/env python3

# Copyright 2018 Weiyi Wang
# Licensed under GPLv2 or any later version
# Refer to the license.txt file included.

import country
import region
import json
import sys
import os

sys.path.append('../')

def loadFromArchive(path):
    result = {}

    regions = result["regions"] = []
    for regionCode in ["CN", "EU", "JP", "KR", "TW", "US"]:
        regions.append(region.loadRegionFromArchive(path, regionCode))

    countries = result["countries"] = []

    for i in range(256):
        countryResult = country.loadCountryFromArchive(path, i)
        if countryResult is not None:
            countries.append(countryResult)

    return result

def writeToArchive(path, archive):
    for regionCode in ["CN", "EU", "JP", "KR", "TW", "US"]:
        os.mkdir(os.path.join(path, regionCode))

    for x in archive["regions"]:
        region.writeRegionToArchive(path, x)


    for x in archive["countries"]:
        country.writeCountryToArchive(path, x)


def main():
    def printHelp():
        print("Usage: {} INPUT OUTPUT".format(sys.argv[0]))
        exit(-1)

    if len(sys.argv) < 3:
        printHelp()

    inPath = sys.argv[1]
    outPath = sys.argv[2]

    with open(inPath, "rt") as f:
        archive = json.load(f)
        writeToArchive(outPath, archive)

if __name__ == "__main__":
    main()
