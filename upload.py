
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from timm.models.resnet import resnet50
from src.models.predict_model import RiceModel
import timm
from pprint import pprint
import uuid

IMAGEDIR = "images/"
app = FastAPI()


IMAGE_SIZE = 224
db = []

@app.post("/files/")
async def create_files(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    m = timm.create_model("resnet50", pretrained=True, checkpoint_path="models/model_best.pth.tar", num_classes=5 )
    m.eval()
    model = RiceModel(m)

    im = IMAGEDIR + file.filename

    return {model.predict(im)}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)