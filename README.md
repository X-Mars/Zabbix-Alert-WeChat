# Zabbix-Alert-WeChat zabbix微信报警
## 作者:火星小刘 邮箱:xtlyk@163.com   

### 2017-08-08
1. 全部重写，代码更简洁易读
2. 舍弃原有**simplejson**，使用**requests**模块
3. 支持**python2**

### 需要具备一下条件  
 * 注册微信企业号（团队类型） [点击注册](https://qy.weixin.qq.com/)   或    注册企业号微信  [点击注册](https://work.weixin.qq.com/）
 * 近期腾讯把**微信企业号**升级为了**企业微信**，本脚本完全兼容。
#### 安装组件
1. 安装方法一
```shell
pip install requests
pip install --upgrade requests
```
2. 安装方法二
```shell
wget https://pypi.python.org/packages/c3/38/d95ddb6cc8558930600be088e174a2152261a1e0708a18bf91b5b8c90b22/requests-2.18.3.tar.gz
tar zxvf requests-2.18.3.tar.gz
cd requests-2.18.3
python setup.py build
python setup.py install
```
  
#### 下载安装脚本  
```bash  
git clone https://github.com/X-Mars/Zabbix-Alert-WeChat.git  
cp Zabbix-Alert-WeChat/wechat.py /etc/zabbix/alertscripts  
chmod +x /etc/zabbix/alertscripts/wechat.py  
```
  
### 微信企业号设置  
#### 通讯录设置  
登陆微信企业号控制台  
点击左侧“通讯录”，新增部门（技术部）与子部门（运维部），并添加用户  
点击（运维部）后方的三角，修改部门，记录**部门ID**  
  
#### 创建应用  
点击左侧“应用中心”，新建消息型应用，应用名称为“zabbix报警”  
“应用可见范围”，添加刚刚新建的子部门（运维部）  
点击“zabbix报警”，记录**应用ID**
  
#### 应用权限设置  
点击左侧“设置”，权限管理，新建普通管理组，名称填写“zabbix报警组”  
点击修改“通讯录权限”，勾选（技术部）后方的管理  
点击修改“应用权限”，勾选刚刚创建的“zabbix报警”  
点击刚刚创建的“zabbix报警组”，记录左侧的**CorpID与Secret**
  
#### 收集微信相关信息
1. 记录**应用ID**
2. 记录**CorpID与Secret**
3. 记录**子部门（运维部）ID**
  
  
### zabbix设置
1. 添加示警媒介  
#### 管理-->示警媒介  
名称填写**微信报警**，类型选择**脚本**，脚本名称填写**wechat.py**  
#### 管理-->用户-->示警媒介  
类型选择**微信报警**，收件人添加**微信企业号通讯录内的，用户帐号**

完成

