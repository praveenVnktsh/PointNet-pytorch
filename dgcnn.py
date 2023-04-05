import os
import sys
import copy
import math
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


def knn(x, k):
    # taken from online sources
    inner_prod = -2*torch.matmul(x.transpose(2, 1), x)
    xx = torch.sum(x**2, dim=1, keepdim=True)
    distances = - xx - inner_prod - xx.transpose(2, 1)
    idx = distances.topk(k=k, dim=-1)[1]  
    return idx


def get_graph_feature(x, k=20, idx=None):
    batch_size = x.size(0)
    num_points = x.size(1)
    x = x.view(batch_size, -1, num_points)

    idx = knn(x, k=k)   # (batch_size, num_points, k)

    idx_base = torch.arange(0, batch_size, device='cuda').view(-1, 1, 1)*num_points

    idx = (idx + idx_base).flatten()

    num_dims = x.size(1)
    # (batch_size, num_points, num_dims)  -> (batch_size*num_points, num_dims) 
    #  batch_size * num_points * k + range(0, batch_size*num_points)
    feature = x.view(batch_size*num_points, -1)[idx, :]
    feature = feature.view(batch_size, num_points, k, num_dims)  # B x N x K x D
    # TODO: convert x = B x N x 1 x D to shape x = B x N x k x D (hint: repeating the elements in that dimension)
    x = x.view(batch_size, num_points, 1, num_dims).repeat(1, 1, k, 1)
    feature = torch.cat((feature-x, x), dim=3)
    feature = feature.view(batch_size, num_dims * 2,  k, num_points)
  
    return feature

class DGCNN(nn.Module):
    def __init__(self, args, output_channels = 3):
        super(DGCNN, self).__init__()
        self.args = args
        self.k = args.k

        # TODO: 4 Batch Norm 2D + 1 Batch Norm 1D
        # TODO: 5 conv2D layers + BN + ReLU/Leaky ReLU
        # TODO: 2 Linear layers + BN + Dropout
        # TODO: 1 final Linear layer

        self.conv1 = nn.Sequential(
            nn.Conv2d(6, 64, kernel_size=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(negative_slope=0.2, inplace=True),
        )

        self.conv2 = nn.Sequential(
            nn.Conv2d(64 * 2, 128, kernel_size=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(negative_slope=0.2, inplace=True),
        )

        self.conv3 = nn.Sequential(
            nn.Conv2d(128 * 2, 256, kernel_size=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(negative_slope=0.2, inplace=True),
        )

        self.conv4 = nn.Sequential(
            nn.Conv2d(256 * 2, 512, kernel_size=1, bias=False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(negative_slope=0.2, inplace=True),
        )

        self.linear = nn.Sequential(
            nn.Linear(82, 256),
            nn.BatchNorm1d(256),
            nn.Dropout(p=0.5),
            nn.LeakyReLU(negative_slope=0.2, inplace=True),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.Dropout(p=0.5),
            nn.LeakyReLU(negative_slope=0.2, inplace=True),
            nn.Linear(128, output_channels),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        batch_size = x.size(0)
        x = get_graph_feature(x, k=self.k)
        x = self.conv1(x)
        x1 = x.max(dim=-1, keepdim=False)[0]
        x = get_graph_feature(x1, k=self.k)
        x2 = x.max(dim=-1, keepdim=False)[0]
        x = get_graph_feature(x2, k=self.k)
        x3 = x.max(dim=-1, keepdim=False)[0]
        x = get_graph_feature(x3, k=self.k)
        x4 = x.max(dim=-1, keepdim=False)[0]
        x = torch.cat((x1, x2, x3, x4), dim=1)
        x1 = F.adaptive_max_pool1d(x, 1).view(batch_size, -1)
        x = self.linear(x1)
        return x