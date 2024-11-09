from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class CrawlingSpider(CrawlSpider):
    name = 'mycrawler'
    allowed_domains = ["localhost"]
    start_urls = ["http://localhost:8000/"]

    rules = (
        # Rule to follow question links from the main page
        Rule(LinkExtractor(restrict_css='.questions a.btn'), callback='parse_question_page', follow=True),
    )


    def parse(self, response, **kwargs):
        questions = response.css('class.questions')
        print(f"Found {len(questions)} questions.")

        for question in questions:
            relative_ulr = question.css('a.btn::attr(href)').get()
            print(relative_ulr)

            question_url = "http://localhost:8000/" + relative_ulr
            print(f"Following URL: {question_url}")


            if question_url:
                yield response.follow(question_url, callback=self.parse_question_page)

    def parse_question_page(self, response):

        yield {
            'title' : response.css('.title h2::text').get()   ,
            'question_date' : response.css('.date::text').get().strip()    ,
            'question_text' : response.css('.text p::text').get().strip()     ,
            'answer_text': response.css('.a_text::text').get().strip() if response.css('.a_text::text').get() else None  ,
            'answer_date'   : response.css('.a_date::text').get().strip() if response.css('.a_date::text').get() else None    ,
            'answer_lawyer' : response.css('.a_lawyer::text').get().strip() if response.css('.a_lawyer::text').get() else None   ,
        }




    # rules = (
    #     Rule(LinkExtractor(allow=r"user/firstPage")),
    #
    # )




