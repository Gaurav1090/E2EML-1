import pandas as pd
import argparse
from src.utils.common_utils import read_params, save_reports, create_dir
from sklearn.linear_model import ElasticNet
import joblib
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
logging.basicConfig(level=logging.DEBUG,format=logging_str)

def train(config_path):
    config = read_params(config_path)
    artifacts = config["artifacts"]
    split_data = artifacts["split_data"]
    train_data_path = split_data["train_path"]
    base = config["base"]
    target = base["target_col"]
    random_seed = base["random_state"]
    reports_dir = artifacts["reports"]["reports_dir"]
    params_file = artifacts["reports"]["params"]

    elasticnet_params = config["estimators"]["ElasticNet"]["params"]
    alpha = elasticnet_params["alpha"]
    l1_ratio = elasticnet_params["l1_ratio"]

    df = pd.read_csv(train_data_path, sep=",")
    train_y = df[target]
    train_x = df.drop(target, axis=1)

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_seed)
    lr.fit(train_x, train_y)

    model_dir = artifacts["models"]["model_dir"]
    model_path = artifacts["models"]["model_path"]

    create_dir([model_dir, reports_dir])

    params = {
        "alpha": alpha,
        "l1_ratio": l1_ratio
    }
    save_reports(params_file, params)
    joblib.dump(lr, model_path)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        train(config_path=parsed_args.config)
        logging.info(f"Stage03: Training of the model is complete")
    except Exception as e:
        logging.error(e)
