#builtin modules
from typing import *
import base64
import io

from PIL import Image

from werkzeug.datastructures import *
from flask import Flask, request
from flask_cors import CORS

from .pixelgen import make_dot


PARAM_LIMIT = {
    'k': (1, 48),
    'scale': (1, 8),
    'precise': (1, 10),
    'blur': (0, 10),
    'erode': (0, 4),
    'saturation': (-10, 10),
    'contrast': (-10, 10),
}


app = Flask(
    __name__
)
CORS(app)


def image_process(img, settings):
    img.thumbnail(
        (512, 512), 
        Image.Resampling.LANCZOS,
    )
    output_img, colors = make_dot(img, **settings)
    output_img.thumbnail(
        (1024, 1024),
        Image.Resampling.LANCZOS,
    )
    
    buf = io.BytesIO()
    output_img.save(buf, format='PNG', quality=0)
    output_b64 = base64.b64encode(buf.getvalue())
    
    return output_b64, colors


def parse_form(
    form: ImmutableMultiDict[str, str],
    files: ImmutableMultiDict[str, FileStorage]
):
    settings = {}
    
    for key, (min, max) in PARAM_LIMIT.items():
        if key not in form:
            return None, None, 'Invalid form: unknown key'
        
        try:
            val = int(form[key])
        except:
            return None, None, f'Invalid value for {key}'
        
        if min <= val <= max:
            settings[key] = val
        else:
            return None, None, f'Invalid value for {key}'
    
    if 'file' in files:
        file = files['file'].stream
    else:
        return None, None, 'Invalid form: No image.'
    
    return file, settings, None


@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.form
    file = request.files
    
    fs, settings, err = parse_form(data, file)
    
    if err is not None:
        return {
            'status': 'Error',
            'data': {},
            'Error': err
        }
    
    img = Image.open(fs)
    output_b64, colors = image_process(img, settings)
    
    return {
        'status': 'ok',
        'data': {
            'output_img': (
                'data:image/png;base64,'
                + output_b64.decode('ASCii')
            ),
            'colors': colors
        }
    }


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)