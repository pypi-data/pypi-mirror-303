# # deploy script for fastapi project

# import os
# import time
# from os import path
# from typing import Annotated

# import typer

# from knifes.deploy.celery import run_command, echo_err, echo_succ, PROJECT_NAME, PROJECT_DIR, LOG_DIR, get_service_state, worker, beat, reload_celery_services

# GUNICORN_SYSTEMD_TEMPLATE = """[Unit]
# Description={NAME}.service
# ConditionPathExists={GUNICORN_PATH}
# After=network.target

# [Service]
# Environment="PROMETHEUS_MULTIPROC_DIR={PROMETHEUS_MULTIPROC_DIR}"
# WorkingDirectory={WORKING_DIRECTORY}
# ExecStart={GUNICORN_PATH} -c {GUNICORN_CONF_PATH}
# ExecReload=kill -HUP $MAINPID
# RestartSec=1
# Restart=always

# [Install]
# WantedBy=multi-user.target"""

# app = typer.Typer(no_args_is_help=True)


# @app.callback()
# def callback():
#     """deploy script for fastapi project"""
#     if not PROJECT_NAME or not PROJECT_DIR or not LOG_DIR:
#         echo_err("please set PROJECT_NAME, PROJECT_DIR, LOG_DIR environment variables")
#         raise SystemExit


# app.add_typer(worker, name="worker", rich_help_panel="Celery")
# app.add_typer(beat, name="beat", rich_help_panel="Celery")


# @app.command(rich_help_panel="Project")
# def knifes():
#     """force install latest knifes"""
#     activate_path = path.join(PROJECT_DIR, "venv/bin/activate")
#     cmd = f"source {activate_path} && pip install knifes --index-url https://pypi.python.org/simple -U"
#     output, err, _ = run_command(cmd)
#     typer.echo(output)
#     echo_err(err)  # warning message


# @app.command(rich_help_panel="Project")
# def modules():
#     """install project dependencies"""
#     _install_modules()


# @app.command(rich_help_panel="Gunicorn")
# def log(line_count: Annotated[int, typer.Argument(help="number of lines to read")] = 10):
#     """read gunicorn last log"""
#     _read_last_log(line_count)


# @app.command(rich_help_panel="Gunicorn")
# def status():
#     """show gunicorn status"""
#     output, err, _ = run_command(f"systemctl status {PROJECT_NAME}")
#     typer.echo(output)
#     echo_err(err)  # warning message


# @app.command(rich_help_panel="Gunicorn")
# def configure():
#     """configure gunicorn service"""
#     typer.echo(f"PROJECT_NAME: {PROJECT_NAME}")
#     typer.echo(f"PROJECT_DIR: {PROJECT_DIR}")
#     typer.echo(f"LOG_DIR: {LOG_DIR}")

#     service_path = f"/etc/systemd/system/{PROJECT_NAME}.service"
#     if path.exists(service_path):
#         echo_err(f"{service_path} already exists, delete it first if you want to reconfigure")
#         return

#     with open(service_path, "w", encoding="utf-8") as f:
#         f.write(
#             GUNICORN_SYSTEMD_TEMPLATE.format(
#                 NAME=PROJECT_NAME,
#                 GUNICORN_PATH=path.join(PROJECT_DIR, "venv/bin/gunicorn"),
#                 GUNICORN_CONF_PATH=path.join(PROJECT_DIR, "gunicorn_conf.py"),
#                 WORKING_DIRECTORY=PROJECT_DIR,
#                 PROMETHEUS_MULTIPROC_DIR=path.join(LOG_DIR, "metrics"),
#             )
#         )
#     os.chmod(service_path, mode=0o755)

#     output, err, code = run_command(f"systemctl daemon-reload && systemctl enable {PROJECT_NAME}")
#     if code != 0:
#         echo_err(f"failed to enable service: {err}")
#         raise SystemExit
#     typer.echo(output)
#     echo_succ(f"{PROJECT_NAME} enabled")


# @app.command(rich_help_panel="Gunicorn")
# def start():
#     """start gunicorn"""
#     if get_service_state(PROJECT_NAME) == "active":
#         echo_err(f"{PROJECT_NAME} is already running, use reload to restart it gracefully")
#         raise SystemExit

#     _pull_latest_code()
#     _install_modules()  # install modules before starting gunicorn

#     _, err, code = run_command(f"systemctl start {PROJECT_NAME}")
#     if code != 0:
#         echo_err(err)
#         raise SystemExit
#     echo_succ(f"{PROJECT_NAME} started")

#     time.sleep(2)
#     _read_last_log()


# @app.command(rich_help_panel="Gunicorn")
# def reload():
#     """reload gunicorn gracefully"""
#     if get_service_state(PROJECT_NAME) == "inactive":
#         echo_err(f"{PROJECT_NAME} is not running, use start to start it")
#         raise SystemExit

#     _pull_latest_code()
#     _install_modules()

#     _, err, code = run_command(f"systemctl reload {PROJECT_NAME}")
#     if code != 0:
#         echo_err(err)
#         raise SystemExit
#     echo_succ(f"{PROJECT_NAME} reloaded")

#     # read last 6 lines of log
#     time.sleep(2)
#     _read_last_log()

#     # reload celery worker and beat
#     reload_celery_services()


# @app.command(rich_help_panel="Gunicorn")
# def stop():
#     """stop gunicorn"""
#     if get_service_state(PROJECT_NAME) == "inactive":
#         echo_err(f"{PROJECT_NAME} is already stopped")
#         raise SystemExit

#     _, err, code = run_command(f"systemctl stop {PROJECT_NAME}")
#     if code != 0:
#         echo_err(err)
#         raise SystemExit
#     echo_succ(f"{PROJECT_NAME} stopped")

#     # read last 6 lines of log
#     time.sleep(2)
#     _read_last_log()


# @app.command()
# def restart():
#     """restart gunicorn"""
#     if get_service_state(PROJECT_NAME) == "inactive":
#         echo_err(f"{PROJECT_NAME} is not running, use start to start it")
#         raise SystemExit

#     _, err, code = run_command(f"systemctl restart {PROJECT_NAME}")
#     if code != 0:
#         echo_err(err)
#         raise SystemExit
#     echo_succ(f"{PROJECT_NAME} restarted")

#     # read last 6 lines of log
#     time.sleep(2)
#     _read_last_log()


# def _pull_latest_code():
#     output, err, code = run_command(f"cd {PROJECT_DIR} && git pull origin main")
#     if code != 0:
#         echo_err(err)
#         raise SystemExit
#     typer.echo(output)
#     echo_err(err)  # warning message


# def _install_modules():
#     activate_path = path.join(PROJECT_DIR, "venv/bin/activate")
#     requirements_path = path.join(PROJECT_DIR, "requirements.txt")
#     cmd = f"source {activate_path} && pip install -r {requirements_path}"
#     output, err, code = run_command(cmd)
#     if code != 0:
#         echo_err(f"failed to install modules: {err}")
#         raise SystemExit
#     typer.echo(output)
#     echo_err(err)  # warning message


# def _read_last_log(line_count=10):
#     gunicorn_log_path = path.join(LOG_DIR, "gunicorn.log")
#     output, err, _ = run_command(f"tail -{line_count} {gunicorn_log_path}")
#     typer.echo(output)
#     echo_err(err)
