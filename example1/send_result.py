import requests

def send_result():
    url = "https://yourusername.github.io/your-repo-name/index.html"  # Replace with your GitHub Pages URL
    params = {
        "check_name": "hello world",
        "status": "pass",
        "message": "The hello world check passed!"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Result sent successfully!")
    else:
        print(f"Failed to send result: {response.status_code}")

if __name__ == "__main__":
    send_result()
