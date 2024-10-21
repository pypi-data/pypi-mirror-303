import requests

import base64
import hashlib
import hmac
import json
import time
import urllib.parse

import NorrisUtils.ImageKitUtils


def sign(secret: str, timestamp):
    """
    生成钉钉消息签名。

    参数:
    dingtalk_secret (str): 钉钉提供的密钥。
    timestamp (str): 当前时间戳。

    返回:
    str: 生成的签名字符串。
    """
    # 将密钥转换为字节串
    secret_enc = secret.encode('utf-8')
    # 构建待签名字符串
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    # 将待签名字符串转换为字节串
    string_to_sign_enc = string_to_sign.encode('utf-8')
    # 使用HMAC-SHA256算法计算签名
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    # 对计算得到的签名进行Base64编码，并使用URL安全方式编码
    signature = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return signature


def send_to_dingtalk(url_webhook: str, **kwargs):
    """
    https://open.dingtalk.com/document/orgapp/custom-robots-send-group-messages
    发送消息到钉钉群。该函数支持发送纯文本消息，并可以根据需要扩展发送其他类型的消息。

    :param url_webhook: 钉钉群机器人的Webhook地址，用于发送消息的接口地址。
    :param kwargs: 可选参数字典，可用于提供额外的消息发送选项，比如：
                   - secret: 钉钉群机器人的secret，用于签名验证，可选。
                   - logfunc: 日志记录函数，默认为print，用于记录发送过程中的信息，可选。
                   - callback: 回调函数，默认为None，用于处理发送消息后的响应，可选。
                   - data: 发送的消息数据，默认为None，可用于直接指定消息内容，可选。
                   - msgtype: 消息类型，默认为"text"，支持多种消息类型如文本、图片等，可选。
                   - title: 消息标题，默认为空字符串，某些消息类型如链接消息需要此参数，可选。
                   - content: 消息内容，默认为空字符串，某些消息类型如文本消息需要此参数，可选。
                   - markdown: markdown格式的消息内容，默认为空字符串，支持发送markdown格式的消息，可选。
                   - isAtAll: 是否@所有人，默认为False，适用于文本消息，可选。
                   - atMobiles: 需要@的用户手机号码列表，默认为空列表，适用于文本消息，可选。

    :return: 成功与否。
    """
    kwargs.setdefault("secret", None)
    kwargs.setdefault("logfunc", print)
    kwargs.setdefault("callback", None)
    kwargs.setdefault("data", None)
    kwargs.setdefault("msgtype", "text")
    kwargs.setdefault("title", "")
    kwargs.setdefault("content", "")
    kwargs.setdefault("markdown", "")
    kwargs.setdefault("isAtAll", False)
    kwargs.setdefault("atMobiles", [])
    logfunc = kwargs["logfunc"]
    secret = kwargs["secret"]
    msgtype = kwargs["msgtype"]
    data = kwargs["data"]
    if kwargs["data"] is None:
        # 构建请求数据，采用JSON格式封装文本消息
        data = {
            "msgtype": msgtype,
            "at": {
                "isAtAll": False if kwargs.get("atMobiles") is None else kwargs["isAtAll"],
                "atMobiles": kwargs["atMobiles"],
            },
            "text": {} if msgtype != "text" else {
                "content": kwargs["content"],
            },
            "markdown": {} if msgtype != "markdown" else {
                "title": "title" if kwargs["title"] is None or kwargs["title"] == "" else kwargs["title"],
                "text": kwargs["markdown"]
            }
        }
    logfunc(str(data))

    # 定义数据类型
    headers = {'Content-Type': 'application/json'}
    if secret is None or secret == "":
        url = url_webhook
    else:
        timestamp = str(round(time.time() * 1000))
        signature = sign(secret, timestamp)
        url = url_webhook + f"&timestamp={timestamp}&sign={signature}"
    try:
        print(url)
        # 发送post请求
        response = requests.post(url, json=data, headers=headers)
        # 发送POST请求到钉钉群机器人Webhook
        print(response.text)
        # 检查响应状态码，确保发送成功
        if response.status_code != 200:
            logfunc(f"发送文本消息至钉钉群失败，状态码：{response.status_code}, 响应内容：{response.text}")
            return False
        else:
            if (response.text.__contains__("errcode\":0")):
                logfunc(f'消息【{str(data)}】已成功发送至钉钉群')
                if kwargs.get("callback"):
                    kwargs["callback"]()
                #     markdown目前不支持@，所以如果markdown有@，则需要补发文本
                if data.get("msgtype") == "markdown":
                    if kwargs["isAtAll"] or (kwargs["atMobiles"] is not None and len(kwargs["atMobiles"]) > 0):
                        send_dingtalk_text(
                            url_webhook,
                            content="请查看",
                            secret=secret,
                            atMobiles=kwargs["atMobiles"],
                            isAtAll=kwargs["isAtAll"]
                        )
                return True
            logfunc(f"发送文本消息至钉钉群失败， 响应内容：{response.text}")
        return False
    except Exception as e:
        logfunc(f"发送请求时发生错误：{e}")
        return False


