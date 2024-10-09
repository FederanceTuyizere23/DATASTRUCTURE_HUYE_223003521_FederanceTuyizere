from collections import deque


photo_albums = ["kivu vacation","Graduation" ,"Birthday", "Wedding"]  

def Album_addition(albumname):
    photo_albums.append(albumname)
    print(f"Album '{albumname}' added")
    print(f"Current albums: {photo_albums}")

photochanges_stack = [] 

def photo_edit(change):
    photochanges_stack.append(change)
    print(f"Change '{change}' applied. Changes stack: {photochanges_stack}")

def undolast_change():
    if photochanges_stack:
        lastchange = photochanges_stack.pop()
        print(f"Undo last change: {lastchange}. Remaining changes: {photochanges_stack}")
    else:
        print("No changes to undo.")

uploadqueue = deque()  

def photo_upload(photo):
    uploadqueue.append(photo)
    print(f"Photo '{photo}' added to upload queue. Upload queue: {list(uploadqueue)}")


def process_upload():
    if uploadqueue:
        next_photo = uploadqueue.popleft()
        print(f"Uploading photo: {next_photo}. Remaining queue: {list(uploadqueue)}")
    else:
        print("No photos to upload.")

Album_addition("bridal shower")  
photo_edit("Photo edited 1") 
photo_edit("Photo edited 2")  
undolast_change()  
photo_upload("Photo1.jpg")  
photo_upload("Photo2.jpg") 
process_upload() 
process_upload() 