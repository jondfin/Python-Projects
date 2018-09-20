from bs4 import BeautifulSoup as BS
import requests
import os

def cleandir():
    # If file directory does not exist, create it
    if not os.path.isdir(os.getcwd() + "\\ScrapedImages"):
        print("Creating directory")
        os.mkdir(os.getcwd() + "\\ScrapedImages")
        os.chdir(os.getcwd() + "\\ScrapedImages")
        print(os.getcwd())
        return

    #Remove files in
    os.chdir(os.getcwd() + "\\ScrapedImages")
    print("Current Directory: " + os.getcwd())
    for file in os.listdir("."):
        try:
            print("Removing " + str(file))
            os.remove(str(file))
        except:
            pass
    os.chdir("..")
    os.rmdir(os.getcwd() + "\\ScrapedImages")
    os.mkdir(os.getcwd() + "\\ScrapedImages")
    os.chdir(os.getcwd() + "\\ScrapedImages")

link = "https://www.pexels.com/search/dog/"
#Open link and convert to BS object for parsing
r = requests.get(link, headers={"User-agent": "Mozilla/62.0 Chrome/69.0.3497.100 Safari/5.1.10"})
soup = BS(r.text, "html.parser")
#Parses through html data to retrieve any img tags
imageData = soup.find_all("img")
images = []
i = 0
for image in imageData:
    #Only save up to 5 images
    if i == 5:
        break
    images.append(image.get("src"))
    i = i + 1
print(images)

cleandir()

#Saved images to folder
i = 0

for link in images:
    print(link)
    try:
        with open("dog" + str(i) + ".jpg", "wb") as f:
            f.write(requests.get(link).raw.read())
            print(requests.get(link).raw.read())
            f.close()
            i = i + 1
    except:
        print("error")
        pass
