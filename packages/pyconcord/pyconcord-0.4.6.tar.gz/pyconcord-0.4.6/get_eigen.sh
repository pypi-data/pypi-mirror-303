#!/bin/bash

# mkdir eigen_build && cd eigen_build && cmake ../eigen-3.4.0 && install && cd ..
if command -v apt-get >/dev/null; then
  apt-get update && apt-get install -y libeigen3-dev build-essential
elif command -v yum >/dev/null; then
  yum update && yum install -y eigen3-devel
elif command -v apk >/dev/null; then
  apk update && apk install eigen3-devel
elif command -v brew >/dev/null; then
  brew install eigen
else
  echo "I have no Idea what im doing here"
fi
