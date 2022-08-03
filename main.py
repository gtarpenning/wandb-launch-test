import wandb
import requests

try:
	wandb.init(project='requests-remote', settings=wandb.Settings(start_method="fork"))
except Exception as e: 
	print("Couldn't load wandb... \n {e}")

import os

r = requests.get("https://docs.wandb.ai/guides/track/launch#init-start-error")
print(r.text)

print(os.listdir())

wandb.log({"text-len":121, "code":402})
