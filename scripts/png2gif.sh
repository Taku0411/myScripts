#! /bin/bash
if [ $# -ne 3 ]; then
  echo "引数が一致しません"
  echo "使用方法: ./png2gif.sh 連番ファイル名 再生倍率 出力解像度"
  exit 1
fi
ffmpeg -i $1.%04d.png  -filter_complex "setpts=PTS/$2,scale=$3:-2, split [a][b];[a] palettegen [p]; [b][p]paletteuse" $1.gif
