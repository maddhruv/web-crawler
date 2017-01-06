import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.amazon.in/Apple-iPhone-5s-Space-Grey/dp/B00FXLC9V4/ref=s9_simh_gw_g107_i1_r?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=0QBR9X8JNB55SYQS7R8V&pf_rd_t=36701&pf_rd_p=ada39a39-ac99-45c5-87be-1cd2d8a1ca7b&pf_rd_i=desktop")


soup = BeautifulSoup(r.content)

title_text = soup.select("div > #title")

print(title_text[0])
