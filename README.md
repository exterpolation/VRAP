silly
=====

这是一个简单的Python程序，用于输出“你好，世界！”。这个项目旨在为初学者提供一个入门级别的编程示例，同时也展示了如何在Python中处理中文字符。

背景
---

在学习任何新的编程语言时，传统上都会从“Hello World”程序开始。这个项目是为了帮助那些刚接触编程的朋友们，以最简洁的方式了解Python编程语言。

目标
---
我们的目标是提供一个简单、易于理解的示例，让初学者能够快速上手Python编程。同时，我们也希望通过这个项目鼓励更多的人参与到开源社区中来。

未来计划
------

我们计划添加更多的功能和示例代码，以展示Python在处理不同类型数据时的强大能力。此外，我们还考虑为项目添加自动化测试，以确保代码的质量和稳定性。

安装
---

首先，您需要确保您的系统上已安装Python。如果尚未安装，请访问[Python官方网站](https://www.python.org/downloads/)下载并安装适合您操作系统的版本。

使用方法
------

要运行此程序，请按照以下步骤操作：

1. 打开命令行或终端。
2. 导航到包含`main.py`文件的目录。
3. 执行以下命令：

```bash 
bash python main.py
```

这将在控制台上打印出“你好，世界！”。

示例代码


[tag download]:https://github.com/Jieli-Tech/fw-AC63_BT_SDK/tags
[tag_badgen]:https://img.shields.io/github/v/tag/Jieli-Tech/fw-AC63_BT_SDK?style=plastic&logo=bluetooth&labelColor=ffffff&color=informational&label=Tag&logoColor=blue

# fw-AC63_BT_SDK   [![tag][tag_badgen]][tag download]

中文 | [EN](./README-en.md)

AC63 系列通用蓝牙SDK 固件程序

本仓库包含SDK release 版本代码，线下线上支持同步发布，并且引用了其他开源项目（如Zephyr RTOS）.

本工程提供的例子，需要结合对应命名规则的库文件(lib.a) 和对应的子仓库进行编译.

快速开始
------------

欢迎使用杰理开源项目，在开始进入项目之前，请详细阅读SDK 介绍文档，
从而获得对杰理系列芯片和SDK 的大概认识，并且可以通过快速开始介绍来进行开发.


工具链
------------

关于如何获取`杰理工具链` 和 如何进行环境搭建，请阅读以下内容：

* 编译工具 ：请安装杰理编译工具来搭建起编译环境, [下载链接](https://doc.zh-jieli.com/Tools/zh-cn/dev_tools/dev_env/index.html) 

* USB 升级工具 : 在开发完成后，需要使用杰理烧写工具将对应的`hex`文件烧录到目标板，进行开发调试, 关于如何获取工具请进入申请 [链接](https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-22883854875.5.504d246bXKwyeH&id=620295020803) 并详细阅读对应的[文档](https://doc.zh-jieli.com/Tools/zh-cn/dev_tools/forced_upgrade/index.html)，以及相关下载脚本[配置](https://doc.zh-jieli.com/AC63/zh-cn/master/getting_started/project_download/INI_config.html)

介绍文档
------------

* 芯片简介 : [SoC 数据手册扼要](https://doc.zh-jieli.com/vue/#/docs/ac63), [下载链接](./doc/datasheet)

* SDK 版本信息 : [SDK 历史版本](https://doc.zh-jieli.com/AC63/zh-cn/master/other/version/index.html)

* SDK 介绍文档 : [SDK 快速开始简介](https://doc.zh-jieli.com/AC63/zh-cn/master/index.html)

* SDK 结构文档 : [SDK 模块结构](./doc/architure)

编译工程
-------------
请选择以下一个工程进行编译，下列目录包含了便于开发的工程文件：

* 蓝牙应用 : [SPP_LE](./apps/spp_and_le), 适用领域：透传, 数传, 扫描设备, 广播设备, 信标, FindMy应用, 多机连接. Dongle(usb / bt). [文档链接](https://doc.zh-jieli.com/AC63/zh-cn/master/module_demo/spple/index.html)

* 蓝牙应用 : [HID](./apps/hid), 适用领域：遥控器, 自拍器, 键盘, 鼠标, 吃鸡王座, 语音遥控器. [文档链接](https://doc.zh-jieli.com/AC63/zh-cn/master/module_demo/hid/index.html)

* 蓝牙应用 : [Mesh](./apps/mesh), 适用领域：物联网节点, 天猫精灵接入, 自组网应用. [文档链接](https://doc.zh-jieli.com/AC63/zh-cn/master/module_demo/mesh/index.html)

已发布版本详见 标签(Tags)。

即将发布：

* 蓝牙应用 ：`IoT (ipv6 / 6lowpan)`

* 2.4G 应用 : `Vendor Wireless`

SDK 同时支持Codeblock 和 Make 编译环境，请确保编译前已经搭建好编译环境，

* Codeblock 编译 : 进入对应的工程目录并找到后缀为 `.cbp` 的文件, 双击打开便可进行编译.

* Makefile 编译 : 双击`tools/make_prompt.bat`，输入 `make target`（具体`target`的名字，参考`Makefile`开头的注释）

  `在编译下载代码前，请确保USB 升级工具正确连接并且进入编程模式`
  
* 蓝牙OTA : [OTA](https://doc.zh-jieli.com/AC63/zh-cn/master/module_demo/ota/index.html) , 适用领域：单备份，双备份蓝牙升级

蓝牙官方认证
-------------

经典蓝牙LMP / 低功耗蓝牙Link Layer 层和Host 协议栈均支持蓝牙5.0 、5.1和5.4版本实现

* Core v5.0 [QDID 134104](https://launchstudio.bluetooth.com/ListingDetails/88799)

* Core v5.1 [QDID 136145](https://launchstudio.bluetooth.com/ListingDetails/91371)

* Core v5.4 [QDID 222830](https://launchstudio.bluetooth.com/ListingDetails/193923)


硬件环境
-------------

* 开发评估板 ：开发板申请入口[链接](https://shop321455197.taobao.com/?spm=a230r.7195193.1997079397.2.2a6d391d3n5udo)

* 生产烧写工具 : 为量产和裸片烧写而设计, 申请入口 [链接](https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-22883854875.8.504d246bXKwyeH&id=620941819219) 并仔细阅读相关 [文档](https://doc.zh-jieli.com/Tools/zh-cn/mass_prod_tools/burner_1tuo2/index.html)

* 无线测试盒 : 为空中升级/射频标定/快速产品测试而设计, 申请入口 [链接](https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-22883854875.10.504d246bXKwyeH&id=620942507511), 阅读[文档](https://doc.zh-jieli.com/Tools/zh-cn/mass_prod_tools/testbox_1tuo2/index.html) 获取更多详细信息.


社区
--------------

* 技术交流群，钉钉群 ID: `3375034077`

* 常见问题集合[链接](./doc/FAQ)

免责声明
------------

AC63_BT_SDK 支持AC63 系列芯片开发.
AC63 系列芯片支持了通用蓝牙常见应用，可以作为开发，评估，样品，甚至量产使用，对应SDK 版本见tag 和 release

解释
---------

`main.py`文件中的代码非常简洁：
python print("你好，世界！")

这里，我们使用Python内置的`print()`函数来向控制台输出字符串“你好，世界！”。

测试
---

为了确保程序的正确性，我们建议用户自行测试程序。在当前阶段，由于程序的简单性，主要的测试方式是直接运行程序并检查输出是否符合预期。

常见问题解答
---------

**Q：我无法运行程序，显示“python”不是内部或外部命令？**

A：这通常意味着Python没有被正确地添加到您的PATH环境变量中。请检查Python的安装路径，并确保它已被添加到PATH中。

**Q：程序运行后没有任何输出？**

A：请确保您的终端或命令行支持UTF-8编码，因为“你好，世界！”是以UTF-8编码的中文字符组成的。

贡献
---

我们欢迎所有形式的贡献，包括但不限于bug报告、功能请求和代码改进。请通过GitHub提交pull请求或创建issue来参与本项目。

许可证
----

本项目采用MIT许可证授权。有关详细信息，请参阅LICENSE文件。

支持
---

如果您在使用过程中遇到任何问题，或有任何疑问，您可以通过GitHub issue系统联系我们。我们会尽快回复您的问题。

依赖
---

此项目目前不依赖于任何第三方库或框架。它仅需要一个标准的Python环境即可运行。

致谢
---

感谢所有为这个项目做出贡献的人们，以及那些提供反馈和建议的用户。你们的支持对我们来说非常重要。

----------------------------------------------------------------------------------------------------------------------------

<img src="https://github.com/noinline/silly/assets/139589029/292e6507-1716-4e43-b8e4-f642a410e117" width="150" height="100">

----------------------------------------------------------------------------------------------------------------------------
