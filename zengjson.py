import json
from PIL import Image, ImageFilter
import json
import os
import re
import fnmatch
import copy
#需要不公开，能够自动对coco数据做数据增强，解决了多类别增强存在的困难，网上应该没有类似的代码
ROOT_DIR = r'F:\paddle\\'  #放新的json的路径
imgdir=r'F:\paddle\red\train\train\img\\'  #原始图片目录，增强后的图片也放在这里
id=0
f = open(r'F:\paddle\red\train\train\1.json', encoding='utf-8')  #原始coco标注的json文件
setting = json.load(f)
setting1 =copy.deepcopy(setting)




def changetag(anns,ids,tids): #改变图片标注，根据变换类型
    hh=setting['images'][anns[0]['image_id']]['height']
    ww=setting['images'][anns[0]['image_id']]['width']
    hh=int(hh)
    ww=int(ww)
    tid=tids
    for i1 in range(len(anns)):
        if ids==0: #如果不旋转和翻转和裁切，图片坐标不会变
            anns[i1]['id']=tid
            anns[i1]['image_id']=imd
            tid=tid+1 #注释条目增加1
        if ids==1:  #需要左右翻转图片
            anns[i1]['id']=tid
            anns[i1]['image_id']=imd
            s1=anns[i1]['bbox']
            print(type(s1[0]),type(ww))
            anns[i1]['bbox']=[int(ww)-s1[0]-s1[2],s1[1],s1[2],s1[3]] #一定要记住左右翻转后顶点变了的，左上顶点变成了之前的右上顶点所以需要减去一个宽
            for i2 in range(0,len(anns[i1]['segmentation'][0]),2):
                anns[i1]['segmentation'][0][i2]=ww-anns[i1]['segmentation'][0][i2]#左右旋转
            tid=tid+1 #注释条目增加1
        if ids == 2:  # 需要上下翻转图片
            anns[i1]['id'] = tid
            anns[i1]['image_id'] = imd
            s1 = anns[i1]['bbox']
            anns[i1]['bbox'] = [s1[0],hh-s1[1]-s1[3], s1[2], s1[3]]  # 一定要记住上下翻转之后顶点变了的，左上顶点变成了之前的右上顶点所以需要减去一个高
            for i2 in range(1, len(anns[i1]['segmentation'][0]), 2):
                anns[i1]['segmentation'][0][i2] = hh - anns[i1]['segmentation'][0][i2]  # 轮廓上下翻转
            tid=tid+1 #注释条目增加1
    return anns,tid

def getann(imgid): #取得指定id的标注信息准备增强
    anns=[]
    #print('len',len(setting['annotations']),setting['annotations'][0])
    for is1 in range(len(setting['annotations'])):
        if setting['annotations'][is1]['image_id']==imgid:
            s=copy.deepcopy(setting['annotations'][is1])
            anns.append(s)
    return anns

def imtag(imid):#生成图片注释
    iminfo=copy.deepcopy(setting['images'][imid])
    iminfo['id']=imd
    iminfo['file_name'] = str(imd)+'.jpg'
    return iminfo


def dochange(idd,idc,imd,tids): #执行图片操作和标签操作，idd标签编号，idc操作模式
    fname = setting1['images'][idd]['file_name']
    iminfo=imtag(idd)
    anns=getann(idd)
    print(fname)
    print(idd,idc,imd,tids)
    if idc==0: #某种不变图像坐标的操作
        im = Image.open(imgdir + fname)
        im2 = im.filter(ImageFilter.GaussianBlur)
        anns,tid = changetag(anns, 0, tids)
        im2.save(imgdir + str(imd) + '.jpg')
        imd=imd+1;
    if idc==1: #某种不变图像坐标的操作
        im = Image.open(imgdir + fname)
        im1 = im.transpose(Image.FLIP_LEFT_RIGHT)  #左右翻转
        #print(i,'anns',anns)
        anns,tid = changetag(anns, 1, tids)
        im1.save(imgdir + str(imd) + '.jpg')
        imd=imd+1;
    if idc==2: #某种改变图像坐标的操作
        im = Image.open(imgdir + fname)
        im1 = im.transpose(Image.FLIP_TOP_BOTTOM)  #上下翻转
        #print(i,'anns',anns)
        anns,tid = changetag(anns, 2, tids)
        im1.save(imgdir + str(imd) + '.jpg')
        imd=imd+1;
    #print(iminfo,anns)
    return iminfo,anns,imd,tid

def dowrite(anns,imtag):
    coco_output["images"].append(imtag)
    #print(coco_output["images"][0])
    for i22 in range(len(anns)):
        coco_output["annotations"].append(anns[i22])







categories=[{"id": 1, "name": "greed", "supercategory": "traffic light"},{"id": 2, "name": "red", "supercategory": "traffic light"}] #
coco_output = {
        "info":[],
        "licenses":[],
        "categories": categories,
        "images": [],
        "annotations": []
    }

tids=len(setting['annotations']) #确定标注编号
imd=len(setting['images']) #确定图片编号
#coco_output=setting1 #如果不注释掉这句那么就会和原来文件写成一个json
#print(len(coco_output['annotations']))
for i in range(len(setting['images'])):
    iminfos,anns,imd,tids=dochange(i,0,imd,tids)
    dowrite(anns, iminfos)  #增强结果到写的json
    iminfos,anns,imd,tids=dochange(i,1,imd,tids)
    dowrite(anns, iminfos)  #增强结果到写的json
    iminfos,anns,imd,tids=dochange(i,2,imd,tids)
    dowrite(anns, iminfos)  #增强结果到写的json
with open('{}/instances_leaf_train2022.json'.format(ROOT_DIR), 'w') as output_json_file:
    json.dump(coco_output, output_json_file)
    print(11111111111111111111111)







"""
fname=setting['images'][2]['file_name']
print(setting['images'][0]['id'])
im = Image.open(imgdir +fname)
#im1 = im.transpose(Image.FLIP_LEFT_RIGHT)  #上下翻转
im1 = im.transpose(Image.FLIP_TOP_BOTTOM)  #上下翻转
im1.save(imgdir+str(imd)+'.jpg')
print(setting['annotations'][0]['image_id'])
print(getann(0))
print(imtag(0))
anns=getann(2)
categories=[{"id": 1, "name": "person", "supercategory": "persons"},{"id": 2, "name": "person1", "supercategory": "persons"}] #
coco_output = {
        "info":[],
        "licenses":[],
        "categories": categories,
        "images": [],
        "annotations": []
    }
coco_output["images"].append(imtag(2))
print(anns)
anns=changetag(anns,2)
print(anns)
for i in range(len(anns)):
    coco_output["annotations"].append(anns[i])
with open('{}/instances_leaf_train2021.json'.format(ROOT_DIR), 'w') as output_json_file:
    json.dump(coco_output, output_json_file)
    print('111111111111111111111111111111!!')
"""