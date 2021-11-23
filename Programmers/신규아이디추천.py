import re

def solution(new_id):
    answer = ''
    if new_id == "":
        new_id = "a"
    
    new_id = new_id.lower()
        
    new_id = re.sub("[^a-z0-9_\.\-]","",new_id)
    if ".." in new_id:
        new_id.replace("..",".")
        
    
    while len(new_id) and new_id[0] == ".":
         new_id = new_id[1:]
    while len(new_id) and new_id[-1] == ".":
        new_id = new_id[:-1]
        
    if new_id == "":
        new_id = "a"

    if len(new_id)>=16:
        new_id = new_id[:15]
    
    if new_id[-1] == ".":
        new_id = new_id[:-1]
        
    while len(new_id) <=2:
        new_id += new_id[-1]
    
    return new_id