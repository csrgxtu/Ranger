#!/bin/sh
# 移除文件里面的特殊unicode字符，清洗文件
# 接手文件夹为参数，然后对该文件夹下面的所有文件逐一操作，移除特殊字符串。

for f in "$1"/*
do
  echo $f
  # first, remove \u001f
  sed -i 's/\\u001f//g' $1

  # second, remove \u001e
  sed -i 's/\\u001e//g' $1
done
