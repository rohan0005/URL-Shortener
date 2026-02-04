# URL-Shortener
 A Django web application which can short URLs and manage them. 


## Features

# User Authentication and Access

1. User registration, login, and logout functionality
2. Only authenticated users can create, manage, and view short URLs

# URL Shortening and Redirection

1. Authenticated users can shorten long URLs into compact, shareable links
2. Unique short keys are generated using a Base62 encoding algorithm
3. Short URLs automatically redirect users to the original long URLs

# URL Management Dashboard

1. Users can view a personalized list of all their created short URLs
2. Edit existing URLs (e.g, edit short url, delete url)

# URL Expiration Control

1. Users can set an expiration time for each short URL
2. Expired links are automatically disabled

# Analytics

1. Track the number of clicks for each short URL
2. Show additional metadata including creation date and expiration status

# QR Code Generation

1. Generate QR codes for short URLs
2. QR codes can be viewed or downloaded for easy sharing on mobile devices
3. QR codes can be viewed on dashboards as well


## Installation Guide

To run the RoomRent platform locally, follow these steps:

1. Install Python
Install python-10 or 11 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://www.tomshardware.com/how-to/install-python-on-windows-10-and-11

2.  Setup virtual environment

    Install Virtual environment
    py -m venv .venv

    Activate the venv
   
        Windows: .\venv\Scripts\activate
        Mac/Linux: source .venv/bin/activate

3.  Clone git repository

        git clone "https://github.com/rohan0005/URL-Shortener.git"

4.  Install requirements

        cd roomrent/
        pip install -r requirements.txt


6.  Run the migration command

      #### Make migrations
        -python manage.py makemigrations
        -python manage.py migrate

8.  Run the server

    Run the server
    
        python manage.py runserver 8000
      
   # your server is up on port 8000
   # Run this url
       http://127.0.0.1:8000/home