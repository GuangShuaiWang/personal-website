## 记录一些常用的知识点

### 小命令
1. 增加运行权限 chmod +x file.sh
2. pip镜像：
    - 中国科学技术大学 : https://pypi.mirrors.ustc.edu.cn/simple
    - 豆瓣：http://pypi.douban.com/simple/
    - 阿里云：http://mirrors.aliyun.com/pypi/simple/
    - 清华：https://pypi.tuna.tsinghua.edu.cn/simple
3. corn可以定时执行脚本，```crontab -e```来启动，数据格式为```0 0 * * * /path/to/your/script.sh```,前五个通配符分别为min，hour，days，month，year。
4. shell脚本中，可以用date命令来获得时间，date +%m/%d/%Y 输出的是04/18/2023。
5. bashrc中的前缀显示可以按照自己的需求更改，主要改PS1参数，示例：```expert PS1='\[\033[42m\]\[\033[1;37m\][\d \t]\[\033[0m\] \[\033[1;30m\]\u\[\033[0m\]:\[\033[1;34m\]\w\[\033[0m\]\$ '```
6. chatgpt网址：[chatgpt](https://chat.openai.com){:target="_blank"}
7. torch.manual_seed(3407) is all you need?
8. 转博ppt：[Epan](https://epan.shanghaitech.edu.cn/l/ZFDjOk){:target="_blank"} 一天有效期
9. 表格图片在线制作：https://www.canva.cn。 目前好像比不好用


