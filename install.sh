sudo apt-get update

sudo apt-get install golang libjpeg-turbo8-dev make zlib1g-dev libav-tools ffmpeg python-numpy python-dev cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev python-opengl libboost-all-dev libsdl2-dev swig libstdc++6 python3-setuptools git -y

pip install keras tensorflow keras-rl


mkdir python_libs


cd python_libs
git clone https://github.com/openai/universe.git
cd universe
pip3 install -e .
cd ..
git clone https://github.com/openai/go-vncdriver.git
cd go-vncdriver/
python build.py 
pip install -e .
cd ..
conda install libgcc
pip install gym