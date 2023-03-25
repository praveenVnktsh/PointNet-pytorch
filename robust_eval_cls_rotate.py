import numpy as np
import argparse

import torch
from models import cls_model
from data_loader import get_data_loader

from utils import create_dir, viz_seg, viz_cls
from tqdm import tqdm
def create_parser():
    """Creates a parser for command-line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--num_cls_class', type=int, default=3, help='The number of classes')
    parser.add_argument('--num_points', type=int, default=5000, help='The number of points per object to be included in the input data')

    # Directories and checkpoint/sample iterations
    parser.add_argument('--load_checkpoint', type=str, default='model_epoch_30')
    parser.add_argument('--i', type=int, default=0, help="index of the object to visualize")
    parser.add_argument('--rotate_strength', type=float, default= 30 * np.pi/180, help="index of the object to visualize")

    parser.add_argument('--test_data', type=str, default='./data/cls/data_test.npy')
    parser.add_argument('--test_label', type=str, default='./data/cls/label_test.npy')
    parser.add_argument('--output_dir', type=str, default='./output/cls/')

    parser.add_argument('--exp_name', type=str, default="exp", help='The name of the experiment')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    args.device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
    args.output_dir = './output/cls' + str(args.rotate_strength) + '/'
    create_dir(args.output_dir)

    # ------ TO DO: Initialize Model for Classification Task ------
    model = cls_model()
    args.main_dir = './data/' 
    args.task = 'cls'
    args.batch_size = 2
    args.num_workers = 0
    # Load Model Checkpoint
    model_path = './checkpoints/cls/{}.pt'.format(args.load_checkpoint)
    with open(model_path, 'rb') as f:
        state_dict = torch.load(f, map_location=args.device)
        model.load_state_dict(state_dict)
    model.eval()
    print ("successfully loaded checkpoint from {}".format(model_path))


    # Sample Points per Object
    ind = np.random.choice(10000,args.num_points, replace=False)
    test_data = torch.from_numpy((np.load(args.test_data))[:,ind,:])
    test_label = torch.from_numpy(np.load(args.test_label))

    # ------ TO DO: Make Prediction ------
    test_dataloader = get_data_loader(args=args, train=False)
    outputs = []
    test_label = []
    R = torch.tensor([[np.cos(args.rotate_strength), -np.sin(args.rotate_strength), 0],
                        [np.sin(args.rotate_strength), np.cos(args.rotate_strength), 0],
                        [0, 0, 1]])
    test_data = torch.matmul(test_data.float(), R.float())
    for batch in tqdm(test_dataloader):
        point_clouds, labels = batch
        point_clouds = torch.matmul(point_clouds.float(), R.float())
        if len(point_clouds) < 2:
            continue
        test_label.append(labels)
        outputs.append(torch.argmax(model(point_clouds).view(-1, 3), dim = 1))

    pred_label = torch.stack(outputs, dim=0).squeeze().flatten()
    test_label = torch.stack(test_label, dim=0).squeeze().flatten()

    wrongindices = pred_label != test_label
    print("wrong indices: {}".format((wrongindices.nonzero().flatten().tolist())))

    # Compute Accuracy
    print(test_label.shape, pred_label.shape)
    test_accuracy = pred_label.eq(test_label.data).cpu().sum().item() / (test_label.size()[0])
    print ("test accuracy: {}".format(test_accuracy))

    for i in tqdm(range(0, len(test_label))):
        if i % 100 == 0:
            viz_cls(test_data[i], test_label[i], pred_label[i].item(), "{}/gt_{}_{}.gif".format(args.output_dir, args.exp_name, i), args.device)

    for i in tqdm(wrongindices.nonzero().flatten().tolist()):
        viz_cls(test_data[i], test_label[i], pred_label[i].item(), "{}/pred_{}_{}.gif".format(args.output_dir, args.exp_name, i), args.device)