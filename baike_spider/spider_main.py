#spider_main
from baike_spider import url_manager, html_downloader, html_outputer
from lxml.html import html_parser

class SpiderMain(object):
    
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader().HtmlDownloader()
        self.parser = html_parser().HtmlParser()
        self.outputer = html_outputer().HtmlOutput()
        
    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            count = 1
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'%(count,new_url)
                html_cont = self.downloader.download(new_url)
            
                new_urls, new_data = self.parser.parser(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
            
                if count == 100:
                    break
                count = count + 1
            except:
                print 'craw failure'
        
        self.outputer.output_html()
    



if __name__=="___main___":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)