def send_dingtalk_text(url_webhook: str, **kwargs):
    """
    https://open.dingtalk.com/document/orgapp/custom-robots-send-group-messages
    发送消息到钉钉群。该函数支持发送纯文本消息，并可以根据需要扩展发送其他类型的消息。

    :param url_webhook: 钉钉群机器人的Webhook地址，用于发送消息的接口地址。
    :param kwargs: 可选参数字典，可用于提供额外的消息发送选项，比如：
                   - secret: 钉钉群机器人的secret，用于签名验证，可选。
                   - logfunc: 日志记录函数，默认为print，用于记录发送过程中的信息，可选。
                   - callback: 回调函数，默认为None，用于处理发送消息后的响应，可选。
                   - content: 消息内容，默认为空字符串，某些消息类型如文本消息需要此参数，可选。
                   - isAtAll: 是否@所有人，默认为False，适用于文本消息，可选。
                   - atMobiles: 需要@的用户手机号码列表，默认为空列表，适用于文本消息，可选。

    :return: 成功与否。
    """
    kwargs.setdefault("secret", None)
    kwargs.setdefault("logfunc", print)
    kwargs.setdefault("callback", None)
    kwargs.setdefault("content", "")
    kwargs.setdefault("isAtAll", False)
    kwargs.setdefault("atMobiles", [])
    callback = kwargs["callback"]
    logfunc = kwargs["logfunc"]
    if kwargs["content"] is None or kwargs["content"] == "":
        logfunc("content不能为空请检查")
        if callback:
            callback()
        return False
    return send_to_dingtalk(
        url_webhook,
        secret=kwargs["secret"],
        atMobiles=kwargs["atMobiles"],
        msgtype="text",
        content=kwargs["content"],
        isAtAll=kwargs["isAtAll"],
    )


