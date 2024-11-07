from dotenv import load_dotenv
import imaplib
import email
from bs4 import BeautifulSoup
import os
import requests

load_dotenv()

username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def connect_to_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    return mail

def extract_links_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    links = [link["href"] for link in soup.find_all("a", href=True) if "unsubscribe" in link["href"].lower()]
    return links

def click_link(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print("Successfully visited the link", link)
            return link, "Successfully visited"
        else:
            print("Failed to visit the link", link, "error code", response.status_code)
            return link, f"Failed to visit (Error {response.status_code})"
    except Exception as e:
        print("Error with", link, str(e))
        return link, f"Failed to visit ({str(e)})"

def search_for_email():
    mail = connect_to_mail()
    _, search_data = mail.search(None, '(BODY "unsubscribe")')
    data = search_data[0].split()

    links = []

    for num in data:
        _, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type == "text/html":
                    html_content = part.get_payload(decode=True).decode()
                    links.extend(extract_links_from_html(html_content))
        else:
            content_type = msg.get_content_type()
            content = msg.get_payload(decode=True).decode()

            if content_type == "text/html":
                links.extend(extract_links_from_html(content))

    mail.logout()
    return links

def save_links(links_with_status):
    with open("links.txt", "w") as f:
        for link, status in links_with_status:
            f.write(f"{status} - {link}\n")

# Collect all unsubscribe links
links = search_for_email()

# Initialize a list to hold link-status tuples
links_with_status = []

# Visit each link and save its status
for link in links:
    link_status = click_link(link)
    links_with_status.append(link_status)

# Save all the links and their status in the file
save_links(links_with_status)