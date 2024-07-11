### 1.2 DCU基础环境完整教程-Centos7.6:

#### 1.2.1 **非root用户安装注意事项:**
   - 确保非root用户已加入`video`组，以便能够使用DCU。
     ```shell
     # 对于有sudo权限的非root用户
     sudo usermod -aG video $USER
     
     # 对于无sudo权限的用户，由root执行
     usermod -aG video <userid>
     ```

#### 1.2.2. **操作系统设置**：

确保启动项中不包含nomodeset选项，如果内核以nomodeset选项启动，则驱动可能无法成功加载。

- 需要保证系统纯净，命令行运行 `lsmod | grep amdgpu` 为空
- 关闭 selinux（可选）

    修改`/etc/selinux/config`，设置`SELINUX=disabled`

- 关闭 firewalld（可选）
    ```bash
    systemctl stop firewalld
    systemctl disable firewalld
    ```


#### 1.2.3. **关闭内核自动更新:**
   - 编辑`/etc/yum.conf`，在`[main]`部分添加：
     ```
     exclude=kernel* 
     exclude=centos-release*
     ```

#### 1.2.4. **更新yum源:**

   - 替换为中科大源，针对CentOS 7.6的示例, （注意使用双引号）：

        ```shell
        sed -e "s|^mirrorlist=|#mirrorlist=|g" -e "s|^#baseurl=http://mirror.centos.org/centos/\$releasever|baseurl=https://mirrors.ustc.edu.cn/centos-vault/$minorver|g"  -i.bak  /etc/yum.repos.d/CentOS-*.repo
        ```

   - 替换  `CentOS-CR.repo` 并且 `enable`（安装python3需要）

        ```shell
        sed -i "s|^baseurl=http://mirror.centos.org/centos/\$releasever|baseurl=https://mirrors.ustc.edu.cn/centos-vault/$minorver|g;s|enabled=0|enabled=1|g"  /etc/yum.repos.d/CentOS-CR.repo
        ```


   - 对 Centos7 配置 SCLo 源（安装devtoolset需要）:

     编辑 `/etc/yum.repos.d/CentOS-SCLo.repo` 配置文件;

        ```shell
        vi /etc/yum.repos.d/CentOS-SCLo.repo
        ```

     在 `/etc/yum.repos.d/CentOS-SCLo.repo` 写入以下内容, `Esc + :wq` 保存退出

        ```shell
        [centos-sclo-sclo]
        name=CentOS-7 - SCLo sclo
        baseurl=https://mirrors.ustc.edu.cn/centos/7/sclo/$basearch/sclo/
        gpgcheck=0
        enabled=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo
        [centos-sclo-rh]
        name=CentOS-7 - SCLo rh
        baseurl=https://mirrors.ustc.edu.cn/centos/7/sclo/$basearch/rh/
        gpgcheck=0
        enabled=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo
        ```
    
   - 对 Centos7 配置 epel 源（安装cmake3需要）

        编辑 `/etc/yum.repos.d/epel-7.repo` 配置文件;

        ```shell
        vi /etc/yum.repos.d/epel-7.repo
        ```

        在/etc/yum.repos.d/epel-7.repo写入以下内容, `Esc + :wq` 保存退出;

        ```shell
        [epel]
        name=Extra Packages for Enterprise Linux 7 - $basearch
        baseurl=http://mirrors.aliyun.com/epel/7/$basearch
        failovermethod=priority
        enabled=1
        gpgcheck=0
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

        [epel-debuginfo]
        name=Extra Packages for Enterprise Linux 7 - $basearch – Debug
        baseurl=http://mirrors.aliyun.com/epel/7/$basearch/debug
        failovermethod=priority
        enabled=0
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
        gpgcheck=0

        [epel-source]
        name=Extra Packages for Enterprise Linux 7 - $basearch – Source
        baseurl=http://mirrors.aliyun.com/epel/7/SRPMS
        failovermethod=priority
        enabled=0
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
        gpgcheck=0
        ```

   - 更新cache

        ```shell
        yum clean all 
        yum makecache 	
        ```

