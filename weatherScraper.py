from bs4 import BeautifulSoup
import requests

url = f"https://weather.com/weather/today/l/{zip}"

class data:
    location = None
    temp = None
    def __init__(self, z):
        self.zip = z
    def retrieveData(x):
        if isinstance(x.zip, int):
            url = f"https://weather.com/weather/today/l/{x.zip}"
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                x.temp = soup.find("span", class_="CurrentConditions--tempValue--zUBSz").text
                x.location = soup.find(class_ = "CurrentConditions--location--yub4l").text
                print(f"The current temperature in {x.location} is {x.temp} F.")
            else:
                print("Error fetching data")
        else:
            print("Please provide a zip code as an integer")

userInput = int(input("Provide zip code:"))
print(type(userInput))
userZip = data(userInput)
userZip.retrieveData()
# issue: zips with leading 0 do not work.
