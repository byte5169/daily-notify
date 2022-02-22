import requests
from bs4 import BeautifulSoup


def _convert_string_rate_list_to_floats(rate_list):
    """
    Convert a list of strings to a list of floats

    :param rate_list: a list of strings, each of which is a rate
    :return: A list of floats.
    """
    _rate_list = []
    for rate in rate_list:
        _rate_list.append(float(rate.strip().replace(",", ".").replace("\n", "")))
    return _rate_list


def _calc_exchange_rate_change(yesterday_rate, today_rate):
    """
    Calculate the exchange rate change between yesterday and today

    :param yesterday_rate: The exchange rate yesterday
    :param today_rate: The current exchange rate
    :return: A string of the exchange rate change.
    """
    rate = round((100 - (yesterday_rate / today_rate * 100)), 2)
    if rate >= 0:
        return "↑" + str(rate) + "%"
    return "↓" + str(abs(rate)) + "%"


def get_exchange_rates(url):
    """
    Given a url, return a dictionary of exchange rates for EUR, USD, and RUB

    :param url: The URL of the page you want to scrape
    :return: A dictionary with three keys: EUR, USD, and RUB.
    Each key has a value of a list of two floats.
    """

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    exchange_rates_block = soup.find(id="p4").find_all("td")

    results = {
        "EUR": _convert_string_rate_list_to_floats(
            [exchange_rates_block[1].text, exchange_rates_block[2].text]
        ),
        "USD": _convert_string_rate_list_to_floats(
            [exchange_rates_block[4].text, exchange_rates_block[5].text]
        ),
        "RUB": _convert_string_rate_list_to_floats(
            [exchange_rates_block[7].text, exchange_rates_block[8].text]
        ),
    }

    exchange_string = (
        f"""EUR: {results.get("EUR")[1]} {_calc_exchange_rate_change(yesterday_rate=results.get("EUR")[0], today_rate=results.get("EUR")[1])}\n"""
        f"""USD: {results.get("USD")[1]} {_calc_exchange_rate_change(yesterday_rate=results.get("USD")[0], today_rate=results.get("USD")[1])}\n"""
        f"""RUB: {results.get("RUB")[1]} {_calc_exchange_rate_change(yesterday_rate=results.get("RUB")[0], today_rate=results.get("RUB")[1])}\n"""
    )

    return exchange_string
