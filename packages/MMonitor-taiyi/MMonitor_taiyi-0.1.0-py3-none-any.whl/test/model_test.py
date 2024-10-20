from model.model import Model
import torch
config = {'epoch': 100, 'w': 224, 'h': 224, 'class_num': 5, 'len': 100, 'lr': 1e-2}
x = torch.randn((config['len'], 3,config['w'],config['h']), requires_grad=True)
model = Model()
y = model(x)
print(f'The running result of the current model is{y}')
