from timm.models.resnet import resnet50
from src.models.predict_model import RiceModel
import timm
from pprint import pprint

IMAGE_SIZE = 224


def main():
    m = timm.create_model("resnet50", pretrained=True, checkpoint_path="models/model_best.pth.tar", num_classes=5 )
    m.eval()
    model = RiceModel(m)

    im = "resources/Karacadag/Karacadag (20).jpg"

    model.predict(im)


if __name__ == '__main__': 
    main()
