# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import NorrisUtils.GarbageGenius as GG
import NorrisUtils.SeleniumUtils.spiders


def more_time_dump(url, browser_driver, **kwargs):
    # 设置kwargs的默认值
    kwargs.setdefault("folder", './captures/')
    kwargs.setdefault("threshold", None)
    # 从kwargs中获取设置好的值
    folder = kwargs["folder"]
    # 从kwargs中获取设置好的值
    threshold = kwargs["threshold"]
    element = browser_driver.find_element(by=By.XPATH, value='//*[@id="panel-yuyue"]/div/div[1]/div[2]')
    text = element.text
    ss = re.findall('\\d{4}-\\d{2}-\\d{2}\\s\\d{2}:\\d{2}:\\d{2}', text)[0]
    filename = ss.replace(' ', '').replace(':', '').replace('-', '')
    png_filename = (folder + '%s.png') % filename
    print(png_filename)
    GG.clean_caches(folder_path=folder, size_threshold=66)
    if threshold is not None:
        kwargs["capture_file_name"] = png_filename
        # 应用阈值算法
        if threshold(url, browser_driver, **kwargs):
            print(f'已经dump过')
            return browser_driver, png_filename

    # # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = browser_driver.execute_script("return document.documentElement.scrollWidth")
    height = browser_driver.execute_script("return document.documentElement.scrollHeight")
    print(width, height)
    # # 将浏览器的宽高设置成刚刚获取的宽高
    browser_driver.set_window_size(width, height)
    browser_driver.save_screenshot(png_filename)  # 截取全屏
    return browser_driver, png_filename


def more_time_threshold(url, browser_driver, **kwargs):
    '''
    阈值逻辑
    检查本地有无dump过
    :return:
    '''
    kwargs.setdefault("capture_file_name", None)
    capture_file_name = kwargs["capture_file_name"]
    print('threshold:' + capture_file_name)
    if capture_file_name == None or capture_file_name == '':
        return True
    # 没有后缀自动补齐
    if not capture_file_name.endswith('.png'):
        capture_file_name += '.png'
        pass
    if os.path.exists(capture_file_name):
        absolute_path = os.path.abspath(capture_file_name)
        file_size = os.path.getsize(absolute_path)
        print(f'已经dump过{absolute_path}，文件大小为 {file_size} 字节')
        return True
    return False


from dotenv import load_dotenv
import os

load_dotenv()  # 加载 .env 文件


def is_debug_mode():
    return os.getenv('DEBUG_MODE', 'False') == 'True'


# if is_debug_mode():
#     import NorrisUtils.SeleniumUtils.Utils

#     from selenium import webdriver
#     from selenium.webdriver.chrome.service import Service
#     from selenium.webdriver.chrome.options import Options

#     # 设置 Chrome for Testing 的路径
#     chrome_for_testing_path = "/Users/htd/Desktop/chrome-mac-x64/Chrome4t.app/Contents/MacOS/Google Chrome for Testing"  # 替换为你的 Chrome for Testing 路径
#     chromedriver_path = "/usr/local/bin/chromedriver"  # 替换为你的 ChromeDriver 路径

#     # 配置 Chrome 选项
#     chrome_options = Options()
#     chrome_options.binary_location = chrome_for_testing_path
#     chrome_options.add_argument("--headless")  # 如果需要无头模式
#     chrome_options.add_argument("--disable-gpclu")
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')

#     # 初始化 ChromeDriver
#     service = Service(chromedriver_path)
#     browser = webdriver.Chrome(service=service, options=chrome_options)

#     turple = NorrisUtils.SeleniumUtils.Utils.dump_page_capture('http://www.qianggou5.com/price/', '', folder='./captures/',
#                                                                spider=more_time_dump,
#                                                                threshold=more_time_threshold, browser=browser)
#     # turple = NorrisUtils.SeleniumUtils.Utils.dump_page_capture('http://www.qianggou5.com/price/', '', folder='./captures/', spider=more_time_dump,
#     #                            threshold=more_time_threshold)
#     print(turple)
