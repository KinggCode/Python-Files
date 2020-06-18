import requests
import time


def get_single_site(url):
    with requests.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def get_all_sites(sites):
    for url in sites:
        get_single_site(url, session)


if __name__ == "__main__":
    start_time = time.time()
    urls =[
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.twitter.com"
        ]

    get_all_sites(urls)
    end_time = time.time() - start_time

    print(f"Downoad {len(sites)} from {end_time} seconds")
