import numpy as np
import argparse

import torch
from pointnetplus import seg_model
from data_loader import get_data_loader
from utils import create_dir, viz_seg
import os
from tqdm import tqdm

os.environ['CUDA_VISIBLE_DEVICES'] = '1'

def create_parser():
    """
    Creates a parser for command-line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--num_seg_class', type=int, default=6, help='The number of segmentation classes')
    parser.add_argument('--num_points', type=int, default=10000, help='The number of points per object to be included in the input data')

    # Directories and checkpoint/sample iterations
    parser.add_argument('--load_checkpoint', type=str, default='best_model')
    parser.add_argument('--i', type=int, default=0, help="index of the object to visualize")
    parser.add_argument('--rotate_strength', type=float, default= 0 * np.pi/180, help="index of the object to visualize")

    parser.add_argument('--test_data', type=str, default='./data/seg/data_test.npy')
    parser.add_argument('--test_label', type=str, default='./data/seg/label_test.npy')
    parser.add_argument('--output_dir', type=str, default='./output/pointnetplus/')

    parser.add_argument('--exp_name', type=str, default="exp", help='The name of the experiment')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    args.device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
    create_dir(args.output_dir)

    # ------ TO DO: Initialize Model for Segmentation Task  ------
    model = seg_model(args.num_seg_class)
    
    # Load Model Checkpoint
    model_path = './checkpoints/seg_plus/{}.pt'.format(args.load_checkpoint)
    with open(model_path, 'rb') as f:
        state_dict = torch.load(f, map_location=args.device)
        model.load_state_dict(state_dict)
    model.eval()
    print ("successfully loaded checkpoint from {}".format(model_path))


    # Sample Points per Object
    ind = np.random.choice(10000,args.num_points, replace=False)
    test_data = torch.from_numpy((np.load(args.test_data))[:,ind,:])
    test_label = torch.from_numpy((np.load(args.test_label))[:,ind])
    # test_data = 
    # rotate test_data
    R = torch.tensor([[np.cos(args.rotate_strength), -np.sin(args.rotate_strength), 0],
                        [np.sin(args.rotate_strength), np.cos(args.rotate_strength), 0],
                        [0, 0, 1]])
    test_data = torch.matmul(test_data.float(), R.float())



    # ------ TO DO: Make Prediction ------
    print('predictin')
    print(test_data.shape)    
    outputs = []
    indices = [157, 416, 595]
    # indices = (range(0, len(test_label)))

    for i in indices:
        outputs.append(torch.argmax(model(test_data[i].unsqueeze(0)), dim = 1))

    pred_label = torch.stack(outputs, dim=0)
    # print("Rand model")
    # test_accuracy = pred_label.eq(test_label.data).cpu().sum().item() / (test_label.reshape((-1,1)).size()[0])
    # print ("test accuracy: {}".format(test_accuracy))

    # Visualize Segmentation Result (Pred VS Ground Truth)
    for i, idx in enumerate(indices):
        viz_seg(test_data[idx], test_label[idx], "{}/gt_{}_{}.gif".format(args.output_dir, args.exp_name, idx), args.device)
        viz_seg(test_data[idx], pred_label[i], "{}/pred_{}_{}.gif".format(args.output_dir, args.exp_name, idx), args.device)
