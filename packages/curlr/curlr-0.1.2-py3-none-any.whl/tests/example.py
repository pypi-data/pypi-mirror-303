# ~/curlr/tests/example.py
from curlr import CURL

command = """
curl 'https://pypi.org/project/curlr/0.1.0/' \
-X 'GET' \
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
-H 'Sec-Fetch-Site: none' \
-H 'Cookie: _ga=GA1.2.5527140.1729286779; _ga_B0F3Y2XW9M=GS1.1.1729286779.1.1.1729286943.0.0.0; _ga_RW7D75DF8V=GS1.1.1729286779.1.1.1729286943.0.0.0; _gid=GA1.2.918407260.1729286780; session_id=76881-ofCHC0ptnY7EC1d3Tettpil8HmxUfRUiwxYjM.ZxLTHw.NlX0Xmp9lzKXtPrAYYoRkwBIDpuONIz0qLMBg1_z9soSK-0UX49XLA6n-JST93x_dVasC0CTQ9USuh8cgL7qPQ; _gat_gtag_UA_55961911_1=1' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Sec-Fetch-Mode: navigate' \
-H 'Host: pypi.org' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15' \
-H 'Accept-Language: en-US,en;q=0.9' \
-H 'Sec-Fetch-Dest: document' \
-H 'Connection: keep-alive'
"""

curl = CURL(command)

print(curl.headers)
print(curl.cookies)
print(curl.url)
print(curl.method)
print(curl.params)
print(curl.data)
print(curl.execute().text)
request = curl.request()
