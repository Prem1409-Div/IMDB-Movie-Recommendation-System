import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import sys

# Force UTF-8 output for Windows terminals
sys.stdout.reconfigure(encoding='utf-8')

def scrape_imdb_1000_movies():
    """
    Scrapes 1000 movies from IMDb 2024 search results.
    Stays on the search page and clicks '50 more' repeatedly.
    """
    print("🚀 Starting IMDb Movie Scraper")
    print("=" * 70)
    
    # Setup Chrome
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Navigate to IMDb
    url = "https://www.imdb.com/search/title/?release_date=2024-01-01,2024-12-31"
    print(f"📍 Opening: {url}\n")
    driver.get(url)
    time.sleep(5)
    
    all_movies = []
    button_clicks = 0
    MAX_CLICKS = 60  # 50 initial + (60 × 50) = 3050 movies (buffer for duplicates)
    
    # Click "50 more" button repeatedly
    while button_clicks < MAX_CLICKS:
        print(f"\n{'='*70}")
        print(f"🔄 Load More Click #{button_clicks + 1}")
        print(f"{'='*70}")
        
        # Extract movies from current page state
        print("🔍 Extracting movies from page...")
        movie_items = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")
        print(f"   Found {len(movie_items)} total movie cards on page")
        
        # Process each movie item
        newly_added = 0
        for item in movie_items:
            try:
                full_text = item.text
                lines = full_text.split('\n')
                
                # Find title (line starting with number)
                title = None
                for line in lines:
                    # Check if line starts with a number followed by a period
                    if line and len(line) > 3 and line[0].isdigit():
                        if '. ' in line:
                            title = line.split('. ', 1)[1].strip()
                            break
                
                # Find storyline (longer text line, not metadata)
                storyline = ""
                for line in lines:
                    if (len(line) > 50 and 
                        not any(x in line for x in [
                            'Rate', 'Add to', 'Watchlist', 'TV-', 'PG-', 
                            'Metascore', 'Mark as', 'See more'
                        ])):
                        storyline = line
                        break
                
                # Add to list if valid and not duplicate
                if title and storyline:
                    if not any(m['Title'] == title for m in all_movies):
                        all_movies.append({
                            "Title": title,
                            "Storyline": storyline
                        })
                        newly_added += 1
                        
            except Exception as e:
                continue
        
        print(f"   ✅ Added {newly_added} new movies")
        print(f"   📊 Total movies collected: {len(all_movies)}")
        
        # Stop if we have 2000+
        if len(all_movies) >= 2000:
            print(f"\n🎉 Target reached! Collected {len(all_movies)} movies")
            break
        
        # Try to find and click "50 more" button
        try:
            print(f"\n🔽 Scrolling to find '50 more' button...")
            
            # Scroll to bottom to reveal button
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            # Find the button using multiple selectors
            button = None
            try:
                # Try finding by text content
                button = driver.find_element(By.XPATH, "//button[contains(., '50 more')]")
            except:
                try:
                    # Try alternate selector
                    button = driver.find_element(By.CSS_SELECTOR, "button.ipc-see-more__button")
                except:
                    pass
            
            if button:
                # Scroll button into view
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                time.sleep(1)
                
                # Try to click
                try:
                    button.click()
                except Exception:
                    # Fallback to JS click if intercepted
                    print("   ⚠️  Standard click failed, trying JS click...")
                    driver.execute_script("arguments[0].click();", button)
                
                button_clicks += 1
                print(f"   ✅ Clicked '50 more' button!")
                print(f"   ⏳ Waiting for new movies to load...")
                time.sleep(5)  # Wait for content to load
            else:
                print(f"   ⚠️  Button not found")
                break
                
        except Exception as e:
            print(f"   ⚠️  Could not click button: {str(e)}")
            print(f"   Stopping with {len(all_movies)} movies")
            break
    
    # Save results
    print(f"\n{'='*70}")
    print("💾 SAVING DATA")
    print(f"{'='*70}")
    
    final_movies = all_movies[:2000]  # Take first 2000
    df = pd.DataFrame(final_movies)
    df.to_csv("imdb_2024_movies.csv", index=False)
    
    print(f"✅ SUCCESS!")
    print(f"📁 File: imdb_2024_movies.csv")
    print(f"📊 Movies saved: {len(df)}")
    print(f"{'='*70}\n")
    
    driver.quit()

if __name__ == "__main__":
    scrape_imdb_1000_movies()
