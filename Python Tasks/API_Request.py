import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    data = response.json()
    if data:
        for post in data[:5]:  # Displaying first 5 posts
            print("Post ID:", post["id"])
            print("Title:", post["title"])
            print("Body:", post["body"])
            print("-" * 40)
    else:
        print("No data available.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
