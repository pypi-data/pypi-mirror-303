from configparser import ConfigParser
import sys
import platform


class IniLoader:
    def __init__(self, **kwargs):
        kwargs.setdefault("path", "")
        kwargs.setdefault("paths", {})
        kwargs.setdefault("logfunc", print)
        path = kwargs["path"]
        paths = kwargs["paths"]
        logfunc = kwargs["logfunc"]

        if path is None or path == "":
            if paths is not None and len(paths) > 0:
                if platform.system().lower() == 'windows':
                    try:
                        path = paths["windows"]
                    except:
                        path = paths["Windows"]
                elif platform.system().lower() == 'linux':
                    try:
                        path = paths["linux"]
                    except:
                        path = paths["Linux"]
                elif platform.system().lower() == 'darwin':
                    try:
                        path = paths["mac"]
                    except:
                        path = paths["Mac"]

        if path is None or path == "":
            raise Exception("请指定ini配置文件的位置")

        # 获取调用者信息
        caller_frame = sys._getframe(1)  # 1 表示获取调用当前方法的上一级帧
        caller_module = caller_frame.f_code.co_filename  # 文件路径
        caller_class = caller_frame.f_locals.get("__class__", None).__name__ if caller_frame.f_locals.get("__class__",
                                                                                                          None) else None  # 类名
        caller_function = caller_frame.f_code.co_name  # 方法名

        if logfunc is not None:
            logfunc(f"{caller_module} 的 {caller_class}正在为您加载位置位于：{path} 的ini配置文件...")
        try:
            self.parser = ConfigParser()
            self.parser.read(path)
        except:
            if logfunc is not None:
                logfunc(f"{caller_module} 的 {caller_function}加载位置位于：{path} 的ini配置文件失败")
            pass

    def get_config(self, section, option, default=None):
        return self.parser.get(section, option, fallback=default)
