# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os

load_dotenv()  # 加载 .env 文件


def is_debug_mode():
    return os.getenv('DEBUG_MODE', 'False') == 'True'


import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import NorrisUtils.GarbageGenius as GG
import NorrisUtils.SeleniumUtils.spiders
import NorrisUtils.SeleniumUtils.thresholds


def dump_page_capture(url, filename, **kwargs):
    """
    截取指定网页的长屏截图并保存到文件。

    :param url: str, 需要截图的网页URL。
    :param filename: str, 截图保存的文件名。
    :param kwargs: dict, 附加参数，包括但不限于以下键值：
        - width: int, 浏览器宽度，默认为2180。
        - height: int, 浏览器高度，默认为1280。
        - maximum: bool, 是否最大化浏览器窗口，默认为False。
        - threshold: function, 阈值算法函数，默认为default_threshold。
    :return: str, 返回截图文件名。
    """
    try:
        # 设置kwargs的默认值
        kwargs.setdefault("debug", False)
        kwargs.setdefault("width", 2180)
        kwargs.setdefault("height", 1280)
        kwargs.setdefault("maximum", True)
        kwargs.setdefault("capture_file_name", filename)
        kwargs.setdefault("browser", None)
        kwargs.setdefault("close", True)
        kwargs.setdefault("threshold", NorrisUtils.SeleniumUtils.thresholds.maximize)
        kwargs.setdefault("spider", NorrisUtils.SeleniumUtils.spiders.save_page_capture)
        # 从kwargs中获取设置好的值
        debug = kwargs["debug"]
        width = kwargs["width"]
        height = kwargs["height"]
        maximum = kwargs["maximum"]
        capture_file_name = kwargs["capture_file_name"]
        browser = kwargs["browser"]
        close = kwargs["close"]
        spider = kwargs["spider"]
        threshold = kwargs["threshold"]
        kwargs["debug"] = debug
        kwargs["width"] = width
        kwargs["height"] = height
        kwargs["maximum"] = maximum
        kwargs["capture_file_name"] = capture_file_name
        kwargs["browser"] = browser
        kwargs["close"] = close
        kwargs["spider"] = spider
        kwargs["threshold"] = threshold
        return freestyle(url, **kwargs)
    except Exception as E:
        # 打印异常信息
        print(str(E))
        return None


def dump_page_source(url, **kwargs):
    '''
    截长屏
    :param url: 访问的目标网页URL
    :param kwargs: 可变关键字参数
        - width: int, 浏览器宽度，默认为2180。
        - height: int, 浏览器高度，默认为1280。
        - maximum: bool, 是否最大化浏览器窗口，默认为False。
        - threshold: function, 阈值算法函数，默认为default_threshold。
        - file_name: str, 保存页面源码的文件名，默认为None。
        - browser: Obj, browser，默认为None
        - close: bool, finally 要不要关闭browser，默认为True。
    :return: 页面源码
    '''
    try:
        # 设置kwargs的默认值
        kwargs.setdefault("debug", False)
        kwargs.setdefault("width", 2180)
        kwargs.setdefault("height", 1280)
        kwargs.setdefault("maximum", False)
        kwargs.setdefault("file_name", None)
        kwargs.setdefault("browser", None)
        kwargs.setdefault("close", True)
        kwargs.setdefault("spider", NorrisUtils.SeleniumUtils.spiders.save_page_source)
        # 从kwargs中获取设置好的值
        debug = kwargs["debug"]
        width = kwargs["width"]
        height = kwargs["height"]
        maximum = kwargs["maximum"]
        file_name = kwargs["file_name"]
        browser = kwargs["browser"]
        close = kwargs["close"]
        spider = kwargs["spider"]
        kwargs["debug"] = debug
        kwargs["width"] = width
        kwargs["height"] = height
        kwargs["maximum"] = maximum
        kwargs["file_name"] = file_name
        kwargs["browser"] = browser
        kwargs["close"] = close
        kwargs["spider"] = spider
        return freestyle(url, **kwargs)
    except Exception as E:
        # 打印异常信息
        print(str(E))
        return None


def freestyle(url, **kwargs):
    '''
    截长屏
    :param url: 访问的目标网页URL
    :param kwargs: 可变关键字参数
        - width: int, 浏览器宽度，默认为2180。
        - height: int, 浏览器高度，默认为1280。
        - maximum: bool, 是否最大化浏览器窗口，默认为False。
        - browser: Obj, browser，默认为None
        - close: bool, finally 要不要关闭browser，默认为True。
        - spider: function, 具体的spider逻辑，可以交给外部传入。
    :return: 页面源码
    '''
    # 设置kwargs的默认值
    kwargs.setdefault("debug", False)
    kwargs.setdefault("width", 2180)
    kwargs.setdefault("height", 1280)
    kwargs.setdefault("maximum", False)
    kwargs.setdefault("browser", None)
    kwargs.setdefault("close", True)
    kwargs.setdefault("threshold", NorrisUtils.SeleniumUtils.thresholds.maximize)
    # 用户自定义的spider逻辑，默认为save_page_source下载全网页源码
    kwargs.setdefault("spider", NorrisUtils.SeleniumUtils.spiders.save_page_source)

    # 从kwargs中获取设置好的值
    debug = kwargs["debug"]
    width = kwargs["width"]
    height = kwargs["height"]
    maximum = kwargs["maximum"]
    browser = kwargs["browser"]
    close = kwargs["close"]
    spider = kwargs["spider"]
    # 初始化Chrome选项
    chrome_options = Options()
    # 设置Chrome为无头模式
    chrome_options.add_argument("--headless")
    # 禁用GPU加速
    chrome_options.add_argument("--disable-gpu")
    # no-sandbox
    chrome_options.add_argument('--no-sandbox')
    # disable-dev-shm-usage
    chrome_options.add_argument('--disable-dev-shm-usage')
    # 初始化Chrome浏览器
    if browser is None:
        browser = webdriver.Chrome(options=chrome_options)
        kwargs['browser'] = browser
    try:
        # 访问URL
        browser.get(url)
        # 根据maximum参数设置窗口大小
        if maximum:
            browser.maximize_window()
        else:
            browser.set_window_size(width, height)
        # 打印页面源码
        if debug and is_debug_mode():
            print(browser.page_source)
        # 调用spider逻辑
        return spider(url, browser, **kwargs)
    except Exception as E:
        # 打印异常信息
        print(str(E))
        return None
    finally:
        if close:
            try:
                # 关闭浏览器
                browser.close()
            except Exception as E:
                # 打印异常信息
                print(str(E))