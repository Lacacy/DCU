# 2.1 基于Docker使用DCU

DCU开发者社区光源镜像介绍:

[https://sourcefind.cn/#/service-list](https://sourcefind.cn/#/service-list)

光源可以查询到基于多种DTK版本的安装的深度学习基础镜像、大模型推理框架(vllm、lmdeploy、fastllm等)镜像、通用模型推理框架镜像(migraphx、AITemplate等)镜像；

## 2.1.1. 安装Docker

参考当前操作系统的版本号，自行安装docker

查看当前操作系统版本号：
```bash
cat /etc/os-release
```

## 2.1.2. 启动容器

基于镜像创建的容器可提供开箱即用的基于DCU的深度学习运行环境：

**前置条件**
1. 安装DCU加速卡，并完成其对应驱动的安装；

2. 正确安装docker；

**启动容器命令**：

```bash
docker run -it \
--network=host \
--ipc=host \
--shm-size=16G \
--device=/dev/kfd \
--device=/dev/mkfd \
--device=/dev/dri \
-v /opt/hyhal:/opt/hyhal \
--group-add video \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--name=dcu_test \
image.sourcefind.cn:5000/dcu/admin/base/custom:alphafold2-2.3.2-dtk23.10-py38 \
/bin/bash


注： 
（1）若出现libhsa-runtime相关报错，启动参数请加上-v /opt/hyhal:/opt/hyhal*；若物理机无/opt/hyhal，请下载hyhal并解压放置容器/opt/下；*
（2）参数解释：
     -it  # i:打开容器标准输入，t:分配一个伪终端
     --network=host  # 连接网络（none|host|自定义网络...）
     --ipc=host  # 设置IPC模式（none|shareable|host...）
     --shm-size=24G  # 设置/dev/shm大小
     --device=/dev/kfd  # 指定访问设备（DCU需要添加/dev/kfd、/dev/mkfd、/dev/dri）
     --device=/dev/mkfd
     --device=/dev/dri
     -v /opt/hyhal:/opt/hyhal  # dtk23.10以上版本镜像需要-v挂载物理机目录/opt/hyhal
     --group-add video  # 设置用户附加组（普通用户使用DCU需要）
     --cap-add=SYS_PTRACE  # 添加权限（SYS_PTRACE|NET_ADMIN...）
     --security-opt seccomp=unconfined  # 安全配置（seccomp=unconfined|label=disable...）
     --name=dcu_test   # 容器名称
     image.sourcefind.cn:5000/dcu/admin/base/custom:alphafold2-2.3.2-dtk23.10-py38  # 所需镜像
     /bin/bash  # 容器内启动bash
```           


