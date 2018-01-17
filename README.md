# MillionHeroHelper

## 介绍

在Win环境下使用，利用夜神模拟器打开西瓜视频的百万英雄进行游戏，免去手机传输图片的延迟，识别问题和选项并进行搜索结果

## 显示效果

- 弹出浏览器并显示搜索结果
- 计算问题包含每个选项的次数
- 计算问题与每个选项进行搜索出现的词条数

## 准备工作

1. 安装[夜神模拟器](https://www.yeshen.com/cn/download/fullPackage)，并安装西瓜视频App
2. 安装最新版本的[Chrome浏览器](https://www.google.com/chrome/browser/thankyou.html?statcb=1&installdataindex=defaultbrowser#)
3. 安装[pyhooked](https://github.com/ethanhs/pyhooked)库（不推荐pip install pyhooked，因为两份源码中函数不一样，虽然版本号相同= =!）
4. 安装本程序所需依赖
   >  ```pip install -r .\requirements.txt```
5. [注册百度开发者账户并申请api_key](http://ai.baidu.com/tech/ocr/general)，并修改```.\config\config.conf```为自己的api_key

## 运行

1. 打开夜神模拟器并运行西瓜视频App，点击百万英雄
2. 运行主程序
```python
python .\main.py
```
3. 题目出现时，点击回车键进行自动识别并搜索
4. 点击```Q```键退出

## PS

本程序只针对百万英雄适配，其他的没试过，自行修改切图参数应该也可以

## 参考项目

- [TopSup](https://github.com/Skyexu/TopSup)
- [wenda-helper](https://github.com/rrdssfgcs/wenda-helper)