import time
from pathlib import Path
from urllib.parse import urlparse

from selenium.webdriver.remote.webdriver import WebDriver
from webdrivermanager_cn import ChromeDriverManager, GeckodriverManager

from P_EO.common.config import Default
from P_EO.common.log import LogMixin
from P_EO.common.time_ import get_time
from P_EO.core.javascript import JavaScript
from P_EO.public_variables.public_variables import Public


class Driver(LogMixin):
    def __init__(self, driver: WebDriver):
        self.__d = driver

    @property
    def web_driver(self):
        """
        返回 WebDriver 对象
        :return:
        """
        return self.__d

    def set_implicitly_wait(self, timeout: float = Default.IMPLICITLY_WAIT):
        """
        设置隐式等待时间
        :param timeout:
        :return:
        """
        self.web_driver.implicitly_wait(time_to_wait=timeout)
        self.log.debug(f'隐式等待设定: {timeout} s')

    @property
    def get_implicitly_wait(self):
        """
        获取当前隐式等待设定时间
        """
        return self.web_driver.timeouts.implicit_wait

    @property
    def get_cur_window_size(self):
        """
        获取当前网页窗口大小
        :return:
        """
        return self.web_driver.get_window_size()

    def set_cur_window_size(self, width=0, height=0):
        """
        设定当前窗口大小，如果窗口大小为0，则默认最大化打开
        :param width:
        :param height:
        :return:
        """
        if width > 0 and height > 0:
            self.web_driver.set_window_size(width=width, height=height)
            self.log.debug(f'设定浏览器窗口: {width} {height}')
        else:
            self.web_driver.maximize_window()
            self.log.debug('浏览器窗口最大化')
        self.log.info(f'当前窗口大小: {self.get_cur_window_size}')

    @property
    def get_cur_url(self):
        """
        获取当前url
        :return:
        """
        return self.web_driver.current_url

    @property
    def get_cur_url_parser(self):
        """
        url解析器
        <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
        :return:
        """
        return urlparse(self.get_cur_url)

    def get(self, url):
        """
        打开新url
        :param url:
        :return:
        """
        self.web_driver.get(url)
        self.log.debug(f'访问url: {url}')

    def switch_frame_to_default(self):
        """
        切换到最外层 frame
        :return:
        """
        self.web_driver.switch_to.default_content()

    @property
    def js(self):
        return JavaScript(driver=self.web_driver)

    def open_new_window(self, url=''):
        """
        打开一个新tab，如果url有值，则打开指定url
        :param url:
        :return:
        """
        self.js.open_new_tab(url)
        self.log.debug(f'浏览器打开新tab: {url}')

    def goto_new_route(self, route=''):
        """
        切换到同host下新route
        :param route:
        :return:
        """
        self.js.goto_new_route(route)
        self.log.debug(f'浏览器切换路由: {route}')

    @property
    def title(self):
        """
        获取title
        :return:
        """
        return self.web_driver.title

    def back(self):
        """
        返回
        :return:
        """
        self.web_driver.back()

    def forward(self):
        """
        前进
        :return:
        """
        self.web_driver.forward()

    def refresh(self, wait=Default.REFRESH_WAIT):
        """
        刷新
        :param wait: 默认刷新后暂停1s
        :return:
        """
        self.web_driver.refresh()
        time.sleep(wait)

    def screenshots(self, file_path=None):
        """
        截图
        :param file_path: 截图完整路径
        :return:
        """
        if not file_path:
            file_path = Default.WEB_PAGE_PATH
            file_path.mkdir(parents=True, exist_ok=True)
            img_name = f'{get_time()}_{self.title}.png'
            file_path = Path(file_path).joinpath(img_name)

        self.web_driver.save_screenshot(filename=file_path)
        self.log.info(f'浏览器截图: {file_path}')
        return file_path

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.web_driver.quit()
        self.log.info('关闭浏览器')

    @property
    def alert(self):
        """
        切换到 Alert 窗口
        :return:
        """
        return self.web_driver.switch_to.alert

    @property
    def error_img(self) -> str:
        return Public.last_error_image

    @property
    def cookie(self):
        """
        返回 Cookie 对象
        :return:
        """
        return Cookie(driver=self.web_driver)

    @property
    def window(self):
        """
        返回 window 对象
        :return:
        """
        return Window(driver=self.web_driver)


class Cookie:
    def __init__(self, driver: WebDriver):
        self.__d = driver

    @property
    def cookies(self):
        return self.__d.get_cookies()

    def get_cookie(self, name):
        return self.__d.get_cookie(name)

    def add_cookie(self, **cookie_dict):
        self.__d.add_cookie(cookie_dict)

    def delete_cookie(self, name):
        self.__d.delete_cookie(name)

    def delete_all_cookies(self):
        self.__d.delete_all_cookies()


class Window(LogMixin):
    def __init__(self, driver: WebDriver):
        self.__d = driver

    @property
    def cur_window_handle(self):
        return self.__d.current_window_handle

    @property
    def window_handles(self):
        return self.__d.window_handles

    def switch_window(self, window_handle):
        if window_handle != self.cur_window_handle:
            self.__d.switch_to.window(window_handle)
        return self.cur_window_handle == window_handle

    def switch_window_by_index(self, index: int):
        """
        根据索引切换windows handle
        :param index: 0, 1, 2,...
        :return:
        """
        _handle = self.window_handles[index]
        self.switch_window(_handle)
        self.log.debug(f'切换到指定索引handle: {index} - {_handle}')

    def switch_to_new_window(self):
        """
        切换到最后一个window handle
        :return:
        """
        self.switch_window_by_index(-1)
        self.log.debug(f'切换到末尾handle')

    def close(self):
        """
        关闭window
        :return:
        """
        self.__d.close()
        self.log.info('关闭当前浏览器window')

    def close_alone(self):
        """
        如果当前window list不唯一，则可以关闭
        :return:
        """
        if len(self.window_handles) > 1:
            self.close()


class WebDriverManager:
    """
    下载浏览器驱动
    """

    def __init__(self, driver_path: str = None, version='latest'):
        self.__driver_path = driver_path
        self.__version = version

    @property
    def chrome(self):
        return ChromeDriverManager(path=self.__driver_path, version=self.__version).install()

    @property
    def firefox(self):
        return GeckodriverManager(path=self.__driver_path, version=self.__version).install()
