# easy_pyweb/helpers.py
import json
import os
import random
from datetime import datetime, timezone
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright, Page


class WebHelper:
    args = [
        '--disable-blink-features=AutomationControlled',
        '--incognito',
        '--enable-automation',
        '--disable-infobars',
        '--disable-impl-side-painting',
    ]
    device = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.71',
        'viewport': {'width': 1280, 'height': 1024},
    }

    # 初始化浏览器，管理上下文
    def __init__(self, **kwargs):
        self.args.extend(kwargs.get('args', []))
        self.device.update(kwargs.get('device', {}))
        executable_path = kwargs.get('executable_path', 'c:\\chrome32\\')
        headless = kwargs.get('headless', False)
        self.cookie_path = kwargs.get('cookie_path', 'cookies.json')
        # initialize browser
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch_persistent_context(
            executable_path=executable_path + '\\chrome.exe',
            user_data_dir=executable_path + 'userdata',
            headless=headless,
            args=self.args,
            user_agent=self.device['user_agent'],
            viewport=self.device['viewport'],
        )
        # 加载js脚本，取当前路径下的stealth.min.js
        js_path = os.path.join(os.path.dirname(__file__), 'js/stealth.min.js')
        with open(js_path) as f:
            js = f.read()
        self.browser.add_init_script(js)

    def new_page(self, **kwargs):
        is_hide_img = kwargs.get('hide_img', False)
        page = self.browser.new_page()
        if is_hide_img:
            # 无图模式
            page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
            page.route("**/*", lambda route: route.abort()
            if route.request.resource_type == "image" else route.continue_())
        return page

    def load_cookies(self, ck_str: str, domain: str):
        if not os.path.exists(ck_str):
            return
        # 打开文件加载ck
        with open(ck_str, 'r') as f:
            if f.read().find(';') != -1:
                cookies = parse_cookie_str(ck_str, domain)
            else:
                cookies = json.load(f)
        self.browser.add_cookies(cookies)

    def save_cookies(self, ck_str: str):
        cookies = self.browser.cookies()
        with open(ck_str, 'w', encoding='utf8') as f:
            json.dump(cookies, f)

    def close(self):
        self.browser.close()
        self.playwright.stop()


class PageHelper:
    def __init__(self, page: Page):
        self.page = page
        self.setIntervalJS = 'setInterval(function(){document.querySelectorAll("[style*=block], [scrolling=no],{business}").forEach(function(ele){ele.remove();}); document.querySelectorAll("[onclick]").forEach(function(e){e.removeAttribute("onclick");});},1000);'

    def rand_wait(self, min_time=1, max_time=3):
        self.page.wait_for_timeout(random.randint(min_time, max_time) * 1000)

    def get_height(self):
        return self.page.evaluate('''() => {
                         return Math.max(
                             document.body.scrollHeight, document.body.offsetHeight,
                             document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight
                         );
                     }''')

    def slide_bottom(self, scroll_step=300, wait_time=500):
        """
        滑动到底部
        :param scroll_step: 300 每次滚动步长
        :param wait_time: 500 滚动后等待时间（单位：秒）
        :return:
        """
        # 慢慢滑动到网页底部
        current_position = 0
        total_height = self.get_height()
        while current_position < total_height:
            self.page.evaluate(f'window.scrollTo(0, {current_position});')
            current_position += scroll_step
            self.page.wait_for_timeout(wait_time)

    def clear_block(self, selector):
        """
        添加定时器清除不需要的元素
        :param selector:
        """
        self.page.evaluate(self.setIntervalJS.replace('{business}', selector))

    def get_attribute_safe(self, node, selector, inner_text=True, attribute='') -> str:
        """
        获取属性忽略异常
        :param node:操作的节点
        :param selector:选择器
        :param inner_text:bool 是否获取行内文本
        :param attribute:src，href等属性
        :return:str
        """
        try:
            rand_time = random.randint(100, 600)
            node = node.locator(selector).first
            if inner_text:
                return node.inner_text(timeout=rand_time)
            return node.get_attribute(attribute, timeout=rand_time)
        except:
            return ''

    def page_element_check(self, selector, retry_count=3):
        """
        执行元素检查，并返回值
        :param selector: js 元素节点
        :param retry_count: 重试次数
        :return: bool
        """
        result = False
        for i in range(retry_count):
            try:
                result = self.page_evaluate_script(selector)
                return result
            except Exception as e:
                print('执行js异常 %s' % e)
                # logger.error('执行js异常 %s' % e)

        return result

    def page_evaluate_script(self, selector):
        """
        执行js检查元素是否存在
        :param selector: js节点
        :return: bool
        """
        return self.page.evaluate('!!document.querySelector("{}")'.format(selector))


# 解析cookie
def parse_cookie_str(ck_str: str, domain: str):
    result = []
    for i in ck_str.split(';'):
        value = i.split('=')
        if not len(value) == 2:
            continue
        # 有效期设置今年12月31号23:59
        now = datetime.now()
        year_end = datetime(now.year, 12, 31, 23, 59, tzinfo=timezone.utc)
        expires_timestamp = year_end.timestamp()  # 转换为时间戳
        result.append({
            'name': value[0].strip(),
            'value': value[1].strip(),
            'domain': urlparse(domain).netloc,
            'path': '/',
            'expires': expires_timestamp,
            'httpOnly': False,
            'secure': True,
            'sameSite': 'Lax'
        })
    return result
