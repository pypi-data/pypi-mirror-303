import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


def findConv2dOutShape(hin,win,conv,pool=2):
    # get conv arguments
    kernel_size=conv.kernel_size
    stride=conv.stride
    padding=conv.padding
    dilation=conv.dilation

    hout=np.floor((hin+2*padding[0]-dilation[0]*(kernel_size[0]-1)-1)/stride[0]+1)
    wout=np.floor((win+2*padding[1]-dilation[1]*(kernel_size[1]-1)-1)/stride[1]+1)

    if pool:
        hout/=pool
        wout/=pool
    return int(hout),int(wout)

class CNN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(CNN, self).__init__()
        
        Cin, Hin, Win = 1, input_dim, input_dim
        init_f = 8
        num_fc1 = 100
        
        self.conv1 = nn.Conv2d(Cin, init_f, kernel_size=3, padding=1)
        self.conv1_bn = nn.BatchNorm2d(init_f)
        h,w=findConv2dOutShape(Hin,Win,self.conv1,pool=0)
        
        self.conv2 = nn.Conv2d(init_f, 2*init_f, kernel_size=3, padding=1)
        self.conv2_bn = nn.BatchNorm2d(2*init_f)
        h,w=findConv2dOutShape(h,w,self.conv2,pool=0)
        
        # self.conv3 = nn.Conv2d(2*init_f, 4*init_f, kernel_size=5, padding=1)
        # self.conv3_bn = nn.BatchNorm2d(4*init_f)
        # h,w=findConv2dOutShape(h,w,self.conv3,pool=0)
        
        self.num_flatten=h*w*init_f*2
        self.fc1 = nn.Linear(self.num_flatten, num_fc1)
        self.fc1_bn = nn.BatchNorm1d(num_fc1)
        
        self.fc2 = nn.Linear(num_fc1, output_dim)
        
        self.dropout = nn.Dropout(0.1)
    
    def forward(self,x):
        x = self.conv1(x)
        x = F.relu(self.conv1_bn(x))
        x = self.dropout(x)
        
        x = self.conv2(x)
        x = F.relu(self.conv2_bn(x))
#         x = self.dropout(x)
        
#         x = self.conv3(x)
#         x = F.relu(self.conv3_bn(x))
        # x = self.dropout(x)
        
        x = x.contiguous().view(-1, self.num_flatten)
        
        x = self.fc1(x)
        x = F.relu(self.fc1_bn(x))
        x = self.dropout(x)
        
        x = self.fc2(x)
#         x = F.relu(self.fc2_bn(x))
#         x = self.dropout(x)
        
#         x = self.fc3(x)
        
        return F.log_softmax(x, dim=1)
    
# class CNN(nn.Module):
#     def __init__(self, input_dim, output_dim):
#         super(CNN, self).__init__()
        
#         Cin, Hin, Win = 1, input_dim, input_dim
#         init_f = 6
#         num_fc1 = 100
        
#         self.conv1 = nn.Conv2d(Cin, init_f, kernel_size=5, padding=1)
#         h,w=findConv2dOutShape(Hin,Win,self.conv1,pool=2)
#         self.conv2 = nn.Conv2d(init_f, 2*init_f, kernel_size=5, padding=1)
#         h,w=findConv2dOutShape(h,w,self.conv2,pool=2)
        
#         self.num_flatten=h*w*init_f*2
#         # self.fc1 = nn.Linear(self.num_flatten, num_fc1)
#         # self.fc2 = nn.Linear(num_fc1, output_dim)
#         self.fc1 = nn.Linear(self.num_flatten, 120)
#         self.fc2 = nn.Linear(120, 84)
#         self.fc3 = nn.Linear(84, output_dim)
#         self.dropout = nn.Dropout(0.2)
    
#     def forward(self,x):
        
#         x = self.conv1(x)
#         x = F.max_pool2d(x, kernel_size=2);
#         x = F.relu(x);
        
#         x = self.conv2(x)
#         x = F.max_pool2d(x, kernel_size=2);
#         x = F.relu(x);
        
#         x = x.contiguous().view(-1, self.num_flatten)
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = self.dropout(x)
#         x = self.fc3(x)
        
#         return F.log_softmax(x, dim=1)
        
    
class LeNet(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        
        self.conv1 = nn.Conv2d(in_channels=1,
                               out_channels=6,
                               kernel_size=5)

        self.conv2 = nn.Conv2d(in_channels=6,
                               out_channels=16,
                               kernel_size=5)
        
        self.fc_1 = nn.Linear(16 * 4 * 4, 120)
        self.fc_2 = nn.Linear(120, 84)
        self.fc_3 = nn.Linear(84, output_dim)

    def forward(self, x):

        # x = [batch size, 1, 28, 28]

        x = self.conv1(x)

        # x = [batch size, 6, 24, 24]

        x = F.max_pool2d(x, kernel_size=2)

        # x = [batch size, 6, 12, 12]

        x = F.relu(x)

        x = self.conv2(x)

        # x = [batch size, 16, 8, 8]

        x = F.max_pool2d(x, kernel_size=2)

        # x = [batch size, 16, 4, 4]

        x = F.relu(x)

        x = x.view(x.shape[0], -1)

        # x = [batch size, 16*4*4 = 256]

        h = x

        x = self.fc_1(x)

        # x = [batch size, 120]

        x = F.relu(x)

        x = self.fc_2(x)

        # x = batch size, 84]

        x = F.relu(x)

        x = self.fc_3(x)

        # x = [batch size, output dim]

        return x