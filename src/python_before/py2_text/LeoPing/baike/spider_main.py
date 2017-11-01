# coding=utf-8
from baike import url_manager, html_downloader, html_parser, html_outputer


class SpiderMian(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)  # 入口URL
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()  # 获取待爬取ＵＲＬ
            html_cont = self.downloader.download(new_url)  # 下载这个URL，保存起来
            new_urls, new_data = self.parser.parse(
                new_url, html_cont)  # 　解析URL，获得新的URL和新的数据
            self.urls.add_new_urls(new_urls)  # 新URL添加进URL管理器
            self.outputer.collect_data(new_data)  # 收集数据


if __name__ == "__main__":
    root_url = "https://baike_spider.baidu.com/view/21087"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
