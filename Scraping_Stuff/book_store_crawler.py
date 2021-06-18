import requests
import re

def get_page_content(url):
	r = requests.get(url)
	html_text = r.text
	html_text = re.sub("\s+", " ", html_text)
	return html_text

def extract_product_links(content):
	product_url_regex = re.compile(r'<article class="product_pod">.*?<h3>.*?<a href="(.*?)"')
	result = re.findall(product_url_regex, content)
	links =["http://books.toscrape.com/catalogue/" + x for x in result]
	return links

def get_all_product_links():
	all_product_urls = []

	for page in range(1, 51):
		url = "http://books.toscrape.com/catalogue/page-{}.html".format(page)
		content = get_page_content(url)
		links = extract_product_links(content)
		all_product_urls.extend(links)

	return all_product_urls

def get_product_details(url):
	content = get_page_content(url)
	title_regex = re.compile(r'<h1>(.*?)</h1>')
	result = re.findall(title_regex, content)
	name = result[0]
	product_details_regrex = re.compile(r'<table class="table table-striped">(.*?)</table>')
	result = re.findall(product_details_regrex, content)
	product_details = result[0]

	upc_regrex = re.compile(r'<th>UPC</th>\s*<td>(.*?)</td>')
	result = re.findall(upc_regrex, product_details)
	upc = result[0]

	price_regrex = re.compile(r'<th>Price \(incl. tax\)</th>\s*<td>(.*?)</td>')
	result = re.findall(price_regrex, product_details)
	price = result[0]

	print(product_details, upc, price)

if __name__ == '__main__':
	all_product_urls = get_all_product_links()
	for url in all_product_urls:
		try:
			get_product_details(url)
		except:
			print("Couldn't scraped ", url)
	# print(all_product_urls)
	# print(links)