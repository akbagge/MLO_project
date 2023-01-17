import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2
import cv2

IMAGE_SIZE = 224

AUGMENT = A.Compose(
            [
                A.Resize(width=IMAGE_SIZE, height=IMAGE_SIZE),
                A.Normalize(mean=(0.485, 0.456, 0.406),
                            std=(0.229, 0.224, 0.225),
                            max_pixel_value=255),
                ToTensorV2(),
            ]
        )

LABELS = ["Arborio", "Basmati", "Ipsala", "Jasmine", "Karacadag"]

class RiceModel( ): 
    
    def __init__(self, timm_model) -> None:
        #super(RiceModel, self).__init__()
        self.model = timm_model

    def predict(self, img_path): 

        with torch.no_grad():
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = AUGMENT(image=img)['image']
            
            output = self.model(img.float().unsqueeze(0))
            output = output.softmax(-1)
            output, indices = output.topk(1)

            print("{} width {:.2f}% certainty".format(LABELS[indices.cpu().numpy()[0][0]], float(output[0][0])*100))







