from flask import Flask, render_template, request
from openai import images, OpenAI

# Setup for flask application
app = Flask(__name__)

# Declaring the following main_func() method as the code to run when user requests the home page of site
global_prompt = ""

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
            furniture_items = ["bed", "table", "dresser", "bookshelf", "chair" ]
            for item in furniture_items:
                if (request.form.get(item)):
                    #print(request.form.get(item+"Width"))
                    updatePrompt(item, request.form.get(item + "Width"), request.form.get(item + "Length"))
                else:
                    return render_template("index.html")


            # dimensions = [roomLength, roomWidth, bedWidth, bedLength, tableLength, tableWidth, ]
            # roomLength = request.form(roomLength)
            # roomWidth = request.form(roomWidth)
            # bedWidth = request.form(bedWidth)
            # bedLength = request.form(bedLength)
            # tableWidth = request.form(tableWidth)
            # tableLength = request.form(tableLength)
            # dresserWidth = request.form(dresserWidth)
            # dresserLength = request.form(dresserLength)
            # bookshelfWidth = request.form(bookshelfWidth)
            # bookshelfLength = request.form(bookshelfLength)
            # chairWidth = request.form(chairWidth)
            # chairLength = request.form(chairLength)

            # if not roomLength:
            #     roomLength = 0
            # if not roomWidth:
            #     roomWidth = 0
            # if not bedLength:
            #     bedLength = 0
            # if not bedWidth:
            #     bedWidth = 0
            # if not tableLength:
            #     tableLength = 0
            # if not tableWidth:
            #     tableWidth = 0
            # if not dresserLength:
            #     dresserLength = 0
            # if not dresserWidth:
            #     dresserWidth = 0
            # if not bookshelfLength:
            #     bookshelfLength = 0
            # if not bookshelfWidth:
            #     bookshelfWidth = 0
            # if not chairLength:
            #     chairLength = 0
            # if not chairWidth:
            #     chairWidth = 0

            #genImage(roomLength, roomWidth, bedWidth, bedLength, tableLength, tableWidth, bookshelfLength, bookshelfWidth, chairLength, chairWidth, dresserLength,dresserWidth)

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