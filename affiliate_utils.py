from urllib.parse import quote
import re

# Replace with your actual affiliate IDs
amazon_tag = "tag=saikat-21"
flipkart_tag = "affid=saikatid"
meesho_tag = "utm_source=saikatmeesho"
myntra_tag = "abc123"  # EarnKaro kid

def convert_amazon_link(link):
    if "tag=" not in link:
        return link + ("&" if "?" in link else "?") + amazon_tag
    return link

def convert_flipkart_link(link):
    if "affid=" not in link:
        return link + ("&" if "?" in link else "?") + flipkart_tag
    return link

def convert_meesho_link(link):
    if "utm_source=" not in link:
        return link + ("&" if "?" in link else "?") + meesho_tag
    return link

def convert_myntra_link(link):
    encoded_url = quote(link, safe='')
    return f"https://ekaro.in/en?kid={myntra_tag}&murl={encoded_url}"

def convert_affiliate_link(link):
    if "amazon." in link:
        return convert_amazon_link(link)
    elif "flipkart." in link:
        return convert_flipkart_link(link)
    elif "meesho." in link:
        return convert_meesho_link(link)
    elif "myntra." in link:
        return convert_myntra_link(link)
    return link

def extract_links(text):
    return re.findall(r'https?://\\S+', text)
