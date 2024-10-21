import requests, re, time
from dotenv import load_dotenv
import os

load_dotenv()  # 加载 .env 文件


def is_debug_mode():
    return os.getenv('DEBUG_MODE', 'False') == 'True'


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',
}


# 迭代溯源
# 支持插入log方法已经插入中断逻辑的溯源
def iterate_redirect(url, **kwargs):
    # 检查URL是否为空，如果为空则直接返回
    if url == None:
        return url
    # 设置kwargs的默认值
    kwargs.setdefault("origin_url", None)
    kwargs.setdefault("intercept_func", None)
    kwargs.setdefault("pause_func", None)
    kwargs.setdefault("special_func", None)
    kwargs.setdefault("log_func", print)
    # 从kwargs中获取设置好的值
    origin_url = kwargs["origin_url"]
    intercept_func = kwargs["intercept_func"]
    pause_func = kwargs["pause_func"]
    log_func = kwargs["log_func"]
    special_func = kwargs["special_func"]

    try:
        # 由拦截方法判定
        if intercept_func != None and intercept_func(url):
            return origin_url
        # 由中断方法判定
        if pause_func != None and pause_func(url):
            return url
        # 发送HTTP请求，获取响应状态码和头信息
        req = requests.get(url, headers=headers, allow_redirects=False)
        status_code = req.status_code
        # 输出状态码日志
        if log_func != None:
            log_func(status_code)
        # 判断是否为重定向
        if status_code == 302 or status_code == 301:
            headers_location_ = req.headers['Location']
            # 处理重定向URL格式
            if (headers_location_.startswith('//')):
                if log_func != None:
                    log_func(req.headers)
                    log_func('溯源成功！原始地址为：【' + url + '】')
                return url
            # 递归调用自身，继续跟踪重定向
            if log_func != None:
                log_func(req.headers)
                log_func('检测到重定向，正在帮您溯源...')
            return iterate_redirect(headers_location_, **kwargs)
        else:
            # 特殊处理逻辑
            if (special_func != None):
                turple = special_func(url, req.text, **kwargs)
                if turple is not None and turple.len == 2:
                    threshold = turple[0]
                    result_url = turple[1]
                    if threshold:
                        return iterate_redirect(result_url, **kwargs)
            # 溯源成功，返回原始URL
            if log_func != None:
                log_func(req.headers)
                log_func('溯源成功！原始地址为：【' + url + '】')
            return url
    except Exception as e:
        # 异常处理，打印异常信息并返回原始URL
        print(e)
        return url


# 批量溯源，找到原文中url的原地址
def batch_redirect(text, delay=0, **kwargs):
    # 检查URL是否为空，如果为空则直接返回
    if text == None:
        return text
    results = text
    # pattern = re.compile('http(s)://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?')
    pattern = re.compile('[a-zA-z]+://[^\s]*')
    items = re.findall(pattern, text)
    for item in items:
        # 设置kwargs的默认值
        kwargs.setdefault("origin_url", None)
        kwargs.setdefault("intercept_func", None)
        kwargs.setdefault("pause_func", None)
        kwargs.setdefault("special_func", None)
        kwargs.setdefault("log_func", print)
        # 从kwargs中获取设置好的值
        log_func = kwargs["log_func"]
        redirect = iterate_redirect(item, **kwargs)
        # 如果log_func存在，则记录item和redirect的日志
        if log_func != None:
            log_func(item)
            log_func(redirect)
        # 将原文中的item替换为redirect
        results = results.replace(item, redirect)
        # 如果设置了延迟，则执行延迟
        time.sleep(delay)

    # 如果log_func存在，则记录最终的results
    if log_func != None:
        log_func(results)
    return results


if is_debug_mode():
    print(iterate_redirect('http://t.cn/RdNtSt1'))
    print(batch_redirect('asdfasdfasdfasf asdfasdfasd http://t.cn/RdNtSt1'))
