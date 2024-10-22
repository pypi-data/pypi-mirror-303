
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


# import os, py7zr

# def decompress_7z(input_file, output_dir):
#     """
#     Decompress a 7z file back to the original file(s) with a progress bar.
    
#     Parameters:
#         input_file (str): Path to the .7z file to be decompressed.
#         output_dir (str): Directory where the files should be extracted.
#     """
#     with py7zr.SevenZipFile(input_file, 'r') as archive:
#         file_list = archive.getnames()
#         total_files = len(file_list)
        
#         with tqdm(total=total_files, desc="Decompressing files", unit="file") as progress_bar:
#             for file in archive.read(targets=file_list).keys():
#                 progress_bar.update(1)
#         print(f"Decompressed {input_file} to {output_dir}")

# def list_7z_files():
#     """
#     List all 7z files in the current directory.
    
#     Returns:
#         list: A list of .7z files in the current directory.
#     """
#     return [file for file in os.listdir('.') if file.endswith('.7z')]

# def select_7z_file():
#     """
#     Let the user select a 7z file from the current directory.
    
#     Returns:
#         str: The selected 7z file path.
#     """
#     files = list_7z_files()
#     if not files:
#         print("No .7z files found in the current directory.")
#         return None
    
#     print("Select a .7z file to decompress:")
#     for idx, file in enumerate(files, 1):
#         print(f"{idx}. {file}")
    
#     choice = int(input("Enter the number of the file: ")) - 1
#     return files[choice] if 0 <= choice < len(files) else None


    # selected_file = select_7z_file()
    # if selected_file:
    #     output_directory = './comfy_portal'
    #     os.makedirs(output_directory, exist_ok=True)
    #     decompress_7z(selected_file, output_directory)
    # else:
    #     print("Operation canceled.")