import requests
from dotenv import load_dotenv
import os
import json
from auth import acquire_access_token_without_user
from emailGenerator import emailGenerator
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

load_dotenv()
sampro_api_key = os.getenv('sampro_api_key')

def sampro_license_in_use_api():
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

def product_name_lookup(skuPartNumber: str):
    if skuPartNumber == 'Office 365 E1':
        return "Office 365 E1"
    elif skuPartNumber == 'STREAM':
        return "Microsoft Stream"
    elif skuPartNumber == 'Microsoft_Teams_Audio_Conferencing_select_dial_out':
        return "Microsoft Teams Audio Conferencing with dial-out to USA/CAN"
    elif skuPartNumber == 'POWER_BI_STANDARD':
        return "Microsoft Fabric (Free)"
    elif skuPartNumber == 'ENTERPRISEPACK':
        return "Office 365 E3"
    elif skuPartNumber == 'FLOW_FREE':
        return "Microsoft Power Automate Free"
    elif skuPartNumber == 'POWER_BI_PRO':
        return "Power BI Pro"
    elif skuPartNumber == 'CCIBOTS_PRIVPREV_VIRAL':
        return "Power Virtual Agents Viral Trial"
    elif skuPartNumber == 'O365_BUSINESS_PREMIUM':
        return "Microsoft 365 Business Standard"
    elif skuPartNumber == 'O365_BUSINESS_ESSENTIALS':
        return "Microsoft 365 Business Basic"
    elif skuPartNumber == 'STANDARDPACK':
        return "Office 365 E1"
    else:
        return skuPartNumber
    
def print_custom_progress_bar(assigned, total, bar_length):
    percent_complete = float(assigned) / total
    filled_length = int(round(bar_length * percent_complete))
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    if percent_complete > 0.75:
        return f"[{bar}] - {Decimal(percent_complete * 100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}% - {total - assigned} left"
    else:
        return f"[{bar}] - {Decimal(percent_complete * 100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}%"

def ms_license_in_use_api():
    access_token = acquire_access_token_without_user()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(
        'https://graph.microsoft.com/v1.0/subscribedSkus',
        headers=headers
    )
    response = response.json()
    result = ""
    if 'value' in response:
        for item in response['value']:
            # result.append({
            #     "License": product_name_lookup(item['skuPartNumber']),
            #     "Assigned Licenses": item['consumedUnits'],
            #     "Total Licenses": item['prepaidUnits']['enabled'],
            #     "Progress": print_custom_progress_bar(item['consumedUnits'], item['prepaidUnits']['enabled'], 20)
            # })
            result += f"""
                <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
                    <tbody>
                        <tr style="width:100%">
                            <td>
                            <li style="margin-bottom:8px;padding-left:6px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                                <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                                <strong>{product_name_lookup(item['skuPartNumber'])}</strong>
                                </p>
                                <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">Assigned: {item['consumedUnits']}</p>
                                <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">Total: {item['prepaidUnits']['enabled']}</p>
                                <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">Usage: {print_custom_progress_bar(item['consumedUnits'], item['prepaidUnits']['enabled'], 20)}</p>
                            </li>
                            </td>
                        </tr>
                    </tbody>
                </table>
            """
    return result


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
            "subject": f"Active License Daily Report [{date.today()}]",
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

def main():
    ccRecipients = [
        "lguo@wearetheone.com",
        "achowdhury@wearetheone.com",
        "jzhang@wearetheone.com",
        "eyuanyin@wearetheone.com",
        "jliu@wearetheone.com",
        "oclaros@wearetheone.com",
        "asam@wearetheone.com",
        "jperry@wearetheone.com"
    ]
    access_token = acquire_access_token_without_user()
    samproLicenseUsage = sampro_license_in_use_api()
    microsoftLicenseUsage = ms_license_in_use_api()
    emailContent = emailGenerator(samproLicenseUsage[0]['Count'], samproLicenseUsage[1]['Count'], samproLicenseUsage[2]['Count'], microsoftLicenseUsage)
    # return emailContent
    status = sendEmail(emailContent, access_token, "it@wearetheone.com", ccRecipients, "it@wearetheone.com")
    if status.status_code == 202:
        res = f"Email sent successfully. {samproLicenseUsage}\n"
    else:
        # print("Failed to renew subscription!")
        res = f"Email sending failed. \n"
    return res

# Dev
print(main())

# Production
# def lambda_handler(event, context):
#     status = main()
#     return status