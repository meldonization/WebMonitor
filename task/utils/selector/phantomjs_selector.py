import warnings
from collections import OrderedDict

from playwright.sync_api import sync_playwright
from task.utils.selector.selector import SelectorABC as FatherSelector

warnings.filterwarnings("ignore")


class PhantomJSSelector(FatherSelector):
    def __init__(self, debug=False):
        self.debug = debug

    def get_html(self, url, headers):
        headers = headers or {}
        with sync_playwright() as p:
            browser = p.firefox.launch()
            context = browser.new_context(extra_http_headers=headers)
            page = context.new_page()
            page.goto(url)
            
            if self.debug:
                import os
                basepath = os.path.dirname(os.path.dirname(__file__))
                save_path = os.path.join(basepath, '..', 'static', 'error')
                os.makedirs(save_path, exist_ok=True)
                page.screenshot(path=os.path.join(save_path, 'screenshot.png'))

            html = page.content()
            browser.close()
        return html

    def get_by_xpath(self, url, selector_dict, headers=None):
        html = self.get_html(url, headers)

        result = OrderedDict()
        for key, xpath_ext in selector_dict.items():
            result[key] = self.xpath_parse(html, xpath_ext)

        return result

    def get_by_css(self, url, selector_dict, headers=None):
        html = self.get_html(url, headers)

        result = OrderedDict()
        for key, css_ext in selector_dict.items():
            result[key] = self.css_parse(html, css_ext)

        return result
    
    def get_by_json(self, url, selector_dict, headers=None):
        html = self.get_html(url, headers)

        result = OrderedDict()
        for key, json_ext in selector_dict.items():
            result[key] = self.json_parse(html, json_ext)

        return result
