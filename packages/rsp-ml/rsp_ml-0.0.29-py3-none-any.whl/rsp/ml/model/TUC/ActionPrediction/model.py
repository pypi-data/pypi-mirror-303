import torch
import torch.nn as nn
import torch.nn.functional as F

class Conv2DBlock(nn.Module):
    def __init__(
            self,
            in_channels:int,
            out_channels:int,
            kernel_size_conv:tuple[int, int],
            kernel_size_pool:tuple[int, int],
            stride:tuple[int, int],
            padding_conv:int = 0,
            p_dropout:float = 0.5
    ):
        super(Conv2DBlock, self).__init__()

        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=kernel_size_conv, padding=padding_conv)
        self.pool = nn.MaxPool2d(kernel_size=kernel_size_pool, stride=stride)
        self.dropout = nn.Dropout2d(p_dropout)
        self.relu = nn.LeakyReLU()
    
    def forward(self, X):
        Y = self.conv(X)
        Y = self.pool(Y)
        Y = self.dropout(Y)
        Y = self.relu(Y)

        return Y

class SelfAttention(nn.Module):
    def __init__(
            self,
            d_q:int = 2,
            d_k:int = 2,
            d_v:int = 4,
            embed_dim:int = 3
        ):
        super().__init__()

        self.d_q = d_q
        self.d_k = d_k
        self.d_v = d_v

        self.W_q = nn.Parameter(torch.rand(embed_dim, d_q))
        self.W_k = nn.Parameter(torch.rand(embed_dim, d_k))
        self.W_v = nn.Parameter(torch.rand(embed_dim, d_v))
        pass

    def forward(self, X):
        Z = []
        # iterate over batch_size
        for x in X:
            Q = x @ self.W_q    # Queries
            K = x @ self.W_k    # Keys
            V = x @ self.W_v    # Values

            omega = Q @ K.T                                     # omega ...unnormalized attantion weights
            alpha = F.softmax(omega / self.d_k**0.5, dim=0)     # alpha ...normalized attention weights
            z = alpha @ V                                       # z     ...context vector -> attention-weighted version of original query input x_i
            Z.append(z)
        
        Z = torch.stack(Z)
        return Z

class MultiHeadSelfAttention(nn.Module):
    def __init__(
            self,
            num_heads:int,
            d_q:int = 2,
            d_k:int = 2,
            d_v:int = 4,
            embed_dim:int = 3
        ):
        super().__init__()

        self.d_q = d_q
        self.d_k = d_k
        self.d_v = d_v

        self.heads = nn.ModuleList([SelfAttention(d_q, d_k, d_v, embed_dim) for _ in range(num_heads)])

    def forward(self, X):
        return torch.cat([head(X) for head in self.heads], dim=-1)

class Model4(nn.Module):
    def __init__(
            self,
            sequence_length = 30,
            num_actions:int = 10
        ):
        super().__init__()
        self.sequence_length = sequence_length,
        self.num_actions = num_actions

        self.embed = nn.Embedding(sequence_length, 1000)

        self.conv1 = Conv2DBlock(
            in_channels = 3,
            out_channels = 16,
            kernel_size_conv = (9, 9),
            kernel_size_pool = (7, 7),
            stride = (5, 5),
            padding_conv=1,
            p_dropout = 0
        )
        self.conv2 = Conv2DBlock(
            in_channels = 16,
            out_channels = 32,
            kernel_size_conv = (7, 7),
            kernel_size_pool = (5, 5),
            stride = (3, 3),
            p_dropout = 0
        )
        self.conv3 = Conv2DBlock(
            in_channels = 32,
            out_channels = 64,
            kernel_size_conv = (5, 5),
            kernel_size_pool = (3, 3),
            stride = (2, 2),
            p_dropout = 0
        )
        # self.conv4 = Conv2DBlock(
        #     in_channels = 64,
        #     out_channels = 128,
        #     kernel_size_conv = (5, 5),
        #     kernel_size_pool = (3, 3),
        #     stride = (2, 2)
        # )

        self.attention = MultiHeadSelfAttention(num_heads=16, embed_dim=256)
        self.flatten = nn.Flatten(start_dim=1)

        readout_dim1 = sequence_length * len(self.attention.heads) * self.attention.d_v
        self.readout = nn.Linear(readout_dim1, num_actions)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, X:torch.Tensor):
        Y = X.reshape((X.shape[0] * X.shape[1], X.shape[2], X.shape[3], X.shape[4]))
        #print(Y.shape)
        Y = self.conv1(Y)
        #print(Y.shape)
        Y = self.conv2(Y)
        #print(Y.shape)
        Y = self.conv3(Y)
        #print(Y.shape)
        #Y = self.conv4(Y)
        #print(Y.shape)
        Y = Y.reshape((X.shape[0], X.shape[1], Y.shape[1] * Y.shape[2] * Y.shape[3]))
        #print(Y.shape)
        Y = self.attention(Y)
        #print(Y.shape)
        Y = self.flatten(Y)
        #print(Y.shape)
        Y = self.readout(Y)
        Y = self.softmax(Y)
        return Y