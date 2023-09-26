import sqlite3
import requests
import json
from bs4 import BeautifulSoup


# creation of database for storage of recorded quotes

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS test 
                  (id INTEGER PRIMARY KEY, 
                  quote TEXT,
                  URL TEXT)''')

conn.commit()



# connecting to the hugging face api
API_TOKEN = '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'

API_URL = "https://api-inference.huggingface.co/models/Hate-speech-CNERG/dehatebert-mono-english"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


#will allow the user to select url to scrape

#URL = input('Enter Target URL: ')
URL = 'https://www.theguardian.com/world/2022/jul/24/viktor-orban-against-race-mixing-europe-hungary'
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

# Get the whole body tag
tag = soup.findAll('p')


# Access each body tag's string recursively
for string in tag:

    output = query({
	"inputs": f"{string.text}"
    })

    

    #<class 'list'>
    #[[{'label': 'NON_HATE', 'score': 0.9632159471511841}, {'label': 'HATE', 'score': 0.036784060299396515}]]
    # print(type(output))
    # print(output)
    
    output = output[0]



    #This is why we access as  parsed_data[0][0]['label']  first list, first or second dictionary, label or score 

    #[
    #   [
    #     {
    #       "label": "NON_HATE",
    #       "score": 0.9776114225387573
    #     },
    #     {
    #       "label": "HATE",
    #       "score": 0.02238861285150051
    #     }
    #   ]
    # ]


    
    # # Access the values #fix this bug 
    label1 = output[0]["label"]
    score1 = output[0]["score"]

    label2 = output[1]["label"]
    score2 = output[1]["score"]

    

    

    # #if the comment is negative lets append it to the database
    if score2 > 0.20:
        cursor.execute("INSERT INTO test (quote, URL) VALUES (?, ?)", (string.text, URL))
        conn.commit()
        

    


cursor.execute('SELECT * FROM test')
rows = cursor.fetchall()

if len(rows) == 0:
    print("The database is empty.")
else:
    print("The database is not empty.")

conn.close()