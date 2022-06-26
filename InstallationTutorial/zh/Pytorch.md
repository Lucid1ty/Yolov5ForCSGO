# Pytorch 安装
在下载安装好 Anaconda 之后，我们开始安装 Pytorch

1. 创建环境
	打开 Anaconda Prompt (在你安装完 Anaconda 之后按 WIN 键，然后搜索) :![image-20220626165815333](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626165815333.png)
	输入 : `conda create -n pytorch3.8 python=3.8`
	上面这条命令中的 pytorch3.8 是这个环境的名字，由你自己指定(取的名字自己要知道什么意思，不然后期环境多了你就懵了)
	
2. 切换到刚刚创建的环境
	输入 : `conda activate pytorch3.8`
	激活这个环境后你应该看到最前面的名称是 : pytorch3.8 而不是 base
	然后我们进入 Pytorch 的官网 : https://pytorch.org/
	点击红色框中的 Install :![image-20220626164616560](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626164616560.png)
	在新的页面中往下找到这样的画面 :![image-20220626164757985](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626164757985.png)
	按照自己的情况依次选择好 :
	![image-20220626164926081](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626164926081.png)
	复制最后一行中给出的命令
	我这里是 : `conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch`
	回到 Anaconda Prompt 中 :
	确保任然在 pytorch3.8 这个环境中
	把指令粘贴进去，回车执行
	等待按照完成即可

这时，我们已经安装好 Pytorch 了