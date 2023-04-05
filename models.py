import torch
import torch.nn as nn
import torch.nn.functional as F

# ------ TO DO ------
class cls_model(nn.Module):
    def __init__(self, num_classes=3):
        super(cls_model, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(3, 64),   
            nn.ReLU(),
            nn.Linear(64, 64),   
            nn.ReLU(),
            nn.Linear(64, 1024),
            nn.ReLU(),
        )

        self.classifier = nn.Sequential(
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(256, num_classes),
            nn.Softmax(dim=1)
        )
        
    def forward(self, points):
        '''
        points: tensor of size (B, N, 3)
                , where B is batch size and N is the number of points per object (N=10000 by default)
        output: tensor of size (B, num_classes)
        '''
        feature = self.model(points)
        outputs, _ = torch.max(feature, dim = 1, keepdim = True)
        out = self.classifier(outputs.squeeze())
        return out



# ------ TO DO ------
class seg_model(nn.Module):
    def __init__(self, num_seg_classes = 6):
        super(seg_model, self).__init__()
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
            nn.Linear(1024 + 64, 512),
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(p=0.3),
            nn.Linear(256, num_seg_classes),
            nn.Softmax(dim=2)
        )

    def forward(self, points):
        '''
        points: tensor of size (B, N, 3)
                , where B is batch size and N is the number of points per object (N=10000 by default)
        output: tensor of size (B, N, num_seg_classes)
        '''
        feature = self.model1(points)
        feature2 =  self.model2(feature)
        outputs, _ = torch.max(feature2, dim = 1, keepdim = True)
        outputs = outputs.repeat(1, points.shape[1], 1)
        newfeats = torch.cat([outputs, feature], dim = 2)
        preds = self.concatmodel(newfeats).squeeze()
        
        return preds
