from utils import read_script
from bs4 import BeautifulSoup
import urllib
from parse_html import find_class_id_attribute

urls, contents = read_script()

r = urllib.urlopen(urls[0]).read()
soup = BeautifulSoup(r, "html.parser")

classes, ids = find_class_id_attribute(soup)