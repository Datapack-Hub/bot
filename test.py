methods = os.listdir(".\\method")

for file in methods:
    print("Method Name: " + file.replace(".txt", ""))
    opened_file = open((".\\method\\" + file), "r")
    file_content = opened_file.read()
    print("Method Description: " + file_content)
    opened_file.close()
