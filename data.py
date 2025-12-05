# data.py
from datetime import date

posts = [
    {
        "id": 1,
        "title": "Welcome to My Blog!",
        "content": "This is the first post on our new Flask + Bootstrap blog. We're excited to share ideas, tutorials, and stories with you!",
        "author": "Admin",
        "date": "December 4, 2025"
    },
    {
        "id": 2,
        "title": "Why Flask is Amazing",
        "content": "Flask is lightweight, flexible, and perfect for building web apps quickly — especially when paired with Bootstrap via CDN!",
        "author": "Admin",
        "date": "December 2, 2025"
    }
]

def get_next_id():
    return max(p["id"] for p in posts) + 1 if posts else 1