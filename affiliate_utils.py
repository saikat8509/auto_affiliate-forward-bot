import re

# Replace these with your affiliate tags
AMAZON_TAG = "your-amazon-tag"
FLIPKART_TAG = "your-flipkart-tag"

def convert_to_affiliate_link(text):
    if "amazon.in" in text:
        return convert_amazon_link(text)
    elif "flipkart.com" in text:
        return convert_flipkart_link(text)
    return text

def convert_amazon_link(url):
    pattern = r"(https://www\.amazon\.in[^\s]+)"
    match = re.search(pattern, url)
    if not match:
        return url
    clean_url = match.group(1).split("?")[0]
    return f"{clean_url}?tag={AMAZON_TAG}"

def convert_flipkart_link(url):
    pattern = r"(https://www\.flipkart\.com[^\s]+)"
    match = re.search(pattern, url)
    if not match:
        return url
    return f"{match.group(1)}&affid={FLIPKART_TAG}"