#### 1.2.5. **安装相关依赖:**
   - 联网执行以下命令安装必要的依赖包：

        ```shell
        #安装 DCU 加速卡驱动所需的依赖包命令
        yum install -y gcc gcc-c++ rpm-build autoconf kernel-devel-$(uname -r) kernel-headers-$(uname -r)
        #安装cmake3
        yum install -y cmake3 
        ln -s /usr/bin/cmake3 /usr/bin/cmake

        #安装 DTK 开发环境所需的依赖包命令
        yum install -y centos-release-scl
        yum install -y gcc gcc-c++ gcc-gfortran elfutils elfutils-devel make rpm-build devtoolset-7
        yum install -y libbabeltrace-devel libbabeltrace pciutils-devel libpciaccess-devel
        yum install -y numactl-devel elfutils-libelf-devel mesa-libGL-devel
        yum install -y epel-release cmake3 pciutils-libs pciutils-devel
        yum install -y perl-File-Which perl-File-BaseDir perl-File-Copy-Recursive perl-File-Listing java-1.8.0-openjdk
        yum install -y git python python-pip python-devel python-wheel python3 python3-pip python3-devel python3-wheel sqlite-devel libibverbs
        yum install -y redhat-lsb-core gettext gettext-devel protobuf
        yum install -y perl-Digest perl-Digest-MD5 perl-Data-Dumper vim-common curl libcurl libcurl-devel
        yum install -y doxygen graphviz texlive texlive-xtab texlive-multirow texlive-sectsty texlive-tocloft
        yum install -y texlive-adjustbox deltarpm tcl automake
        ```

   - 离线安装依赖:
    <br>
        依赖离线包：rpm_DTK2404_centos7.6_3.10.0-957.tar
    <br>
        链接：https://pan.baidu.com/s/1jnWfddL4lHWVQb3btD34Iw?pwd=wj6q
    <br>
        提取码：wj6q
    <br>
        下载好导入服务器，进行解压：
    <br>
        1. `vi /etc/yum.repos.d/localyum.repo`，输入如下内容，请根据解压的路径，修改baseurl的内容，下面配置是在root路径下解压的依赖包;

            ```shell
            [local-repo]
            name=local-repo
            baseurl=file:///root/centos7-dtk24.04
            enabled=1
            gpgcheck=0
            ```

        2. 开始安装离线依赖包

            ```shell
            sudo yum clean all
            #以安装cmake3为例
            yum --disablerepo="*" --enablerepo="local-repo" install cmake3
            ```

#### 1.2.6. **校验系统配置:**

| 设备名称 | 设备码 |
| -----   | ----- |
| Z100L  | 1d94:55b7 |
| K100   | 1d94:62b7 |
| K100_AI | 1d94:6210 |

- 查看DCU设备

```shell
# Z100L
root@sugontest79:/mnt#lspci -nn |grep -i 55b7
------------------------------------------------------------------------------------------------------
07:00.0 Display controller [0380]: Chengdu Haiguang IC Design Co., Ltd. ZIFANG [1d94:55b7] (rev 01)
0a:00.0 Display controller [0380]: Chengdu Haiguang IC Design Co., Ltd. ZIFANG [1d94:55b7] (rev 01)
------------------------------------------------------------------------------------------------------

root@sugontest79:/mnt#lspci -nn |grep -i 62b7
------------------------------------------------------------------------------------------------------
07:00.0 Co-processor [0b40]: Chengdu Haiguang IC Design Co., Ltd. KONGMING [1d94:62b7] (rev 01)
0a:00.0 Co-processor [0b40]: Chengdu Haiguang IC Design Co., Ltd. KONGMING [1d94:62b7] (rev 01)
------------------------------------------------------------------------------------------------------

root@sugontest79:/mnt#lspci -nn |grep -i 6210
------------------------------------------------------------------------------------------------------
07:00.0 Co-processor [0b40]: Chengdu Haiguang IC Design Co., Ltd. KONGMING [1d94:6210] (rev 01)
0a:00.0 Co-processor [0b40]: Chengdu Haiguang IC Design Co., Ltd. KONGMING [1d94:6210] (rev 01)
------------------------------------------------------------------------------------------------------

```

> 注：输出信息可能和截图不完全一致。

- 配置环境变量

    <br>
    创建文件 `/etc/profile.d/devtoolset-7.sh`，内容如下：
    <br>
    `source /opt/rh/devtoolset-7/enable`
    <br>
    退出当前登录会话重新登录，或者执行source /etc/profile.d/devtoolset-7.sh。




#### 1.2.7. **安装驱动:**

