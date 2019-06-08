from telethon import TelegramClient, events, sync
import time
import datetime
import os

os.system("clear")

print("\n\n\n\n\033[1;32m  ____ ___ ___ _   _ ____  _   _ _     ____  ")
print(" / ___/ _ \_ _| \ | | __ )| | | | |   | __ ) ")
print("| |  | | | | ||  \| |  _ \| | | | |   |  _ \ ")
print("| |__| |_| | || |\  | |_) | |_| | |___| |_) |")
print(" \____\___/___|_| \_|____/ \___/|_____|____/ ")
print("   \033[1;36m[\033[0;31m馃嚫馃嚱\033[1;36m] \033[0;36mAUTHOR   :\033[0;32m DAMANG")
print("   \033[1;36m[\033[0;31m馃嚫馃嚱\033[1;36m] \033[0;36mFACEBOOK :\033[0;32m TEMUX DAMANG")
print("   \033[1;36m[\033[0;31m馃嚫馃嚱\033[1;36m] \033[0;36mYOUTUBE  :\033[0;32m TERMUX TRICKS & TUT")
print("   \033[1;36m[\033[0;31m馃嚫馃嚱\033[1;36m] \033[0;36mDECLAIMER:\033[0;32m USE AT YOUR OWN RISK!!!")


api_id = 491787
api_hash = '58839ada91de89607ec39b86c3f85247'
client = TelegramClient("DAMANG", api_id, api_hash)
client.start()
BCbot = client.get_entity('CoinBulb_bot')
print("\n")
count=0
while 1:
    client.send_message(BCbot, "/Ads")
    currentDT = datetime.datetime.now()
    print (currentDT.strftime("   \033[1;36m[\033[0;31m%H:%M\033[1;36m] \033[0;32mClaim Reward Success!"))
    time.sleep(33)
end
