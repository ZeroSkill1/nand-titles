#!/bin/sh

create_font() {
	mkdir -p tmp_pngs;
	rm tmp_pngs/* -rf;
    ./create_png.py "$1" tmp_pngs;
	cd tmp_pngs;
    ../bcfnt.py -f ../"$2" -m ../"$1";
	cd ../;
	rm tmp_pngs/* -rf;
}

create_font cbf_std_manifest.json cbf_std.bcfnt
#create_font cbf_ko-Hang-KR_manifest.json cbf_ko-Hang-KR.bcfnt
#create_font cbf_zh-Hans-CN_manifest.json cbf_zh-Hans-CN.bcfnt
#create_font cbf_zh-Hant-TW_manifest.json cbf_zh-Hant-TW.bcfnt

rm romfs -rf;
mkdir romfs;

3dstool -zf cbf_std.bcfnt --compress-out cbf_std.bcfnt.lz --compress-type lzex
#3dstool -zf cbf_ko-Hang-KR.bcfnt --compress-out cbf_ko-Hang-KR.bcfnt.lz --compress-type lzex
#3dstool -zf cbf_zh-Hans-CN.bcfnt --compress-out cbf_zh-Hans-CN.bcfnt.lz --compress-type lzex
#3dstool -zf cbf_zh-Hant-TW.bcfnt --compress-out cbf_zh-Hant-TW.bcfnt.lz --compress-type lzex

echo "Cleanups..."
rm *.bcfnt;

echo "Done"
