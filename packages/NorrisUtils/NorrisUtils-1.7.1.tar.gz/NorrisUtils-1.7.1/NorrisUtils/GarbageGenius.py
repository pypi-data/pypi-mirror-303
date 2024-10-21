import os


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


def get_size(folder_path):
    """
    获取文件夹大小
    :param folder_path: 文件夹目录
    :return: 文件夹大小
    """
    total_size = 0
    for filename in os.listdir(folder_path):
        total_size = total_size + os.path.getsize(os.path.join(folder_path, filename))
    return total_size / 1024 / 1024


# 1文件目录   2文件夹最大大小(M)   3超过后要删除的大小(M)
def clean_caches(folder_path, size_threshold=111):
    """
    垃圾回收，清理缓存
    :param folder_path:     文件夹路径
    :param size_threshold:  清理阈值，达到多少兆后清理文件夹
    :return: 
    """
    folder_size = get_size(folder_path)
    print(folder_size)
    if folder_size > size_threshold:
        file_list = get_file_list(folder_path)
        file_list.reverse()
        for i in range(len(file_list)):
            if folder_size > size_threshold:
                print("del :%d %s" % (i + 1, file_list[i]))
                os.remove(folder_path + file_list[i])
