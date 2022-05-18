import os
from pathlib import Path

print(os.getcwd)
print(os.listdir())

print(list(Path('LOGS_SYSTEM').iterdir()))


