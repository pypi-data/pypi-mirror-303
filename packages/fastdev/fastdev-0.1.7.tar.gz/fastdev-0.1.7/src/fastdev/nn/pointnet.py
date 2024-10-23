"""
PointNet implementation in PyTorch.

Adapted from: https://github.com/yanx27/Pointnet_Pointnet2_pytorch/
"""

from typing import Optional

import torch
import torch.nn as nn


# https://github.com/yanx27/Pointnet_Pointnet2_pytorch/blob/master/models/pointnet_utils.py
class STNkd(nn.Module):
    def __init__(self, k: int = 64):
        super().__init__()
        self.k = k
        self.conv1 = nn.Conv1d(k, 64, 1)
        self.conv2 = nn.Conv1d(64, 128, 1)
        self.conv3 = nn.Conv1d(128, 1024, 1)
        self.fc1 = nn.Linear(1024, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, k * k)

        self.relu = nn.ReLU(inplace=True)
        self.bn1 = nn.BatchNorm1d(64)
        self.bn2 = nn.BatchNorm1d(128)
        self.bn3 = nn.BatchNorm1d(1024)
        self.bn4 = nn.BatchNorm1d(512)
        self.bn5 = nn.BatchNorm1d(256)

        self.iden = torch.eye(k).flatten().view(1, k * k)

    def forward(self, x: torch.Tensor):
        batchsize = x.size(0)
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.relu(self.bn3(self.conv3(x)))
        x = torch.max(x, 2, keepdim=True)[0].view(-1, 1024)

        x = self.relu(self.bn4(self.fc1(x)))
        x = self.relu(self.bn5(self.fc2(x)))
        x = self.fc3(x)

        iden = self.iden.repeat(batchsize, 1).to(device=x.device)
        x = (x + iden).view(-1, self.k, self.k)
        return x


class PointNetEncoder(nn.Module):
    """
    Encoder for PointNet.

    This implementation differs from the original repository by adding an option to apply a transformation to the input points (default: False).
    STNkd is reused for both point and feature transformations, with STN3d being a special case of STNkd.

    Forward method:
        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, channels, num_points).
        Returns:
            torch.Tensor: Extracted features.
            torch.Tensor: Transformation matrix applied to the points.
            torch.Tensor: Transformed features.

    Reference: https://github.com/yanx27/Pointnet_Pointnet2_pytorch/blob/master/models/pointnet_utils.py
    """

    def __init__(
        self,
        input_dim: int = 3,
        feature_dim: int = 1024,
        global_feature: bool = True,
        point_transform: bool = False,
        feature_transform: bool = False,
    ):
        """Initialize PointNet encoder.

        Args:
            input_dim (int, optional): Dimension of input points. Defaults to 3.
            feature_dim (int, optional): Dimension of extracted global features. Defaults to 1024.
            global_feature (bool, optional): If True, return global features only. If False, return concatenated features. Defaults to True.
            point_transform (bool, optional): Whether to apply a spatial transformer to the input points. Defaults to False.
            feature_transform (bool, optional): Whether to apply a spatial transformer to feature vectors. Defaults to False.
        """
        super().__init__()
        self.global_feat = global_feature
        self.point_transform = point_transform
        self.feature_transform = feature_transform

        self.conv1 = torch.nn.Conv1d(input_dim, 64, 1)
        self.conv2 = torch.nn.Conv1d(64, 128, 1)
        self.conv3 = torch.nn.Conv1d(128, 1024, 1)
        self.bn1 = nn.BatchNorm1d(64)
        self.bn2 = nn.BatchNorm1d(128)
        self.bn3 = nn.BatchNorm1d(1024)
        self.relu = nn.ReLU(inplace=True)
        if self.point_transform:
            self.stn = STNkd(k=3)
        if self.feature_transform:
            self.fstn = STNkd(k=64)
        if feature_dim != 1024:
            self.feat_linear: Optional[nn.Linear] = torch.nn.Linear(1024, feature_dim)
        else:
            self.feat_linear = None

    def forward(self, x: torch.Tensor):
        """Forward pass.

        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, channels, num_points).

        Returns:
            torch.Tensor: Extracted features.
            torch.Tensor: Transformation matrix applied to the points.
            torch.Tensor: Transformation matrix applied to the features.
        """
        B, D, N = x.size()
        if self.point_transform:
            trans = self.stn(x)
            x = x.transpose(2, 1)
            if D > 3:
                feature = x[:, :, 3:]
                x = x[:, :, :3]
            x = torch.bmm(x, trans)
            if D > 3:
                x = torch.cat([x, feature], dim=2)
            x = x.transpose(2, 1)
        else:
            trans = None

        x = self.relu(self.bn1(self.conv1(x)))

        if self.feature_transform:
            trans_feat = self.fstn(x)
            x = x.transpose(2, 1)
            x = torch.bmm(x, trans_feat)
            x = x.transpose(2, 1)
        else:
            trans_feat = None

        pointfeat = x
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.bn3(self.conv3(x))
        x = torch.max(x, 2, keepdim=True)[0]
        x = x.view(-1, 1024)
        if self.feat_linear is not None:
            x = self.feat_linear(x)

        if self.global_feat:
            return x, trans, trans_feat
        else:
            x = x.view(-1, 1024, 1).repeat(1, 1, N)
            return torch.cat([x, pointfeat], 1), trans, trans_feat


