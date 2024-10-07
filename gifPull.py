import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()

# Number of gifs you wish to pull. Idk  whay but it only works with a max of 100 right now. open to ideas :)
number = 100

# Replace with your Giphy API key
API_KEY = os.getenv('GIPHY_API_KEY')

# Giphy API endpoint to fetch user GIFs
GIPHY_API_USER_ENDPOINT = 'https://api.giphy.com/v1/gifs'

# Define the export directory
EXPORT_DIR = '/workspaces/gifPull/lib'

# Giphy Channel Name
CHANNEL = os.getenv('GIPHY_CHANNEL')

# Function to fetch all GIFs from a user's Giphy account
def fetch_user_gifs(api_key, channel):
    gifs = []
    url = f'https://api.giphy.com/v1/channels/{channel}/gifs'
    params = {
        'api_key': api_key,
        'limit': number,  # Adjust the limit as needed to retrieve more GIFs per request
    }

    while url:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            fetched_gifs = response.json().get('data', [])
            gifs.extend(fetched_gifs)

            # Check if there is a next page
            pagination = response.json().get('pagination', {})
            next_offset = pagination.get('offset', 0) + pagination.get('count', 0)
            if pagination.get('total_count', 0) > next_offset:
                params['offset'] = next_offset
            else:
                break
        else:
            print(f'Failed to fetch GIFs. Status code: {response.status_code}')
            break

    return gifs

# Function to sanitize a string to be used as a filename
def sanitize_filename(name):
    return re.sub(r'[^\w\s-]', '_', name).strip().replace(' ', '_')

# Get and download GIFs at the highest resolution
def download_gifs(gifs):
    if not gifs:
        print('No GIFs to download.')
        return

    # Ensure the export directory exists
    os.makedirs(EXPORT_DIR, exist_ok=True)

    for gif in gifs:
        original = gif['images']['original']  # Get the highest resolution available
        gif_url = original['url']

        # Use the GIF's title or ID for the filename
        filename_base = sanitize_filename(gif.get('title', gif['id']))
        if not filename_base:
            filename_base = gif['id']

        gif_filename = os.path.join(EXPORT_DIR, f'{filename_base}_original.gif')

        # Download the GIF
        response = requests.get(gif_url)
        if response.status_code == 200:
            with open(gif_filename, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded: {gif_filename}')
        else:
            print(f'Failed to download GIF from {gif_url}')

# Main function
def main():
    # Fetch all GIFs from the user's Giphy account
    gifs = fetch_user_gifs(API_KEY, CHANNEL)
    download_gifs(gifs)

if __name__ == '__main__':
    main()

# You did it you pulled some gifs. You are a level .5 gif wizard now or something.