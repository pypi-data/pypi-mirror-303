import os

from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions


def parse_result(raw):
    """
    解析上传结果，提取并返回文件的URL。

    参数:
    raw (dict): 原始的上传结果数据。

    返回:
    str or None: 如果URL存在，则返回URL字符串，否则返回None。
    """
    if raw["url"]:
        return raw["url"]
    else:
        return None


def upload_file(file_path, **kwargs):
    """
    上传文件到ImageKit服务器。

    :param file_path: str，待上传文件的本地路径。
    :param kwargs: dict，额外的参数，包括：
                   - url_endpoint: str，URL端点，默认为"https://ik.imagekit.io/alaricnorris"。
                   - folder: str，上传到的文件夹，默认为"/"。
                   - use_unique_file_name: bool，是否使用唯一文件名，默认为False。
                   - logfunc: function，用于日志输出的函数，默认为print。
                   - debug: bool，是否启用调试模式，默认为False。
                   - parse_result: bool，是否解析结果，默认为True。
    :return: dict or None，上传结果字典，若出错则返回None。
    """
    # 设置默认参数值
    kwargs.setdefault("url_endpoint", "https://ik.imagekit.io/alaricnorris")
    kwargs.setdefault("public_key", "public_U+dy607HsxgkY44ni/lX3G3N4wk=")
    kwargs.setdefault("private_key", "private_iKwiR2Gb5hwoJ2xzYqJ857428N4=")
    kwargs.setdefault("folder", "/")
    kwargs.setdefault("use_unique_file_name", False)
    kwargs.setdefault("logfunc", print)
    kwargs.setdefault("debug", False)
    kwargs.setdefault("parse_result", True)
    logfunc = kwargs["logfunc"]

    # 初始化ImageKit实例
    imagekit = ImageKit(
        public_key=kwargs["public_key"],
        private_key=kwargs["private_key"],
        url_endpoint=kwargs["url_endpoint"],
    )
    # 检查图片文件是否存在
    if not os.path.exists(file_path):
        logfunc("文件不存在")
        return None
    try:
        # 获取文件名
        path_basename = os.path.basename(file_path)
        print(path_basename)
        # 执行上传操作
        upload = imagekit.upload(
            file=open(file_path, "rb"),
            file_name=path_basename,
            options=UploadFileRequestOptions(
                folder=kwargs["folder"],
                use_unique_file_name=kwargs["use_unique_file_name"],
            )
        )
        # Raw Response
        if kwargs["debug"]:
            logfunc(upload.response_metadata.raw)
        # 打印上传文件的ID
        if kwargs["debug"]:
            logfunc(upload.file_id)
        # 根据参数决定是否解析结果
        if kwargs["parse_result"]:
            return parse_result(upload.response_metadata.raw)
        return (upload.response_metadata.raw)
    except Exception as e:
        # 异常处理
        logfunc(f"上传过程中发生错误：{e}")
        return None
