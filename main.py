import wandb
import requests

wandb.init(project='requests-remote')

# r = requests.get("www.wandb.ai")
print("Belly")

wandb.log({"text-len":121, "code":402})

