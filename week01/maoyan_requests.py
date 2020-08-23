import requests
import lxml.etree
import pandas as pd

# define variable
myurl = 'https://maoyan.com/films?showType=3&sortId=1'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15'
header = {'user-agent':user_agent}
export = pd.DataFrame()

# crawl page
response = requests.get(myurl, headers=header)

# xml page text
selector = lxml.etree.HTML(response.text)

# acquire film information
film_infos = selector.xpath('*//div[@class="movie-hover-info"]')

for film_info in film_infos:
    film_name = film_info.xpath('div[1]/span/text()')[0]
    film_cat = film_info.xpath('div[2]/text()')[1].strip()
    film_releasedate = film_info.xpath('div[4]/text()')[1].strip()
    print(film_cat)
    export = export.append([[film_name, film_cat, film_releasedate]], ignore_index=True)

# export first 10 record into maoyan.csv
export.columns = ["电影名称","电影类别","上映时间"]
export.head(10).to_csv('./maoyan.csv', encoding='utf8', index=False)