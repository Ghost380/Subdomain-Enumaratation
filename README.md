
# Subdomain Enumerator

A fast and simple Python tool for discovering subdomains of a target domain using a customizable wordlist. This script leverages multithreading for efficient enumeration and includes smart detection to reduce false positives.

![Screenshot](https://i.imgur.com/b0yCg1L.png)

---

## Features

- **Interactive**: Prompts for the target domain.
- **Multithreaded**: Checks multiple subdomains concurrently for speed.
- **Customizable Threads**: Set the number of threads for performance tuning.
- **Wildcard Detection**: Identifies wildcard DNS to avoid false positives.
- **Protocol Checking**: Tries `https` first, then falls back to `http`.
- **Minimal Dependencies**: Requires only Python and the `requests` library.

---

## Requirements

- Python 3.x
- `requests` library

---

## Installation

Install the required Python package:

```sh
pip install requests
```

---

## Usage

1. **Prepare the Wordlist**

   - Create a file named `wordlist.txt` in the same directory as the script.
   - Add potential subdomain names, one per line.

2. **Run the Script**

   Open a terminal, navigate to the project directory, and run:

   ```sh
   py subdomain_enumerator.py
   ```

   The script will prompt you to enter the target domain.

3. **Optional: Set Number of Threads**

   Use the `-t` or `--threads` flag to specify the number of concurrent threads (default is 20):

   ```sh
   py subdomain_enumerator.py -t 50
   ```

---

## Example

```sh
py subdomain_enumerator.py
# Enter target domain when prompted

py subdomain_enumerator.py -t 50
# Uses 50 threads for faster enumeration
```

---

## License

This project is licensed under the terms of the LICENSE file.

