import wandb
import requests
import argparse
import os

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--debug", type=bool, default=True, help="sets base_url")
args = parser.parse_args()

settings = wandb.Settings()
settings.update({"enable_job_creation":True, start_method="fork"})
if args.debug:
	settings.update({"base_url": "https://api.wandb.test"})

run = wandb.init(settings=settings)
print(f"Started run with api: {wandb.Settings().base_url=}")

run.log_code()

r = requests.get("https://docs.wandb.ai/guides/track/launch#init-start-error")
print(r.status_code)

print(f"{os.listdir()=}")

run.log({"text-len":121, "code":402})
run.finish()
