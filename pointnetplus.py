import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
from torch import nn

class KNN(nn.Module):
    def __init__(self, k):
        super().__init__()
        self.k = k

    def forward(self, x):
        batch_size, num_points, _ = x.size()
        x = x.view(batch_size * num_points, -1)
        dists, idx = self._knn(x, self.k + 1)
        dists = dists[:, 1:].view(batch_size, num_points, self.k)
        idx = idx[:, 1:].view(batch_size, num_points, self.k)
        return dists, idx

    def _knn(self, x, k):
        inner = -2 * torch.matmul(x, x.transpose(1, 0))
        xx = torch.sum(x ** 2, dim=1, keepdim=True)
        pairwise_distance = -xx - inner - xx.transpose(1, 0)

        dists, idx = pairwise_distance.topk(k=k, dim=-1, largest=False)
        return dists, idx


# ------ TO DO ------
class seg_model(nn.Module):
    def __init__(self, num_seg_classes = 6):
        super(seg_model, self).__init__()
        self.k = 3
        self.model1 = nn.Sequential(
            nn.Linear(3, 64),   
            nn.ReLU(),
            nn.Linear(64, 64),   
            nn.ReLU(),
        )
        self.model2 = nn.Sequential(
            nn.Linear(64, 1024),
            nn.ReLU(),
        )

        self.concatmodel = nn.Sequential(
            nn.Linear(1100, 512),
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(256, num_seg_classes),
            nn.Softmax(dim=2)
        )
        self.knn = KNN(self.k)

    def forward(self, points):
        '''
        points: tensor of size (B, N, 3)
                , where B is batch size and N is the number of points per object (N=10000 by default)
        output: tensor of size (B, N, num_seg_classes)
        '''
        batch_size, num_points, _ = points.size()
        
        feature = self.model1(points)
        feature2 = self.model2(feature)

        knn_dists, knn_idx = self.knn(feature2)
        knn_pts = torch.gather(points.unsqueeze(2).expand(-1, -1, self.k, -1), 1, knn_idx.unsqueeze(-1).expand(-1, -1, -1, 3))
        knn_feats = torch.cat([knn_pts - points.unsqueeze(2), knn_dists.unsqueeze(-1)], dim=-1)
        knn_feats = knn_feats.view(batch_size * num_points, -1)

        outputs, _ = torch.max(feature2, dim=1, keepdim=True)
        outputs = outputs.repeat(1, num_points, 1)
        newfeats = torch.cat([outputs, feature], dim=2)

        newfeats = newfeats.view(batch_size * num_points, -1)
        newfeats = torch.cat([newfeats, knn_feats], dim=1)
        newfeats = newfeats.view(batch_size, num_points, -1)
        preds = self.concatmodel(newfeats).squeeze()
        
        return preds
