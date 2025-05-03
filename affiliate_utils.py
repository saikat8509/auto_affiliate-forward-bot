# affiliate_utils.py

from config import CUELINKS_ID

def convert_to_cuelinks(url: str) -> str:
    """
    Convert a given product URL (from Myntra, Meesho, Flipkart, Amazon) to a Cuelinks affiliate URL.
    """
    return f"https://www.cuelinks.com/out?url={url}&subid={CUELINKS_ID}"

def convert_to_flipkart_affiliate(url: str) -> str:
    """
    Convert a Flipkart product URL to a Flipkart affiliate link.
    """
    flipkart_affiliate_id = "your_flipkart_affiliate_id"  # Replace with your actual Flipkart affiliate ID
    return f"https://www.flipkart.com/affiliate/{flipkart_affiliate_id}/redirect?url={url}"

def convert_to_amazon_affiliate(url: str) -> str:
    """
    Convert an Amazon product URL to an Amazon affiliate link.
    """
    amazon_affiliate_id = "your_amazon_affiliate_id"  # Replace with your actual Amazon affiliate ID
    return f"https://www.amazon.in/dp/{url.split('/')[-1]}?tag={amazon_affiliate_id}"

def convert_link_to_affiliate(url: str) -> str:
    """
    Convert a URL from any supported platform (Amazon, Flipkart, Myntra, Meesho) to your affiliate link.
    """
    if "flipkart.com" in url:
        return convert_to_flipkart_affiliate(url)
    elif "amazon.in" in url:
        return convert_to_amazon_affiliate(url)
    elif "myntra.com" in url or "meesho.com" in url:
        return convert_to_cuelinks(url)
    else:
        return url  # Return the original URL if it's not from a supported platform
