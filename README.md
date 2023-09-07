# google_maps_scraper

Google Maps Scraper
Overview
This repository contains a Python-based tool for scraping Google Maps to collect information about places with specific keywords. This tool uses Google's Places API to search for places within a certain radius from a given latitude and longitude.

The primary objective of this scraper is to populate listings for Tidal Directory, a local business directory.

Features
Collects the names and addresses of places based on keywords.
Customizable search radius.
JSON output support for easy data storage and manipulation.
Installation and Setup
Clone the Repository

bash
Copy code
git clone https://github.com/jamesmarkosborne/google_maps_scraper.git
cd google_maps_scraper
Install Dependencies

Make sure Python 3.x is installed and run:

Copy code
pip install -r requirements.txt
Set up Google API Key

Obtain a Google Maps API key and set it up in the google_maps_scraper.py file:

python
Copy code
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')
Usage
Configure the search parameters

Update location and radius in google_maps_scraper.py to set your search location and radius, respectively.

Run the Script

Copy code
python google_maps_scraper.py
Check Output

The scraped data will be stored in a JSON file, and a summary will be displayed in the terminal.

Known Issues
Warning message for OpenSSL might appear for certain Python versions.
Contributing
Feel free to contribute to this project by opening issues or sending pull requests.

License
MIT License. See LICENSE for details.
