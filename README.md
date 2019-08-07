# Convolutional Recurrent Neural Network

## Introduction

This is a PyTorch re-implementation of CRNN: Convolutional Recurrent Neural Network ([paper](https://arxiv.org/pdf/1507.05717.pdf)). The features are summarized blow:


## DataSet

We use the synthetic dataset ([mjsynth](http://www.robots.ox.ac.uk/~vgg/data/text/)) released by Jaderberg et al. as the training data. The dataset contains 8 millions training images and their corresponding ground truth words.
Such images are generated by a synthetic text engine and are highly realistic.

<pre>
@article{Jaderberg14c,
      title={Synthetic Data and Artificial Neural Networks for Natural Scene Text Recognition},
      author={Jaderberg, M. and Simonyan, K. and Vedaldi, A. and Zisserman, A.},
      journal={arXiv preprint arXiv:1406.2227},
      year={2014}
    }
</pre>

## Dependency

- PyTorch 1.1.0

## Usage
### Data Pre-processing
Extract training & test images:
```bash
$ python extract.py
```

### Train
```bash
$ python train.py
```

If you want to visualize during training, run in your terminal:
```bash
$ tensorboard --logdir runs
```

### Demo
Pick 10 random examples from test set of mjsynth:
```bash
$ python demo.py
```

Image| Word|
|----|----|
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_0.jpg)|U---n-r-e--a-l--is-t-i---c => Unrealistic         |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_1.jpg)|O---V-E-R--R-U--L--E-----S => OVERRULES           |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_2.jpg)|W---E-S--T-M-IIN-S-T-E---R => WESTMINSTER         |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_3.jpg)|m-------o----r--ee-l-----s => morels              |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_4.jpg)|P--E-R-P-L-E-A-I-T-A--R--S => PERPLEAITARS        |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_5.jpg)|E----------D-------------P => EDP                 |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_6.jpg)|G-----e-o-lo--giis-t-----s => Geologists          |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_7.jpg)|r-----e----b---a----t---ee => rebate              |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_8.jpg)|F--O-R-E-D-O--O-M--IIN---G => FOREDOOMING         |
|![image](https://github.com/foamliu/CRNN/raw/master/images/img_9.jpg)|u--n--re-p-r-es-e-n-te---d => unrepresented       |