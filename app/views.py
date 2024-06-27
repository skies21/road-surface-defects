from django.core.files.storage import default_storage
from django.shortcuts import render
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet_v2 import preprocess_input
from keras.models import Sequential, load_model
import numpy as np

from app.forms import ImageUploadForm

# Loading the model
model = load_model("app/ResNet152V2.h5")


def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array


def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['image']
            img_path = default_storage.save('tmp/' + img.name, img)
            img_array = prepare_image(img_path)
            prediction = model.predict(img_array)
            result = prediction[0]

            return render(request, 'result.html', {'result': result, 'img_path': img_path})

    else:
        form = ImageUploadForm()

    return render(request, 'index.html', {'form': form})
