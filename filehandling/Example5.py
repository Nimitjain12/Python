# how to read from a file
# need a json file in current project

with open("details.json","r") as f:
    data=f.read()
    print(data)

print("Done")


