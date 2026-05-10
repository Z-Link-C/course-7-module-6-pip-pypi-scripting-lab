from datetime import datetime
import os
import requests

def generate_log(data):
    # TODO: Implement log generation logic
    if not isinstance(data,list):
        raise ValueError("This should be a list")
    log_data=data
    filename=(f"log_{datetime.now().strftime("%Y%m%d")}.txt")
    #filename=(f"log_{datetime.now().strftime('%Y%m%d')}.txt")

    with open(filename,"w") as file:
        for e in log_data:
            file.write(f"{e}\n")
    print(f"Log written to {filename}")
    return filename
def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
