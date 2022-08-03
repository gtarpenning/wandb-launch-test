import wandb

try:
	wandb.init(project='requests-remote')
except Exception as e: 
	print("Couldn't load wandb... \n {e}")

import os

print(os.listdir())

wandb.log({"text-len":121, "code":402})
