import requests

def hit_scraper_endpoint():
    url = '/scrape-superfund/'
    response = requests.get(url)

    if response.status_code == 200:
        print("Hit endpoint")
    else:
        print(f"error hitting endpoint {response.status_code}")

if __name__ == "__main__":
    hit_scraper_endpoint()