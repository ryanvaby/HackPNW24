from flask import Flask, render_template, request
from openai import images, OpenAI

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
            return render_template("index.html")

    else:
        return render_template("index.html")
        #def genImage(bed, table, bookshelf, chair, dresser):
    
    global_prompt = global_prompt + ", with no additional furniture. Draw like the attached image. Keep it as bare bones as possible."
    print(global_prompt)
def updatePrompt(furniture, d1, d2):
    if(d1 !=0 and d2 !=0):
        global global_prompt
        dem1 = str(d1)
        dem2 = str(d2)
        global_prompt = global_prompt + (f" a {dem1} by {dem2} {furniture}")
        print(global_prompt)