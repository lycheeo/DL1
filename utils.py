import requests
from bs4 import BeautifulSoup

class DBLPScraper:
    def __init__(self):
        self.base_url = 'https://dblp.org'

    def get_author_articles(self,author_name):
        # 构建作者页面的URL
        search_url = f'https://dblp.org/search?q={author_name}'

        response = requests.get(search_url)

        soup = BeautifulSoup(response.text, 'lxml')

        sec= soup.find_all('ul', class_='result-list')

        if sec:

            author_url = sec[0].a.get("href")

            # 发送HTTP请求，获取页面内容
            response = requests.get(author_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')

                # 在作者页面中查找文章列表
                articles = soup.find_all('li', {'class': ['entry inproceedings toc', 'entry article toc'] })

                # 提取文章标题
                article_titles = [article.find('span', class_='title').text for article in articles]

                return article_titles
            else:
                print(f"Failed to fetch data for author: {author_name}")
                return []
