#基于itchat实现的微信机器人
1、电脑打开
2、输入你想要管理的微信群名称（注意不能填错）
3、输入账号和密码，在软件里有例子
    623708478 007633，687248622 764155
    直接复制粘贴输入即可
4、软件会下载打印二维码
5、手机微信扫码，点击登录微信网页版
6、然后就可以不用管这个软件了，最小化软件就行

实现的功能：
    1、下载百度文库文件（只能是需要下载券的文档）：只要有人在群里发送"文库下载+百度文库文档链接"
          链接形如：文库下载https://wenku.baidu.com/view/65f3f07f77c66137ee06eff9aef8941ea76e4b21.html?from=search，
         机器人（也就是扫码的微信）会自动回复一个链接，点击这个链接就可以下载相应的百度文库文档
    2、资源搜索功能，当有人想找一个稀缺资源，只要在群里发送:“搜索+资源名称”，如：搜索计算机二级
         机器人（也就是扫码的微信）会自动回复链接，点击链接即可
    3、观影功能，支持爱奇艺、优酷、腾讯三大电影库的VIP视频观看，只需在群里发送“观看电影+电影链接”
         机器人（也就是扫码的微信）会自动回复链接观影地址，点击链接即可观看，如果未打开，可以复制链接到手机浏览器中打开，
         若在电脑浏览器中打开，浏览器会下载一个m3u8文件，这个文件需要VLC media player播放器才可以打开看电影，VLC media player播放器可以在电脑管家里面下载
    4、机器人陪聊功能，@机器人发送消息即可和机器人聊天，如：@机器人查询北京的天气，更多有趣的功能你来撩才会发现哦
