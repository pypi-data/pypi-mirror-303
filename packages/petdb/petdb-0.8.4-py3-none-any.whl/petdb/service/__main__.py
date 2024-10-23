
import os
import sys
import hashlib

from petcmd import Commander

from petdb.service.api import DEFAULT_PORT
from petdb.service.server import Server, STORAGE_PATH

commander = Commander()

SERVICE_NAME = "petdb.database.service"
SERVICE_PATH = os.path.join("/etc/systemd/system", SERVICE_NAME)

template = f"""
[Unit]
Description=PetDB Service

[Service]
User={os.environ.get("USER", "root")}
Environment="LD_LIBRARY_PATH=/usr/local/lib"
Environment="PYTHONUNBUFFERED=1"
WorkingDirectory={STORAGE_PATH}
ExecStart={sys.executable} -u -m petdb.service run -p {{port}}
Restart=always

[Install]
WantedBy=multi-user.target
""".strip()

os.makedirs(STORAGE_PATH, exist_ok=True)

def check_current_configuration(service_path: str) -> bool:
	try:
		with open(service_path, "r") as f:
			executable = f.read().split("ExecStart=")[1].split(" ")[0]
		if executable != sys.executable:
			print(f"PetDB service have already been configured with another python executable: {executable}")
			if input(f"Want to replace it with the current one: {sys.executable} (y/n)? ").lower() != "y":
				return False
	except Exception:
		pass
	return True

@commander.command("init", "reinit")
def init_service(port: int = DEFAULT_PORT):
	if os.path.exists(SERVICE_PATH):
		if not check_current_configuration(SERVICE_PATH):
			return
		os.system(f"sudo systemctl stop {SERVICE_NAME}")
		os.system(f"sudo systemctl disable {SERVICE_NAME}")
		os.remove(SERVICE_PATH)
		os.system(f"sudo systemctl daemon-reload")
	with open(SERVICE_PATH, "w") as f:
		f.write(template.format(port=port))
	os.system(f"sudo systemctl daemon-reload")
	os.system(f"sudo systemctl enable {SERVICE_NAME}")
	os.system(f"sudo systemctl start {SERVICE_NAME}")

@commander.command("run")
def run_service(port: int):
	passwords = {}
	for database in os.listdir(STORAGE_PATH):
		path = os.path.join(STORAGE_PATH, database)
		if os.path.isdir(path) and "pw" in os.listdir(path):
			with open(os.path.join(STORAGE_PATH, database, "pw"), "r") as f:
				passwords[database] = f.read().strip()
	Server(port=port, passwords=passwords).run()

@commander.command("create", "modify")
def create_database(name: str, password: str):
	os.makedirs(os.path.join(STORAGE_PATH, name), exist_ok=True)
	with open(os.path.join(STORAGE_PATH, name, "pw"), "w") as f:
		f.write(hashlib.sha256(password.encode("utf-8")).hexdigest())
	os.system(f"sudo systemctl restart {SERVICE_NAME}")

@commander.command("hash")
def hash_password(password: str):
	print(hashlib.sha256(password.encode("utf-8")).hexdigest())

if __name__ == "__main__":
	commander.process()
