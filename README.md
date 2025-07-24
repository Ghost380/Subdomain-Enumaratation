# Simple Subdomain Enumerator

A fast, simple, and effective Python script for discovering subdomains of a given domain using a wordlist. This tool uses multithreading to perform checks concurrently, making the enumeration process significantly faster.

![A screenshot of the terminal showing the script running and finding subdomains.](https://i.imgur.com/b0yCg1L.png)

---

## Features

-   **User-Friendly**: Prompts for the target domain interactively.
-   **Fast Enumeration**: Uses a thread pool to check multiple subdomains at once.
-   **Customizable Threads**: Allows you to specify the number of threads for performance tuning.
-   **Wildcard Detection**: Automatically checks for wildcard DNS configurations to reduce false positives.
-   **Smart Protocol Checking**: Tries to connect via `https` first and falls back to `http`.
-   **Minimal Dependencies**: Only requires Python and the `requests` library.

---

## Requirements

-   Python 3.x
-   The `requests` library

---

## Setup & Usage

### 1. Install Dependencies

If you don't have the `requests` library installed, open your terminal and run:

```bash
pip install requests

2. Prepare the Wordlist
Create a file named wordlist.txt in the same directory as the script. Add a list of potential subdomain names to this file, with one name per line.

Example wordlist.txt:

www
api
dev
test
blog
shop
mail
ftp
staging

3. Run the Script
Open a terminal, navigate to the project directory, and run the script using the py or python command.

py subdomain_enumerator.py

The script will then prompt you to enter the target domain.

Optional: Specify Number of Threads
You can use the -t or --threads flag to set the number of concurrent threads (default is 20).

py subdomain_enumerator.py -t 50

Example
Here is an example of running the script and its potential output:

# Navigate to the script's directory
C:\Users\YourUser\Desktop> cd SubdomainTool

# Run the script
C:\Users\YourUser\Desktop\SubdomainTool> py subdomain_enumerator.py

# The script will prompt for input
Enter the target domain (e.g., google.com): example.com

# The script starts the enumeration process
[*] Starting subdomain enumeration for: example.com
[*] Using wordlist: wordlist.txt
[*] Number of threads: 20
--------------------------------------------------
[+] Found Subdomain: [https://www.example.com](https://www.example.com)
[+] Found Subdomain: [https://blog.example.com](https://blog.example.com)
--------------------------------------------------
[*] Enumeration complete.
