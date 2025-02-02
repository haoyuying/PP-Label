# 图像分类标注

![image](https://user-images.githubusercontent.com/29757093/182839949-e032d095-759f-40c5-9d38-c6c506e024c4.png)

PaddleLabel支持单类别分类与多类别分类两种图像分类标注任务。



## <div id="test1">数据结构</div>

### 单分类

也称为 ImageNet 格式，每条数据只有一个类别。样例数据集：[vegetables_cls](https://bj.bcebos.com/paddlex/datasets/vegetables_cls.tar.gz)，[flowers102](https://paddle-imagenet-models-name.bj.bcebos.com/data/flowers102.zip)(需经预处理)

示例格式如下：

```shell
Dataset Path
├── Cat
│   ├── cat-1.jpg
│   ├── cat-2.png
│   ├── cat-3.webp
│   └── ...
├── Dog
│   ├── dog-1.jpg
│   ├── dog-2.jpg
│   ├── dog-3.jpg
│   └── ...
├── monkey.jpg
├── train_list.txt
├── val_list.txt
├── test_list.txt
└── label.txt

# labels.txt
Monkey
Mouse
```

单分类中图像所在的文件夹名称将被视为它的类别。所以如上数据集导入后，三张猫和三张狗的图片会有分类，monkey.jpg 没有分类。如果与文件夹名同名的标签不存在，导入过程中会自动创建。

为了避免冲突，单分类项目只导入`xx_list.txt`中的数据集划分信息，**这三个文件中的类别信息不会被导入**。您可以使用[此脚本](../tool/clas/mv_image_acc_split.py)在导入数据之前根据三个`xx_list.txt`文件更改数据的位置。

### 多分类

在多分类项目中，一条数据可以有多个类别。

示例格式如下：

```shell
Dataset Path
├── image
│   ├── 9911.jpg
│   ├── 9932.jpg
│   └── monkey.jpg
├── labels.txt
├── test_list.txt
├── train_list.txt
└── val_list.txt
# labels.txt
cat
dog
yellow
black
# train_list.txt
image/9911.jpg 0 3
image/9932.jpg 2 0
image/9928.jpg monkey
```

在多分类项目中，数据的类别仅由`xx_list.txt`决定，不会考虑文件夹名称。


### 新项目创建

浏览器打开PaddleLabel后，可以通过创建项目下的“图像分类”卡片创建一个新的图像分类标注项目（如果已经创建，可以通过下方“我的项目”找到对应名称的项目，点击“标注”继续标注）。


项目创建选项卡有如下选项需要填写：

- 项目名称（必填）：填写该分类标注项目的项目名
- 数据地址（必填）：填写本地数据集文件夹的路径，可以直接通过复制路径并粘贴得到
- 数据集描述（选填）：填写该分类标注项目的使用的数据集的描述文字
- 标签格式（必选）：选择该任务为单分类还是多分类任务

### 数据导入

在创建项目时需要填写数据地址，该地址对应的是数据集的文件夹，为了使PaddleLabel能够正确的识别和处理数据集，请参考[数据结构](#test1)组织数据集，对于txt文件的详细组织方式，请参考[数据集文件结构说明](dataset_file_structure.md)。同时PaddleLabel提供了参考数据集，位于`~/.paddlelabel/sample/clas`路径下，也可参考该数据集文件结构组织数据。

## 数据标注

完成后进入标注界面，PaddleLabel的界面分为五个区域，上方为可以切换的标签页，下方为标注进度展示，左侧包含图像显示区域与工具栏，右侧为标签列表，用于添加不同的标签和标注。在分类任务的标注中，可以按以下步骤进行使用：

1. 点击右侧“添加标签”，填写信息并创建标签
2. 选择当前图像对应的标签（多分类任务可以选择多个标签），点击后自动保存
3. 点击左右按钮切换图像，重复上述操作，直到所有数据标注完毕
4. 下方进度展示可以查看标注进度

## 完成标注

完成数据标注后，PaddleLabel提供了方便的数据划分功能，以便与Paddle其他工具套件（如PaddleClas）进行快速衔接。点击右侧工具栏的**项目总览**按钮，来到该项目的总览界面，这里可以看到数据以及标注状态。

### 数据划分

点击**划分数据集**按钮弹出划分比例的设置，分别填入对应训练集、验证集和测试集的占比，点击确定即可完成数据集的划分。

### 数据导出

点击**导出数据集**，输入需要导出到的文件夹路径，点击确认，即可导出标注完成的数据到指定路径。
