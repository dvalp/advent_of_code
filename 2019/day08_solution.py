import numpy as np
from PIL import Image


def decode_image():
    with open("input_day08", "r") as f:
        input_data = np.array(list(f.read().strip()), dtype=int).reshape(-1, 6, 25)

    layers = input_data.reshape(input_data.shape[0], -1)
    layer_idx = (layers == 0).sum(axis=1).argmin()

    # Validate image
    assert ((layers[layer_idx] == 1).sum() * (layers[layer_idx] == 2).sum()) == 2760
    # 2.15 ms ± 16.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

    comp_img = [layer[(layer < 2).argmax()] for layer in layers.T]

    img = Image.new('1', (25, 6), "white")
    img.putdata(comp_img)
    img.show()
    # CPU times: user 5.27 ms, sys: 8.26 ms, total: 13.5 ms
    # Wall time: 12.9 ms
