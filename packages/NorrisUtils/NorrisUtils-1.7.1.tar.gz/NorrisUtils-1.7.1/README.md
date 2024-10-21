[//]: # (# SDK 文档)

[//]: # ()
[//]: # (## 概述)

[//]: # ()
[//]: # (此 SDK 提供了截取网页长屏截图和获取网页源码的功能。通过 Selenium 库实现对网页的操作，并支持自定义参数以满足不同场景的需求。)

[//]: # ()
[//]: # (## 安装依赖)

[//]: # ()
[//]: # (确保安装了 `Selenium` 库以及对应的浏览器驱动程序。)

[//]: # ()
[//]: # (## 导入模块)

[//]: # ()
[//]: # (``` python)

[//]: # (python from selenium import webdriver )

[//]: # (from selenium.webdriver.chrome.options import Options )

[//]: # (import NorrisUtils.SeleniumUtils.spiders )

[//]: # (import NorrisUtils.SeleniumUtils.thresholds)

[//]: # (```)

[//]: # ()
[//]: # (## 函数说明)

[//]: # ()
[//]: # (### `dump_page_capture&#40;url, filename, **kwargs&#41;`)

[//]: # ()
[//]: # (- **功能**：截取指定网页的长屏截图并保存到文件。)

[//]: # (- **参数**：)

[//]: # (    - `url` &#40;str&#41;：需要截图的网页 URL。)

[//]: # (    - `filename` &#40;str&#41;：截图保存的文件名。)

[//]: # (    - `kwargs` &#40;dict&#41;：附加参数，包括但不限于以下键值：)

[//]: # (        - `width` &#40;int&#41;：浏览器宽度，默认为 2180。)

[//]: # (        - `height` &#40;int&#41;：浏览器高度，默认为 1280。)

[//]: # (        - `maximum` &#40;bool&#41;：是否最大化浏览器窗口，默认为 True。)

[//]: # (        - `threshold` &#40;function&#41;：阈值算法函数，默认为 `NorrisUtils.SeleniumUtils.thresholds.maximize`。)

[//]: # (- **返回值**：截图文件名 &#40;str&#41;。)

[//]: # ()
[//]: # (### `dump_page_source&#40;url, **kwargs&#41;`)

[//]: # ()
[//]: # (- **功能**：获取指定网页的源码。)

[//]: # (- **参数**：)

[//]: # (    - `url` &#40;str&#41;：访问的目标网页 URL。)

[//]: # (    - `kwargs` &#40;dict&#41;：可变关键字参数，包括但不限于以下键值：)

[//]: # (        - `width` &#40;int&#41;：浏览器宽度，默认为 2180。)

[//]: # (        - `height` &#40;int&#41;：浏览器高度，默认为 1280。)

[//]: # (        - `maximum` &#40;bool&#41;：是否最大化浏览器窗口，默认为 False。)

[//]: # (        - `threshold` &#40;function&#41;：阈值算法函数，默认为 `NorrisUtils.SeleniumUtils.thresholds.default_threshold`。)

[//]: # (        - `file_name` &#40;str&#41;：保存页面源码的文件名，默认为 None。)

[//]: # (        - `browser` &#40;Obj&#41;：浏览器对象，默认为 None。)

[//]: # (        - `close` &#40;bool&#41;：是否关闭浏览器，默认为 True。)

[//]: # (- **返回值**：页面源码 &#40;str&#41;。)

[//]: # ()
[//]: # (### `freestyle&#40;url, **kwargs&#41;`)

[//]: # ()
[//]: # (- **功能**：通用函数，用于执行具体的爬虫逻辑。)

[//]: # (- **参数**：)

[//]: # (    - `url` &#40;str&#41;：访问的目标网页 URL。)

[//]: # (    - `kwargs` &#40;dict&#41;：可变关键字参数，包括但不限于以下键值：)

[//]: # (        - `width` &#40;int&#41;：浏览器宽度，默认为 2180。)

[//]: # (        - `height` &#40;int&#41;：浏览器高度，默认为 1280。)

[//]: # (        - `maximum` &#40;bool&#41;：是否最大化浏览器窗口，默认为 False。)

[//]: # (        - `browser` &#40;Obj&#41;：浏览器对象，默认为 None。)

[//]: # (        - `close` &#40;bool&#41;：是否关闭浏览器，默认为 True。)

[//]: # (        - `spider` &#40;function&#41;：具体的爬虫逻辑，默认为 `NorrisUtils.SeleniumUtils.spiders.save_page_source`。)

[//]: # (- **返回值**：页面源码 &#40;str&#41;。)

[//]: # ()
[//]: # (## 示例代码)

[//]: # ()
[//]: # (### 截图示例)

[//]: # ()
[//]: # (``` )

[//]: # (dump_page_capture&#40;'https://www.example.com', 'example.png', width=1920, height=1080&#41;)

[//]: # (```)

[//]: # ()
[//]: # (### 获取源码示例)

[//]: # ()
[//]: # (``` )

[//]: # (source_code = dump_page_source&#40;'https://www.example.com', file_name='example.html', width=1920, height=1080&#41;)

[//]: # (```)

[//]: # ()
[//]: # (## 注意事项)

[//]: # ()
[//]: # (- 确保安装了相应的浏览器驱动程序，并将其路径添加到环境变量中。)

[//]: # (- 在无头模式下运行时，确保服务器支持无头浏览器操作。)

[//]: # (- 异常处理已加入，确保程序在遇到错误时能够正常退出。)

[//]: # ()
[//]: # ()
[//]: # ()
