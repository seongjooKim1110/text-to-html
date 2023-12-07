from src.utils import *

#set openAI api key 
client = OpenAI(api_key='')

save_img_path = './test_img'
save_html_path = './test_html'

#extract the text 
#text = extract()
text = 'create a modern dark log in UI'

img, img_url = txt_to_img(client, text)

save_img(save_img_path, img)

html_text = img_to_html(client, save_img_path+'/image.png')

save_html(save_html_path, html_text)