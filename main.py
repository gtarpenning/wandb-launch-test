import wandb
import requests

wandb.init(project='requests-remote')

r = requests.get("www.wandb.ai")
print(r.text)

wandb.log({"text-len":len(r.text), "code":r.response_code})

