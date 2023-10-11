import requests
from bs4 import BeautifulSoup

def scrape_leetcode_profile(username):
    url = f'https://leetcode.com/{username}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Locate the HTML elements containing your profile data
    profile_data = soup.find('div', {'class': 'user-info__username'})
    return profile_data.text if profile_data else 'Profile not found'

def scrape_gfg_profile(username):
    # Similar code to scrape GFG profile
    return ""

if __name__ == '__main__':
    leetcode_username = 'DxBros'
    gfg_username = 'YourGFGUsername'

    leetcode_profile = scrape_leetcode_profile(leetcode_username)
    gfg_profile = scrape_gfg_profile(gfg_username)

    print(f'LeetCode Profile: {leetcode_profile}')
    print(f'GeeksforGeeks Profile: {gfg_profile}')