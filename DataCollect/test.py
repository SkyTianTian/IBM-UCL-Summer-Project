import json

top = 1
height = 2
left = 3
width = 4

a = {"object": "building","location":{"top": top,"height": height,"left": left,"width": width}
}
print(a)
b ={"object": "building","location":{"top": top,"height": height,"left": left,"width": width}}

list = [a]
list.append(b)

c = json.dumps({"objests":list})
print(c)
#print(json.dumps(a, indent=5))



text_file = open("Data/test.json", "w")

text_file.write(c)

text_file.close()




