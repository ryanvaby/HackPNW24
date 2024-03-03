import random

def updateRandomPrompt():
    all_furniture_items = ["bed", "table", "dresser", "bookshelf", "chair" ]
    room_items = []
    
    for i in all_furniture_items:
        if (random.choice([True, False])):
            room_items.append(i)
    print(room_items)
    for i in room_items:
        if i == "chair":
            #updatePrompt("chair", 2, 2)
            print(i)
        elif (i == "bed"):
            #updatePrompt("bed", random.randrange(6, 11), random.randrange(4, 8))
            print(i)
        else:
            #updatePrompt(i, random.randrange(2, 4), random.randrange(2, 6))
            print(i)


updateRandomPrompt() 
    
    
"""""
    if(d1 !=0 and d2 !=0):
        global global_prompt
        dem1 = str(d1)
        dem2 = str(d2)
        global_prompt = global_prompt + (f" a {dem1} by {dem2} {furniture}")
        print(global_prompt)
"""