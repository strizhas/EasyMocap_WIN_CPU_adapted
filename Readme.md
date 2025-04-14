<!--
 * @Date: 2021-01-13 20:32:12
 * @Author: Qing Shuai
 * @LastEditors: Qing Shuai
 * @LastEditTime: 2022-11-03 13:09:58
 * @FilePath: /EasyMocapRelease/Readme.md
-->

<div align="center">
    <img src="https://raw.githubusercontent.com/chingswy/Dataset-Demo/main/EasyMocap/23EfsN7vEOA%2B003170%2B003670.gif" width="80%">
    <br>
    <sup>The raw video is from <a href="https://www.youtube.com/watch?v=23EfsN7vEOA">Youtube</a>.</sup>
</div>

## Info

This is forked version of [easyMocap project](https://chingswy.github.io/easymocap-public-doc/install/install.html). I made some small code changes to make it work on Windows 10 without CUDA. 
I successfully tested it on some monocular videos with openPose and yolov models. This is how I use it:

Monocular example for openPose:
```

python .\scripts\preprocess\extract_video.py .\folder_with_video\ --mode openpose --openpose .\openpose\
# folder with video - base folder for your project. This folder with video must contain 'videos' folder with your video

python .\apps\demo\mocap.py .\folder_with_video\ --fps 25 --mono --mode smpl
# fps argument must correspond with your video fps

path_to_blender\blender.exe -b -t 12 -P .\scripts\postprocess\convert2bvh.py -- .\folder_with_video\\output-output-smpl-3d\smplfull\dancing_man\ --o .\output path\
# blender must be installed to convert result to bvh format

```

Monocular example for yolov. The command specifies HRNet, but due to the lack of a CUDA, another model will be used

```
emc --data config/datasets/svimage.yml --exp config/1v1p/hrnet_pare_finetune.yml --root .\folder_with_video\ --ranges 0 100 1 --subs video_name
# -ranges - not necessary. you can specify a specific part of the video you want to work with (in frames) 
# -subs - name of your video file (without extension)
```

## Installation

First part of installation goes from original [documentation](https://chingswy.github.io/easymocap-public-doc/install/install.html).
You can skip part with SMPL models, and definitely you can skip CUDA settings (because probably you, like me, don't have a nvidia GPU 😉)  

Then you must download next archives and extract in repository root folder. So it will look like so:
```
3rdparty
apps
config
data
doc
easymocap
library
models
myeasymocap
openpose
scripts
```

links to archives: 

[openPose 1.7.0](https://disk.yandex.ru/d/f9fOilyCP1cMFQ)

[data](https://disk.yandex.ru/d/L6MYzcZ7vtKfCA)

[models](https://disk.yandex.ru/d/ia1V4mkRiez05Q)

In case of some problems with openPose you can try another versions from [here](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases)

## Contact

You can open an issue if you have any questions, but I'm not an author, and not even a programmer, so I'm not sure what I can help you. But anyway you can try 😉
    

## Original contributors

EasyMocap is **built by** researchers from the 3D vision group of Zhejiang University: [**Qing Shuai**](https://chingswy.github.io/), [**Qi Fang**](https://raypine.github.io/), [**Junting Dong**](https://jtdong.com/), [**Sida Peng**](https://pengsida.net/), **Di Huang**, [**Hujun Bao**](http://www.cad.zju.edu.cn/home/bao/), **and** [**Xiaowei Zhou**](https://xzhou.me/). 

We would like to thank Wenduo Feng, Di Huang, Yuji Chen, Hao Xu, Qing Shuai, Qi Fang, Ting Xie, Junting Dong, Sida Peng and Xiaopeng Ji who are the performers in the sample data. We would also like to thank all the people who has helped EasyMocap [in any way](https://github.com/zju3dv/EasyMocap/graphs/contributors).

## Original citation

This project is a part of our work [iMocap](https://zju3dv.github.io/iMoCap/), [Mirrored-Human](https://zju3dv.github.io/Mirrored-Human/), [mvpose](https://zju3dv.github.io/mvpose/), [Neural Body](https://zju3dv.github.io/neuralbody/), [MultiNeuralBody](https://chingswy.github.io/easymocap-public-doc/works/multinb.html), [enerf]().

Please consider citing these works if you find this repo is useful for your projects.

```bibtex
@Misc{easymocap,  
    title = {EasyMoCap - Make human motion capture easier.},
    howpublished = {Github},  
    year = {2021},
    url = {https://github.com/zju3dv/EasyMocap}
}

@inproceedings{shuai2022multinb,
  title={Novel View Synthesis of Human Interactions from Sparse
Multi-view Videos},
  author={Shuai, Qing and Geng, Chen and Fang, Qi and Peng, Sida and Shen, Wenhao and Zhou, Xiaowei and Bao, Hujun},
  booktitle={SIGGRAPH Conference Proceedings},
  year={2022}
}

@inproceedings{lin2022efficient,
  title={Efficient Neural Radiance Fields for Interactive Free-viewpoint Video},
  author={Lin, Haotong and Peng, Sida and Xu, Zhen and Yan, Yunzhi and Shuai, Qing and Bao, Hujun and Zhou, Xiaowei},
  booktitle={SIGGRAPH Asia Conference Proceedings},
  year={2022}
}

@inproceedings{dong2021fast,
  title={Fast and Robust Multi-Person 3D Pose Estimation and Tracking from Multiple Views},
  author={Dong, Junting and Fang, Qi and Jiang, Wen and Yang, Yurou and Bao, Hujun and Zhou, Xiaowei},
  booktitle={T-PAMI},
  year={2021}
}
    
@inproceedings{dong2020motion,
  title={Motion capture from internet videos},
  author={Dong, Junting and Shuai, Qing and Zhang, Yuanqing and Liu, Xian and Zhou, Xiaowei and Bao, Hujun},
  booktitle={European Conference on Computer Vision},
  pages={210--227},
  year={2020},
  organization={Springer}
}

@inproceedings{peng2021neural,
  title={Neural Body: Implicit Neural Representations with Structured Latent Codes for Novel View Synthesis of Dynamic Humans},
  author={Peng, Sida and Zhang, Yuanqing and Xu, Yinghao and Wang, Qianqian and Shuai, Qing and Bao, Hujun and Zhou, Xiaowei},
  booktitle={CVPR},
  year={2021}
}

@inproceedings{fang2021mirrored,
  title={Reconstructing 3D Human Pose by Watching Humans in the Mirror},
  author={Fang, Qi and Shuai, Qing and Dong, Junting and Bao, Hujun and Zhou, Xiaowei},
  booktitle={CVPR},
  year={2021}
}

```

[^loper2015]: Loper, Matthew, et al. "SMPL: A skinned multi-person linear model." ACM transactions on graphics (TOG) 34.6 (2015): 1-16.

[^romero2017]: Romero, Javier, Dimitrios Tzionas, and Michael J. Black. "Embodied hands: Modeling and capturing hands and bodies together." ACM Transactions on Graphics (ToG) 36.6 (2017): 1-17.

[^pavlakos2019]: Pavlakos, Georgios, et al. "Expressive body capture: 3d hands, face, and body from a single image." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019.

<!-- [4] Bogo, Federica, et al. "Keep it SMPL: Automatic estimation of 3D human pose and shape from a single image." European conference on computer vision. Springer, Cham, 2016. -->

[^cao2018]: Cao, Z., Hidalgo, G., Simon, T., Wei, S.E., Sheikh, Y.: Openpose: real-time multi-person 2d pose estimation using part affinity fields. arXiv preprint arXiv:1812.08008 (2018)

[^kolotouros2019]: Kolotouros, Nikos, et al. "Learning to reconstruct 3D human pose and shape via model-fitting in the loop." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2019

[^bochkovskiy2020]: Bochkovskiy, Alexey, Chien-Yao Wang, and Hong-Yuan Mark Liao. "Yolov4: Optimal speed and accuracy of object detection." arXiv preprint arXiv:2004.10934 (2020).

[^hrnet]: Sun, Ke, et al. "Deep high-resolution representation learning for human pose estimation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2019.
