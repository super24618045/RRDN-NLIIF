# A Study of Residual in Residual Dense Networks with New Local Implicit Image Function for Arbitrary-Scale Image Super Resolution



## Environment
- Ubuntu 18.04
- python 3.7
- pytorch 1.12
- cuda 11.3

## Requirment
`$ pip install -r requirements.txt`


## Quick start
1. Download a DIV2K pre-trained model.

| Model           | Download      |
|:---------------:|:-------------:|
| RRDN-NLIIF      |[Google Drive](https://drive.google.com/file/d/1ARa6EUC9tOncFhlA8ypvlSqe7TKMPubs/view?usp=share_link)  |

2. Convert your image to LIIF and present it in a given resolution (with GPU 0, `[MODEL_PATH]` denotes the `.pth` file)

```
python demo.py --input xxx.png --model [MODEL_PATH] --resolution [HEIGHT],[WIDTH] --output output.png --gpu 0
```

## Experiments

### Data
`mkdir load` for putting the dataset folders.

We use the same dataset as [liif
](https://github.com/yinboc/liif). Please follow their instructions.

### Running the code

**1. DIV2K experiments**

**Train**: `python train_liif.py --config configs/train-div2k/train_rrdbnet-nliif.yaml` 

**Test**: `bash scripts/test-div2k.sh [MODEL_PATH] [GPU]` for div2k validation set, `bash scripts/test-benchmark.sh [MODEL_PATH] [GPU]` for benchmark datasets. `[MODEL_PATH]` is the path to a `.pth` file, we use `epoch-last.pth` in corresponding save folder.

**If you need the reconstructed result of testing set, use scripts like `testd-div2k.sh` instead of `test-div2k.sh`**

**2. celebAHQ experiments**

**Train**: `python train_liif.py --config configs/train-celebAHQ/train_celebAHQ-32-256_RRDN_NLIIF.yaml`(or `python train_liif.py --config configs/train-celebAHQ/train_celebAHQ-64-128_RRDN_NLIIF.yaml`)

**Test**: `python test.py --config configs/test/test-celebAHQ-32-256.yaml --model [MODEL_PATH]` (or `test-celebAHQ-64-128.yaml` for another task). We use `epoch-best.pth` in corresponding save folder.


## Reference
* paper
    * [Learning Continuous Image Representation with Local Implicit Image Function](https://arxiv.org/abs/2012.09161)
    * [ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks](https://arxiv.org/abs/1809.00219)
    * [UltraSR: Spatial Encoding is a Missing Key for Implicit Image Function-based Arbitrary-Scale Super-Resolution](https://arxiv.org/abs/2103.12716)
* implement
    * [liif](https://github.com/yinboc/liif)
    * [image-super-resolution](https://github.com/idealo/image-super-resolution)

