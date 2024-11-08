# Python-Email-Auto-Unsubscribe

This Python script automatically searches through your Gmail inbox for unsubscribe links, visits each link, and logs the result in a file (links.txt). It uses IMAP to access your inbox, BeautifulSoup to extract the links, and Requests to visit each link.

**Note**: This is not 100% accurate and will only unsubscribe from emails that provide a direct unsubscribe link. Emails requiring you to fill out a form after clicking the unsubscribe link will not be processed. Additionally, some important emails, like banking or service-related messages, might also contain unsubscribe links, and this code could unsubscribe from them as well. Be sure to check your inbox first and modify the code as necessary to fit your needs.

**Read my blog for better understanding of working of the code - [Ankush Kapoor Blog Page](https://ankushhkapoor.wordpress.com/)**

## Screenshot

This is an example of links.txt which contains the link visited along with it's status code.

<div align="center">
<img src="https://github.com/Ankush1626/Python-Email-Auto-Unsubscriber-/blob/main/links.txt%20ss.png" align="center" style="width: 100%" />
</div>

## Features
- Connects to Gmail via IMAP and logs into your account securely.
- Searches all emails for unsubscribe links.
- Extracts the unsubscribe links from HTML email bodies.
- Visits each unsubscribe link and logs whether it was successfully visited or failed.
- Saves the status and link information into a text file (`links.txt`).

## Requirements

- Python 3.6+
- Check more below in 3rd step of Setup.

## Setup

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/Ankush1626/Python-Email-Auto-Unsubscribe
   cd Python-Email-Auto-Unsubscribe
   ```

2. **.env file**: The repository includes a .env file containing environment variables for your Gmail credentials:

   ```text
   EMAIL="your-email@gmail.com"
   PASSWORD="your-app-password"
   ```

   - Repace ```your-email@gmail.com``` with your own gmail and ```your-app-password``` with your own app password.
     
   - For Gmail, you should use an App Password instead of your regular email password. To create an App Password, enable Two-Factor Authentication (2FA) on your Google account and generate an app-specific password.
   
   - Important: The .env file is included to keep your credentials secure. Do not upload or share this file publicly. Ensure that the credentials are correct before running the script.
   
   - You can generate an app password [here](https://support.google.com/accounts/answer/185833?hl=en).

4. **Install required modules**:

    Install the required dependencies listed in the requirements.txt file:
    
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:
   
   Once you've set up the `.env` file, you can run the script:

   ```bash
   python main.py
   ```

4. The script will generate a `links.txt` file, where each line will contain the status and the corresponding link, like so:

   ```
   Successfully visited - http://example.com/unsubscribe
   Failed to visit (Error 404) - http://example.com/unsubscribe
   ```

## How it Works

1. The script connects to your Gmail account using IMAP, authenticates using the credentials in the `.env` file, and searches the inbox for emails containing the word "unsubscribe".
2. It then extracts the unsubscribe links from the HTML content of those emails.
3. Each link is visited using the `requests` library, and the script logs the result (whether the link was successfully visited or an error occurred).
4. Finally, it writes all the links and their statuses into `links.txt`.

# Dislaimer

<div align="center">
This code was not originally developed by me. I learned it from a tutorial by the channel Tech with Tim on Youtube and hold no copyright over this code or its related files.
<br/>
PS - I did not just copy and paste the code. Instead, I understood it and then rewrote the entire code from scratch.
</div>
