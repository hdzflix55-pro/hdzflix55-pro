import requests
from bs4 import BeautifulSoup
import os
import time

# --- CONFIGURATION ---
URL = "YAHAN_WO_URL_DAALO_JISSE_MOVIES_UTHAANI_HAI"
FILE_NAME = "movies_list.txt"
LAST_MOVIE_FILE = "last_movie.txt"

def get_latest_movie():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # YAHAN TUMHE CHANGE KARNA HAI:
        # Website inspect karke dekho movie ka title kahan hai
        # Example: movie = soup.find('h2', class_='post-title').text.strip()
        movie = soup.find('h2').text.strip() 
        
        return movie
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def push_to_github(movie_name):
    with open(FILE_NAME, 'a') as f:
        f.write(movie_name + "\n")
    
    with open(LAST_MOVIE_FILE, 'w') as f:
        f.write(movie_name)
        
    os.system("git add .")
    os.system(f'git commit -m "Auto-update: {movie_name}"')
    os.system("git push origin main")
    print(f"Pushed: {movie_name}")

# --- MAIN LOOP ---
while True:
    print("Checking for updates...")
    current_movie = get_latest_movie()
    
    if current_movie:
        if os.path.exists(LAST_MOVIE_FILE):
            with open(LAST_MOVIE_FILE, 'r') as f:
                last_movie = f.read()
        else:
            last_movie = ""

        if current_movie != last_movie:
            push_to_github(current_movie)
        else:
            print("No new movies found.")
            
    time.sleep(3600) # 1 ghanta wait karega
