# Pytorch 安装

在下载安装好 Anaconda 之后，我们开始安装 Pytorch

1. 创建环境
	
    打开 Anaconda Prompt，在你安装完 Anaconda 之后按下 Win 键就应该能看到
    如果没有，按 WIN 键，然后搜索 : Anaconda Prompt
	
    ![image-20220626165815333](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626165815333.png)
	
    打开之后在其中输入 : `conda create -n pytorch python=3.8`
    上面这条命令中的 pytorch 是这个环境的名字，同时 python=3.8 指定了我们安装的 python 版本为 3.8
    ⭐你最好和我取一样的名字，后面我一说激活 pytorch 环境你就知道是哪个环境了
    等待它创建完成
	
2. 激活刚刚创建的环境并执行安装
    
    输入 : `conda activate pytorch`

    激活这个环境后你应该看到最前面的名称是 : pytorch 而不是 base

    然后我们进入 Pytorch 的官网 : https://pytorch.org/

    点击红色框中的 Install :
   
    ![image-20220626164616560](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626164616560.png)
       
    在新的页面中往下找到这样的画面 :
   
    ![image-20220626164757985](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626164757985.png)
       
    按照自己的情况依次选择好 :

    ![image-20220626164926081](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626164926081.png)
    
    复制最后一行中给出的命令
    
    我这里是 : `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch`

    回到 Anaconda Prompt 中 : 确保任然在 pytorch 环境中，把指令粘贴进去，回车执行等待安装完成即可

    这时，我们已经在创建的环境(pytorch)中安装好了 Pytorch

3. 检验安装是否正确
	1. 确保任然在 pytorch 环境中
	2. 输入 : `python` 然后回车
	3. 在出现的 >>> 后面输入 : `import torch` 然后回车
	4. 第一次执行需要等待一会，等待它再次出现 >>> 
	5. 然后输入 : `torch.cuda.is_available()` 并回车
	6. 如果你的显卡支持 Cuda 并且正确的安装了 Pytorch，那么你应该看到 True。如果你的显卡不支持 Cuda 并且你安装的是 CPU 版本的 Pytorch，那么你应该看到 False
	6. 如果你的显示不正确，那么请回头检查每一步，直到正确为止

至此，Pytorch 的安装完成！
