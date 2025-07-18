import torch
import torch.nn as nn

class BiomassRegressor(nn.Module):
    def __init__(self, in_features=1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_features, 32),
            nn.ReLU(),
            nn.Linear(32,1)
        )
    def forward(self, x):
        return self.net(x)