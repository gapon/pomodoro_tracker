# pomodoro_tracker


## Установка Ubuntu

- Скачать образ: [http://wiki.banana-pi.org/Banana_Pi_BPI-M1#Image_Release](http://wiki.banana-pi.org/Banana_Pi_BPI-M1#Image_Release)
    - Лучше брать Armbian он меньше весит и там Ubuntu 18.04 и место на SD карте сразу распределено
- Манипуляции над SD картой:
  ```bash
    diskutil list
    diskutil unmountDisk /dev/disk2
    sudo newfs_msdos -F 32 /dev/disk2
    sudo dd bs=1m if=/Users/gapon/Downloads/2018-07-26-ubuntu-16.04-server-preview-bpi-m1-m1p-r1-sd-emmc.img of=/dev/rdisk2
  ```
- Можно подключаться: ssh root@192.168.1.49 / pass: bananapi
- Для armbian: root@192.168.1.49 / pass: 1234
    - Сначала нужно подключить к монтитору и конфигурацию сделать. ssh сервер запуститься только после конфигурации.
    - Сразу попросит поменять пароль и создать юзера
    - После конфигурации можно ssh

## Установка OpenCV 3.2 на Ubuntu 18.04

- [https://linuxize.com/post/how-to-install-opencv-on-ubuntu-18-04/](https://linuxize.com/post/how-to-install-opencv-on-ubuntu-18-04/)
    - тут и из бинарника инструкция (работча) и собрать можно
    - именно по этой инструкции я поставил OpenCV
    - OpenCV 3.4 on BananaPi (не тестил):
        - [http://wiki.banana-pi.org/OpenCV_3.4x_on_BananaPi](http://wiki.banana-pi.org/OpenCV_3.4x_on_BananaPi)

## Установка и пробрасывание jupyter

- [https://www.digitalocean.com/community/tutorials/how-to-install-run-connect-to-jupyter-notebook-on-remote-server](https://www.digitalocean.com/community/tutorials/how-to-install-run-connect-to-jupyter-notebook-on-remote-server)
- Для пробрасывания:
```bash
    - ssh -L 8000:localhost:8888 gapon@192.168.1.49
```

## Enable SSH

- [https://linuxhint.com/enable-ssh-server-debian/](https://linuxhint.com/enable-ssh-server-debian/)

## Добавить место на SD карте

- [https://www.xelent.ru/blog/rasshirenie-diskovogo-prostranstva-v-ubuntu-linux/](https://www.xelent.ru/blog/rasshirenie-diskovogo-prostranstva-v-ubuntu-linux/)
- resize2fs /dev/vdb1

## Добавить место на Centos без LVM

1. Run fdisk on the right disk (X is the correct letter of your disk): **fdisk /dev/sd*X***

2. Check the partition table by pressing **p** (to view partition details)

3. Delete the partition by pressing **d** (to delete the partition)

4. Select the right partition that you want to delete, in most cases will be the only on the disk, so press **1** (to select the partition)

5. Create a new partition by pressing **n** (to create a new partition) and select the partition type whether Primary (by pressing **p**) and the right number

6. Get the first block from the partition details in point 2

7. Press enter to accept the default as the last block.

8. *Check the partition table by pressing **p** (to list the partition and confirm)*

9. Save your new partition table by pressing **w**

```bash
$ partprobe

$ xfs_growfs /dev/vda1

meta-data=/dev/vda1 isize=512 agcount=201, agsize=524224 blks

= sectsz=512 attr=2, projid32bit=1

= crc=1 finobt=0 spinodes=0

data = bsize=4096 blocks=104857344, imaxpct=25

= sunit=0 swidth=0 blks

naming =version 2 bsize=4096 ascii-ci=0 ftype=1

log =internal bsize=4096 blocks=2560, version=2

= sectsz=512 sunit=0 blks, lazy-count=1

realtime =none extsz=4096 blocks=0, rtextents=0

data blocks changed from 104857344 to 132120320
```
