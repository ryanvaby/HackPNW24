from flask import Flask, render_template, request, redirect, url_for, flash
from openai import images, OpenAI
global_prompt = "Give me "

def genImage(furniture, d1, d2):
    if(d1 !=0 and d2 !=0):
        global global_prompt
        dem1 = str(d1)
        dem2 = str(d2)
        global_prompt += f" a {dem1} by {dem2} {furniture}"


genImage("table", 12, 4)
print(global_prompt)

    #with no additional furniture. Draw like the attached image. Keep it as bare bones as possible