**注意：**
> DTK和rock驱动有对应关系，可参考[dcu-环境安装手册](#DCU环境安装手册)，推荐安装最新的使用<br>
> -安装驱动之前需要安装基础包，包括cmake、gcc等多种基础依赖包，请先参考`DCU环境安装手册`完成基础环境包的安装。


**驱动下载地址**:  [https://cancon.hpccube.com:65024/6/main](https://cancon.hpccube.com:65024/6/main) → latest 驱动→ rock-xxx-xxx.aio.run


1. 安装 DCU 加速卡驱动

    ```bash
    chmod 755 rock-5.7.1-6.2.13-V1.0.1a.aio.run
    ./rock-5.7.1-6.2.13-V1.0.1a.aio.run
    ```

2. 如果安装过程更新了`vbios`, 则需要重启机器

    ```bash
    reboot
    ```

3. 查看验证是否安装成功

    ```bash
    # 出现如下类似结果则安装成功
    [root@b04r3n02 ~]# lsmod | grep hydcu
    hydcu           1435342     0
    hydcu_sched     34432       1   hydcu
    hyttm           61919       1   hydcu
    hykcl           46567       3   hydcu_sched,hydcu,hyttm
    hy_extra        32140       3   hydcu_sched,hydcu,hykcl
    amd_iommu_v2    18821       1   hydcu
    drm_kms_helper  179394      3   ast,hydcu,hykcl
    drm             429744      8   ast,ttm,hydcu,hykcl,hyttm,drm_kms_helper
    ```

4. 卸载驱动步骤：

    <br>
    如遇到异常情况或需要更新版本，先执行驱动卸载。
    <br>

    ```shell
    rpm -qa | grep rock   #查询安装的驱动版本
    rmmod hydcu
    rpm -e rock-5.7.1-6.2.18-1.x86_64
    ```




#### 1.2.8. **安装DTK:**
   
**DTK下载地址**:  [https://cancon.hpccube.com:65024/1/main](https://cancon.hpccube.com:65024/1/main)  → latest → 对应的操作系统 → DTK-version-OS-version-x86_64.tar.gz


1. 安装

    ```bash
    # 解压安装
    tar xvf DTK-24.04.1-CentOS7.6-x86_64.tar.gz -C /opt
    # 创建软连接
    ln -s /opt/dtk-24.04.1 /opt/dtk
    ```

3. 设置 DTK 环境变量

    > DTK 压缩文件中提供了设置环境变量脚本 env.sh。可以通过 source /opt/dtk/env.sh 的方式临时加载环境变量。为避免多次配置，常用以下方式加载环境变量

    ```bash
    echo "source /opt/dtk/env.sh">> ~/.bashrc
    # 激活环境变量
    source  ~/.bashrc
    ```

4. 验证 DCU 环境

    ```bash
    # 查看并执行 hy-smi 或者 rocm-smi 指令查看 dcu 基本信息
    [root@h01r4n04~]# rocm-smi
    # 出现如下内容, 则安装成功
    ===================System Management Interface =================
    ==========================================================
    DCU Temp AvgPwr Fan Perf PwrCap VRAM% DCU%
    0 50.0c 55.0W 0.0% auto 450.0W 0% 0%
    1 50.0c 58.0W 0.0% auto 450.0W 0% 0%
    2 49.0c 58.0W 0.0% auto 450.0W 0% 0% 
    3 49.0c 55.0W 0.0% auto 450.0W 0% 0%
    ==========================================================
    ======================End of SMI Log========================
    ```

#### 1.2.9. **验证安装结果:**

1. 使用`rocminfo`命令检查ROCm系统状态

    <br>
    终端输入如下内容:
    <br>

    ```shell
    rocminfo | grep gfx

    # 其中Z100/Z100L为gfx906，K100为gfx926，K100_AI为gfx928; 有输出即说明驱动和DTK安装成功
    ------------------------------------------------------------------------------------------------------------
        Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
        Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
        Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
        Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
        Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
        Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
        Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
        Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
    ```
    <br>

2. 运行`hy-smi`或`rocm-smi`来监控DCU的状态和性能指标；

    ```shell
    # 查看并执行 hy-smi 或者 rocm-smi 指令查看 dcu 基本信息
    [root@h01r4n04~]# rocm-smi
        # 出现如下内容, 则安装成功
    ============================ System Management Interface =============================
    ======================================================================================
    DCU     Temp     AvgPwr     Perf     PwrCap     VRAM%      DCU%      Mode     
    0       42.0C    39.0W      auto     280.0W     0%         0%        Normal   
    1       41.0C    39.0W      auto     280.0W     0%         0%        Normal   
    2       41.0C    36.0W      auto     280.0W     0%         0%        Normal   
    3       40.0C    38.0W      auto     280.0W     0%         0%        Normal   
    4       40.0C    39.0W      auto     280.0W     0%         0%        Normal   
    5       41.0C    41.0W      auto     280.0W     0%         0%        Normal   
    6       42.0C    37.0W      auto     280.0W     0%         0%        Normal   
    7       41.0C    36.0W      auto     280.0W     0%         0%        Normal   
    ======================================================================================
    =================================== End of SMI Log ===================================
    ```
