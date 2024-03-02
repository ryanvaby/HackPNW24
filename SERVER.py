from flask import Flask, render_template, request, redirect, url_for, flash
import numpy
import pandas
from openai import images, OpenAI

# Setup for flask application
app = Flask(__name__)

# Declaring the following main_func() method as the code to run when user requests the home page of site
    
@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
            roomHeight = request.form(roomHeight)
            roomWidth = request.form(roomWidth)
            bedWidth = request.form(bedWidth)
            bedHeight = request.form(bedHeight)
            tableWidth = request.form(tableWidth)
            tableHeight = request.form(tableHeight)
            dresserWidth = request.form(dresserWidth)
            dresserHeight = request.form(dresserHeight)
            bookshelfWidth = request.form(bookshelfWidth)
            bookshelfHeight = request.form(bookshelfHeight)
            chairWidth = request.form(chairWidth)
            chairHeight = request.form(chairHeight)

            if not user:
                print('User is required!')

            # Determing whether the use wants to input their own domains or use the hard-coded ones
            if user.lower() == "my own":
                domains = request.form['domains']
                if not domains:
                    print('Domains is required!')

                # Collecting the user's desired domains and running the measure_RTT function to store the average RTT of each domain
                return redirect(url_for('output', target_domains=domains))
            # Performing the same functions on pre-entered domains
            elif user.lower() == "yours":
                area = request.form['area']
                if not area:
                    print('Area is required!')

                return redirect(url_for('output', target_domains=area))
            else:
                return render_template("home.html")
        
    return render_template("home.html")
