from time import sleep
import requests
from bs4 import BeautifulSoup
import os

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }

    # 创建题库目录
    if not os.path.exists('./题库/'):
        os.makedirs('./题库/')

    for i in range(1, 195):
        # 1.指定url
        url = f'https://www.luogu.com.cn/problem/list?orderBy=name&order=asc&page={i}'
        # 2.发起请求，获取结果
        response = requests.get(url=url, headers=headers).content
        # 3.解析数据
        soup = BeautifulSoup(response, 'lxml')
        t_url_len = len(soup.find_all('a'))
        for t in range(0, t_url_len - 2):
            sleep(1)
            t_url = 'https://www.luogu.com.cn/problem/' + soup.select('a')[t]['href']
            # print(t_url)
            content = requests.get(url=t_url, headers=headers).content
            content_soup = BeautifulSoup(content, 'lxml')
            # get_text（）会移除一些运算符
            t_content = content_soup.get_text()
            # print(t_content)
            # 持久化存储
            fp = open(f'./题库/{soup.select("a")[t]["href"]}.md', 'w', encoding='utf-8')
            fp.write(t_content)
            fp.close()  # 确保文件被正确关闭
            print(f'{soup.select("a")[t]["href"]}爬取成功!')
            t += 1
        i += 1
        # print(t_url_len)