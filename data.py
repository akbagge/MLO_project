import os
import requests
import shutil
import pytorch_lightning as pl
from torch.utils.data import DataLoader, random_split

#Set the URL for the dataset in Google Drive
url = "https://drive.google.com/drive/folders/1HVajOnnTGOt594MAvehNxf_jeWaeooTf"

#Set the local file path for the dataset
file_path = "dataset.zip"

#Download the dataset from Google Drive
response = requests.get(url, stream=True)
with open(file_path, "wb") as f:
    shutil.copyfileobj(response.raw, f)

#Extract the dataset
shutil.unpack_archive(file_path, ".")

#Delete the zip file
os.remove(file_path)

#Create a PyTorch Lightning DataModule to handle the dataset

class MyDataModule(pl.LightningDataModule):
    def init(self):
        super().__init__()

    def setup(self, stage=None):
        # Load and preprocess the dataset
        self.dataset = MyDataset()
        
        # Split the dataset into training and test sets
        self.train_dataset, self.test_dataset = random_split(self.dataset, [0.8, 0.2])
        
    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=32)

    def val_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=32)

#Initialize the DataModule
data_module = MyDataModule()

#Use the DataModule to retrieve the training and test dataloaders
train_dataloader = data_module.train_dataloader()
test_dataloader = data_module.val_dataloader()
