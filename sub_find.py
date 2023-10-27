import requests

Domain = input("Enter your domain: ")
def subfinder():
    sub_domain = "word.txt"

    with open(sub_domain, "r") as file:
            file1 = file.read().splitlines()  # Split the lines in the file into a list

    for sub in file1:
        url = f"https://{sub}.{Domain}"
        try:
         response = requests.get(url)
         response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
         if response.status_code == 200:
              print(f"Found: {url}")
        except requests.RequestException as e:
         print(f"Error with {url}: {e}")

subfinder()