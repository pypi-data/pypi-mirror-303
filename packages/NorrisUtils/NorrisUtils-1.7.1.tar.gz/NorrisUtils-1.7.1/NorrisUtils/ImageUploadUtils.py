import os
import requests
from NorrisUtils.FileUtil import compress_image


def get_api_token(username, password):
    """
    根据用户名和密码尝试获取API Token。
    注意：此示例基于假设的API端点和流程，实际API可能需要不同的实现方式。

    :param username: 用户名
    :param password: 密码
    :return: API Token字符串，如果失败则返回None
    """
    # 假设的API端点，实际应根据文档或开发者指南确定
    api_url = "https://sm.ms/api/v2/token"

    # 准备POST请求的数据
    auth_data = {
        'username': username,
        'password': password
    }

    try:
        # 发起POST请求
        response = requests.post(api_url, data=auth_data)
        print(response.text)

        # 检查响应状态码
        if response.status_code == 200:
            # 假设响应是一个JSON对象，包含Token
            json_response = response.json()
            token = json_response.get('data').get('token')
            if token:
                return token
            else:
                print("Token未在响应中找到")
        else:
            print(f"请求失败，状态码：{response.status_code}")
    except requests.RequestException as e:
        print(f"请求过程中发生错误：{e}")

    return None


def upload_image_to_smms(image_path, **kwargs):
    """
    使用PostImage API上传本地图片并返回图片的公网URL。

    :param image_path: 本地图片的路径
    :param kwargs: 可选参数字典，可用于提供额外的选项，比如：
                   - token: 图床token，可选。
                   - logfunc: 日志记录函数，默认为print，用于记录发送过程中的信息，可选。
    :return: 图片的公网URL，如果失败则返回None
    """
    kwargs.setdefault("token", "Sx3b2Rbbb0gbr5hffo6144Fxp0T0s5BG")
    kwargs.setdefault("logfunc", print)
    logfunc = kwargs["logfunc"]
    api_url = "https://sm.ms/api/v2/upload"

    # 检查图片文件是否存在
    if not os.path.exists(image_path):
        logfunc("图片文件不存在")
        return None

    compress_image(os.path.abspath(image_path), kb=5 * 1024)
    try:
        # 准备上传的文件
        with open(image_path, 'rb') as file:
            files = {'smfile': file}

            headers = {
                "Authorization": "Basic " + kwargs["token"]
            }
            print(api_url)
            # 发送POST请求
            response = requests.post(api_url, files=files, headers=headers)
            print(response)
            print(response.text)

            # 解析响应内容
            if response.status_code == 200:
                json_response = response.json()
                if json_response.get('code') == "success":
                    return json_response['data']['url']
                if json_response.get('code') == "image_repeated":
                    return json_response['images']
                else:
                    logfunc(f"上传失败，错误信息：{json_response.get('message')}")
                    return None
            else:
                logfunc(f"上传请求失败，状态码：{response.status_code}")
                return None
    except Exception as e:
        logfunc(f"上传过程中发生错误：{e}")
        return None
