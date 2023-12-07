# text-to-html
* Text to Website(T2W) 최소 기능 구현으로 Text to Image -> Image to HTML 순으로 진행된다. 
* GUI는 파이썬의 tkinter를 사용하여 제작였다.
* 사용 OpenAPI
  * DALL-E 3 : Text to Image에 사용되어 이미지를 생성
  * GPT-4 : Image to HTML을 위해 사용되어 HTML 코드를 생성  

## Description
### 1. 텍스트를 넘겨 이미지를 생성
<p align="center">
  <img src="https://github.com/seongjooKim1110/text-to-html/assets/49272721/7f1b4b45-6c87-43ef-8210-a755e1841e47">
</p>
<p align="center">
  <img src="https://github.com/seongjooKim1110/text-to-html/assets/49272721/77310f5f-b591-412c-ac97-5c270b626288">
</p>

### 2. 생성된 이미지를 HTML 코드로 변환
<p align="center">
  <img src="https://github.com/seongjooKim1110/text-to-html/assets/49272721/7bf0e78a-bafd-4724-a27f-39c2b4bc1e23">
</p>

### 3. 변환된 HTML 코드를 렌더링 결과 
<p align="center">
  <img src="https://github.com/seongjooKim1110/text-to-html/assets/49272721/6518a54e-8cda-4798-bc8f-7c8cb899c5de">
</p>

## Setup
### Prerequisites

* python3 

* pip

* main_gui.py 에서 DALL-E와 GPT-4를 사용하기 위해 OpenAI API key를 설정해야 함. 

### Install Dependencies

```
pip install -r  requirements.txt
```

## Usage
T2W GUI 실행방법

```
python3 main_gui.py
```
