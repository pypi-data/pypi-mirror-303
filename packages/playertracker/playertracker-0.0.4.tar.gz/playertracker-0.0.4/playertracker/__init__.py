import requests
import time
from datetime import datetime

regions = ["US", "USW", "EU"]
title = "63FDD"
FingerPainter = "LBADE."
Stick = "LBAAK."
Admin = "LBAAD."
HighTech = "LMAAV."
UnreleasedSweater = "LBACP."
IllustratorBadge = "LBAGS."
Cowboy = "LHAAN."

def successful_log(login_response):
    print(f'Success Fetching Session Ticket\n\n{login_response}')

def login_stuff(steamticket, Codes):
    loginresponse = get_session_ticket(steamticket)
    session_ticket = loginresponse["data"]["SessionTicket"]
    check_data(session_ticket, Codes)

def error_log(login_response):
    print(f"Session Ticket Was Invalid\n\n{login_response}")


def Player_Found(item, room, count):
    print(f"Found {item} In Room {room}, Player Count: {count}")

def get_session_ticket(steamticket):
    login = requests.post(
        url=f"https://{title}.playfabapi.com/Client/LoginWithSteam",
        json={
            "SteamTicket": steamticket,
            "CreateAccount": True,
            "TitleId": title,
        },
    )
    loginresponse = login.json()
    if "data" in loginresponse and "SessionTicket" in loginresponse["data"]:
        return loginresponse
    else:
        error_log(loginresponse)
        print("Error fetching session ticket:")
        print(loginresponse)
        return None


def check_data(session_ticket, Codes):
    ClientHeaders = {"X-Authorization": session_ticket}
    for word in Codes:
        for region in regions:
            combined_code = word + region
            Keys = ""
            request = {
                "SharedGroupId": combined_code,
                "GetMembers": True,
                "Keys": Keys,
            }
            createshared = requests.post(
                url=f"https://{title}.playfabapi.com/Client/GetSharedGroupData",
                json=request,
                headers=ClientHeaders,
            )
            response_data = createshared.json()
            count = "N/A"
            if "data" in response_data and Cowboy in str(
                    response_data["data"]):
                Player_Found("COWBOY HAT", word, count)
            if "data" in response_data and FingerPainter in str(
                    response_data["data"]):
                Player_Found("FINGER PAINTER", word, count)
            if "data" in response_data and HighTech in str(
                    response_data["data"]):
                Player_Found("HIGHTEC SLINGSHOT", word, count)
            if "data" in response_data and Stick in str(response_data["data"]):
                Player_Found("STICK", word, count)
            if "data" in response_data and Admin in str(response_data["data"]):
                Player_Found("ADMIN BADGE", word, count)
            if "data" in response_data and UnreleasedSweater in str(
                    response_data["data"]):
                Player_Found("UnreleasedSweater", word, count)
            if "data" in response_data and IllustratorBadge in str(
                    response_data["data"]):
                Player_Found("IllustratorBadge", word, count)
            time.sleep(0.3)


def format_account_info_message(account_info):
    formatted_message = (
        f"**DisplayName:** {account_info['DisplayName']}\n"
        f"**PlayerId:** {account_info['PlayerId']}\n"
        f"**Email:** {account_info['Email']}\n"
        f"**Banned:** {account_info['IsBanned']}\n"
        f"**LastLoginDate:** {account_info['LastLoginDate']}\n"
        f"**CreationDate:** {account_info['CreationDate']}\n")
    return formatted_message


def get_account_info(session_ticket, playfab_id):
    ClientHeaders = {"X-Authorization": session_ticket}
    request = {"PlayFabId": playfab_id}

    account_info_response = requests.post(
        url=f"https://{title}.playfabapi.com/Client/GetAccountInfo",
        json=request,
        headers=ClientHeaders,
    )

    response_data = account_info_response.json()
    account_info = response_data.get("data", {}).get("AccountInfo", {})
    creation_date = account_info.get("Created", "N/A")
    last_login_date = account_info.get("LastLogin", "N/A")
    player_id = account_info.get("PlayFabId", "N/A")
    is_banned = account_info.get("BannedUntil", None) is not None
    display_name = account_info.get("TitleInfo", {}).get("DisplayName", "N/A")
    email = account_info.get("PrivateInfo", {}).get("Email", "N/A")

    return {
        "CreationDate": creation_date,
        "LastLoginDate": last_login_date,
        "PlayerId": player_id,
        "IsBanned": is_banned,
        "DisplayName": display_name,
        "Email": email,
    }
