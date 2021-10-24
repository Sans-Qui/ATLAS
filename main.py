from PIL import Image
from resizeimage import resizeimage
from IPython.display import display
import random
import json
import webbrowser
import os

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Blue", "Blue2", "Grey", "Mauve", "Pink", "Rainbow", "Yellow", "Rare"]
background_weights = [14,14,14,14,14,14,14, 1]

body = ["Body1", "Black", "Women", "Genius", "Ogre", "Demon","Bubble",]
body_weights = [46, 40, 8, 2, 2, 1, 1]

hairs = ["Bald", "Brown1", "Blond1", "Ginger1", "Grey1", "Blue1", "Green1", "Sayajin"]
hairs_weights = [20,20,15,10,10,5,4,1]

costume = ["Bionic", "Superman","Sacha", "Boat", "Bath", "Prison","Pot","Saitama","Luffy","Vader", "Mario", "Luigi", "Michael", "ArmorCuir", "ArmorSilver", "ArmorGold", "ArmorGoldCape", "Egypt", "NoCostume", "Squelette","Squeletteblck", "AllBlack", "BaseBlue", "BasePink", "BaseRed","BasketBlack", "BasketWhite", "Flame", "Kakarot", "Naruto", "PinkSmoking","Pirate1", "PirateInv", "Santa", "ShinyBlue","SmokingPinkTie", "Magician"]
costume_weights = [3, 1, 3, 3, 3, 2, 1, 3, 3, 3, 2, 2, 3, 2, 2.5, 1.5, 1, 3, 4, 2.5, 2.5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

tool = ["Lampe", "Altères", "Jesus","Cercueil", "France",  #1
        "USA", "HarryPotterCristal", "dko", "AirportGuy", "AquariumClownFish", #2
        "AquariumCrab", "AquariumMedusa","AquariumRedFish", "Axe", "BlueFire", #3
        "Banana", "BaseBall","BasketBall", "Bitcoin", "BowArrow", #4
        "BubbleGum","CanneBotte", "CatchBlueButterfly", "CatchingFishBlue","CatchYellowButterfly",#5
        "CatGinger", "CatGold","CatGrey", "ChrismasTree", "CrocoBlue",#6
        "CrocoRed", "CrocoGreen", "Diamond", "Dogecoin", "DoubleCheese",#7
        "Earth", "Elephant", "ElephantPink", "FireBall", "Giant",#8
        "Guitar", "HandCuff", "HoldFace", "HolyPoo", "ILoveNFT",#9
        "JumpRope", "KeyIron", "Maracas", "Matches", "Naruto",#10
        "Phone", "PinkFloyd", "Poo", "PyramidHorus", "ReverseShadow",#11
        "Supporter", "SwordShieldDiamond", "SwordShieldGold", "SwordShieldIron","Tennis",#12
        "Treasure", "TreasureRare", "Tree", "TripleCheese", "Soucoupe",#13
        "Saturne", "SaturneShiny", "Squirtle", "Bulbasaur", "Charmander",#14
        "MineurCoal", "MineurGold", "MineurDiamant", "HarryPotter", "CieldeBillets", #15
        "Column","Rasta","MarioBrique", "MarioStar", "MarioGold", #16
        "LuigiChampi", "Angleterre", "Vader", "Luffy","HandsUp", #17
        "Duck",]
tool_weights = [1,2,1,1,1,   #1
                1,1,2,1,0.5,  #2
                0.5,0.5,0.5,1,1, #3
                1,1,1,1,1, #4
                1,1,1,2,2, #5
                1,0.5,2,1,1, #6
                1,1,0.5,2,1, #7
                1,2,1,2,2, #8
                2,1,2,0.5,1, #9
                1,1,2,1,1, #10
                1.5,1,2,1,1, #11
                1,1,2,1,2, #12
                1,1.5,1.5,2,1, #13
                1,2,1,2,1, #14
                1,1,1.5,1,1, #15
                1,1,0.5,0.5,0.25, #16
                0.25,1,1,1,1, #17
                1,]


print( len(tool_weights))
# Dictionary variable for each trait.
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

background_files = {
    "Blue": "blue",
    "Blue2": "blue2",
    "Grey": "grey",
    "Mauve": "mauve",
    "Pink": "pink",
    "Rainbow": "rainbow",
    "Yellow": "yellow",
    "Rare": "rare",
}
body_files = {
    "Body1": "body1",
    "Black": "black",
    "Women": "women",
    "Genius": "genius",
    "Ogre": "ogre",
    "Demon": "demon",
    "Bubble": "bubble",
}
hairs_files = {
    "Bald": "bald",
    "Brown1": "brown1",
    "Blond1": "blond1",
    "Ginger1": "ginger1",
    "Blue1": "blue1",
    "Green1": "green1",
    "Grey1": "grey1",
    "Sayajin": "sayajin"

}
costume_files = {
    "ArmorCuir": "armorcuir",
    "ArmorSilver": "armorsilver",
    "ArmorGold": "armorgold",
    "ArmorGoldCape": "armorgoldcape",
    "Egypt": "egypt",
    "AllBlack": "allblack",
    "BaseBlue": "baseblue",
    "BasePink": "basepink",
    "BaseRed": "basered",
    "BasketBlack": "basketblack",
    "BasketWhite": "basketwhite",
    "Flame": "flame",
    "GreenMonster": "greenmonster",
    "Kakarot": "kakarot",
    "Magician": "magician",
    "Naruto": "naruto",
    "PinkSmoking": "pinksmoking",
    "Pirate1": "pirate1",
    "PirateInv": "pirateinv",
    "Santa": "santa",
    "ShinyBlue": "shinyblue",
    "SmokingPinkTie": "smokingpinktie",
    "Squelette": "squelette",
    "Squeletteblck": "squeletteblck",
    "NoCostume": "nocostume",
    "Michael": "michael",
    "Mario": "mario",
    "Luigi": "luigi",
    "Vader": "vader",
    "Luffy": "luffy",
    "Saitama": "saitama",
    "Pot": "pot",
    "Prison": "prison",
    "Bath": "bath",
    "Boat": "boat",
    "Sacha": "sacha",
    "Superman": "superman",
    "Bionic": "bionic",
}
tool_files = {
    "AirportGuy": "airportguy",
    "AquariumClownFish": "aquariumclownfish",
    "AquariumCrab": "aquariumcrab",
    "AquariumMedusa": "aquariummedusa",
    "AquariumRedFish": "aquariumredfish",
    "Axe": "axe",
    "Banana": "banana",
    "BaseBall": "baseball",
    "BasketBall": "basketball",
    "Bitcoin": "bitcoin",
    "BowArrow": "bowarrow",
    "BubbleGum": "bubblegum",
    "BlueFire": "bluefire",
    "CanneBotte": "cannebotte",
    "CatchBlueButterfly": "catchbluebutterfly",
    "CatchingFishBlue": "catchingFishBlue",
    "CatchYellowButterfly": "catchyellowbutterfly",
    "CatGinger": "catginger",
    "CatGold": "catgold",
    "CatGrey": "catgrey",
    "ChrismasTree": "chrismastree",
    "CrocoBlue": "crocoblue",
    "CrocoRed": "crocored",
    "CrocoGreen": "crocogreen",
    "Diamond": "diamond",
    "Dogecoin": "dogecoin",
    "DoubleCheese": "doublecheese",
    "Earth": "earth",
    "Elephant": "elephant",
    "ElephantPink": "elephantpink",
    "FireBall": "fireball",
    "Giant": "giant",
    "Guitar": "guitar",
    "HandCuff": "handcuff",
    "HoldFace": "holdface",
    "HolyPoo": "holypoo",
    "ILoveNFT": "ilovenft",
    "JumpRope": "jumprope",
    "KeyIron": "keyiron",
    "Maracas": "maracas",
    "Matches": "matches",
    "Naruto": "naruto",
    "Phone": "phone",
    "PinkFloyd": "pinkfloyd",
    "Poo": "poo",
    "PyramidHorus": "pyramidhorus",
    "ReverseShadow": "reverseshadow",
    "Supporter": "supporter",
    "SwordShieldDiamond": "swordshielddiamond",
    "SwordShieldGold": "swordshieldgold",
    "SwordShieldIron": "swordshieldiron",
    "Soucoupe": "soucoupe",
    "Saturne": "saturne",
    "SaturneShiny": "saturneshiny",
    "Tennis": "tennis",
    "Treasure": "treasure",
    "TreasureRare": "treasurerare",
    "Tree": "tree",
    "TripleCheese": "triplecheese",
    "Squirtle": "squirtle",
    "Bulbasaur": "bulbasaur",
    "Charmander": "charmander",
    "MineurCoal": "mineurcoal",
    "MineurGold": "mineurgold",
    "MineurDiamant": "mineurdiamant",
    "HarryPotter": "harrypotter",
    "CieldeBillets": "cieldebillets",
    "dko": "dko",
    "Altères": "altères",
    "Jesus": "jesus",
    "Cercueil": "cercueil",
    "France": "france",
    "USA": "usa",
    "HarryPotterCristal": "harrypottercristal",
    "Lampe": "lampe",
    "Column": "column",
    "Rasta": "rasta",
    "MarioBrique": "mariobrique",
    "MarioStar": "mariostar",
    "MarioGold": "mariogold",
    "LuigiChampi": "luigichampi",
    "Angleterre": "angleterre",
    "Vader": "vader",
    "Luffy": "luffy",
    "HandsUp": "handsup",
    "Duck": "duck",
}

TOTAL_IMAGES = 400  # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = []


def create_new_image():
    new_image = {}  #

    # For each trait category, select a random trait based on the weightings
    new_image["Background"] = random.choices(background, background_weights)[0]
    new_image["Body"] = random.choices(body, body_weights)[0]
    new_image["Hairs"] = random.choices(hairs, hairs_weights)[0]
    new_image["Costume"] = random.choices(costume, costume_weights)[0]
    new_image["Tool"] = random.choices(tool, tool_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES):
    new_trait_image = create_new_image()

    all_images.append(new_trait_image)


def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


print("Are all images unique?", all_images_unique(all_images))

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)

