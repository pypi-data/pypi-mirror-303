import torch
from mdfa import MDFA

def test_mdfa():
    mdfa = MDFA(dim_in=64, dim_out=128)
    x = torch.randn(1, 64, 64, 64)
    output = mdfa(x)
    assert output.size() == torch.Size([1, 128, 64, 64])

if __name__ == '__main__':
    test_mdfa()
