import os
import shutil
import hashlib
import stat


# 查找文件夹中的某个文件
def findMyFileDir(dirPath, findFile):
    files = []
    dirs = []
    for root, dirs, files in os.walk(dirPath, topdown=False):
        for file in files:
            if file == findFile:
                return root
        for dir in dirs:
            findMyFileDir(os.path.join(root, dir), findFile)


# 创建一个文件夹
def createDir(dirPath):
    os.makedirs(dirPath, exist_ok=True)


# 删除一个文件
def delFile(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)


# 删除文件夹里所有的文件
def delDir(dir):
    if (os.path.isdir(dir)):
        for f in os.listdir(dir):
            delDir(os.path.join(dir, f))
        if (os.path.exists(dir)):
            os.rmdir(dir)
    else:
        if (os.path.exists(dir)):
            os.remove(dir)


# 拷贝文件
def copyFile(sourceFilePath, destFilePath):
    if not (os.path.exists(sourceFilePath)):
        return False

    if os.path.exists(destFilePath):
        if getFileMd5(sourceFilePath) == getFileMd5(destFilePath):
            return True
        else:
            os.remove(destFilePath)

    destFileDir = os.path.dirname(destFilePath)
    os.makedirs(destFileDir, exist_ok=True)
    if not (shutil.copyfile(sourceFilePath, destFilePath, follow_symlinks=False)):
        return False
    return True


# 拷贝文件夹里的文件
def copyDir(sourceDir, destDir):
    if not (os.path.exists(sourceDir)):
        return False

    if os.path.exists(destDir):
        shutil.rmtree(destDir)

    if not (shutil.copytree(sourceDir, destDir, symlinks=True)):
        return False
    return True


# 获取文件的md5
def getFileMd5(filePath):
    with open(filePath, 'rb') as f:
        content = f.read()
    hash = hashlib.md5()
    hash.update(content)
    return hash.hexdigest()


# 获取一个文件夹里的所有的文件和该文件对应的md5
def dirList(dirPath):
    listDict = {}
    files = []
    dirs = []
    for root, dirs, files in os.walk(dirPath, topdown=False, followlinks=True):
        for file in files:
            filePath = os.path.join(root, file)
            listDict[os.path.relpath(filePath, dirPath).replace(
                '\\', '/')] = getFileMd5(filePath)
    for dir in dirs:
        dirList(os.path.join(root, dir))
    return listDict


# 逐行读一个文件，并过来文件中某些行里回车和空格
def readLineForFile(filePath):
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()
    newLines = []
    for line in lines:
        line = line.replace('\n', '').strip()
        if line:
            newLines.append(line)
    return newLines


# 保存
def saveDict(dict, fileName='temp.cache'):
    file = open(fileName, 'w')
    file.write(str(dict))
    file.close()


# 读取
def loadDict(fileName='temp.cache'):
    dict = {}
    try:
        file = open(fileName, 'r')
        binary = file.read()
        dict = eval(binary)
        file.close()
    except:
        pass
    return dict


def get_file_list(folder_path):
    """
    拉取文件夹下文件列表
    :param folder_path:
    :return:
    文件按最后修改时间排序
    """
    dir_list = os.listdir(folder_path)
    if not dir_list:
        return
    else:
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
        return dir_list


def get_folder_size(folder_path):
    """
    获取文件夹大小
    :param folder_path: 文件夹目录
    :return: 文件夹大小
    """
    total_size = 0
    for filename in os.listdir(folder_path):
        total_size = total_size + os.path.getsize(os.path.join(folder_path, filename))
    return total_size / 1024 / 1024


def clean_folder(folder_path, size_threshold=111):
    """
    垃圾回收，清理缓存
    :param folder_path:     文件夹路径
    :param size_threshold:  清理阈值，达到多少兆后清理文件夹
    :return:
    """
    folder_size = get_folder_size(folder_path)
    print(folder_size)
    if folder_size > size_threshold:
        file_list = get_file_list(folder_path)
        file_list.reverse()
        for i in range(len(file_list)):
            print("del :%d %s" % (i + 1, file_list[i]))
            os.remove(folder_path + file_list[i])


import os
from PIL import Image
from PIL import ImageFile


# 压缩图片文件
def compress_image(outfile, kb=1024, quality=85, k=0.9):  # 通常你只需要修改mb大小
    """不改变图片尺寸压缩到指定大小
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param k: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """

    o_size = os.path.getsize(outfile) // 1024  # 函数返回为字节，除1024转为kb（1kb = 1024 bit）
    print('before_size:{} after_size:{}'.format(o_size, kb))
    if o_size <= kb:
        return outfile

    ImageFile.LOAD_TRUNCATED_IMAGES = True  # 防止图像被截断而报错

    while o_size > kb:
        im = Image.open(outfile)
        x, y = im.size
        out = im.resize((int(x * k), int(y * k)), Image.Resampling.LANCZOS)  # 最后一个参数设置可以提高图片转换后的质量
        try:
            out.save(outfile, quality=quality)  # quality为保存的质量，从1（最差）到95（最好），此时为85
        except Exception as e:
            print(e)
            break
        o_size = os.path.getsize(outfile) // 1024
        print(o_size)
    return outfile
