import requests
from bs4 import BeautifulSoup
import bs4
import re
import json
import NorrisUtils.RequestUtils
import redis

FEATURE_PARSER = 'html.parser'


def find_links_with_keyword(url, keyword):
    return find_tags_by_query(url, tag='a', query=keyword, redis=None, extract_logic=extract_logic_href)


def find_tags_by_query(url, **kwargs):
    """
    根据查询条件从网页中提取指定标签。

    :param url: 网页的URL，用于从网络上获取网页内容。
    :param kwargs: 可变关键字参数，包括：
                   - src: 网页源码。
                   - redis: Redis数据库连接，用于缓存网页内容。
                   - query: 查询字符串。
                   - regex: 正则表达式。
                   - extract_logic: 提取逻辑函数，用于指定如何从网页中提取标签。
    :return: 包含提取到的标签的列表，如果无法提取或参数不正确，则返回空列表。
    """
    try:
        # 设置默认值
        kwargs.setdefault("src", None)
        kwargs.setdefault("redis", None)
        kwargs.setdefault("query", None)
        kwargs.setdefault("regex", None)
        kwargs.setdefault("extract_logic", extract_logic_regex)
        # 从kwargs中获取设置好的值
        src = kwargs["src"]
        redis_db = kwargs["redis"]
        extract_func = kwargs["extract_logic"]

        # 判断是否需要从网页抓取数据
        if (url is None or url == '') and (src is None or src == ''):
            return []

        # 从Redis获取数据或从网页抓取数据
        if src is None or src == '':
            if redis_db is not None and redis_db.get(url) is not None and redis_db.get(url) != '':
                print('cached')
                src = redis_db.get(url)
                soup = BeautifulSoup(src, FEATURE_PARSER)
            else:
                response = requests.get(url)
                response.encoding = 'utf-8'  # 设置编码为 utf-8
                print(response.text)
                if redis_db is not None:
                    redis_db.set(url, response.text, ex=60 * 60 * 24 * 3)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, FEATURE_PARSER)
                else:
                    print(f"请求网页时发生错误，状态码：{response.status_code}")
                    return []

        # 使用BeautifulSoup解析页面源码
        else:
            soup = BeautifulSoup(src, FEATURE_PARSER)

        # 使用指定的提取逻辑查找标签
        results = extract_func(soup, url, **kwargs)
        return results
    except Exception as e:
        # 发生异常时打印错误信息并返回空列表
        print(f"发生错误：{e}")
        return []


def process_element(element, url):
    """
    处理HTML元素，尤其是链接<a>标签，以确保它们的URL是完整的。

    参数:
    - element: BeautifulSoup对象，表示一个HTML元素，尤其是<a>标签。
    - url: 字符串，表示当前页面的URL，用于确定链接的协议（http或https）。

    该函数尝试更新元素的href属性，以确保链接是绝对URL，并且协议与当前页面一致。
    """
    """处理元素，这里仅作为示例，您可以根据需要定义具体的逻辑"""
    if element.name == 'a':  # 检查当前元素是否为<a>标签
        # 在此处添加针对<a>标签的具体逻辑处理
        try:
            if element.attrs is not None and element.attrs['href'] is not None:
                prefix = "https" if url is not None and url.startswith("https") else "http"
                element.attrs['href'] = NorrisUtils.RequestUtils.valid_url(element.attrs['href'], prefix=prefix)
        except:
            pass
        print(f"Processing a tag with text: {element.get_text(strip=True)} and href: {element.get('href')}")


def deep_traverse(soup_element, url):
    """
    深度遍历 BeautifulSoup 对象。

    递归地遍历给定的 BeautifulSoup 对象的所有子元素，对每个元素调用 process_element 函数。

    参数:
    - soup_element: BeautifulSoup 对象的子元素，可以是标签、文本等。
    - url: 相关的 URL，用于处理元素时的上下文信息。
    """
    """深度优先遍历 BeautifulSoup 对象中的所有元素"""
    for child in soup_element.children:
        # 只处理标签类型的子元素
        if isinstance(child, bs4.element.Tag):  # 确保处理的是标签元素
            process_element(child, url)  # 对当前元素进行处理
            # 递归处理当前标签的子元素
            deep_traverse(child, url)  # 递归遍历子元素


def extract_logic_bym_img(soup, url, **kwargs):
    """
    <p><img fetchpriority="high" decoding="async" class="alignnone size-full wp-image-43842" src="https://img.zrfan.com/2024/08/20240808143355746.png" alt="2024-8-9日周五刷卡指南" alt="" width="694" height="13515" /> <img decoding="async" class="alignnone size-full wp-image-43843" src="https://img.zrfan.com/2024/08/20240808143357890.png" alt="2024-8-9日周五刷卡指南" alt="" width="672" height="13419" /></p>
<h2>当日必做</h2>
    """
    matching_imgs = [img for img in soup.find_all('img') if img.get('width') and img.get('height')]
    return matching_imgs


