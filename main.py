import os 

loc = input("Enter a valid directory path : ")
try :
    total_folders = os.listdirdir(loc)
    print(f"The total number of folders are : {total_folders}")
    
    for i in total_folders : 
        if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".gif") or i.endswith(".svg") or i.endswith(".jfif") or i.endswith(".avif") or i.endswith(".jpeg") or i.endswith(".webp") or i.endswith(".ico") or i.endswith(".bmp") or i.endswith(".tif") or i.endswith(".tiff") : 
            
except : 
    print("The path that you have provided is invalid.")