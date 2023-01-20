import scrapy


def is_valid_paragraph(paragraph):
    paragraph = paragraph.strip()
    paragraph = paragraph.replace(' ', ' ')
    paragraph = paragraph.replace('​', ' ')

    if ' ' not in paragraph:
        return None

    if paragraph[-1].isalnum():
        return None

    if paragraph[-1] == '”':
        return None

    if paragraph[0] == '"' and paragraph[-1] == '"':
        paragraph = paragraph[1:-1]

    return paragraph

"""
Spring 3.2.0
    allowed_domains = ['docs.spring.io']
    start_urls = ['https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/']
    base_url = 'https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/'
     
AI21 Labs
    allowed_domains = ['docs.ai21.com']
    start_urls = ['https://docs.ai21.com/docs/overview']
    base_url = 'https://docs.ai21.com'
    
    allowed_domains = ['studio.ai21.com']
    start_urls = ['https://studio.ai21.com/']
    base_url = 'https://studio.ai21.com'


LabLab.ai
    allowed_domains = ['lablab.ai']
    start_urls = ['https://lablab.ai']
    base_url = 'https://lablab.ai'
"""

class TextSpider(scrapy.Spider):
    name = "text"
    allowed_domains = ['lablab.ai']
    start_urls = ['https://lablab.ai']
    base_url = 'https://lablab.ai'

    def parse(self, response):
        for paragraph in response.css('p').xpath('normalize-space()').getall():
            paragraph = is_valid_paragraph(paragraph)
            if paragraph:
                yield {'paragraphs': paragraph, 'link': response.request.url}

        for link in response.xpath('.//@href').getall():
            if not link.startswith("https"):
                link = self.base_url + link
            yield response.follow(link, self.parse)

