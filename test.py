from task.utils.selector.phantomjs_selector import *

self = PhantomJSSelector()
url = "https://search.smzdm.com/?c=home&s=招行活动合集+完成任务抽现金红包&order=time&mall_id=2297&cate_id=1523&v=b"
html = self.get_html(url, headers=None)
res = self.xpath_parse(html, '//*[@id="feed-main-list"]/li[1]/div/div[2]/h5/a[1]/text()')