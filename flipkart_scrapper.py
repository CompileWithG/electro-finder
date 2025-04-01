import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify
from flask_cors import CORS
import urllib3
import random
import time

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Expanded set of user agents to rotate through
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
]

def get_random_headers():
    # Generate random headers for each request
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.google.com/',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache'
    }

def get_proxy():
    # You can implement proxy rotation here if needed
    # For now, returning None which means no proxy
    return None

def get_details(input_string):
    try:
        input_string1 = input_string
        link1 = f"https://www.flipkart.com/search?q={input_string1}"
        
        # Add random delay to mimic human behavior
        time.sleep(random.uniform(1, 3))
        
        # Get random headers and proxy for this request
        headers = get_random_headers()
        proxy = get_proxy()
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        
        # Make request with improved parameters
        session = requests.Session()
        response = session.get(
            link1, 
            headers=headers, 
            verify=False,
            proxies=proxies,
            timeout=15,
            allow_redirects=True
        )
        
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Check for empty response or redirects to captcha/login pages
        if len(response.text) < 1000 or "captcha" in response.text.lower() or "access denied" in response.text.lower():
            raise Exception("Received blocked response from Flipkart")
        
        soup = bs(response.text, 'html.parser')
        elements = soup.find_all("div", class_="cPHDOP col-12-12")
        
        # If no elements are found, try alternative selectors (Flipkart may change their HTML structure)
        if not elements:
            elements = soup.find_all("div", class_="_1AtVbE col-12-12")
        
        product_list = []
        
        for element in elements:
            product_details = []
            try:
                # Flexible navigation logic with multiple fallbacks
                # Try the original selectors
                inner_div = element.find("div", class_="_75nlfW") or element.find("div", class_="_1xHGtK _373qXS")
                
                if inner_div:
                    data_div = inner_div.find("div", attrs={"data-id": True}) or inner_div
                    
                    if data_div:
                        link_div = data_div.find("div", class_="tUxRFH") or data_div.find("a", class_="_1fQZEK")
                        
                        # If link_div is actually an <a> tag itself
                        product_link = None
                        if link_div and link_div.name == "a":
                            product_link = link_div
                        elif link_div:
                            product_link = link_div.find("a", class_="CGtC98") or link_div.find("a")
                            
                        if product_link and 'href' in product_link.attrs:
                            # Product URL
                            full_url = f"https://www.flipkart.com{product_link['href']}"
                            if not product_link['href'].startswith('/'):
                                full_url = product_link['href']  # Already a full URL
                            product_details.append(full_url)
                            
                            # Product Image - try multiple possible selectors
                            img_tag = None
                            for img_class in ["DByuf4", "_396cs4", "_2r_T1I"]:
                                img_tag = product_link.find("img", class_=img_class)
                                if img_tag and 'src' in img_tag.attrs:
                                    product_details.append(img_tag['src'])
                                    break
                            
                            # If no image found, add placeholder
                            if len(product_details) == 1:
                                product_details.append("No image available")
                            
                            # Product Info - try multiple possible layouts
                            info_container = product_link.find("div", class_="yKfJKb row") or product_link.find("div", class_="_3pLy-c row") or product_link
                            
                            if info_container:
                                # Title - try multiple possible selectors
                                title = None
                                for title_class in ["KzDlHZ", "_4rR01T", "s1Q9rs"]:
                                    title_element = info_container.find("div", class_=title_class) or info_container.find("span", class_=title_class)
                                    if title_element:
                                        title = title_element
                                        break
                                
                                if title:
                                    product_details.append(title.text.strip())
                                else:
                                    product_details.append("Unknown Product")
                                
                                # Features - try multiple possible selectors
                                features_list = []
                                features_div = info_container.find("div", class_="_6NESgJ") or info_container.find("div", class_="fMghEO")
                                
                                if features_div:
                                    features_ul = features_div.find("ul", class_="G4BRas") or features_div.find("ul")
                                    if features_ul:
                                        for li in features_ul.find_all("li"):
                                            features_list.append(li.text.strip())
                                
                                product_details.append(features_list)
                                
                                # Price - try multiple possible selectors
                                price_text = None
                                for price_class in ["Nx9bqj _4b5DiR", "_30jeq3", "_1_WHN1"]:
                                    price_element = info_container.find("div", class_=price_class) or info_container.find("span", class_=price_class)
                                    if price_element:
                                        price_text = price_element.text.strip()
                                        break
                                
                                if price_text:
                                    product_details.append(price_text)
                                else:
                                    product_details.append("Price not available")
                            
                            # Add product only if we have at least url, image and title
                            if len(product_details) >= 3:
                                product_list.append(product_details[:])
                                    
            except Exception as e:
                print(f"Error processing product: {str(e)}")
                continue
                
        return product_list
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data from Flipkart: {str(e)}")
    except Exception as e:
        raise Exception(f"Error in scraping process: {str(e)}")

@app.route('/<product_name>')
def get_product_details(product_name):
    try:
        decoded_name = product_name
        results = get_details(decoded_name)
        
        if not results:
            return jsonify({
                "status": "warning",
                "message": "No products found or access was restricted",
                "count": 0,
                "products": []
            }), 200
            
        return jsonify({
            "status": "success",
            "count": len(results),
            "products": results
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)