# 1. 构建DCU基础环境


## 1.1. 操作系统版本兼容列表


**注意**:

> 使用`iso`镜像安装操作系统时，请勿允许任何操作系统的更新行为, 否则会带来内核版本的升级，导致安装失败; <br>
> 可参考 `1.4` 下的常用操作系统安装步骤之中的锁核操作; 

**操作系统**:

| 操作系统 | 版本 | 内核 | 
| ------- | ---  | ---- |
| Centos  | 7.6         | 3.10.0-957.el7.x86_64 | 
| Centos  | 8.5         | 4.18.0-348.el8.x86_64 | 
| Rocky   | 8.6         | 4.18.0-348.el8.x86_64 |
| Rocky   | 9.2         | 4.18.0-348.el8.x86_64 |
| Ubuntu  | 20.04.1     |  5.4.0-42-generic  |
| Ubuntu  |  22.04      |  5.15.0-25-generic |
| NFS     |  3.2        |  3.10.0-957.nfs.5.x86_64 |
| NFS     | 4.0         |  4.19.113-14.1.nfs4.x86_64 |
| NFS     | 4.0-Desktop |  5.4.0-49-generic |
| UOS     | 1021e       |  4.19.90-2109.1.0.0108.up2.uel20.x86_64 |
| Kylin   | v10 SP2     |  4.19.90-24.4.v2101.ky10.x86_64 |
| Anolis  | 8.4         | 4.19.91-23.4.an8.x86_64 |
| Anolis  | 8.6         | 4.19.91-26.an8.x86_64 |
| openEuler | 22.03     | 5.10.0-60.18.0.50.oe2203.x86_64 |
| BCLinux   | 8.2       | 4.19.0-240.23.11.el8_2.bclinux.x86_64 |



---

## 1.2. 支持的DCU型号

- Z100
- Z100L
- K100 
- K100_AI


## 1.3. 开发者社区 DCU 环境安装手册

该文档主要针对 DCU 加速卡，提供基础软件环境安装部署以及基础测试的参考指导。

具体信息开发者社区的环境搭建文档:
[https://cancon.hpccube.com:65024/1/main/latest/Document](https://cancon.hpccube.com:65024/1/main/latest/Document)

建议参考如下文档进行安装DCU基础环境:

`https://developer.hpccube.com/tool/` → DCU Toolkit → latest → Document → DTK 开发环境安装部署手册.pdf

![DCU 环境安装手册](./imgs/env_install.png)
<!-- <center><img src="./imgs/env_install.png" alt="DCU 环境安装手册" style="zoom:50%;" /></center> -->

## 1.4. 驱动和DTK的下载安装地址:

**驱动下载地址**:  [https://cancon.hpccube.com:65024/6/main](https://cancon.hpccube.com:65024/6/main) → latest 驱动→ rock-xxx-xxx.aio.run

**DTK下载地址**:  [https://cancon.hpccube.com:65024/1/main](https://cancon.hpccube.com:65024/1/main)  → latest → 对应的操作系统 → DTK-version-OS-version-x86_64.tar.gz

## 1.5 常用操作系统安装DCU环境示例:

