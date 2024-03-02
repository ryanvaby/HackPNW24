from flask import Flask, render_template, request, redirect, url_for, flash
from openai import images, OpenAI
global_prompt = "Give me "

<<<<<<< HEAD
def main():
    print("hi")
    print(genImage(1,2,3,4,5,6,7,8,9,10,11,12))
=======
def genImage(furniture, d1, d2):
    if(d1 !=0 and d2 !=0):
        global global_prompt
        dem1 = str(d1)
        dem2 = str(d2)
        global_prompt += f" a {dem1} by {dem2} {furniture}"
>>>>>>> 8f672506137ed31d2f61b05a596c55d08a924ec8


<<<<<<< HEAD
    #make a string for each item name and dimensions
    prompt = "Simple 2 dimensional floor plan of my " + roomD1 + " by " + roomD2 + " foot room with"
    bedString = "a " + bedD1 + " by " + bedD2 + " bed"
    tableString = "a " + tableD1 + " by " + tableD2 + " table"
    bookshelfString = "a " + bookshelfD1 + " by " + bookshelfD2 + " bookshelf"
    chairString = "a " + chairD1 + " by " + chairD2 + " chair"
    dresserString = "a " + dresserD1 + " by " + dresserD2 + " dresser"

    return(bedString)
=======
genImage("table", 12, 4)
print(global_prompt)
>>>>>>> 8f672506137ed31d2f61b05a596c55d08a924ec8

    #with no additional furniture. Draw like the attached image. Keep it as bare bones as possible