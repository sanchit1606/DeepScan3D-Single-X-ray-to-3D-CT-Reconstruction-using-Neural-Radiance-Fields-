import torch
print(torch.cuda.is_available())  # Should return True
print(torch.version.cuda)         # Should print 12.1