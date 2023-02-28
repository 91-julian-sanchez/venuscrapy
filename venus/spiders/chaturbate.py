import scrapy
import datetime

class ChaturbateSpider(scrapy.Spider):
    name = 'chaturbate'
    # allowed_domains = ['https://chaturbate.com']
    # start_urls = ['https://chaturbate.com/']
    page_counter = 1
    # custom_settings = {
    #     'FEEDS': { f'./output/extract/chaturbate-latina-{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv': { 'format': 'csv',}}
    # }
    def start_requests(self):
        urls = [
            'https://chaturbate.com/',
        ]
        
        for url in urls:
            tag = getattr(self, 'tag', None)
            if tag is not None:
                url = url + 'tag/' + tag
            yield scrapy.Request(url=url, callback=self.parse)

    def build_next_page(self, counter):
        return "?page="+str(counter)
    
    def parse(self, response): 
        for room in response.css('li.room_list_room'):
            yield {
                'model': room.css('div.title a::text').get().strip(),
                'age': room.css('span.age::text').get().strip(),
                'viewers': (room.css('span.viewers::text').get().strip()).replace(" viewers", ""),
                'time':  room.css('span.time::text').get().strip(),
                'tags':  room.css("[data-floatingnav]::text").extract(),
                'gender': room.xpath('//div[@class="age_gender_container"]/span[2]/@title').get().strip(),
                'link':  "https://chaturbate.com/"+room.css('div.title a::text').get().strip()+"/",
                'page':  self.page_counter,
            }
           
        self.page_counter = self.page_counter + 1
        next_page = self.build_next_page(self.page_counter)
        
        print("=="*10,"NEXT PAGE","=="*10)
        print('https://chaturbate.com/tag/latina/'+next_page)
                  
        if next_page is not None:
            yield response.follow(next_page, self.parse)
