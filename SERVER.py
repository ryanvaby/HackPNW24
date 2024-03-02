from flask import Flask, render_template, request, redirect, url_for, flash
import numpy
import pandas
import openai

# Setup for flask application
app = Flask(__name__)

# Declaring the following main_func() method as the code to run when user requests the home page of site
    
@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("index.html")

def genImage(bed, table, bookshelf, chair, dresser):
    