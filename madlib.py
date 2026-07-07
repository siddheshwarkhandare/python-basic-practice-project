with open("story.txt","r")as f:
    story=f.read()
word=[]
start_of_word= -1
starting_target="<"
ending_target=">"

for i,char in enumerate(story):
    if char==starting_target:
        starting_target= i
    if char == starting_target and