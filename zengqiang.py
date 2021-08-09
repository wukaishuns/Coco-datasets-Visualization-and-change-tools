#对训练集进行增强
import os
import random
from PIL import Image
from shutil import copyfile
rootdir = r'D:\models\change\A_Training_Aera_before_change\1000\img\\' #存放图片
trainpath=r"D:\models\change\A_Training_Aera_before_change\1000\img1\\" #存放标签
rootdir1 = r'D:\models\change\A_Training_Aera_before_change\1000\ezh\\' #存放增强图片
trainpath1=r"D:\models\change\A_Training_Aera_before_change\1000\ezh1\\" #存放增强标签
for parent, dirnames, filenames in os.walk(rootdir):  # 遍历每一张图片
    lens=len(filenames)
inum=1000;
for i in range(0,int(len(filenames)/10)):
    for ii in range(i*10,(i+1)*10):
            chai=random.randint(0,9)
            if chai>=0 and chai<=9:
                im=Image.open(rootdir+filenames[ii])
                im1=Image.open(rootdir1 + filenames[ii])
                if chai==0 or chai==1:
                    ip=random.randint(0,1)
                    if ip==0:
                        im3 = im.transpose(Image.FLIP_TOP_BOTTOM)
                        im4 = im1.transpose(Image.FLIP_TOP_BOTTOM)
                    else:
                        im3 = im.transpose(Image.FLIP_LEFT_RIGHT)
                        im4 = im1.transpose(Image.FLIP_LEFT_RIGHT)
                    ip=random.randint(0,9)
                    if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                        im3.save(trainpath +str(inum)+'.jpg')
                        im4.save(trainpath1 + str(inum)+'.jpg')
                        inum=inum+1;
                    if ip>0 and ip<=3:
                        im3 = im3.rotate(90*ip)
                        im4 = im4.rotate(90 * ip)
                        if os.path.getsize(rootdir + filenames[ii]) > 12288:
                            im3.save(trainpath + str(inum)+'.jpg')
                            im4.save(trainpath1 + str(inum)+'.jpg')
                            inum = inum + 1;
                else:
                    ip = random.randint(1, 3)
                    im3 = im.rotate(90 * ip)
                    im4 = im1.rotate(90 * ip)
                    if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                        im3.save(trainpath + str(inum)+'.jpg')
                        im4.save(trainpath1 + str(inum)+'.jpg')
                        inum = inum + 1;
                    ip=random.randint(0,2)
                    if ip==1:
                        im3 = im3.transpose(Image.FLIP_LEFT_RIGHT)
                        im4 = im4.transpose(Image.FLIP_LEFT_RIGHT)
                        if os.path.getsize(rootdir + filenames[ii]) > 12288:
                            im3.save(trainpath + str(inum)+'.jpg')
                            im4.save(trainpath1 + str(inum)+'.jpg')
                            inum = inum + 1;
                    if ip==0:
                        im3 = im3.transpose(Image.FLIP_TOP_BOTTOM)
                        im4 = im4.transpose(Image.FLIP_TOP_BOTTOM)
                        if os.path.getsize(rootdir + filenames[ii]) > 12288:
                            im3.save(trainpath + str(inum)+'.jpg')
                            im4.save(trainpath1 + str(inum)+'.jpg')
                            inum = inum + 1;
                ip=random.randint(0,4)
                if ip==1 or ip==0 or ip==2:
                    a=random.randint(2,350)
                    im3 = im3.rotate(a)
                    im4 = im4.rotate(a)
                    if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                        im3.save(trainpath + str(inum)+'.jpg')
                        im4.save(trainpath1 + str(inum)+'.jpg')
                        inum = inum + 1;
for i in range(0,int(len(filenames)/10)):
    for ii in range(i*10,(i+1)*10):
            chai=random.randint(0,9)
            if chai>=0 and chai<=9:
                im=Image.open(rootdir+filenames[ii])
                im1=Image.open(rootdir1 + filenames[ii])
                if chai==0:
                    ip=random.randint(0,1)
                    if ip==0:
                        im3 = im.transpose(Image.FLIP_TOP_BOTTOM)
                        im4 = im1.transpose(Image.FLIP_TOP_BOTTOM)
                    else:
                        im3 = im.transpose(Image.FLIP_LEFT_RIGHT)
                        im4 = im1.transpose(Image.FLIP_LEFT_RIGHT)
                    ip=random.randint(0,9)
                    if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                        im3.save(trainpath +str(inum)+'.jpg')
                        im4.save(trainpath1 + str(inum)+'.jpg')
                        inum=inum+1;
                    if ip>0 and ip<=3:
                        im3 = im3.rotate(90*ip)
                        im4 = im4.rotate(90 * ip)
                        if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                            im3.save(trainpath + str(inum)+'.jpg')
                            im4.save(trainpath1 + str(inum)+'.jpg')
                            inum = inum + 1;
                else:
                    ip = random.randint(1, 3)
                    im3 = im.rotate(90 * ip)
                    im4 = im1.rotate(90 * ip)
                    if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                        im3.save(trainpath + str(inum)+'.jpg')
                        im4.save(trainpath1 + str(inum)+'.jpg')
                        inum = inum + 1;
                    ip=random.randint(0,4)
                    if ip==1:
                        im3 = im3.transpose(Image.FLIP_LEFT_RIGHT)
                        im4 = im4.transpose(Image.FLIP_LEFT_RIGHT)
                        if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                            im3.save(trainpath + str(inum)+'.jpg')
                            im4.save(trainpath1 + str(inum)+'.jpg')
                            inum = inum + 1;
                    if ip==0:
                        im3 = im3.transpose(Image.FLIP_TOP_BOTTOM)
                        im4 = im4.transpose(Image.FLIP_TOP_BOTTOM)
                        if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                            im3.save(trainpath + str(inum)+'.jpg')
                            im4.save(trainpath1 + str(inum)+'.jpg')
                            inum = inum + 1;
                ip=random.randint(0,4)
                if ip==1:
                    a=random.randint(2,350)
                    im3 = im3.rotate(a)
                    im4 = im4.rotate(a)
                    if os.path.getsize(rootdir1 + filenames[ii]) > 12288:
                        im3.save(trainpath + str(inum)+'.jpg')
                        im4.save(trainpath1 + str(inum)+'.jpg')
                        inum = inum + 1;

