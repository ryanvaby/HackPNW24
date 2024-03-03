from flask import Flask, render_template, request
from openai import images, OpenAI
import openai
import base64
from datetime import datetime 
from PIL import Image 
import requests 
from io import BytesIO
import random



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
            if (request.form.get("randomize")):
                updateRandomPrompt()
            for item in furniture_items:
                if (request.form.get(item)):
                    updatePrompt(item, request.form.get(item + "Width"), request.form.get(item + "Length"))
                else:
                    continue
            return genImage()

    else:
        return render_template("index.html")
    
def updatePrompt(furniture, d1, d2):
    if(d1 !=0 and d2 !=0):
        global global_prompt
        dem1 = str(d1)
        dem2 = str(d2)
        global_prompt = global_prompt + (f" a {dem1} by {dem2} {furniture}")
        print(global_prompt)

def genImage():
    print("first")
    global global_prompt
    global_prompt = global_prompt + ", with no additional furniture. Draw like the attached image. Keep it as bare bones as possible."
    image = fetch_dalle_image()
    return render_template("result.html", image = image)


def fetch_dalle_image():
    
    client = OpenAI(api_key="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")
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
    
    return image_url

def updateRandomPrompt():
    global global_prompt
    all_furniture_items = ["bed", "table", "dresser", "bookshelf", "chair" ]
    room_items = []
    
    for i in all_furniture_items:
        if (random.choice([True, False])):
            room_items.append(i)
    print(room_items)
    for i in room_items:
        if i == "chair":
            updatePrompt("chair", 2, 2)
        elif (i == "bed"):
            updatePrompt("bed", random.randrange(6, 11), random.randrange(4, 8))
        else:
            updatePrompt(i, random.randrange(2, 4), random.randrange(2, 6))