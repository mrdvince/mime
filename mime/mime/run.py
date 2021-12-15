import io
import pathlib
import sys

import torch
from charset_normalizer import logging
from PIL import Image
from torchvision import transforms

sys.path.append("/app/ajime/")
import model.model as module_arch  # noqa: E402


def load_model():
    model = module_arch.AjimeModel()
    checkpoint_path = (
        pathlib.Path("/app") / "ajime/saved/models/ajime/1212_124412/model_best.pth"
    )
    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    state_dict = checkpoint["state_dict"]
    model.load_state_dict(state_dict)
    model = model.to("cpu")
    mapping = checkpoint["cls_to_idx"]
    mapping = dict((v, k) for k, v in mapping.items())
    return model.eval(), mapping


model, mapping = load_model()
logging.info("Loading mapping..:" + str(mapping))


def transform_image(image_bytes):
    """
    Transform image into required DenseNet format: 224x224 with 3 RGB channels and normalized.
    Return the corresponding tensor.
    """
    my_transforms = transforms.Compose(
        [
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    """For given image bytes, predict the label using the pretrained DenseNet"""
    tensor = transform_image(image_bytes)

    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    class_name = mapping[int(predicted_idx)]
    return class_name
