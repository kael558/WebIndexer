import scrapy


def is_valid_paragraph(paragraph):
    paragraph = paragraph.strip()
    paragraph = paragraph.replace(' ', ' ')
    if ' ' not in paragraph:
        return None

    if paragraph[-1].isalnum():
        return None

    if paragraph[-1] == '”':
        return None

    if paragraph[0] == '"' and paragraph[-1] == '"':
        paragraph = paragraph[1:-1]

    return paragraph


class TextSpider(scrapy.Spider):
    name = "text"
    allowed_domains = ['docs.spring.io']
    start_urls = ['https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/']
    base_url = 'https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/'

    def parse(self, response):
        for paragraph in response.css('p').xpath('normalize-space()').getall():
            paragraph = is_valid_paragraph(paragraph)
            if paragraph:
                yield {'paragraphs': paragraph, 'link': response.request.url}

        for link in response.xpath('.//@href').getall():
            # print("follow link: " + link)
            yield response.follow(self.base_url + link, self.parse)

        '''    yield {
                "link": self.base_url + link.xpath('.//@href').get()
            }

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
        '''
