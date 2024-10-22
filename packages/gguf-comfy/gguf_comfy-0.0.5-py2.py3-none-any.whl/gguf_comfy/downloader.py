
import requests
from tqdm import tqdm

def download_7z_file(url, output_filename):
    """
    Download a 7z file from a URL to the current directory with a progress bar.
    
    Parameters:
        url (str): URL of the 7z file to download.
        output_filename (str): Name for the downloaded file.
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        with open(output_filename, 'wb') as file, tqdm(
            desc=f"Downloading {output_filename}",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                progress_bar.update(len(chunk))
        print(f"Downloaded {output_filename} to the current directory.")
    else:
        print("Failed to download the file. Please check the URL.")

url = "https://github.com/calcuis/gguf-comfy/releases/download/0.0.2/ComfyUI_GGUF_windows_portable.7z"
output_filename = "comfy.7z"
download_7z_file(url, output_filename)