import requests
import time
from datetime import datetime

api_key = 'b1f4ec0a86974bafb71124001240312'  
cityes = ['Moscow', 'New York'] 

while True:
    print(f"Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (System Time)\n")
    
    for city in cityes:
        url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

        try:
            response = requests.get(url)
            data = response.json()

            location = data['location']['region']
            country = data['location']['country']
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']
            local_time = data['location']['localtime'] 
            print(f'Weather in {location}, {country} ({local_time}): {condition}')
            print(f'Temperature: {temperature}⁰C\n')

        except Exception as e:
            print(f"Error fetching data for {city}: {e}")

    print("-" * 40)
    time.sleep(1) 
