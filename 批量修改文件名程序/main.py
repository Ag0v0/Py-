import os

def rename():
    count=1
    print("欢迎使用文件批量重命名程序！\n修改后，文件名将自动修改为序号累加类型，如：1.png,2.png...20.png")
    path=input("请输入文件夹路径：")

    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files) #原来的文件路径
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue
        filename=os.path.splitext(files)[0] #文件名
        filetype=os.path.splitext(files)[1] #文件扩展名
        Newdir=os.path.join(path,str(count)+filetype) #新的文件路径
        os.rename(Olddir,Newdir) #重命名
        count+=1

rename()
print("重命名完成！")