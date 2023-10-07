import os 
import shutil

imgfold = []
vidfold = []
docsfold = []
appfold = []
extrasfold = []

loc = input("Enter a valid directory path : ")
try : 
    loc = loc.replace("\\", "/")
except : 
    pass

total = os.listdir(loc)
print(f"The total number of files are : {len(total)}")

for i in total : 
    if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".gif") or i.endswith(".svg") or i.endswith(".jfif") or i.endswith(".avif") or i.endswith(".jpeg") or i.endswith(".webp") or i.endswith(".ico") or i.endswith(".bmp") or i.endswith(".tif") or i.endswith(".tiff") or i.endswith(".gifv") : 
        imgfold.append(i)
        
    elif i.endswith(".mp4") or i.endswith(".mov") or i.endswith(".wmv") or i.endswith(".flv") or i.endswith(".avi") or i.endswith(".webm") or i.endswith(".mkv") or i.endswith(".flv") or i.endswith(".m4v") or i.endswith(".mpeg") or i.endswith(".svi") or i.endswith(".nsv") : 
        vidfold.append(i)
    
    elif i.endswith(".doc") or i.endswith(".docx") or i.endswith(".html") or i.endswith(".htm") or i.endswith(".fb2") or i.endswith(".md") or i.endswith(".sxw") or i.endswith(".pdf") or i.endswith(".ps") or i.endswith(".rtf") or i.endswith(".odt") or i.endswith(".xls") or i.endswith(".xlsx") or i.endswith(".ppt") or i.endswith(".pptx") : 
        docsfold.append(i)
    
    elif i.endswith(".apk") or i.endswith(".appx") or i.endswith(".ipg") or i.endswith(".jar") or i.endswith(".bin") or i.endswith(".exe") or i.endswith(".rbxl") or i.endswith(".rbxlx") or i.endswith(".sb") or i.endswith(".vol") : 
        appfold.append(i)
    
    else : 
        extrasfold.append(i)
        

if len(imgfold) > 0 : 
    os.mkdir(f"{loc}/images")        
if len(vidfold) > 0 : 
    os.mkdir(f"{loc}/videos")        
if len(docsfold) > 0 : 
    os.mkdir(f"{loc}/documents")        
if len(appfold) > 0 : 
    os.mkdir(f"{loc}/apps")        
if len(extrasfold) > 0 : 
    os.mkdir(f"{loc}/extras")        

if os.path.isdir(f"{loc}/images") : 
    for x1 in imgfold : 
        shutil.move(f"{loc}/{x1}", f"{loc}/images/{x1}")
if os.path.isdir(f"{loc}/videos") : 
    for x2 in vidfold : 
        shutil.move(f"{loc}/{x2}", f"{loc}/videos/{x2}")
if os.path.isdir(f"{loc}/documents") : 
    for x3 in docsfold : 
        shutil.move(f"{loc}/{x3}", f"{loc}/documents/{x3}")
if os.path.isdir(f"{loc}/apps") : 
    for x4 in appfold : 
        shutil.move(f"{loc}/{x4}", f"{loc}/apps/{x4}")
if os.path.isdir(f"{loc}/extras") : 
    for x5 in extrasfold : 
        shutil.move(f"{loc}/{x5}", f"{loc}/extras/{x5}")
    
            
            
