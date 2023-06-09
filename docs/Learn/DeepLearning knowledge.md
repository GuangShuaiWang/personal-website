## 深度学习相关知识

这里记录的就不是小的知识点了，会梳理一些可能容易混淆的深度学习概念，需要更加的系统化。

### batch和epoch之间的区别

这两个概念应该是初学者非常容易混淆的内容，这里进行一些介绍。
1. 首先，epoch中是包含不同的batch的，将一个大型的数据集分成小的batch可以减少内存压力，加快计算效率，这是最主要的优点。
2. 另一方面，我认为batch中所做的贡献要大于每个epoch的。在每个不同的batch中，模型都需要经过前向传播，计算损失，反向传播，更新参数的步骤。
3. 在每个epoch之间，出了需要遍历batch外，可以选择计算模型的表现效果，比如准确率，也可以更改模型的学习率；同样也可以选择保存模型。

### DataLoader都做了些什么？

在PyTorch中，DataLoader是一个用于数据加载和批次处理的实用程序类。它提供了以下功能：

1. **数据加载：** DataLoader可以从给定的数据集（如PyTorch的Dataset对象）中加载数据。数据集可以是自定义的，也可以是PyTorch提供的预定义数据集，如MNIST、CIFAR-10等。

2. **批次处理：** DataLoader能够将数据集分成批次（batches）。通过指定批次大小（batch size），DataLoader会自动从数据集中按照指定大小加载数据并组成批次。

3. **数据随机化：** DataLoader可以对数据进行随机化处理。它会在每个 epoch 开始时重新洗牌数据，以确保模型在不同的批次中看到多样化的样本。这对于提高模型的泛化能力非常重要。

4. **并行加载：** DataLoader支持多线程并行数据加载。它可以利用多个线程同时从存储介质（如硬盘）中读取数据，并在需要时预先准备下一批数据，从而减少模型训练过程中的数据加载等待时间。

5. **数据转换：** DataLoader可以通过指定数据变换（如图像缩放、裁剪、标准化等）来对加载的数据进行预处理。这些变换可以通过组合PyTorch的Transforms来定义，并在DataLoader加载数据时应用到每个样本上。

6. **迭代支持：** DataLoader是一个可迭代的对象，可以在训练循环中使用for循环逐个访问每个批次的数据。这样可以方便地将数据传递给模型进行训练。

通过使用DataLoader，可以简化数据加载和批次处理的过程，使数据准备部分与模型训练部分分离，从而使代码更加清晰、可读性更强，并提高数据加载的效率。

### Position encoding



### Scaled Dot-Product Attention
如何就算的？如何mask的？

### Multi-Head Attention

由Scaled Dot-Product Attention的原理我们可以知道，其中是Q，K，V之间的矩阵乘法，并没有可以学习的参数。那么为了匹配不同问题中的不同的模式，给模型更多的的学习机会，所以就使用了这种多头注意力机制。他是怎么做的呢？他将Q，K，V值通过线性层映射了h次，分别计算每次的点积注意力，concat之后再经过一个线性层输出，这样就增加了很多的学习机会。

每个映射层的纬度是d_model/h,因此在代码实操中会涉及拆分的步骤，目的是为了并行计算，但*实际原理上好像是有差异的？这里的理解有点问题，可以是示意图给出来的不太合适*。在实际（代码）操作上，是将映射后的特征向量拆分成head份，来分别计算每个head的注意力得分。

1. 论文的描述是通过多个W（线性层）映射到子空间里，但是实际操作时是通过一个映射然后切分，原理上一样，为什么一样呢？

[答案](https://datascience.stackexchange.com/questions/80660/splitting-into-multiple-heads-multihead-self-attention)：文章描述是无问题的，不过是在实际应用的时候，通过reshape和矩阵乘法等操作进行并行计算了，但是为什么通过这种方式可以并行计算了，我还是不能理解。

主要问题就是下图描述的，为什么两者等价？
![multihead](../doc_images/learn/mutihead.png)

### Transformer Decoder

Docoder相较于Encoder比较麻烦，存在一个mask操作，mask的含义是，在t时刻的输入，decoder的输入是无法看到t+1时刻的内容的，那么在实际操作的时候，是通过一个三角矩阵（右上角为0）将后面的内容变为0，在代码中替换为-inf。~~因此好像这一步操作不是在模型代码中构建的，而是在训练过程中构造的。~~ 

这里其实是比较好理解的。首先，在模型的训练过程中，Decoder是进行并行计算的，因为此时可以一次性的得到全部的输入，虽然输入是经过mask的，而在模型测试或者说是应用时，并不是并行的，而是需要一个个的获得输入，进行self masked attention.

### src-mask & tar_mask

src-mask与tar-mask之间有着本质性的不同，虽然两种都是用来作为屏蔽矩阵的。但是src-mask是在encoder中使用的，目的是为了屏蔽那些padding的位置，src-mask应用于输入的序列。tar_mask则是应用于目标序列，它除了屏蔽padding的位置外，还应用于屏蔽未来信息。