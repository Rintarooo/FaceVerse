#!/bin/bash
# https://qiita.com/namakemono/items/c963e75e0af3f7eed732

# FILE_ID=1V80ntpWj1BJb7jriWR2ipdcSQIFTHOwv
# FILE_NAME=faceverse_v0.zip

# faceverse_v0.zip: https://drive.google.com/file/d/1V80ntpWj1BJb7jriWR2ipdcSQIFTHOwv/view
# faceverse_v1.zip: https://drive.google.com/file/d/1CWnZMxI_lH9lPo-_hbRvgM6b-KfSRtFJ/view
# faceverse_v3_6_s.npy: https://drive.google.com/file/d/1WrQ1UNMY30YAl8WxAbqVb6ZsPEQ_FHW4/view

# wget "https://drive.google.com/uc?export=download&id=${FILE_ID}" -O ${FILE_NAME}

file_ids=(
    "1V80ntpWj1BJb7jriWR2ipdcSQIFTHOwv"
    "1CWnZMxI_lH9lPo-_hbRvgM6b-KfSRtFJ"
    "1WrQ1UNMY30YAl8WxAbqVb6ZsPEQ_FHW4"
)

file_names=(
  "data/faceverse_v0.zip"
  "data/faceverse_v1.zip"
  "faceversev3_jittor/data/faceverse_v3_6_s.npy"
)

# PRETRAINED_DIR="pretrained"
# if [ ! -d "$PRETRAINED_DIR" ]; then
#   mkdir -p "$PRETRAINED_DIR"
#   echo "'$PRETRAINED_DIR' is made"
# else
#   echo "$PRETRAINED_DIR' already exists"
# fi

for ((i=0; i<${#file_names[@]}; i++)); do
# for file_name in "${file_names[@]}"; do
#   echo "$file_name"
  FILE_NAME=${file_names[i]}
  FILE_ID=${file_ids[i]}
  curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null
  CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
  # curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${PRETRAINED_DIR}/${FILE_NAME}
  curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}
done

# curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null
# CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
# curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}