import requests
from bs4 import BeautifulSoup

def fetch_dreams(series_list, min_value, max_value, n):
    dreams = []  # Initialize an empty list to store dreams

    for series in series_list:
        url = f'https://dreambank.net/random_sample.cgi?series={series}&min={min_value}&max={max_value}&n={n}'
        
        print(f"Attempting to fetch URL: {url}")
        response = requests.get(url)

        if response.status_code == 200:
            print("Successfully fetched the page!")
            
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract dream text using the appropriate selector
            dream_divs = soup.find_all('span')  # Change this to the appropriate tag that contains the dream text
            
            for dream in dream_divs:
                dream_text = dream.get_text(strip=True)  # Get the text of each dream
                if dream_text:  # Ensure that the dream text is not empty
                    dreams.append(dream_text)  # Add the dream text to the list
        else:
            print(f"Failed to fetch dreams for series '{series}'. Status code: {response.status_code}")

    return dreams  # Move the return statement outside of the loop

# Example usage
series_list = [
    'angie',
    'arlie',
    'b',
    'bay_area_girls_456'
]

fetched_dreams = fetch_dreams(series_list, 50, 300, 100)
print(f"Fetched {len(fetched_dreams)} dreams:")
for dream in fetched_dreams:
    print(dream)
