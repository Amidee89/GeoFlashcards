import requests
from bs4 import BeautifulSoup
import os

# Use a session to re-use the connection
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
})

def download_svg(url, folder_path):
    try:
        # Parse the filename from the URL
        filename = url.split("/")[-1]
        file_path = f"{folder_path}/{filename}"
        
        # Check if file already exists
        if os.path.exists(file_path):
            print(f"File '{filename}' already exists. Skipping download.")
            return
        
        # If the file doesn't exist, proceed with download
        response = session.get(url, stream=True, allow_redirects=True)
        
        if response.status_code == 200:
            response.raw.decode_content = True
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
            print(f"Downloaded: {filename}")
        else:
            print(f"Unable to retrieve the image: {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading the image: {url}. Error: {str(e)}")


def main():
    # URL of the category page
    url = "https://commons.wikimedia.org/wiki/Category:SVG_locator_maps_of_territories_of_Antarctica_(16:9_regional_location_map_scheme)"
    
    # Folder for downloaded SVGs
    output_folder = "downloaded_svgs"
    os.makedirs(output_folder, exist_ok=True)

    # Send HTTP request
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for a_tag in soup.find_all("a", href=True, class_="galleryfilename"):
        if "/wiki/File:" in a_tag['href']:
            file_page_url = f"https://commons.wikimedia.org{a_tag['href']}"
            print(file_page_url)
            # Request the individual file page
            file_page_response = requests.get(file_page_url)
            file_soup = BeautifulSoup(file_page_response.content, 'html.parser')

            # Find the SVG file URL
            svg_url_tag = file_soup.find("a", href=lambda href: href and href.endswith(".svg"))
            if svg_url_tag:
                svg_url = svg_url_tag['href']  # Remove the "https:" prefix here
                download_svg(svg_url, output_folder)

if __name__ == "__main__":
    main()
