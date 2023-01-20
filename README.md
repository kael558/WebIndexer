# Scraper
1. Navigate to the spiders directory in the scraper directory
2. Change the urls and domains in the Spider class
3. Run the command in the terminal `scrapy crawl text -O ../data/{filename}.csv`
4. Specify pages to scrape with `CLOSESPIDER_PAGECOUNT = 10` in settings.py

#scrapy crawl text -O ../data/LabLabAI.csv

## To see content of html file
1. Navigate to main directory
2. Run `scrapy shell <url>`

# To do
1. Add more websites collect data from (Konva, AI21, ZenML, LabLab)
2. Test params with https://studio.ai21.com/playground/complete
3. Make an interface 
   1. Add a select bar to choose the website
   2. Choose AI21 params (e.g. temperature, etc.)
   3. Choose context params (e.g. number of sentences, threshold)
   4. Enter question
   5. Get link to top site related to answer
   6. Get links from context construction
   7. Display answer and links
4. Compare alternatives (chatgpt, google, no-context AI21, ZenML)
5. Make email request for website
6. Presentation and demo
7. Future work

# Future work
1. Add more websites collect data from (Konva, AI21, ZenML, LabLab)
2. Finetune scraped data by splitting sentences
3. Finetune embeddings, finetune AI21 model 
4. 

