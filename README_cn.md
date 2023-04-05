# 哔哩哔哩弹幕爬虫

[English](https://github.com/gallifreyCar/BilibiliBarrageSpider/blob/master/README.md) |  [中文](https://github.com/gallifreyCar/BilibiliBarrageSpider/blob/master/README_cn.md)

## 概要

本项目是一个基于Python的弹幕爬虫，用于爬取在[哔哩哔哩 (゜-゜)つロ 干杯~-bilibili](https://www.bilibili.com/)上收集弹幕数据（包括弹幕内容，弹幕发送时间，弹幕在视频中出现的时间，弹幕颜色，字体大小）。

## 安装

1. 确保你已经安装了Python 3.8+和pip。
2. 使用pip安装依赖库：`pip install -r requirements.txt`

## 使用

1. 打开你需要爬取的网站，在网站名前添加一`i`，跳转到api网站

   ![image-20230322013318617](README_cn/image-20230322013318617.png)

   ![image-20230322013353601](README_cn/image-20230322013353601.png)

2. 在api网站复制cid

   ![image-20230322013644953](README_cn/image-20230322013644953.png)

3. 把cid复制到main.py的代码中

   ![image-20230322014044073](README_cn/image-20230322014044073.png)

4. 运行程序，运行结果会保存到`target/output.xlsx`（excel格式）和`target/output.json`(JSON 格式)当中

## 贡献

如果您发现了任何问题或者有任何改进意见，请在issue中提出。如果您愿意为项目做出贡献，请fork本项目并提交pull request。

## 许可证

本项目基于MIT许可证开源，详情请参见LICENSE文件。
