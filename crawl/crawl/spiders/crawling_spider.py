from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawl_scrape.models import Question, Answer


# from my_core.models import ScrapedQuestion, ScrapedAnswer


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

        # getting all the questions url:
        questions_url = response.css('div.q_url a::attr(href)::text').getall()
        # questions_url = response.css('a.btn::attr(href)').getall()

        yield {
            'questions_url': questions_url
        }

        for question in questions:
            relative_ulr = question.css('a.btn::attr(href)').get()
            print(relative_ulr)

            question_url = "http://localhost:8000/" + relative_ulr
            print(f"Following URL: {question_url}")

            if question_url:
                yield response.follow(question_url,
                                      callback=self.parse_question_page,
                                      # meta={'questions_url' : questions_url}      # meta for passing some attributes between 2 methods whenever we send a request
                                      )

    def parse_question_page(self, response):

        question_title = response.css('.title h2::text').get()
        question_date = response.css('.date::text').get().strip()
        question_text = response.css('.text p::text').get().strip()
        question_url = response.request.url.replace("http://localhost:8000/", "")
        # question_url = response.meta[]

        question = {'question_title': question_title,
                    'question_date': question_date,
                    'question_text': question_text,
                    'question_url': question_url,
                    # 'question_url' : question_url ,
                    }

        # answerText = response.css('.answer')

        answer_content = response.css('.a_text::text').getall()
        answer_date = response.css('.a_date::text').getall()
        answer_lawyer = response.css('.a_lawyer::text').getall()
        answer_rate = response.css('div.a_rating h4::text').getall()

        for i in range(len(answer_content)):
            answer_content[i] = answer_content[i].strip()
            answer_date[i] = answer_date[i].strip()
            answer_lawyer[i] = answer_lawyer[i].strip()
            answer_rate[i] = answer_rate[i].strip()

        answers = []
        for i in range(len(answer_content)):
            answer = {
                'answer_content': answer_content[i].strip() if i < len(answer_content) else None,
                'answer_date': answer_date[i].strip() if i < len(answer_date) else None,
                'answer_lawyer': answer_lawyer[i].strip() if i < len(answer_lawyer) else None,
                'answer_rating': answer_rate[i].strip() if i < len(answer_rate) else None,
            }
            answers.append(answer)

        yield {
            'question': question,
            'answers': answers
        }

        scraped_answer = {
            'answer_content': answer_content,
            'answer_date': answer_date,
            'answer_lawyer': answer_lawyer,
            'answer_rate': answer_rate,
        }

        # for answer in answerText:
        #
        #     scraped_answer = {
        #         'answer_content' : answer.css('.a_text::text').getall()  ,
        #         'answer_date' : answer.css('.a_date::text').getall()
        #     }
        # answer_content = answer.css('.a_text::text').get(default='').strip()
        # answer_date = answer.css('.a_date::text').get(default='').strip()

        # answers = {
        #     'answer_content' : answer_content   ,
        #     'answer_date' : answer_date ,
        # }

        scraped_data = {
            'question': question,
            'answers': scraped_answer,
        }

        # Write to JSON file
        # with open('output.json', 'a') as f:
        #     json.dump(scraped_data, f, indent=4)
        #     f.write(",\n")
        #
        # yield scraped_data

        ###############################################################################################################

        # yield {
        #     'question' : question ,
        #     'answers' : scraped_answer2 ,
        # }

        # yield {
        #     'questions_url' : response.meta['questions_url']
        # }

        # yield {
        #     'title' : response.css('.title h2::text').get()   ,
        #     'question_date' : response.css('.date::text').get().strip()    ,
        #     'question_text' : response.css('.text p::text').get().strip()     ,
        #
        #     'answer_text': response.css('.a_text::text').get().strip() if response.css('.a_text::text').get() else None  ,
        #     'answer_date'   : response.css('.a_date::text').get().strip() if response.css('.a_date::text').get() else None    ,
        #     'answer_lawyer' : response.css('.a_lawyer::text').get().strip() if response.css('.a_lawyer::text').get() else None   ,
        # }

    # rules = (
    #     Rule(LinkExtractor(allow=r"user/firstPage")),
    #
    # )
