import wandb
import requests

wandb.init(project='requests-remote')

// r = requests.get("www.wandb.ai")
print("Belly")

wandb.log({"text-len":12, "code":404})

