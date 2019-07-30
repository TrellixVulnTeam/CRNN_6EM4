import os

import cv2 as cv
import numpy as np
from torch.utils.data import Dataset

from config import IMG_FOLDER, annotation_files, imgH, imgW, alphabet
import utils


class MJSynthDataset(Dataset):

    def __init__(self, split):
        annotation_file = annotation_files[split]

        with open(annotation_file, 'r') as file:
            self.lines = file.readlines()

        self.converter = utils.strLabelConverter(alphabet)

    def __len__(self):
        return self.lines

    def __getitem__(self, i):
        line = self.lines[i]
        img_path = line.split(' ')[0]
        img_path = os.path.join(IMG_FOLDER, img_path)
        text = img_path.split('_')[1].lower()
        img = cv.imread(img_path, 0)
        img = cv.resize(img, (imgW, imgH))
        img = np.transpose(img, (1, 0))

        text, length = self.converter.encode(text)

        return img, text, length