def send_dingtalk_markdown(url_webhook: str, **kwargs):
    """
    https://open.dingtalk.com/document/orgapp/custom-robots-send-group-messages
    发送消息到钉钉群。该函数支持发送纯文本消息，并可以根据需要扩展发送其他类型的消息。

    :param url_webhook: 钉钉群机器人的Webhook地址，用于发送消息的接口地址。
    :param kwargs: 可选参数字典，可用于提供额外的消息发送选项，比如：
                   - secret: 钉钉群机器人的secret，用于签名验证，可选。
                   - logfunc: 日志记录函数，默认为print，用于记录发送过程中的信息，可选。
                   - callback: 回调函数，默认为None，用于处理发送消息后的响应，可选。
                   - title: 消息标题，默认为空字符串，某些消息类型如链接消息需要此参数，可选。
                   - markdown: markdown格式的消息内容，默认为空字符串，支持发送markdown格式的消息，可选。
                   - isAtAll: 是否@所有人，默认为False，适用于文本消息，可选。
                   - atMobiles: 需要@的用户手机号码列表，默认为空列表，适用于文本消息，可选。

    :return: 成功与否。
    """
    kwargs.setdefault("secret", None)
    kwargs.setdefault("logfunc", print)
    kwargs.setdefault("callback", None)
    kwargs.setdefault("title", "")
    kwargs.setdefault("markdown", "")
    kwargs.setdefault("isAtAll", False)
    kwargs.setdefault("atMobiles", [])
    callback = kwargs["callback"]
    logfunc = kwargs["logfunc"]

    if kwargs["markdown"] is None or kwargs["markdown"] == "":
        logfunc("markdown不能为空请检查")
        if callback:
            callback()
        return False

    # 构建请求数据，采用JSON格式封装文本消息
    data = {
        "msgtype": "markdown",
        "at": {
            "isAtAll": kwargs["isAtAll"],
            "atMobiles": kwargs["atMobiles"],
        },
        "markdown": {
            "title": kwargs["title"],
            "text": kwargs["markdown"]
        }
    }
    return send_to_dingtalk(
        url_webhook,
        secret=kwargs["secret"],
        atMobiles=kwargs["atMobiles"],
        isAtAll=kwargs["isAtAll"],
        data=data,
    )


def send_dingtalk_image(url_webhook: str, image_path: str, **kwargs):
    """
    https://open.dingtalk.com/document/orgapp/custom-robots-send-group-messages
    发送消息到钉钉群。该函数支持发送纯文本消息，并可以根据需要扩展发送其他类型的消息。

    :param url_webhook: 钉钉群机器人的Webhook地址，用于发送消息的接口地址。
    :param secret:      钉钉群机器人的secret，用于签名验证，可选。
    :param image_path: 要发送的图片的本地文件路径或者网络链接。
    :param kwargs: 可选参数字典，可用于提供额外的消息发送选项，比如：
                   - secret: 钉钉群机器人的secret，用于签名验证，可选。
                   - logfunc: 日志记录函数，默认为print，用于记录发送过程中的信息，可选。
                   - callback: 回调函数，默认为None，用于处理发送消息后的响应，可选。
                   - token: 图床token，可选。
                   - magic: 魔法函数，默认为None，用来一键传图到图床，获取链接，可选。
                   - isAtAll: 是否@所有人，默认为False，适用于文本消息，可选。
                   - atMobiles: 需要@的用户手机号码列表，默认为空列表，适用于文本消息，可选。
    :return: 成功与否。
    """
    kwargs.setdefault("secret", None)
    kwargs.setdefault("logfunc", print)
    kwargs.setdefault("callback", None)
    kwargs.setdefault("token", "Sx3b2Rbbb0gbr5hffo6144Fxp0T0s5BG")
    kwargs.setdefault("magic", None)
    kwargs.setdefault("isAtAll", False)
    kwargs.setdefault("atMobiles", [])
    callback = kwargs["callback"]
    logfunc = kwargs["logfunc"]
    magic = kwargs["magic"]
    if magic is not None:
        image_url = magic(image_path)
    else:
        image_url = NorrisUtils.ImageKitUtils.upload_file(image_path)
    if image_url is None or image_url == "":
        logfunc("未能成功上传图片，请检查！")
        if callback:
            callback()
        return False
    markdown = f"markdown图片![image]({image_url})"
    # # 构建请求数据，采用JSON格式封装文本消息
    # data = {
    #     "msgtype": "markdown",
    #     "at": {
    #         "isAtAll": kwargs["isAtAll"],
    #         "atMobiles": kwargs["atMobiles"],
    #     },
    #     "markdown": {
    #         "title": "图片",
    #         "text": markdown
    #     }
    # }
    return send_dingtalk_markdown(
        url_webhook,
        secret=kwargs["secret"],
        atMobiles=kwargs["atMobiles"],
        isAtAll=kwargs["isAtAll"],
        title="markdown图片",
        markdown=markdown,
    )
