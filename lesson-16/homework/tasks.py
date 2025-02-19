import threading
def print_theard():
    print("Current thread name:", threading.current_thread().name)

threads = []
for i in range(7):
    thread = threading.Thread(target=print_theard)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

import threading
import urllib.request
def down_file(url, filename):
    print(f"\nDownloading {filename} from {url}...")
    urllib.request.urlretrieve(url, filename)
    print(f"\n{filename} downloaded successfully.")

files_to_download = [
    {"url": "https://en.wikipedia.org/wiki/British_logistics_in_the_Normandy_campaign", "filename": "i:\wfile1"},
    {"url": "https://en.wikipedia.org/wiki/Graph_(abstract_data_type)", "filename": "i:\Graph_abstract_data_type"},
    {"url": "https://example.com/", "filename": "i:\example"}
]

threads = []

for file_info in files_to_download:
    thread = threading.Thread(
        target=down_file,
        args=(file_info["url"], file_info["filename"])
    )
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

import threading
def even_numbers():
    print("List of even numbers:")
    for i in range(30, 51, 2):
        print(i, end = " ")

def odd_numbers():
    print("\nList of odd numbers:")
    for i in range(31, 51, 2):
        print(i, end = " ")

even_thread = threading.Thread(target=even_numbers)
odd_thread = threading.Thread(target=odd_numbers)
even_thread.start()
odd_thread.start()
even_thread.join()
odd_thread.join()

import threading

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def calculate_factorial(n):
    print(f"\nCalculating factorial of {n} in thread {threading.current_thread().name}")
    result = factorial(n)
    print(f"Factorial of {n} is {result} in thread {threading.current_thread().name}")

n = 12

thread1 = threading.Thread(target=calculate_factorial, args=(n,))
thread2 = threading.Thread(target=calculate_factorial, args=(n,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

import requests
import threading
def make_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")
urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org"
]
threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()

import requests
import threading
def request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")

urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org"
]

threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

import sqlite3

conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()

table = '''CREATE TABLE IF NOT EXISTS users (
    name VARCHAR,
    id INTEGER PRIMARY KEY,
    age INTEGER
)'''
isert_value = "insert into my_database.sqlite('madina,234,15)"
cursor.execute(table)
