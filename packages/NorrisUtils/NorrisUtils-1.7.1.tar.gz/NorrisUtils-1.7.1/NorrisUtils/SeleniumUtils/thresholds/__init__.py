# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import time


def default(url, browser_driver, **kwargs):
    pass


def maximize(url, browser_driver, **kwargs):
    """
    将浏览器窗口调整到页面的最大尺寸。

    该函数通过执行JavaScript代码来获取页面的宽度和高度，并将浏览器窗口的尺寸调整到包含页面的最小尺寸。
    它确保浏览器窗口不会遮挡页面的任何部分，提供更好的用户体验。

    参数:
    - browser_driver: 浏览器实例，支持执行JavaScript代码和调整窗口尺寸。
    - **kwargs: 可选参数，目前未使用。

    返回:
    无返回值。
    """
    # 使用JavaScript获取页面的宽度和高度
    width = browser_driver.execute_script("return document.documentElement.scrollWidth")
    height = browser_driver.execute_script("return document.documentElement.scrollHeight")
    print(width, height)

    # 获取当前浏览器窗口的尺寸
    k = browser_driver.get_window_size()
    # 将浏览器窗口的宽高设置成页面的宽高和当前窗口宽高的较大值
    maxw = max(width, k["width"])
    maxh = max(height, k["height"])
    print(maxw, maxh)
    browser_driver.set_window_size(maxw, maxh)
    time.sleep(2)
