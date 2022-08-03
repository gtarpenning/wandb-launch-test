import wandb
import requests

try:
	wandb.init(project='requests-remote')
except Exception as e: 
	print("Couldn't load wandb... \n {e}")

import os

r = requests.get("https://docs.wandb.ai/guides/track/launch#init-start-error")
print(r.status_code)

print(os.listdir())

wandb.log({"text-len":121, "code":402})
