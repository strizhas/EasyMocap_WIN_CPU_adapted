import os
from os.path import join
from easymocap.config.baseconfig import load_object, Config
from easymocap.mytools import Timer
import cv2
from easymocap.dataset.config import CONFIG
from easymocap.mytools.vis_base import plot_keypoints

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    for name in ['data', 'model', 'exp']:
        parser.add_argument('--cfg_{}'.format(name), type=str)
        parser.add_argument('--opt_{}'.format(name), type=str, nargs='+', default=[])
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    joined_opt_data = " ".join(args.opt_data).split(" ")
    args.opt_data = joined_opt_data

    cfg_data = Config.load(args.cfg_data, args.opt_data)
    cfg_model = Config.load(args.cfg_model, args.opt_model)
    cfg_exp = Config.load(args.cfg_exp, args.opt_exp)

    # print(cfg_data)
    # print(cfg_model)
    # print(cfg_exp)

    cfg_data.args.camera = cfg_data.args.camera.replace('"', '')
    cfg_data.args.path = cfg_data.args.path.replace('"', '')

    out = cfg_data.args.out

    os.makedirs(out, exist_ok=True)

    print(cfg_model, file=open(join(out, 'cfg_model.yml'), 'w'))
    print(cfg_exp, file=open(join(out, 'cfg_exp.yml'), 'w'))
    print(cfg_data, file=open(join(out, 'cfg_data.yml'), 'w'))

    with Timer('Loading {}'.format(args.cfg_data)):
        dataset = load_object(cfg_data.module, cfg_data.args)

    with Timer('Loading {}'.format(args.cfg_model)):
        body_model = load_object(cfg_model.module, cfg_model.args)

    print("LOAD OBJECT")
    fitter = load_object(cfg_exp.module, cfg_exp.args)
    fitter.fit(body_model, dataset)
