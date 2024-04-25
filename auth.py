from msal import ConfidentialClientApplication
from fastapi import HTTPException
from urllib.parse import urlencode
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

# client_secret = os.getenv('client_secret')

# Define the required parameters
tenant_id = '68ca5a97-b4cd-4f5f-8dd0-48993f42f7ea'
authority = f'https://login.microsoftonline.com/{tenant_id}'
client_id = 'cf725436-f4d4-4b8b-b0c2-da0d69c4d48d'

client_secret = os.getenv('client_secret')
scope = ["https://graph.microsoft.com/.default"]

app = ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)

def acquire_access_token_without_user():
    result = None
    try:
        result = app.acquire_token_for_client(scopes=scope)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to acquire access token")

    # print(result)
    if "access_token" in result:
        access_token = result['access_token']
        return access_token
    else:
        raise HTTPException(status_code=500, detail="Access token not found")

# print(acquire_access_token_without_user())