ffmpeg -i $1.mp4 -pix_fmt yuv420p -vf "scale=$2:-1" $1_compress.mp4