def extract_logic_regex(soup, url, **kwargs):
    """
    使用正则表达式根据给定的查询字符串或正则表达式提取逻辑。

    参数:
    - soup: BeautifulSoup对象，用于解析HTML或XML。
    - url: 字符串，表示网页的URL。
    - **kwargs: 可变关键字参数，包括:
        - query: 查询字符串，默认为None。
        - regex: 正则表达式，默认为None。
        - tag: 标签名称，默认为'a'。

    返回:
    - 匹配的元素列表。
    """
    # 设置默认值
    kwargs.setdefault("query", None)
    kwargs.setdefault("regex", None)
    kwargs.setdefault("tag", 'a')
    query = kwargs["query"]
    regex = kwargs["regex"]
    tag = kwargs["tag"]

    # 当查询字符串和正则表达式都为空时，直接返回空列表
    if (query is None or query == '') and (regex is None or regex == ''):
        return []

    # 根据查询字符串生成默认的正则表达式
    regex = regex if (regex is not None and regex != "") else f".*{query}.*"

    # # 找到所有指定标签的元素
    # elements = soup.find_all(tag)
    # # 筛选匹配正则表达式的元素
    # filtered_elements = [element for element in elements if
    #                      element.text is not None and re.match(regex, element.text)]
    # 合并查找指定标签的元素与筛选匹配正则表达式的元素
    filtered_elements = [element for element in soup.find_all(tag) if
                         match_logic(element, regex)]

    print(filtered_elements)

    # 递归处理每个匹配元素的子元素
    for link in filtered_elements:
        deep_traverse(link, url)

    # 将匹配的元素转换为字符串列表并返回
    return filtered_elements


def match_logic(element, regex):
    """
    使用正则表达式匹配元素的文本内容，并递归地在元素的所有子元素中应用相同的逻辑。

    参数:
    - element: BeautifulSoup 中的 Tag 对象，表示 HTML 或 XML 元素。
    - regex: 字符串类型的正则表达式，用于匹配元素的文本内容。

    返回:
    - 如果存在至少一个元素的文本内容与正则表达式匹配，则返回 True。
    - 否则，返回 False。
    """
    # 检查当前元素的文本内容是否与给定的正则表达式匹配
    if element.text is not None and re.match(regex, element.text):
        return True
    else:
        """深度优先遍历 BeautifulSoup 对象中的所有元素"""
        for child in element.children:
            # 只处理标签类型的子元素
            if isinstance(child, bs4.element.Tag):  # 确保处理的是标签元素
                if match_logic(child, regex):
                    return True
        return False


def extract_logic_href(soup, url, **kwargs):
    """
    根据关键字提取HTML中特定标签的href属性。

    :param soup: BeautifulSoup对象，用于解析HTML内容。
    :param url: 当前HTML页面的URL，用于构造完整的链接。
    :param kwargs: 额外的关键字参数，包括:
                   - query: 关键字，用于匹配链接文本或链接URL。
                   - tag: 指定需要检查的HTML标签，默认为'a'标签。
                   - only_href: 布尔值，指示是否仅返回匹配链接的URL，默认为True。
    :return: 返回匹配链接的URL字符串或包含URL的链接标签，如果没有匹配项则返回空列表。
    """
    # 设置默认值
    kwargs.setdefault("query", None)
    kwargs.setdefault("tag", 'a')
    kwargs.setdefault("only_href", True)
    query = kwargs["query"]
    tag = kwargs["tag"]
    only_href = kwargs["only_href"]

    # 如果query为空或只包含空格，则直接返回空列表
    if query is None or query == '':
        return None

    # 查找所有的指定标签
    elements = soup.find_all(tag)

    # 遍历每个链接元素
    for link in elements:
        # 获取链接的URL
        href = link.get('href')

        # 检查链接内容和链接URL是否包含关键字
        for item in link.contents:
            # 如果链接内容包含关键字
            if query in item:
                # 验证并格式化链接URL
                href = NorrisUtils.RequestUtils.valid_url(href)
                print(href)
                # 根据only_href参数的值决定返回URL还是整个链接标签
                if only_href:
                    return href
                return link

        # 如果链接URL本身包含关键字
        if query in link:
            # 验证并格式化链接URL
            href = NorrisUtils.RequestUtils.valid_url(href)
            print(href)
            # 根据only_href参数的值决定返回URL还是整个链接标签
            if only_href:
                return href
            return link

# from configparser import ConfigParser
#
# parser = ConfigParser()
# parser.read('/Users/htd/Desktop/config_genius.ini')
#
# redis_db = redis.Redis(parser.get('redis', 'host'))
# urll = (find_links_with_keyword('https://www.zrfan.com/category/zhinan/', '2024-8-6'))


# urll = 'https://www.zrfan.com/7379.html'
# urll = 'https://www.zrfan.com/7387.html'
# urll = 'https://www.zrfan.com/7454.html'
# tags = find_tags_by_query(urll, extract_logic=extract_logic_regex,  regex=".*累计.*", tag='blockquote')
# print('\n aaaaa:' + str(tags))
# print('\n aaaaa:' + str(tags.__len__()))
