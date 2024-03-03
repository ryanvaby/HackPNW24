import random

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

updateRandomPrompt() 
    