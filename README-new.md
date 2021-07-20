# pomodoro_tracker

## Установить Raspberry Pi OS

Для PyTorch нужно версии нужна 64 bit Raspi OS
Скачать образ можно здесь https://downloads.raspberrypi.org


https://github.com/KumaTea/pytorch-aarch64



Инструкция для установки из под wheels тут https://mathinf.com/pytorch/arm64/


```bash
sudo apt update && sudo apt upgrade
```
- Установить Vim
```bash
sudo apt install vim
```
- Unzip
```bash
sudo apt install unzip
```

## Enable ssh

- Install the openssh-server:
```bash
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```
- Проверить статус ssh:
```bash
sudo systemctl status ssh
```
- Если включен фаервол, то нужно разрешить ssh:
```bash
sudo ufw status # проверить статус
sudo ufw allow ssh
```

## Установка и настройка git
- Установить git
```bash
sudo apt install git
```
- Настройка git
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```
- Посмотреть текущие настройки
```bash
git config --list
```

## Настройка среды

- Установить pip
```bash
sudo apt install python3-pip
```
- Установить virtualenvwrapper
```bash
pip3 install virtualenvwrapper
```
- Добавить в `~/.profile`
```bash
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source $HOME/.local/bin/virtualenvwrapper.sh
```
- Засорсить `~/.profile`
```bash
source ~/.profile
```
- Создать virtualenv
```bash
mkvirtualenv -p python3.9 venv_name
```

## Установка jupyter
```bash
pip install jupyter
```

Добавить kernel в jupyter

```bash
# Inside venv
pip install ipykernel
python -m ipykernel install --user --name=myenv
```

Для пробрасывания
```bash
ssh -L 8000:localhost:8888 pi@192.168.1.43
```



## Доступ к вебкамере
```bash
sudo chmod 777 /dev/video0
```


