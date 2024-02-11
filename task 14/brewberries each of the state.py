import requests

url = "https://api.openbrewerydb.org/breweries"  # Url to fetch the data

def fetch_data(url, params=None):       # Function initiated to fetch the data from url.
    response = requests.get(url, params=params)
    return response.json()

states = ['Alaska', 'Maine', 'New York']    # Task 1: List of breweries in Alaska, Maine, and New York.
for state in states:                        # iterate method the get the individual state from the list.
    print(f"\nBreweries in {state}:")       # Display the Breweries state list
    breweries1 = fetch_data(url, {'state': state})  # fetch the breweries data in state list
    for brewery in breweries1:                  # For loop method to iterate breweries list in the given list.
        print(brewery['name'])                  # Display the breweries in the given state list.

print("\nCount of breweries in each state:")        # Count the breweries in each state 
for state in states:                                # iterate method to get the count in states list.
    breweries2 = fetch_data(url, {'state': state})  # fetch the data to get the 
    print(f"{state}: {len(breweries2)}")

print("\nNumber of types of breweries in individual cities:")   # Count the number of types of breweries in individual cities.
for state in states:                # iterate method the get the individual state from the list.
    print(f"\n{state}:")            # display the brewery state.
    breweries3 = fetch_data(url, {'state': state})  # fetch the cities of brewery from the given state list. 
    for brewery in breweries3:      # iterate method the get the cities in the individual state list
        city = brewery['city']      # Brewery city
        types = brewery['brewery_type'] # Brewery type
        print(f"{city}: {types}")       # Display the Brewery city and the type.

print("\nCount and list of breweries with websites:")   # Display Count and list how many breweries having websites.
for state in states:                # iterate method to get the individual state from the list.
    breweries_in_state = fetch_data(url, {'state': state})  # fetch the data from the url.
    websites_count = 0              # empty count to fed the value.
    print(f"\n{state}:")            # Display the given state list.
    for brewery in breweries_in_state:  # iterate method get the cities having the website.
        if brewery['website_url']:
            websites_count += 1         # if the breweries having website count will be added.
            print(f"{brewery['name']}: {brewery['website_url']}")   # Display the brewery company name and the website link.
    print(f"Total breweries with websites: {websites_count}")       # Display the total count of brewery having websites.  
