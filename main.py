import requests
from dotenv import load_dotenv
import os
import json
import asyncio
from auth import acquire_access_token_without_user
from emailGenerator import emailGenerator
from datetime import date

load_dotenv()
sampro_api_key = os.getenv('sampro_api_key')

def license_in_use_api():
    headers = {
        'Authorization': f'api_key {sampro_api_key}',
        'Content-Type': 'application/json'    
    }
    data = {
        'tokenList': [],
        'queryName': 'LicenseInUseAPI'
    }
    response = requests.post(
        'https://sampro.wearetheone.com/DBAnalytics/SAMProAPI.svc/postKPIData', 
        headers=headers, 
        json=data
    )
    text = response.text
    dataFromText = json.loads(json.loads(text))
    return dataFromText

def sendEmail(
        licenseUsage: str,
        access_token: str,
        email_address: str,
        ccRecipients: list[str],
        my_email: str
    ):
    headers = {'Authorization': 'Bearer ' + access_token,
               'Content-Type' : 'application/json'}
    
    msg = {
        "message": {
            "subject": f"Sampro Active License Daily Report [{date.today()}]",
            "body": {
                "contentType": "HTML",
                "content": licenseUsage
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": email_address
                    }
                }
            ],
            "ccRecipients": [{"emailAddress": {"address": recipients}} for recipients in ccRecipients]
        },
        "saveToSentItems": "true"
    }
    
    status = requests.post(f'https://graph.microsoft.com/v1.0/users/{my_email}/sendMail', 
                           headers=headers, json=json.loads(json.dumps(msg)))
    return status

async def main():
    ccRecipients = [
        "lguo@wearetheone.com",
        "achowdhury@wearetheone.com",
        "jzhang@wearetheone.com"
    ]
    access_token = await acquire_access_token_without_user()
    licenseUsage = license_in_use_api()
    emailContent = emailGenerator(licenseUsage[0]['Count'], licenseUsage[1]['Count'], licenseUsage[2]['Count'])
    # return emailContent
    status = sendEmail(emailContent, access_token, "it@wearetheone.com", ccRecipients, "it@wearetheone.com")
    if status.status_code == 202:
        res = f"Email sent successfully. {licenseUsage}\n"
    else:
        # print("Failed to renew subscription!")
        res = f"Email sending failed. \n"
    return res

# Dev
# print(asyncio.run(main()))

# Production
def lambda_handler(event, context):
    status = asyncio.run(main())
    return status