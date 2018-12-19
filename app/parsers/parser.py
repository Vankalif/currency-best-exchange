import re
import requests

curr_code = []
curr_name = []


def parse(url: str) -> dict:
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()

    raw_data = re.findall(r'(data-currency-code="...").+(data-currency-name=".+")', response.text)
    for elem in raw_data:
        curr_code.append(re.findall(r'"(.*?)"', elem[0])[0])
        curr_name.append(re.findall(r'"(.*?)"', elem[1])[0])

    return {c_n: c_c for c_n, c_c in zip(curr_name, curr_code)}
