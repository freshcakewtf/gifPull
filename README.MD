# GIF Pull

This Python script allows you to fetch and download GIFs from a specific Giphy channel using the Giphy API. The script pulls a specified number of GIFs (up to 100) and saves them to a directory of your choice.

## Features
- Fetches GIFs from a specified Giphy channel.
- Downloads GIFs in the highest resolution available.
- Saves GIFs to a directory, with sanitized filenames based on the GIF title or ID.

## Prerequisites
1. **Python 3.x**
2. **Required Python Packages**:
   - `requests`
   - `python-dotenv`

   Install these by running:

   ```bash
   pip install requests python-dotenv

## Giphy API Key
**(You’ll need to obtain an API key from Giphy)[https://developers.giphy.com]**

## .env file
**Create a .env file in the root directory with the following variables**
    ```bash
    GIPHY_API_KEY=your_giphy_api_key  
    GIPHY_CHANNEL=your_giphy_channel_name  

## Setup
1.	Clone the repository or copy the script to your project.
2.	Ensure you have created a .env file with your Giphy API key and channel name.
3.	Define the export directory where GIFs will be saved. By default, it is set to /workspaces/gifPull/lib. You can change this by editing the EXPORT_DIR variable in the script.

## Usage
1. Run the script:
    ```bash
    python gifpulle.py
2.	The script will:
- Fetch up to 100 GIFs from your Giphy channel.
- Save them to the specified directory.

## Notes
- The script is currently limited to pulling a maximum of 100 GIFs at a time. You can modify the number variable to pull fewer GIFs. If you have suggestions on how to work around this limit, feel free to contribute!
- Filenames are sanitized to ensure compatibility with different file systems.

## Example Output

- The downloaded GIFs will be saved in the specified export directory with filenames like:
    ```bash
    funny_dog_original.gif
    cat_dance_original.gif

### Future Improvements
- Add support for fetching more than 100 GIFs in one run.
- Add a command-line interface for easier configuration.
- Handle errors more gracefully and improve logging.

