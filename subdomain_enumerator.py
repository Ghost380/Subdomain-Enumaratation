import requests
import sys
import argparse
import uuid
from concurrent.futures import ThreadPoolExecutor

# Disable insecure request warnings for self-signed SSL certificates
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def check_subdomain(subdomain, domain):
    """
    Checks if a subdomain exists by trying HTTPS and then HTTP.
    """
    for protocol in ['https', 'http']:
        url = f"{protocol}://{subdomain}.{domain}"
        try:
            requests.get(url, timeout=3, verify=False, allow_redirects=False)
        except requests.exceptions.RequestException:
            continue
        else:
            print(f"[+] Found Subdomain: {url}")
            return
            
def has_wildcard(domain):
    """
    Checks for a wildcard subdomain by testing a random, non-existent subdomain.
    """
    random_sub = f"{uuid.uuid4().hex[:12]}.{domain}"
    try:
        requests.get(f"https://{random_sub}", timeout=3, verify=False, allow_redirects=False)
        return True
    except requests.exceptions.RequestException:
        return False

def main():
    """
    Main function to parse arguments and run the enumeration.
    """
    # Setup argument parser ONLY for threads
    parser = argparse.ArgumentParser(description="A simple and fast subdomain enumerator.")
    parser.add_argument("-t", "--threads", help="Number of threads to use (default: 20).", type=int, default=20)
    args = parser.parse_args()

    # --- MODIFIED SECTION ---
    # Get domain directly from user input
    domain = input("Enter the target domain (e.g., google.com): ").strip()
    if not domain:
        print("[-] Error: Domain cannot be empty.")
        sys.exit(1)
        
    # Hardcode the wordlist path
    wordlist_path = "wordlist.txt"
    # --- END OF MODIFIED SECTION ---

    num_threads = args.threads
    
    print(f"[*] Starting subdomain enumeration for: {domain}")
    print(f"[*] Using wordlist: {wordlist_path}")
    print(f"[*] Number of threads: {num_threads}")
    print("-" * 50)
    
    if has_wildcard(domain):
        print("[!] Warning: Wildcard subdomain detected. Results may include false positives.")
        print("-" * 50)

    try:
        with open(wordlist_path, 'r') as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[-] Error: Wordlist file '{wordlist_path}' not found in the current directory.")
        sys.exit(1)

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(lambda sub: check_subdomain(sub, domain), subdomains)

    print("-" * 50)
    print("[*] Enumeration complete.")

if __name__ == "__main__":
    main()