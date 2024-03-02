#!/usr/bin/python3
""" Fetching value from header response """
if __name__ == '__main__':
    import requests
    import requests.exceptions
    import sys

    val = sys.argv[1] if len(sys.argv) > 1 else ""
    values = {"q": val}
    post = requests.post('http://0.0.0.0:5000/search_user', values)
    try:
        val = post.json()
        if val:
            print("[{}] {}".format(val.get("id"), val.get("name")))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