# https://github.com/yanx27/Pointnet_Pointnet2_pytorch/blob/master/models/pointnet_cls.py
class PointNetCls(nn.Module):
    def __init__(
        self,
        k: int = 40,
        normal_channel: bool = True,
        point_transform: bool = False,
        feature_transform: bool = False,
    ):
        super().__init__()
        channel = 6 if normal_channel else 3
        self.feat = PointNetEncoder(
            input_dim=channel,
            global_feature=True,
            point_transform=point_transform,
            feature_transform=feature_transform,
        )
        self.fc1 = nn.Linear(1024, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, k)
        self.dropout = nn.Dropout(p=0.4)
        self.bn1 = nn.BatchNorm1d(512)
        self.bn2 = nn.BatchNorm1d(256)
        self.relu = nn.ReLU(inplace=True)
        self.log_softmax = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x, trans, trans_feat = self.feat(x)
        x = self.relu(self.bn1(self.fc1(x)))
        x = self.relu(self.bn2(self.dropout(self.fc2(x))))
        x = self.fc3(x)
        x = self.log_softmax(x)
        return x, trans_feat


def feature_transform_reguliarzer(trans: torch.Tensor) -> torch.Tensor:
    d = trans.size()[1]
    iden = torch.eye(d)[None, :, :]
    if trans.is_cuda:
        iden = iden.cuda()
    loss = torch.mean(torch.norm(torch.bmm(trans, trans.transpose(2, 1)) - iden, dim=(1, 2)))
    return loss


# https://github.com/yanx27/Pointnet_Pointnet2_pytorch/blob/master/models/pointnet_sem_seg.py
class PointNetSemSeg(nn.Module):
    def __init__(
        self,
        num_classes: int,
        point_transform: bool = False,
        feature_transform: bool = False,
    ):
        super().__init__()
        self.k = num_classes
        self.feat = PointNetEncoder(
            input_dim=9,
            global_feature=False,
            point_transform=point_transform,
            feature_transform=feature_transform,
        )
        self.conv1 = torch.nn.Conv1d(1088, 512, 1)
        self.conv2 = torch.nn.Conv1d(512, 256, 1)
        self.conv3 = torch.nn.Conv1d(256, 128, 1)
        self.conv4 = torch.nn.Conv1d(128, self.k, 1)
        self.bn1 = nn.BatchNorm1d(512)
        self.bn2 = nn.BatchNorm1d(256)
        self.bn3 = nn.BatchNorm1d(128)
        self.relu = nn.ReLU(inplace=True)
        self.log_softmax = nn.LogSoftmax(dim=-1)

    def forward(self, x):
        batchsize = x.size()[0]
        n_pts = x.size()[2]
        x, trans, trans_feat = self.feat(x)
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.relu(self.bn2(self.conv2(x)))
        x = self.relu(self.bn3(self.conv3(x)))
        x = self.conv4(x)
        x = x.transpose(2, 1).contiguous()
        x = self.log_softmax(x.view(-1, self.k))
        x = x.view(batchsize, n_pts, self.k)
        return x, trans_feat


__all__ = ["PointNetEncoder", "PointNetCls", "PointNetSemSeg", "feature_transform_reguliarzer"]
