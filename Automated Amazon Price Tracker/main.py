import os
import requests
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv("./amazon_price_tracker/.env")
email = os.getenv("EMAIL")
password = os.getenv("PASS")

product_url = "https://www.amazon.com/Nintendo-SwitchTM-Neon-Blue-Joy‑ConTM-Switch/dp/B0BFJWCYTL/?_encoding=UTF8&pd_rd_w=gcr3D&content-id=amzn1.sym.41f1b87d-2e7a-4fe4-bfcc-e038cab8f79e&pf_rd_p=41f1b87d-2e7a-4fe4-bfcc-e038cab8f79e&pf_rd_r=ZSK7G524TZ8SK1X8TV5F&pd_rd_wg=gRgV7&pd_rd_r=e6e59b24-f8ba-4b99-8ee3-cb7914206394&ref_=pd_hp_d_btf_crs_zg_bs_468642&th=1"
target_price = 300

headers = {
    "User-Agent": "defined",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site":"cross-site",
    "sec-fetch-mode":"navigate",
    "sec-fetch-dest":"document",
    "Referer":"https://www.google.com/",
    "Accept-Encoding":"gzip, deflate, br"
    }

amz_response = requests.get(product_url,
                            headers=headers)

amz_soup = BeautifulSoup(amz_response.text, "lxml")
whole = amz_soup.find(class_="a-price-whole").getText()
fraction = amz_soup.find(class_="a-price-fraction").getText()
product_name = amz_soup.find(name="span", id="productTitle").getText()
price = float(whole+fraction)
print(product_name)

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        
        subject = "Amazon Price Update"
        body = f"{product_name} is available at ${price}\n check it out: {product_url}"
        msg = EmailMessage()
        msg.set_content(body)
        print(msg)
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = email
        
        connection.send_message(from_addr=email, to_addrs=email, msg= msg)
        connection.close()