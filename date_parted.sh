#!/bin/bash
#====================================================
# 利用parted 格式化T级别硬盘并利用lvm将其扩展到根分区下
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

#将卷组剩余全部空间扩展到cl-root上
#lvextend -l +100%free /dev/mapper/cl-root

#对扩展后的lv文件格式大小进行调整
#xfs_growfs /dev/mapper/cl-root
