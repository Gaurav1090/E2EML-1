import yaml
import os
import shutil
import logging
import json

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=logging_str)


def read_params(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    logging.info(f"Read parameter Successful")

    return config


def clean_prev_dir_if_exist(artifacts: str):
    if os.path.isdir(artifacts):
        shutil.rmtree(artifacts)
        logging.info(f"Clean Directory Successful")


def create_dir(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"New Directory Created as {dir_path}")


def save_local_df(df, df_path, header=False):
    if header:
        new_cols = [col.replace(" ", "_") for col in df.columns]
        df.to_csv(df_path, index=False, header=new_cols)
    else:
        df.to_csv(df_path, index=False)
    logging.info(f"Dataframe successfully saved  at {df_path}")


def save_reports(filepath: str, report: dict):
    with open(filepath, "w") as f:
        json.dump(report, f, indent=4)
    logging.info(f"Report Generated at {filepath}")
