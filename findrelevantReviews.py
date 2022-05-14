import json
import pyautogui
import time
import random
def findMostCommonCategoriesForKey(filename,key):
    mostCommon = dict()
    errors = 0
    count = 0
    with open(filename) as f:
        line = True

        while line:
            try:
                line = f.readline()
                x = json.loads(line)
                if key in x["name"]:
                    categories = x["categories"].split(",")
                    for cat in categories:
                        if cat in mostCommon:
                            mostCommon[cat] += 1
                        else:
                            mostCommon[cat] = 1
            except:
                errors += 1
    print(errors)
    print({k: v for k, v in sorted(mostCommon.items(), key=lambda item: item[1])})

def getAllBusinessIdsRelevantToCategories(filename,storeName):
    businessIds = set()
    count = 0
    with open(filename) as f:
        line = True
        while line:
            try:
                line = f.readline()
                x = json.loads(line)
                if storeName in x["name"]:
                    businessIds.add(x["business_id"])
            except:
                error = 0
    return businessIds

def writeRelevantReviews(fileReadName,fileWriteName,businessIds):
    print("here")
    with open(fileReadName,"r") as fInput,open(fileWriteName,"w") as fOutput:
        line = True
        count = 0
        while line:
            try:
                if count == 10:
                        return
                line = fInput.readline()
                x = json.loads(line)
                # print(x["name"])
                if x["business_id"] in businessIds:
                    print("here")
                    fOutput.writelines(str(x["stars"]) + "\n" + x["text"]+"\n")
                    count += 1
                    print(count)
            except :
                error = 0

def getStatesAndCities():
    global statesAndCities
    statesAndCities = json.load(open("cities.json"))
    
def getRandomCityCoordinates():
    x = random.choice(statesAndCities)
    return [x["latitude"],x["longitude"]]
def getRandomBusinessName():
    r = random.randint(0, 150000)
    with open("yelp_academic_dataset_business.json") as f:
        for i in range(r):
            try:
                next(f)
            except:
                error = 0
        x = json.loads(f.readline())
        return x["name"],x["business_id"]
    
def getAReview(business_id):
    reviews = []
    with open("yelp_academic_dataset_review.json") as f:
        line = True
        while line:
            try:
                line = f.readline()
                x = json.loads(line)
                if business_id == x["business_id"]:
                    reviews.append((x["text"],x["stars"]))
            except:
                error = 0 
    index = random.randint(0,len(reviews) - 1)
    return reviews[index]

def searchAndReviewPlace(coordinates,businessName,stars,review):
    for x in ["chromeIcon","maximizeChrome"]:
        if y:=pyautogui.locateOnScreen(f"./images/signInToAccount/{x}.PNG"):
            pyautogui.click(y)
        time.sleep(3)
    coordinates = ",".join([str(item) for item in coordinates])
    pyautogui.write(f"https://www.google.com/maps/search/{businessName}/@{coordinates},8.32z",interval=0.01)
    pyautogui.press('enter')
    time.sleep(10)
    if y:=(pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review2.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review3.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review4.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review5.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review6.PNG")):
        if pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/closed.PNG"):
            pyautogui.click(pyautogui.locateOnScreen("./images/signInToAccount/X.PNG"))
            return False
        print("108")
        pyautogui.click(y)
        time.sleep(5)
    else:
        print("113")
        pyautogui.click(y:=(pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/dollarSymbol.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/star.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/star2.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/star3.PNG")))
        time.sleep(10)
        if pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/closed.PNG"):
            pyautogui.click(pyautogui.locateOnScreen("./images/signInToAccount/X.PNG"))
            return False

        pyautogui.click(z:=(pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review2.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review3.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review4.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review5.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/review6.PNG")))
        if not y or not z:
            pyautogui.click(pyautogui.locateOnScreen("./images/signInToAccount/X.PNG"))
            return False
        time.sleep(10)
    if z:=(pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/writeAReview.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/writeAReview2.PNG")):
        pyautogui.click(z)
        time.sleep(5)
    else:
        pyautogui.keyDown('ctrl')
        pyautogui.press('f')
        pyautogui.keyUp('ctrl')
        pyautogui.write("write a review",interval=0.1)
        pyautogui.press('enter')
        if z:=pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/writeAReview2.PNG"):
            pyautogui.click(z)
            time.sleep(5)
        else:
            pyautogui.click(pyautogui.locateOnScreen("./images/signInToAccount/X.PNG"))
            return False
    pyautogui.click(pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/posting.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/posting2.PNG"))
    time.sleep(3)
    if not clickOnXStars(stars):
        pyautogui.click(pyautogui.locateOnScreen("./images/signInToAccount/X.PNG"))
        return False

    pyautogui.click(pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/shareDetails.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/shareDetails2.PNG"))
    time.sleep(1)
    pyautogui.write(review,interval=0.009)
    time.sleep(1)

    pyautogui.click(pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/post.PNG"))
    time.sleep(5)
    pyautogui.click(pyautogui.locateOnScreen("./images/signInToAccount/X.PNG"))
    return True

def clickOnXStars(stars):
    try:
        x,y = pyautogui.center(pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/firstStar.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/firstStar2.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/firstStar3.PNG") or pyautogui.locateOnScreen(f"./images/searchAndReviewPlace/firstStar4.PNG"))
        x += 70 * (stars - 1)
        pyautogui.click(x,y)
        time.sleep(1)
        return True
    except:
        return False

def signInToAccount(email,extension):
    for x in ["chromeIcon","maximizeChrome","gmailWord","gmailSignIn","useAnotherAccount","beforeClickingEmailInput","EmailOrPhone"]:
        if y:=pyautogui.locateOnScreen(f"./images/signInToAccount/{x}.PNG"):
            pyautogui.click(y)
            time.sleep(3)
    pyautogui.write(email+str(extension),interval=0.1)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.write(accounts[email],interval=0.1)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(pyautogui.locateOnScreen("./images/signInToAccount/NotNow.PNG"))
    time.sleep(2)
    pyautogui.click(pyautogui.locateOnScreen("./images/signInToAccount/X.PNG"))

def signOutAccount():
    for x in ["chromeIcon","maximizeChrome","gmailWord"]:
        if y:=pyautogui.locateOnScreen(f"./images/signInToAccount/{x}.PNG"):
            pyautogui.click(y)
            time.sleep(3)
    pyautogui.click(1867,156)
    time.sleep(2)
    for x in ["SignOutAllAccounts","SignOutAllAccounts2","removeAccount","removeAccountDeleteSymbol",'yesRemove','X']:
        if y:=pyautogui.locateOnScreen(f"./images/signInToAccount/{x}.PNG"):
            pyautogui.click(y)
            time.sleep(5)



if __name__ == "__main__":
    
    accounts = {
    "spindafi":"Nilla1974",
    }

    # searchAndReviewPlace([33.7825194, -117.2286478],'Therapeutic Elements Center for Massage Therapy',3,"")
    # businessIds = getAllBusinessIdsRelevantToCategories("yelp_academic_dataset_business.json","Liquor")
    # writeRelevantReviews("yelp_academic_dataset_review.json","reviews",businessIds)
    signOutAccount()
    for i in range(1,19):
        print(i)
        output = False
        signInToAccount("spindafi",i)
        while not output:
            getStatesAndCities()
            coordinates = getRandomCityCoordinates()
            businessName,businessId = getRandomBusinessName()
            review,stars = getAReview(businessId)
            # review,stars = "great place",5
            output = searchAndReviewPlace(coordinates,businessName,stars,review)
        signOutAccount()
