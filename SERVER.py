from flask import Flask, render_template, request, redirect, url_for, flash
from openai import images, OpenAI

# Setup for flask application
app = Flask(__name__)

# Declaring the following main_func() method as the code to run when user requests the home page of site
gloabl_prompt = ""

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
            furniture_items = ["bedSelect", "tableSelect", "dresserSelect", "bookshelfSelect", "chairSelect" ]
            for item in furniture_items:
                if request.form.get(item) == 'on':
                genImage("bed", request.form(bedLength), request.form(bedWidth))

            dimensions = [roomLength, roomWidth, bedWidth, bedLength, tableLength, tableWidth, ]
            roomLength = request.form(roomLength)
            roomWidth = request.form(roomWidth)
            bedWidth = request.form(bedWidth)
            bedLength = request.form(bedLength)
            tableWidth = request.form(tableWidth)
            tableLength = request.form(tableLength)
            dresserWidth = request.form(dresserWidth)
            dresserLength = request.form(dresserLength)
            bookshelfWidth = request.form(bookshelfWidth)
            bookshelfLength = request.form(bookshelfLength)
            chairWidth = request.form(chairWidth)
            chairLength = request.form(chairLength)

            if not roomLength:
                roomLength = 0
            if not roomWidth:
                roomWidth = 0
            if not bedLength:
                bedLength = 0
            if not bedWidth:
                bedWidth = 0
            if not tableLength:
                tableLength = 0
            if not tableWidth:
                tableWidth = 0
            if not dresserLength:
                dresserLength = 0
            if not dresserWidth:
                dresserWidth = 0
            if not bookshelfLength:
                bookshelfLength = 0
            if not bookshelfWidth:
                bookshelfWidth = 0
            if not chairLength:
                chairLength = 0
            if not chairWidth:
                chairWidth = 0

            #genImage(roomLength, roomWidth, bedWidth, bedLength, tableLength, tableWidth, bookshelfLength, bookshelfWidth, chairLength, chairWidth, dresserLength,dresserWidth)

    else:
        return render_template("index.html")
        #def genImage(bed, table, bookshelf, chair, dresser):