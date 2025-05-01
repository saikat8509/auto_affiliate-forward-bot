import re
from config import REMOVE_KEYWORDS

def clean_text(text):
    for keyword in REMOVE_KEYWORDS:
        text = text.replace(keyword, "")
    return text.strip()

def convert_to_affiliate(text):
    # Replace placeholders with your real affiliate tags
    amazon_tag = "tag=youramazontag"
    flipkart_tag = "affid=yourflipkartid"
    meesho_tag = "utm_source=yourmesho"
    myntra_tag = "utm_source=yourmyntra"

    # Amazon
    text = re.sub(r"(https?://www\.amazon\.in/[^\s]+)", lambda m: m.group(1).split("?")[0] + "?" + amazon_tag, text)
    # Flipkart
    text = re.sub(r"(https?://www\.flipkart\.com/[^\s]+)", lambda m: m.group(1).split("?")[0] + "?" + flipkart_tag, text)
    # Meesho
    text = re.sub(r"(https?://meesho\.com/[^\s]+)", lambda m: m.group(1).split("?")[0] + "?" + meesho_tag, text)
    # Myntra
    text = re.sub(r"(https?://www\.myntra\.com/[^\s]+)", lambda m: m.group(1).split("?")[0] + "?" + myntra_tag, text)

    return text
