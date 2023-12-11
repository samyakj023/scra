import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=potato+leaf+late+blight+images+256+*+256+pixels&tbm=isch&ved=2ahUKEwi61dveroeDAxUV6KACHZH2BXMQ2-cCegQIABAA&oq=potato+leaf+late+blight+images+256+*+256+pixels&gs_lcp=CgNpbWcQAzoECCMQJ1DFFFj9RGCIR2gFcAB4AIAB0QGIAb4VkgEGMC4xOS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=6P12ZbrBJpXQg8UPke2XmAc&bih=796&biw=1536'

html = requests.get(url)
content = html.text

parse = BeautifulSoup(content,'html.parser')

img = parse.find_all('img')

def download_images(images):
    count = 0
    print(f"Total {len(images)} Image Found!")

    if len(images) != 0:
        for i, image in enumerate(images):

            try:
                image_link = image["data-srcset"]                
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:                        
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            pass
            try:
                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open(f"images{i+1}.jpg", "wb+") as f:
                        f.write(r)
                    count += 1
            except:
                pass    
            
download_images(img)            