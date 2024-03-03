from flask import Flask, render_template, request
from openai import images, OpenAI
import openai
import base64
from datetime import datetime 
from PIL import Image 
import requests 
from io import BytesIO



# Setup for flask application
app = Flask(__name__)

# Declaring the following main_func() method as the code to run when user requests the home page of site
global_prompt = ""

@app.route("/", methods=["GET", "POST"])
def main():

    if request.method == "POST":
            global global_prompt
            global_prompt = global_prompt + "Simple 2 dimensional floor plan of my " + str(request.form.get("roomLength")) + " by " + str(request.form.get("roomWidth")) + " foot room with "
            furniture_items = ["bed", "table", "dresser", "bookshelf", "chair" ]
            for item in furniture_items:
                if (request.form.get(item)):
                    updatePrompt(item, request.form.get(item + "Width"), request.form.get(item + "Length"))
                else:
                    continue
            return genImage()

    else:
        return render_template("index.html")
        #def genImage(bed, table, bookshelf, chair, dresser):
    
def updatePrompt(furniture, d1, d2):
    if(d1 !=0 and d2 !=0):
        global global_prompt
        dem1 = str(d1)
        dem2 = str(d2)
        global_prompt = global_prompt + (f" a {dem1} by {dem2} {furniture}")
        print(global_prompt)

def genImage():
    print("first")
    image = fetch_dalle_image()
    return render_template("result.html", image = image)


def fetch_dalle_image():
    
    client = OpenAI(api_key="RUCHI & NANCY: PUT API KEY HERE")
    print("second")
    global global_prompt
    print(global_prompt)
    response = client.images.generate(
        model="dall-e-2",
        prompt= global_prompt,
        n=1,
        size="1024x1024"
    )
    
    # Assuming the first image in the response is the one we want
    image_url = response.data[0].url
    print(image_url)

    
    # Fetch the image
    # image_response = requests.get(image_url)
    # other_thing = get_as_base64(image_response)   
    
    return image_url

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

