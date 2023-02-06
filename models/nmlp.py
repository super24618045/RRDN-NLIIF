import torch.nn as nn
import torch
from models import register


@register('nmlp')
class NMLP(nn.Module):

    def __init__(self, in_dim, out_dim, hidden_list):
        super().__init__()
        layers = []
        lastv = in_dim
        """
        for hidden in hidden_list:
            layers.append(nn.Linear(lastv, hidden))
            layers.append(nn.ReLU())
            lastv = hidden
            count = count + 1
        layers.append(nn.Linear(lastv, out_dim))
        self.layers = nn.Sequential(*layers)
        """
        self.lin1 = nn.Linear(lastv,256)
        self.lin2 = nn.ModuleList([nn.Linear(304, 256) for i in range(8)])
        self.lin3 = nn.Linear(256,out_dim)
        #self.dropout = nn.Dropout(p=0.2)
        #self.activate = nn.ReLU()
        self.activate = nn.LeakyReLU(negative_slope=0.2)

    def forward(self, x,spatial = None):
        code = spatial
        code = code.view(-1,code.shape[-1])
        shape = x.shape[:-1]
        x = self.lin1(x.view(-1, x.shape[-1]))
        x = self.activate(x)
        for i in range(0,8,2):
            res = x
            x = torch.cat([x,code], dim=-1)
            x = self.lin2[i](x)
            x = self.activate(x)
            x = torch.cat([x,code], dim=-1)
            x = self.lin2[i+1](x)
            x = res + x
            x = self.activate(x)
        x = self.lin3(x)
        return x.view(*shape, -1)

