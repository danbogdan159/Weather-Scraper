from bs4 import BeautifulSoup
import requests

zip = None
# zip = input("Provide zip code:")
url = f"https://weather.com/weather/today/l/{zip}"
if isinstance(zip, int):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        currentTemp = soup.find("span", class_="CurrentConditions--tempValue--zUBSz")
        location = soup.find(class_ = "CurrentConditions--location--yub4l")
        print(f"The current temperature in {location.text} is {currentTemp.text} F.")
    else:
        print("Error fetching data")
else:
    print("Please provide a zip code as an integer")