from http.server import BaseHTTPRequestHandler

#!/usr/bin/python
from src.send_personalized_emails import send_personalized_emails

class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        send_personalized_emails("../data/websites.txt", "../data/AIA Sales Hacker.docx")
        return