from flask import Flask, render_template, request, redirect, url_for, flash
from openai import images, OpenAI

def main():
    print("hi")
    print(genImage(1,2,3,4,5,6,7,8,9,10,11,12))

def genImage(roomD1, roomD2, bedD1, bedD2, tableD1, tableD2, bookshelfD1, bookshelfD2, chairD1, chairD2, dresserD1, dresserD2):
    #make a string for each name + demiension parameter 
    #if dimensions greater than zero concatenate each string to prompt 
    # statement 
    ##send prompt and return image url

    #make a string for each item name and dimensions
    prompt = "Simple 2 dimensional floor plan of my " + roomD1 + " by " + roomD2 + " foot room with"
    bedString = "a " + bedD1 + " by " + bedD2 + " bed"
    tableString = "a " + tableD1 + " by " + tableD2 + " table"
    bookshelfString = "a " + bookshelfD1 + " by " + bookshelfD2 + " bookshelf"
    chairString = "a " + chairD1 + " by " + chairD2 + " chair"
    dresserString = "a " + dresserD1 + " by " + dresserD2 + " dresser"

    return(bedString)

    #with no additional furniture. Draw like the attached image. Keep it as bare bones as possible