import MPLI # Importing the MPLI module

MPLI.welcome("ARJUN")
MPLI.goodbye("NAGARJUN")


# File: Day25/main.py

import MPLI as mpli  # Importing the MPLI module with an alias
mpli.welcome("Harshith")


import greet.greeting as greeting  # Importing the greeting module from greet package
greeting.greet()


# Importing the wikipedia module to fetch summaries of topics
# First you need to install "pip install wikipedia" in your terminal

import wikipedia

print(wikipedia.summary("Puneeth rajkumar", sentences=10))  # Fetching a summary of the topic "Puneeth Rajkumar"
