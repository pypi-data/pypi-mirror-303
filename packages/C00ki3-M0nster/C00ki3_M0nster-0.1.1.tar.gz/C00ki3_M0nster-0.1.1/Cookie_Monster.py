import requests
from bs4 import BeautifulSoup
import re

# Function to extract cookies and tokens from a URL
def extract_cookies_and_tokens(url):
    response = requests.get(url)
    cookies = response.cookies
    headers = response.headers
    html = response.text

    cookie_details = {cookie.name: cookie.value for cookie in cookies}
    token_details = {}

    # Extract tokens from headers
    for header in headers:
        if 'token' in header.lower():
            token_details[header] = headers[header]

    # Extract tokens from JavaScript
    soup = BeautifulSoup(html, 'html.parser')
    scripts = soup.find_all('script')
    for script in scripts:
        text = script.string
        if text:
            tokens = re.findall(r'(?i)\b(token|auth|session)[^\s]*\s*[:=]\s*["\']([^"\']+)["\']', text)
            for match in tokens:
                token_name, token_value = match
                token_details[token_name] = token_value

    return cookie_details, token_details

# Function to analyze cookies
def analyze_cookie(cookie_name, cookie_value):
    print(f"Analyzing Cookie: {cookie_name}")
    if 'session' in cookie_name.lower():
        print("[!] Cookie may be a session cookie.")
    if 'token' in cookie_name.lower():
        print("[!] Cookie may be a token.")
    print("")

# Function to analyze tokens
def analyze_token(token_name, token_value):
    print(f"Analyzing Token: {token_name}")
    if 'session' in token_name.lower():
        print("[!] Token may be a session token.")
    if 'auth' in token_name.lower():
        print("[!] Token may be an authentication token.")
    print("")

# Function to scan a website for cookies and tokens
def scan_website(url):
    print(f"[*] Scanning website: {url}")
    cookies, tokens = extract_cookies_and_tokens(url)
    for name, value in cookies.items():
        print(f"[*] Cookie: {name} = {value}")
        analyze_cookie(name, value)
    for name, value in tokens.items():
        print(f"[*] Token: {name} = {value}")
        analyze_token(name, value)

def main(url):
    scan_website(url)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 Cookie_Monster.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    main(url)
