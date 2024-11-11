import argparse

def handle_options():
    parser = argparse.ArgumentParser(
        description="send_marketing_emails.py that creates personalized marketing emails and send them to a list of recipients"
    )
    parser.add_argument("-w",
                        "--websites",
                        required=True,
                        type=str,
                        help="file containing a list of websites to scrape for information")
    parser.add_argument("-o",
                        "--offer_document",
                        required=True,
                        type=str,
                        help="offer document to use for creating personalized emails")
    
    args = parser.parse_args()
    option_values = vars(args)

    return option_values

def parse_websites(websites):
    with open(websites, 'r') as file:
        websites = file.readlines()
    return websites
