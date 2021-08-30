import numpy
import cv2
import os
import matplotlib.pyplot as plt
# 显示图片
def cv_img_show(name,name2,flag):
    # 获取
    # img是一个m*n*1 或者m*n*2 或者m*n*3的数组 具体看是由几个色彩数组组储层
    img=cv2.imread(name,flag)#默认三色图
    img2=cv2.imread(name2,flag)
    # print(img.shape)

    # 切片处理
    # img=img[0:1000,0:1000]

    # 对不同的颜色矩阵的处理
    #一个小细节对不同
    # print(cv2.split(img))
    # b,g,r=cv2.split(img)
    # shape可以表示数组的m*n
    # print(b.shape)
    # print(b)
    # print(g)
    # print(r)

    #保留色彩
    # 数组的操作[:,:,x]表示数组中第几个
    # img[:,:,0]=0
    # img[:,:,1]=0
    # print(img[:,:,0])

    # 边界填充
    top_size,bottom_size,left_size,right_size=(25,25,25,25)
    # img=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REPLICATE)#复制填充
    # img=cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT)#反射填充
    # img = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)  # 反射填充
    # img = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP) # 外包装填充
    # img = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT) # 常量填充

    # 维度一致可以相加并且不大于256 大于256则取余 相当于%256
    # img_2=img+10
    # print(img[:5,:5,0])
    # print(img_2[:5,:5,0])
    # print((img_2+img)[:5,:5,0])
    # cv2.add(img_2,img)[:5,:5,0] #cv2.add和直接数组相加有所不同 不同之处在于add的值如果超过了255 那么取255 不会取余

    # 图像融合
    # print(img.shape)
    # print(img2.shape)
    img2=cv2.resize(img2,(img.shape[1],img.shape[0])) #这里有个坑 resize的时候 第二个参数并不是m*n 而是反过来 n*m放入
    # print(img2.shape==img.shape)
    # # cv2.imshow(img2+img) 错误的图像融合方式
    # merge_img=cv2.addWeighted(img,0.5,img2,0.5,100) #公式为 res=a*X1+b*X2+c a为第一张图像占空比，b为第二张图像占空比，c为图像的亮度
    # cv2.imshow('merge_img',merge_img)
    # resize_img=cv2.resize(img,(0,0),fx=1.2,fy=1.2) #同比例放大2倍
    # cv2.imshow('resize_img',resize_img)#一定要记住这个imshow 必须给图像命名

    # 图像的阈值操作
    # ret,dst=cv2.threshold(src,thresh,maxval,type) ret为阈值，dst为转换后的图像，src为图像，threshold为阈值，maxval为超过阈值部分可以赋予的值，type为模式
    # type分为4个模式 cv2.THRESHOLD_BINARY cv2.THRESHOLD_BINARY_INV cv2.THRESHOLD_TRUNC cv2.THRESHOLD_TOZERO cv2.THRESHOLD_TOZERO_INV
    # ret,img2=cv2.threshold(img2,127,255,cv2.THRESH_BINARY)#超出部分去maxval 小于部分取0
    # ret, img2=cv2.threshold(img2,127,255,cv2.THRESH_TOZERO)#小于部分取0 大于部分不变
    # ret, img2 = cv2.threshold(img2, 127, 255, cv2.THRESH_TOZERO_INV)#小于部分不变 大于阈值部分取0
    # ret, img2 = cv2.threshold(img2, 127, 255, cv2.THRESH_TRUNC)#大于部分取阈值 小于部分不变

    # 显示
    # cv2.imshow('img',img)
    cv2.imshow('img2',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 显示视频
def cv_video_show(name,flag):
    video_file=cv2.VideoCapture(name)
    if video_file.isOpened():
        open_flag=True
    else:
        open_flag=False
    while open_flag:
        #read() will return the tuple.The first arg is the flag which shows whether the file is opened.The second arg is the mat.
        opened_flag,video = video_file.read()
        if video is None:
            break
        elif opened_flag==True:
            # video=cv2.cvtColor(video,flag)
            cv2.imshow('video',video)
            #这段话必须加不加不行
            if cv2.waitKey(5) & 0xFF == 'Q':
                break
    video_file.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    img_name='1.png'
    video_name='1.mp4'
    img_2_name='2.png'
    cv_img_show(img_name,img_2_name,cv2.IMREAD_GRAYSCALE)
    # cv_img_show(img_name,img_2_name,cv2.COLOR_RGB2BGR)
    # cv_video_show(video_name,cv2.COLOR_RGB2GRAY)