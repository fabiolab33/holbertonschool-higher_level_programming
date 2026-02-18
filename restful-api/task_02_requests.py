#!/usr/bin/python3
"""
Module that fetches and processes data from JSONPlaceholder API.
"""

import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch posts from the API and print their titles.
    """
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts from the API and save selected fields to posts.csv.
    """
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        structured_data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(structured_data)
