import wandb
import requests

wandb.init(project='requests-remote')

try:
	r = requests.get("https://www.wandb.ai")
	print(f"{r.status_code=} -- {len(r.text)=}")
except Exception as e:
	print("Unable to connect to url")
	print(e)

import os

print(os.listdir())
print("Belly")

wandb.log({"text-len":121, "code":402})
