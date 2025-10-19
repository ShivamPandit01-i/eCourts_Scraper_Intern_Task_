eCourts Cause List Downloader is a real-time web scraping application built using Flask, BeautifulSoup, and Requests.
It allows users to input State, District, Court Complex, Court Name, and Date, and automatically fetches the daily cause list PDFs directly from the official District Court (eCourts) website.

This project demonstrates practical implementation of:

Dynamic web scraping

Real-time data fetching

File handling and PDF management

Clean user interface with Flask templates

It’s developed as part of the Internshala eCourts Internship Task (October 2025).

🧠 Tech Stack

Python 3

Flask

BeautifulSoup4

Requests

HTML, CSS (for frontend)

🧾 Features

✅ Fetch cause lists dynamically for selected courts
✅ Download all available judge-wise PDFs in one click
✅ Store PDFs automatically by date in the /downloads/ folder
✅ Easy-to-use web interface (no coding needed)

📸 Example Use

Enter:

State → Delhi

District → New Delhi

Court Complex → Patiala House

Date → 2025-10-16

Click “Fetch Cause List”

PDFs are downloaded automatically in /downloads/202
