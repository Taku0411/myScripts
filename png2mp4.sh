#! /bin/zsh
ffmpeg -framerate 10 -i $1.%04d.png -vcodec libx264 -pix_fmt yuv420p -r 10 $1.mp4