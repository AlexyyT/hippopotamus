import requests
from bs4 import *


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

#URL = "https://www.amazon.fr/s?k=ecouteurs&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3021BOLC4Q25U&sprefix=ecouteurs%2Caps%2C112&ref=nb_sb_noss_1"
#URL = "https://www.amazon.fr/s?k=baladeurs&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2G5YQTRUS78Y5&sprefix=baladeurs%2Caps%2C102&ref=nb_sb_noss_1"

def HTMLparser(URL):
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, 'lxml')
    return soup

#soup = HTMLparser(URL)

def itemSelectionParser(soup):
    soup_list = soup.body.find_all('div', {'class': 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'})

    dict = {'Titre': [],
        'Note Moyenne': [],
        'Avis clients': [],
        'Prix': [],
        'Devise': [],
        'Url': [],
        'Position': [],
        'Page': []
    }

    pos = 1
    for i in soup_list:
        dict['Titre'].append(i.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).text)
        dict['Note Moyenne'].append(i.find('span', {'class': 'a-icon-alt'}).getText())
        dict['Avis clients'].append(i.find('span', {'class': 'a-size-base s-underline-text'}).getText())
        dict['Prix'].append(i.find('span', {'class': 'a-price-whole'}).getText())
        dict['Devise'].append(i.find('span', {'class': 'a-price-symbol'}).getText())
        dict['Url'].append('www.amazon.fr' + i.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href'])
        dict['Position'].append(pos)
        dict['Page'].append(1)
        pos = pos + 1
        i =+ 1

    return dict

# product_list = itemSelectionParser(soup)

# index = 47
# print(product_list['Titre'][index])
# print(product_list['Note Moyenne'][index])
# print(product_list['Avis clients'][index])
# print(product_list['Prix'][index])
# print(product_list['Devise'][index])
# print(product_list['Url'][index])
# print(product_list['Position'][index])
# print(product_list['Page'][index])

def itemReviewsParser(soup, dict):
    reviews = soup.body.find_all('div', {'class': 'a-section review aok-relative'})


    for i in reviews:
        dict['Titre'].append(i.find('a', {
            'class': 'a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'}).getText())
        dict['Note'].append(i.find('span', {'class': 'a-icon-alt'}).getText())
        dict['Date'].append(i.find('span', {'class': 'a-size-base a-color-secondary review-date'}).getText())
        dict['Spec'].append(i.find('a', {'class': 'a-size-mini a-link-normal a-color-secondary'}).getText())
        dict['Achat'].append(i.find('span', {'class': 'a-size-mini a-color-state a-text-bold'}).getText())
        dict['Verbatim'].append(i.find('span', {'class': 'a-size-base review-text review-text-content'}).getText())
        i = + 1

    return dict

URL = 'https://www.amazon.fr/Blukar-Intra-Auriculaires-Oreillettes-Ergonomique-Smartphones/product-reviews/B07YCDW6JP/ref=cm_cr_getr_d_paging_btm_next_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
# print(URL)
#
# soup = HTMLparser(URL)
#
# reviews_list = itemReviewsParser(soup)
#
# index = 2
# print(reviews_list['Titre'][index])
# print(reviews_list['Note'][index])
# print(reviews_list['Date'][index])
# print(reviews_list['Spec'][index])
# print(reviews_list['Achat'][index])
# print(reviews_list['Verbatim'][index])
#
# #Parse page 2 reviews
# URL = 'https://amazon.fr/' + soup.body.find('li',{'class': 'a-last'}).find('a')['href']
# print(URL)
#
#
# soup = HTMLparser(URL)
# reviews_list = itemReviewsParser(soup)
#
# index = 2
# print(reviews_list['Titre'][index])
# print(reviews_list['Note'][index])
# print(reviews_list['Date'][index])
# print(reviews_list['Spec'][index])
# print(reviews_list['Achat'][index])
# print(reviews_list['Verbatim'][index])

def main(URL):

    dict = {'Titre': [],
        'Note': [],
        'Date': [],
        'Spec': [],
        'Achat': [],
        'Verbatim': []
    }

    while URL:
        soup = HTMLparser(URL)
        reviews_list = itemReviewsParser(soup, dict)

        # index = 2
        # print(reviews_list['Titre'][index])
        # print(reviews_list['Note'][index])
        # print(reviews_list['Date'][index])
        # print(reviews_list['Spec'][index])
        # print(reviews_list['Achat'][index])
        # print(reviews_list['Verbatim'][index])

        URL = 'https://amazon.fr/' + soup.body.find('li',{'class': 'a-last'}).find('a')['href']

        print(reviews_list)
    return reviews_list

total_avis = main(URL)