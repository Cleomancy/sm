'''
Sitemap page generator by the Cleomancer.
using os and Path this little script sifts through the directory it's in
and looks for every HTML/XHTML file paths that exists within.
This includes subdirectories. Then through clever printing it writes
an XHTML page listing every link in an unordered list.

credits: thanks to these guys on stack overflow :)
https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
'''
from pathlib import Path
import os

sm = open("sitemap.xhtml", "w")

output="<!DOCTYPE html>\n<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='en' lang='en'>\n<head><meta charset='utf-8' />\n<meta name='viewport' content='width=device-width, initial-scale=1' />\n<link rel='stylesheet' type='text/css' href='./style.css' />\n<link rel='icon' type='image/x-icon' href='./static/favicon.ico' />\n<title>Sitemap</title>\n</head>\n<body id='sitemap'><h1>Sitemap</h1>"

sm.write(output)

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".html") or file.endswith(".xhtml"):
			m=os.path.join(root) #this equals file path WITHOUT file name
			if m == os.path.join("."):
				sm.write("<h2>Root/</h2><ul>\n")#root directory gets renamed, make sure it comes first in the script to open the <ul> properly
				for file in os.listdir(m):# from this path print every page existing there
					if file.endswith(".html") or file.endswith(".xhtml"):
						sm.write("<li><a href='"+os.path.join(root, file)+"'>"+os.path.join(file)+"</a></li>\n")
			else:
				sm.write("</ul><h2>"+str(Path(m))+"/</h2><ul>\n")#any subdirectory under ./
				for file in os.listdir(m):
					if file.endswith(".html") or file.endswith(".xhtml"):
						sm.write("<li><a href='"+os.path.join(root, file)+"'>"+os.path.join(file)+"</a></li>\n")
			break #at this point the whole list of every file/path is generated. We break to avoid repeating the loop x times where x is the number of files of HTML and XHTML type.
sm.write("</ul>\n</body>\n</html>")#properly finish the sitemap.html

sm.close()
