import yaml
import os
import shutil
import logging
import json

def read_params(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)

    return config

def clean_prev_dir_if_exist(artifacts: str):
    if os.path.isdir(artifacts):
        shutil.rmtree(artifacts)

def create_dir(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)

def save_local_df(df,df_path,header=False):
    if header:
        new_cols = [col.replace(" ","_") for col in df.columns]
        df.to_csv(df_path,index=False,header=new_cols)
    else:
        df.to_csv(df_path,index=False)
