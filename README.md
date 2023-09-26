# Hate Speech Detection and Database Storage

## Overview

This Python script is designed to scrape text from a specified web page, analyze the text for hate speech using the Hugging Face API, and store any identified hateful quotes in a SQLite database. The script provides a streamlined way to monitor online content for hate speech and maintain a record of problematic quotes.

## Prerequisites

Before using this script, ensure you have the following prerequisites in place:

1. **Python**: The script is written in Python, so you need a Python interpreter installed on your system.

2. **Required Libraries**:
   - `sqlite3`: For managing the SQLite database.
   - `requests`: To make HTTP requests to web pages and the Hugging Face API.
   - `json`: For parsing JSON responses from the API.
   - `bs4` (Beautiful Soup): For web scraping.
   
   You can install these libraries using `pip` if they are not already installed:


3. **Hugging Face API Token**: You will need to obtain an API token from Hugging Face to access their hate speech detection model. Replace the placeholder in the script with your actual API token.

## Setup

1. **Database Creation**: The script creates a SQLite database named `example.db` to store recorded quotes. A table named `test` with columns `id`, `quote`, and `URL` is created within the database. Ensure that you have write permissions in the script's directory.

2. **Hugging Face API Token**: Replace the `API_TOKEN` variable in the script with your valid Hugging Face API token.

3. **Target URL**: You can choose a target URL to scrape. You can either prompt the user to enter a URL or hardcode it in the script.

## Usage

1. The script sends an HTTP request to the specified URL and uses Beautiful Soup to parse the HTML content, extracting all the `<p>` (paragraph) tags.

2. For each paragraph, it sends the text to the Hugging Face API for hate speech detection using the `query` function. The API response includes labels and scores.

3. If the score for the "HATE" label is greater than 0.20, the script inserts the quote and the URL into the SQLite database.

4. After processing all paragraphs, the script checks if the database is empty or not.

5. The database connection is closed at the end of the script.

## Customization

- You can customize the threshold for hate speech detection by adjusting the value `0.20` in the script to your desired threshold.
- This script serves as a basic example and may require further customization and refinement for your specific use case.

## Example

Here's an example of how to run the script:

```shell
python your_script.py
