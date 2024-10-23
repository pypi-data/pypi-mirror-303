# server.py

from ciferai import get_eval_fn, set_initial_parameters, get_parameters, set_parameters, create_cifer_client
import torch
import torchvision
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# การตั้งค่าของโมเดลและข้อมูล
model = torchvision.models.resnet18(pretrained=False, num_classes=10)
trainloader = DataLoader(datasets.MNIST('.', train=True, download=True, transform=transforms.ToTensor()), batch_size=32, shuffle=True)
testloader = DataLoader(datasets.MNIST('.', train=False, transform=transforms.ToTensor()), batch_size=32, shuffle=False)

# การสร้าง client ของ cifer
cifer_client = create_cifer_client(model, trainloader, testloader)

# การทดสอบการใช้งานฟังก์ชันที่ import มา
params = get_parameters(model)
print("Model parameters:", params)

# การกำหนดพารามิเตอร์ใหม่ให้กับโมเดล
new_params = params  # สมมติว่าคุณมีพารามิเตอร์ใหม่ที่ต้องการตั้ง
set_parameters(model, new_params)

# การเรียกใช้ evaluation function
eval_fn = get_eval_fn(model, testloader)
loss, accuracy = eval_fn()
print(f"Loss: {loss}, Accuracy: {accuracy}")
