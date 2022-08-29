import wandb
import requests

try:
	wandb.init()
except Exception as e: 
	print(f"Couldn't load wandb... \n {e}")

import os

r = requests.get("https://docs.wandb.ai/guides/track/launch#init-start-error")
print(r.status_code)

print(f"{os.listdir()=}")

try:
	wandb.log({"text-len":121, "code":402})
except Exception as e:
	print(e)
