# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urlparse


def get_filename_from_url(url):
    """
    从URL中提取endpoint作为文件名。

    :param url: str, 完整的URL。
    :return: str, 提取的文件名。
    """
    # 解析URL，获取URL各组成部分
    parsed_url = urlparse(url)
    # 获取URL路径部分
    path = parsed_url.path
    # 判断URL路径是否为根路径
    if path == '/':
        # 如果是根路径，则直接使用查询字符串作为文件名
        file_name = parsed_url.query
    else:
        # 如果不是根路径，则提取路径中的最后一个endpoint，并使用查询字符串作为文件名的一部分
        end_point = path.strip('/').split('/')[-1]
        file_name = end_point + '@' + parsed_url.query
    # 返回构造的文件名
    return file_name
