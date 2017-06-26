**Part 1**

Get VirtualBox: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

Get the latest Linux mint image (I recommend Cinnamon): [https://www.linuxmint.com/download.php](https://www.linuxmint.com/download.php)

Install Linux: [https://askubuntu.com/questions/64915/how-do-i-install-ubuntu-on-a-virtualbox-client-from-an-iso-image](https://askubuntu.com/questions/64915/how-do-i-install-ubuntu-on-a-virtualbox-client-from-an-iso-image)


**NOTE**: 

Mint VM must have at least 4GB ram and 40GB disk.


Once Mint is installed:

Go to (inside the VM): [https://www.continuum.io/downloads#linux](https://www.continuum.io/downloads#linux)

Download the 3.6 Python.

Type:

```
bash Anaconda3-4.4.0-Linux-x86_64.sh
```


where *Anaconda3-4.4.0-Linux-x86_64.sh* will be replaced by the file you downloaded.

Agree to terms and conditions. Press space to jump over the text. Once installed, make sure you type yes to add Anaconda to your path.

Type:

```
$ source ~/.bashrc

$ which python
```

Should get:

```
/home/USER/anaconda3/bin/python
```

NOT:

```
/usr/bin/python
```



2) Then run these commands:

```
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
```

  

Run this file, it will tell you if everything has been installed: https://github.com/shantnu/RL/blob/master/test_install.py