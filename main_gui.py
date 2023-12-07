from src.utils import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def generate_image():
    # 텍스트를 추출하고 이미지를 생성하는 함수 (여기서는 예시 코드로 대체)
    text = text_entry.get()
    img, img_url = txt_to_img(client, text) # 실제 함수 호출
    #img = Image.open("placeholder.png")  # 임시 이미지
    update_image(img)
    save_img(save_img_path, img)

def update_image(img):
    img = img.resize((250, 250), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    img_label.config(image=img_tk)
    img_label.image = img_tk

def convert_to_html():
    global css_text, css_name
    html_text, css_text, css_name = img_to_html(client, save_img_path+'/image.png')
    # 이미지를 HTML로 변환하는 함수 (여기서는 예시 코드로 대체)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, html_text)


def save_html():
    global css_text, css_name
    # 생성된 HTML 텍스트를 파일로 저장
    file_path = filedialog.askdirectory()#filedialog.asksaveasfilename() #defaultextension=".html"
    if file_path:
        with open(file_path+"/index.html", "w") as file:
            file.write(output_text.get("1.0", tk.END))
    print()
    if css_text is not None:
        css_file_path = file_path
        with open(css_file_path+"/"+css_name, "w") as file:
                file.write(css_text)


client = OpenAI(api_key='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')
save_img_path = './test_img'
save_html_path = './test_html'
css_text = None
css_name = None

# GUI 설정
root = tk.Tk()
root.title("Image and HTML Generator")

# 텍스트 입력란
text_entry = tk.Entry(root, width=40)
text_entry.insert(0, 'create a modern dark log in UI')  # 기본 텍스트 설정
text_entry.pack()

# 이미지 생성 버튼
generate_button = tk.Button(root, text="Generate Image", command=generate_image)
generate_button.pack()

# 이미지 레이블 (이미지 표시)
img_label = tk.Label(root)
img_label.pack()

# HTML 변환 버튼
html_button = tk.Button(root, text="Convert to HTML", command=convert_to_html)
html_button.pack()

# HTML 출력 텍스트 박스
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# HTML 저장 버튼
save_button = tk.Button(root, text="Save HTML", command=save_html)
save_button.pack()

root.mainloop()