from openai import OpenAI
import base64
from urllib import request
from io import BytesIO
from PIL import Image

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def save_img(save_path, img):
    img.save(save_path+'/image.png', 'PNG')

def save_html(save_path, html_text):
    html_file = open(save_path + '/index.html', 'w')
    html_file.write(html_text)
    html_file.close()

def txt_to_img(client, text):
    response = client.images.generate(
    model="dall-e-3",
    prompt=text,
    size="1024x1024",
    quality="standard",
    n=1,
    )   

    image_url = response.data[0].url

    res = request.urlopen(image_url).read()
    img = Image.open(BytesIO(res))

    return img, image_url

def extract_href_value(html_text):
    start_index = html_text.find('href="')
    if start_index == -1:
        return None
    start_q = start_index + len('href="')
    end_q = html_text.find('"', start_q)

    href_value = html_text[start_q:end_q]

    return href_value

def img_to_html(client, image_url):
    base64_image = encode_image(image_url)
    
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Please tell me in detail by attaching the HTML code and CSS code to make this image into a web page."},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
        
          },
        },
      ],
    }
    ],
        max_tokens=4000,
    )

    res = response.choices[0].message.content
    print(res)
    html_text_parts = res.split('```')

    if len(html_text_parts) > 3: 
        html_text = html_text_parts[1]
        css_text = html_text_parts[3]
        css_name = extract_href_value(html_text)
        return html_text, css_text, css_name
    else :
        html_text = html_text_parts[1]
        return html_text, None, None

    
