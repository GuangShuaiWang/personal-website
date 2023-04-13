一个问题：
如何去构建一个像mkdocs一样的动态的homepage？
根据作者的描述知道由于涉及到版权的问题，该部分的代码是不公布的，除非称为赞助商。但是在相应的[issue](https://github.com/squidfunk/mkdocs-material/issues/1996)中，已经有人提供了解决方案，就是在index.md文件中指定我们想要的Html的template。还有一个相应的[项目](https://github.com/up42/up42-py)提供了相应的代码，可以仿照他们的工作进行更改。

主要的内容就是如何定制化修改.overrides文件夹下的home.html文件，这里就需要一些html语法知识来行，对比着来用，更简单一些。

这里需要的知识点就有点多了，因为对HTML的理解不够