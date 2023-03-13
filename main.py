import wandb
import requests
import argparse
import os
import random

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--debug", type=bool, default=True, help="sets base_url")
args = parser.parse_args()

run = wandb.init()
print(f"Started run with api: {wandb.Settings().base_url=}")

run.log_code()

r = requests.get("https://docs.wandb.ai/guides/track/launch#init-start-error")
print(r.status_code)

print(f"{os.listdir()=}")

run.log({"text-len":121, "code":402})

if len(wandb.config.keys()) > 0:
	print("This is a sweep!")
	
	for i in range(100):
		loss = random.random() * (100 - i)
		print(f"{i}> {loss}")
		wandb.log({"loss":loss})

run.finish()
