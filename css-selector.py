from utils import read_script
from bs4 import BeautifulSoup
import urllib

urls, contents = read_script()

r = urllib.urlopen(urls[0]).read()
soup = BeautifulSoup(r, "html.parser")
print contents[0]
print soup
