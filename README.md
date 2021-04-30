#Automation Home Assignment by Mark Ambrus

The project consists of two parts: Python and Google App Scripts.

##Requirements
The Python part was written using python 3.9.0.
For development MacOS was used.

##Installation:
###Python
Navigate into the root directory and execute the following command:

```
install.sh
```

If you have trouble running the code above enter `chmod +x` then try
again.

This is an important step, as it sets up the virtual environment, installs all
dependencies and concludes the Google authentication process via a browser.
If the `install.sh` command would not execute properly, you can execute these
steps manually via the following commands:

```source bin/activate
pip install -r requirements.txt
python3 google_auth.py
```

You also need to create an OAuth 2.0 Client IDs on the following website:
https://console.cloud.google.com/apis/credentials
by clicking Create Credentials on the top.
Then save it as credentials.json in the root directory of the project.

```
export GOOGLE_APPLICATION_CREDENTIALS="creds.json"
```

In the `emails.csv` file include all email addresses to which you would like to
send the emails.

###Google App Script

1. Go to https://script.google.com
2. Create a new project and open it
3. Replace the content of the Code.gs on the website with the content of the
   `Code.gs` file of this repository
4. Add the Google Sheets API from the Services on the left side

##Launch
###Python
Execute the following command in the root directory of the project to scrape
https://www.imdb.com/chart/top/ and save the most frequent cast members in a
Google Sheet on Google Drive.

```
python3 main.py
```

###Google App Script
Run the `SendForm` function.

##Automation
###Python
Start crontab by typing `crontab` then execute the following command:

```
0 0 * * 0 /automation-home-assignment/automation.sh >/dev/null 2>&1
```

The scraping process will take place every Sunday right after midnight.

###Google App Script
Make sure that `top-cast` and `emails` exist in your Google Drive.
Add a trigger from the Triggers menu with the following settings: Run the
`SendForm` function, Head, Time-driven, Week timer, Every Sunday,
1pm to 2pm, weekly notifications. The forms will be generated and the emails
will be sent out between 1pm and 2pm.
