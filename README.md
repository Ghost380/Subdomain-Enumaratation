# Subdomain Enumerator 🕵️‍♂️

A simple and fast Python script to discover subdomains for a given domain using a wordlist. This tool demonstrates basic reconnaissance techniques, web requests, and concurrent processing.

## ✨ Features

-   **Fast Enumeration**: Uses multithreading to check multiple subdomains concurrently.
-   **Easy to Use**: Simple command-line interface.
-   **Customizable**: Use any wordlist you provide.

## 🛠️ Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/subdomain-enumerator.git](https://github.com/your-username/subdomain-enumerator.git)
    cd subdomain-enumerator
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## 🚀 Usage

Run the script from your terminal using the following command structure.

```sh
python subdomain_enumerator.py -d <domain> -w <wordlist_path>
```

### Example

```sh
python subdomain_enumerator.py -d example.com -w wordlist.txt
```

### Command-line Arguments

-   `-d`, `--domain`: **(Required)** The target domain (e.g., `google.com`).
-   `-w`, `--wordlist`: **(Required)** The path to the file containing subdomains to test.
-   `-t`, `--threads`: (Optional) The number of threads to use for scanning (default is 10).

### Example with more threads

```sh
python subdomain_enumerator.py -d example.com -w wordlist.txt -t 50
```

## 📜 License

This project is licensed under the MIT License.