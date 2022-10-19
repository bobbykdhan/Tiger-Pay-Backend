from fastapi import FastAPI
from pylibdmtx.pylibdmtx import decode
from PIL import Image
from bs4 import BeautifulSoup as bs4
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/card")
async def read_item(skey: str = 0, cid: str = "105", side: str = ""):
    im = Image.open(r"testlol.jpeg")

    im1 = im.crop((250, 685, 451, 885))
    # im1.show()
    print(decode(Image.open("final.png")))

    payload = {
        'skey': skey,
        'cid': cid,
        'side': "front"
    }

    response = requests.get(
        "https://tigerspend.rit.edu/virtualcardnew.php", payload).content
    test = bs4(response, "html.parser")


    if "Login" in test.text:
        print("SKEY INVALID")
        return

    card = requests.get(
        "https://tigerspend.rit.edu/" + 'imagestudentcard.php?cid=105&skey=' + payload["skey"] + '&side=front')

    with open('card.jpg', 'wb') as handler:
        handler.write(card.content)
        im = Image.open(r"card.jpg")
        im.show()
        im1 = im.crop((250, 685, 451, 885))
        im1.show()
        im1.save("crop.png")
        code = decode(Image.open("crop.png"))[0].data
        print(code)
        return {("Card code: "  +str(code) ) : ("Skey: " +skey)}



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
