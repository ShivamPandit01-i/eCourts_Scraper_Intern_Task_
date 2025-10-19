from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import pdfkit
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        state = request.form['state']
        district = request.form['district']
        court_complex = request.form['court_complex']
        court_name = request.form['court_name']
        date = request.form['date']

        # Construct the URL (example for Delhi Courts)
        # You can modify for other states/districts
        url = f"https://newdelhi.dcourts.gov.in/cause-list-%E2%81%84-daily-board/"

        # Fetch the page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract links of PDFs
        pdf_links = []
        for a in soup.find_all('a', href=True):
            if a['href'].endswith('.pdf'):
                pdf_links.append(a['href'])

        # Download PDFs
        downloaded_files = []
        for link in pdf_links:
            filename = link.split('/')[-1]
            pdf_data = requests.get(link)
            with open(filename, 'wb') as f:
                f.write(pdf_data.content)
            downloaded_files.append(filename)

        return f"Downloaded PDFs: {', '.join(downloaded_files)}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
