#!/usr/bin/env python

# SPDX-FileCopyrightText: 2024 Philip Zerull
#
# SPDX-License-Identifier: MIT

import argparse
import datetime
import os
import subprocess
from pathlib import Path
from urllib.request import urlopen

from dotenv import dotenv_values


def run_backup(*, host, database_name, user_name, path, password):
    args = [
        "pg_dump",
        "-h",
        host,
        "-d",
        database_name,
        "-U",
        user_name,
        "-f",
        path,
    ]
    env = {**os.environ, "PGPASSWORD": password}
    subprocess.run(args, env=env, check=False)  # noqa: S603
    # Regarding the noqa: S603, I may be mistaken, but I belive a parameter
    # injection is impossible due to how we manually produce the args - PhilZ


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("settings_filename", type=str)
    args = parser.parse_args()
    values = dotenv_values(args.settings_filename)
    database_name = values["POSTGRES_DATABASE"]
    today = datetime.datetime.now().isoformat()
    filename = f"{database_name}-{today}.backup.sql"
    folder = values["BACKUP_PATH"]
    path = Path(folder) / filename
    run_backup(
        host=values["POSTGRES_HOST"],
        database_name=database_name,
        user_name=values["POSTGRES_USER"],
        path=path,
        password=values["POSTGRES_PASSWORD"],
    )
    url = values["BACKUP_HEALTH_CHECK_URL"]
    if url.startswith(("http:", "https:")):
        with urlopen(url):  # noqa: S310 - False positive. - PhilZ
            pass


if __name__ == "__main__":
    main()
