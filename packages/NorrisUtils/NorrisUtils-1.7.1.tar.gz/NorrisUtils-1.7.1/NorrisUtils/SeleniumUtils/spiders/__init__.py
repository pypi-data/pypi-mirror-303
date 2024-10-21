# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import time
import NorrisUtils.SeleniumUtils.spiders.Helper as Helper
import NorrisUtils.SeleniumUtils.thresholds


def save_page_source(url, browser_driver, **kwargs):
    '''
    保存页面源码
    :param browser_driver: 浏览器驱动器
    :param url: 访问的目标网页URL
    :param kwargs: 可变关键字参数
        - src_file_name: str, 保存页面源码的文件名，默认为None
        - threshold: function, 阈值算法函数，默认为default_threshold。
    :return: 页面源码
    '''
    try:
        # 设置kwargs的默认值
        kwargs.setdefault("src_file_name", None)
        # 从kwargs中获取设置好的值
        src_file_name = kwargs["src_file_name"]
        # 如果没有指定文件名，则从URL中获取文件名
        if src_file_name is None:
            src_file_name = f"{Helper.get_filename_from_url(url)}.html"
        # 将最终的HTML保存到文件中
        with open("%s" % src_file_name, "w", encoding="utf-8") as file:
            file.write(browser_driver.page_source)
        # 返回页面源码
        return browser_driver, browser_driver.page_source, src_file_name
    except Exception as E:
        # 打印异常信息
        print(str(E))
        return None


def save_page_capture(url, browser_driver, **kwargs):
    '''
    保存页面源码
    :param browser_driver: 浏览器驱动器
    :param url: 访问的目标网页URL
    :param kwargs: 可变关键字参数
        - capture_file_name: str, 截图网页的文件名，默认为None
        - threshold: function, 阈值算法函数，默认为default_threshold。
    :return: 文件名
    '''
    try:
        # 设置kwargs的默认值
        kwargs.setdefault("capture_file_name", None)
        kwargs.setdefault("threshold", NorrisUtils.SeleniumUtils.thresholds.maximize)
        # 从kwargs中获取设置好的值
        capture_file_name = kwargs["capture_file_name"]
        # 从kwargs中获取设置好的值
        threshold = kwargs["threshold"]
        # 如果没有指定文件名，则从URL中获取文件名
        if capture_file_name is None:
            capture_file_name = f"{Helper.get_filename_from_url(url)}.png"
        # 应用阈值算法
        threshold(url, browser_driver, **kwargs)
        # 保存截图
        browser_driver.save_screenshot(capture_file_name)
        # 返回截图文件名
        return browser_driver, capture_file_name
    except Exception as E:
        # 打印异常信息
        print(str(E))
        return None


def save_page_capture_and_source(url, browser_driver, **kwargs):
    '''
    保存页面截图以及源码
    :param browser_driver: 浏览器驱动器
    :param url: 访问的目标网页URL
    :param kwargs: 可变关键字参数
        - capture_file_name: str, 截图网页的文件名，默认为None
        - threshold: function, 阈值算法函数，默认为default_threshold。
    :return: 文件名
    '''
    try:
        # 设置kwargs的默认值
        kwargs.setdefault("src_file_name", None)
        kwargs.setdefault("capture_file_name", None)
        kwargs.setdefault("threshold", NorrisUtils.SeleniumUtils.thresholds.maximize)
        # 从kwargs中获取设置好的值
        src_file_name = kwargs["src_file_name"]
        # 从kwargs中获取设置好的值
        capture_file_name = kwargs["capture_file_name"]
        # 从kwargs中获取设置好的值
        threshold = kwargs["threshold"]
        # 如果没有指定文件名，则从URL中获取文件名
        if src_file_name is None:
            src_file_name = f"{Helper.get_filename_from_url(url)}.html"
        # 如果没有指定文件名，则从URL中获取文件名
        if capture_file_name is None:
            capture_file_name = f"{Helper.get_filename_from_url(url)}.png"
        # 将最终的HTML保存到文件中
        with open("%s" % src_file_name, "w", encoding="utf-8") as file:
            file.write(browser_driver.page_source)
        # 应用阈值算法
        threshold(url, browser_driver, **kwargs)
        # 保存截图
        browser_driver.save_screenshot(capture_file_name)
        # 返回截图文件名
        return browser_driver, capture_file_name
    except Exception as E:
        # 打印异常信息
        print(str(E))
        return None
