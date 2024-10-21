# # celery service management

# import os
# from os import path
# import subprocess
# from enum import Enum
# from dotenv import load_dotenv

# import typer

# load_dotenv()  # # take environment variables from .env.
# PROJECT_NAME = os.getenv("PROJECT_NAME", "")
# PROJECT_DIR = os.getenv("PROJECT_DIR", "")
# LOG_DIR = os.getenv("LOG_DIR", "")

# CELERY_WORKER_SYSTEMD_TEMPLATE = """[Unit]
# Description={NAME}.worker.service
# ConditionPathExists={CELERY_PATH}
# After=network.target

# [Service]
# Environment="PROMETHEUS_MULTIPROC_DIR={PROMETHEUS_MULTIPROC_DIR}"
# WorkingDirectory={WORKING_DIRECTORY}
# ExecStart={CELERY_PATH} --app={NAME}.tasks worker --pool=gevent --loglevel=INFO --concurrency=1
# ExecReload=kill -HUP $MAINPID
# RestartSec=1
# Restart=always

# [Install]
# WantedBy=multi-user.target"""


# CELERY_BEAT_SYSTEMD_TEMPLATE = """[Unit]
# Description={NAME}.beat.service
# ConditionPathExists={CELERY_PATH}
# After=network.target

# [Service]
# Environment="PROMETHEUS_MULTIPROC_DIR={PROMETHEUS_MULTIPROC_DIR}"
# WorkingDirectory={WORKING_DIRECTORY}
# ExecStart={CELERY_PATH} --app={NAME}.tasks beat --loglevel=INFO
# ExecReload=kill -HUP $MAINPID
# RestartSec=1
# Restart=always

# [Install]
# WantedBy=multi-user.target"""


# def run_command(command) -> tuple[str, str, int]:
#     result = subprocess.run(command, shell=True, capture_output=True, text=True, check=False, executable="/bin/bash")
#     return result.stdout.strip(), result.stderr.strip(), result.returncode


# def echo_succ(content):  # 绿色
#     typer.secho(content, fg=typer.colors.GREEN)


# def echo_err(content):  # 红色
#     typer.secho(content, fg=typer.colors.RED)


# def get_service_state(service_name: str):
#     state, _, _ = run_command(f"systemctl is-active {service_name}")
#     return state


# class CeleryService(Enum):
#     WORKER = "worker"
#     BEAT = "beat"

#     def __str__(self):
#         return self.value


# def configure(service: CeleryService):
#     """configure service"""
#     typer.echo(f"PROJECT_NAME: {PROJECT_NAME}")
#     typer.echo(f"PROJECT_DIR: {PROJECT_DIR}")
#     typer.echo(f"LOG_DIR: {LOG_DIR}")

#     service_name = f"{PROJECT_NAME}.{service}"
#     service_path = f"/etc/systemd/system/{service_name}.service"
#     if path.exists(service_path):
#         echo_err(f"{service_path} already exists, delete it first if you want to reconfigure")
#         return

#     template = CELERY_WORKER_SYSTEMD_TEMPLATE if service == CeleryService.WORKER else CELERY_BEAT_SYSTEMD_TEMPLATE
#     celery_path = path.join(PROJECT_DIR, "venv/bin/celery")
#     with open(service_path, "w", encoding="utf-8") as f:
#         f.write(
#             template.format(
#                 NAME=PROJECT_NAME,
#                 CELERY_PATH=celery_path,
#                 WORKING_DIRECTORY=PROJECT_DIR,
#                 PROMETHEUS_MULTIPROC_DIR=path.join(LOG_DIR, "metrics"),
#             )
#         )
#     os.chmod(service_path, mode=0o755)

#     output, err, code = run_command(f"systemctl daemon-reload && systemctl enable {service_name}")
#     if code != 0:
#         echo_err(f"failed to enable service: {err}")
#         raise SystemExit
#     typer.echo(output)
#     echo_succ(f"{service_name} enabled")


# def start(service: CeleryService):
#     """start service"""
#     service_name = f"{PROJECT_NAME}.{service}"
#     if get_service_state(service_name) == "active":
#         echo_err(f"{service_name} is already running, use reload to restart it gracefully")
#         raise SystemExit

#     _, err, code = run_command(f"systemctl start {service_name}")
#     if code != 0:
#         echo_err(err)
#         raise SystemExit
#     echo_succ(f"{service_name} started")


# def stop(service: CeleryService):
#     """stop service"""
#     service_name = f"{PROJECT_NAME}.{service}"
#     if get_service_state(service_name) == "inactive":
#         echo_err(f"{service_name} is already stopped")
#         raise SystemExit

#     _, err, code = run_command(f"systemctl stop {service_name}")
#     if code != 0:
#         echo_err(err)
#         raise SystemExit
#     echo_succ(f"{service_name} stopped")


# def reload(service: CeleryService):
#     """reload service gracefully"""
#     service_name = f"{PROJECT_NAME}.{service}"
#     if get_service_state(service_name) == "inactive":
#         echo_err(f"{service_name} is not running, use start to start it")
#         raise SystemExit

#     _, err, code = run_command(f"systemctl reload {service_name}")
#     if code != 0:
#         echo_err(err)
#         raise SystemExit
#     echo_succ(f"{service_name} reloaded")


# def status(service: CeleryService):
#     """show service status"""
#     service_name = f"{PROJECT_NAME}.{service}"
#     output, err, _ = run_command(f"systemctl status {service_name}")
#     typer.echo(output)
#     echo_err(err)  # warning message


# def log(service: CeleryService):
#     """show service last 30 lines of log"""
#     service_name = f"{PROJECT_NAME}.{service}"
#     output, err, _ = run_command(f"journalctl -u {service_name} -n 30")
#     typer.echo(output)
#     echo_err(err)  # warning message


# def reload_celery_services():
#     """reload celery worker and beat gracefully"""
#     if get_service_state(f"{PROJECT_NAME}.{CeleryService.WORKER}") == "active":
#         reload(CeleryService.WORKER)
#     if get_service_state(f"{PROJECT_NAME}.{CeleryService.BEAT}") == "active" and typer.confirm("Do you want to reload beat?"):
#         reload(CeleryService.BEAT)


# worker = typer.Typer(help="celery worker management", no_args_is_help=True)
# worker.command("configure", help="configure celery worker")(lambda: configure(CeleryService.WORKER))
# worker.command("start", help="start celery worker")(lambda: start(CeleryService.WORKER))
# worker.command("stop", help="stop celery worker")(lambda: stop(CeleryService.WORKER))
# worker.command("reload", help="reload celery worker gracefully")(lambda: reload(CeleryService.WORKER))
# worker.command("status", help="show celery worker status")(lambda: status(CeleryService.WORKER))
# worker.command("log", help="show celery worker last 30 lines of log")(lambda: log(CeleryService.WORKER))

# beat = typer.Typer(help="celery beat management", no_args_is_help=True)
# beat.command("configure", help="configure celery beat")(lambda: configure(CeleryService.BEAT))
# beat.command("start", help="start celery beat")(lambda: start(CeleryService.BEAT))
# beat.command("stop", help="stop celery beat")(lambda: stop(CeleryService.BEAT))
# beat.command("reload", help="reload celery beat gracefully")(lambda: reload(CeleryService.BEAT))
# beat.command("status", help="show celery beat status")(lambda: status(CeleryService.BEAT))
# beat.command("log", help="show celery beat last 30 lines of log")(lambda: log(CeleryService.BEAT))
