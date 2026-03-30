import sqlite3
import os

API_KEY = "sk-1234567890abcdef"  

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchall()

def process_items(items):
    result = []
    for item in items:
        user = get_user(item["user_id"])
        result.append(user)
    return result

def calculate_total(orders):
    total = 0
    for order in orders:
        total += order["amount"]
    return total
