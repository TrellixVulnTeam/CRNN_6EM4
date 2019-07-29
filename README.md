# Convolutional Recurrent Neural Network

## Introduction

This is a PyTorch re-implementation of CRNN: Convolutional Recurrent Neural Network ([paper](https://arxiv.org/pdf/1507.05717.pdf)). The features are summarized blow:


## DataSet

We use the synthetic dataset (Synth) released by Jaderberg et al. as the training data. The dataset contains 8 millions training images and their corresponding ground truth words.
Such images are generated by a synthetic text engine and are highly realistic. 

<pre>
@article{Jaderberg14c,
      title={Synthetic Data and Artificial Neural Networks for Natural Scene Text Recognition},
      author={Jaderberg, M. and Simonyan, K. and Vedaldi, A. and Zisserman, A.},
      journal={arXiv preprint arXiv:1406.2227},
      year={2014}
    }
</pre>