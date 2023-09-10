import argparse
from utils.config import Config

if __name__ == "__main__":

    # loading configures
    # print(123)
    # parser = argparse.ArgumentParser()
    # parser.add_argument('config')
    # print(parser)
    # args = parser.parse_args()
    # print(args.config)
    config = Config.from_file("configs/config_test_w_sgm.py")


    print(config)
