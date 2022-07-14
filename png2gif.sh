#! /bin/zsh
ffmpeg -i $1.%04d.png  -vf "setpts=$2*PTS,scale=800:-1" $1.gif
