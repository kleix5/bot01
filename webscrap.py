import requests
from bs4 import BeautifulSoup

def scrape_accommodation_data(city):
    # Define the URL for the city on booking.com
    url = f'https://www.booking.com/searchresults.en-gb.html?city={city}'

    # Send an HTTP request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML elements containing accommodation information
        accommodation_elements = soup.find_all('div', class_='sr_property_block')

        # Create a list to store parsed data
        accommodation_data = []

        for element in accommodation_elements:
            # Extract relevant information (modify based on the actual HTML structure)
            name = element.find('span', class_='sr-hotel__name').text.strip()
            location = element.find('span', class_='location_score').text.strip()
            availability = element.find('div', class_='bui-u-sr-only').text.strip()

            # Store the data in a dictionary
            data_entry = {
                'name': name,
                'location': location,
                'availability': availability
            }

            accommodation_data.append(data_entry)

        return accommodation_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# Example usage for New York City
nyc_data = scrape_accommodation_data('New York City')

# Example usage for Boston
boston_data = scrape_accommodation_data('Boston')

# Print the results
print("Accommodation data for New York City:")
print(nyc_data)

print("\nAccommodation data for Boston:")
print(boston_data)

