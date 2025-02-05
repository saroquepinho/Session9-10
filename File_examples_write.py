# lets create a virtual diary
with open("diary.txt", "a") as fp: # a just keeps the history of what was previously written in your diary
    while True:
        text = input("How do you feel today? (type q to quit): ")
        if text == "q":
            break
        fp.write(f"{text}\n") # \n means new line