background_count = {}
for item in background:
    background_count[item] = 0

body_count = {}
for item in body:
    body_count[item] = 0

hairs_count = {}
for item in hairs:
    hairs_count[item] = 0

costume_count = {}
for item in costume:
    costume_count[item] = 0

tool_count = {}
for item in tool:
    tool_count[item] = 0


for image in all_images:
    background_count[image["Background"]] += 1
    body_count[image["Body"]] += 1
    hairs_count[image["Hairs"]] += 1
    costume_count[image["Costume"]] += 1
    tool_count[image["Tool"]] +=1

print(background_count)
print(body_count)
print(hairs_count)
print(costume_count)
print(tool_count)


METADATA_FILE_NAME = './metadata/all-traits.json'
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

for item in all_images:
    im1 = Image.open(f'./layers/background/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/body/{body_files[item["Body"]]}.png').convert('RGBA')
    im3 = Image.open(f'./layers/hairs/{hairs_files[item["Hairs"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/costume/{costume_files[item["Costume"]]}.png').convert('RGBA')
    im5 = Image.open(f'./layers/tool/{tool_files[item["Tool"]]}.png').convert('RGBA')

    # Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)

    # Convert to RGB
    taille = [300, 300]
    rgb_im = com4.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im_resized = rgb_im.resize(taille, Image.NEAREST)
    rgb_im_resized.save("./images/" + file_name)

f = open('./metadata/all-traits.json', )
data = json.load(f)

IMAGES_BASE_URI = "ATLAS"
PROJECT_NAME = "ATLAS NFT"


def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }


for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Body", i["Body"]))
    token["attributes"].append(getAttribute("Hairs", i["Hairs"]))
    token["attributes"].append(getAttribute("Costume", i["Costume"]))
    token["attributes"].append(getAttribute("Tool", i["Tool"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)

webbrowser.open(os.getcwd()+"/images/display.html")
f.close()

