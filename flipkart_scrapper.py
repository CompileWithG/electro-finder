import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Configure headers to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

def get_details(input_string):
    try:
        input_string1 = input_string
        link1 = f"https://www.flipkart.com/search?q={input_string1}"
        
        # Use headers in the request
        response = requests.get(link1, headers=HEADERS)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        soup = bs(response.text, 'html.parser')
        elements = soup.find_all("div", class_="cPHDOP col-12-12")
        
        product_list = []
        
        for element in elements:
            product_details = []
            try:
                # Navigation logic remains the same
                inner_div = element.find("div", class_="_75nlfW")
                if inner_div:
                    data_div = inner_div.find("div", attrs={"data-id": True})
                    if data_div:
                        link_div = data_div.find("div", class_="tUxRFH")
                        if link_div:
                            product_link = link_div.find("a", class_="CGtC98")
                            if product_link and 'href' in product_link.attrs:
                                # Product URL
                                full_url = f"https://www.flipkart.com/{product_link['href']}"
                                product_details.append(full_url)
                                
                                # Product Image
                                image_container = product_link.find("div", class_="Otbq5D")
                                if image_container:
                                    image_div = image_container.find("div", class_="_4WELSP")
                                    if image_div:
                                        img_tag = image_div.find("img", class_="DByuf4")
                                        if img_tag and 'src' in img_tag.attrs:
                                            product_details.append(img_tag['src'])
                                
                                # Product Info
                                info_container = product_link.find("div", class_="yKfJKb row")
                                if info_container:
                                    # Title
                                    text_div = info_container.find("div", class_="col col-7-12")
                                    if text_div:
                                        title = text_div.find("div", class_="KzDlHZ")
                                        if title:
                                            product_details.append(title.text.strip())
                                        
                                        # Features
                                        features_div = text_div.find("div", class_="_6NESgJ")
                                        if features_div:
                                            features_list = []
                                            features_ul = features_div.find("ul", class_="G4BRas")
                                            if features_ul:
                                                for li in features_ul.find_all("li", class_="J+igdf"):
                                                    features_list.append(li.text.strip())
                                            product_details.append(features_list)
                                    
                                    # Price
                                    price_div = info_container.find("div", class_="col col-5-12 BfVC2z")
                                    if price_div:
                                        price_container = price_div.find("div", class_="cN1yYO")
                                        if price_container:
                                            price_wrapper = price_container.find("div", class_="hl05eU")
                                            if price_wrapper:
                                                price_element = price_wrapper.find("div", class_="Nx9bqj _4b5DiR")
                                                if price_element:
                                                    product_details.append(price_element.text.strip())
                                
                                
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
        return {
            "status": "success",
            "count": len(results),
            "products": results
        }
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)