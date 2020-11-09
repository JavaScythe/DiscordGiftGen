import random, string
import json
import datetime
import time
import requests
#UI UPDATED
#STABLE BUILD AS PUBLISHED
#BEFORE MULTI-VERSION TESTING
repeat = 0
read_valids = input("Press enter to continue: ")
time.sleep(0.1)
print("Connecting verification service")
time.sleep(0.3)
print("Complete")
time.sleep(0.2)
num=input('Input How Many Codes to Generate and Check: ')
for n in range(int(num)):
  repeat = repeat+1
  y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
  URL = "https://discordapp.com/api/v8/entitlements/gift-codes/" + y + "?with_application=false&with_subscription_plan=true"
  #URL = "https://genserver.vincentziemerin.repl.co?code=4383jf33"
  r = requests.get(url = URL) 
  data = r.json()
  data_json = json.dumps(data, indent = 1)   
  data_json_loaded = json.loads(data_json)
  if data_json_loaded["message"] == "You are being rate limited.":
    try_again = data_json_loaded["retry_after"]
    try_again = try_again/1000
    try_again_num = try_again
    try_again = str(try_again)
    now = datetime.datetime.now()
    print("TryLimit: re-try in "+try_again+" seconds "+"["+str(now)+"]")
    time.sleep(try_again_num)
  elif data_json_loaded["message"] == "Unknown Gift Code":
    print(data_json_loaded["message"]+" | https://discord.gifts/"+y+" ["+str(repeat)+"]")
#delay time here
    time.sleep(11.88)
  elif data_json_loaded["message"] == 'null':
    ValueError("null")
    print("get* did not return any value")
    break
  else:
    print(" Invalid | https://discord.gifts/"+y)
    exit()
    break
input("Enter to exit")
