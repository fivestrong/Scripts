#!/bin/bash
#====================================================
# 利用parted 格式化T级别硬盘并利用lvm将其扩展到根分区下
#
# 将卷组剩余全部空间扩展到cl-root上
# lvextend -l +100%free /dev/mapper/cl-root
#
# 对扩展后的lv文件格式大小进行调整
# xfs_growfs /dev/mapper/cl-root
#
# 补充命令
# 创建新的逻辑分区(LV) lvcreate -l +100%FREE VolGroup -n lv_mnt
# 格式化分区为xfs 
# mkfs.xfs -f -i attr=2 -l size=128m,lazy-count=1,sectsize=4096 -b size=4096 -d sectsize=4096 -L data /dev/mapper/VolGroup-lv_mnt
# 利用下面命令来加载模块,扫描并激活卷组
# modprobe dm-mod
# vgscan
# vgchange -ay
#====================================================

for x in a b c d e f g h i j
do 
echo "
mklabel gpt
mkpart primary 0% 100%
set 1 lvm on
quit
" | parted /dev/sd$x

partprobe /dev/sd${x}1
pvcreate /dev/sd${x}1
vgextend cl /dev/sd${x}1
done

