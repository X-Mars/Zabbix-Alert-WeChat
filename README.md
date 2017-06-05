# Zabbix-Alert-WeChat zabbix微信报警
## 作者:火星小刘 邮箱:xtlyk@163.com   
  
### 需要具备一下条件  
 * 注册微信企业号（团队类型） [点击注册](https://qy.weixin.qq.com/)   或    注册企业号微信    [点击注册](https://work.weixin.qq.com/）
 * 近期腾讯把**微信企业号**升级为了**企业微信**，本脚本完全兼容。
#### 安装simplejson 3.8.2
```bash
wget https://pypi.python.org/packages/f0/07/26b519e6ebb03c2a74989f7571e6ae6b82e9d7d81b8de6fcdbfc643c7b58/simplejson-3.8.2.tar.gz#md5=53b1371bbf883b129a12d594a97e9a18
tar zxvf simplejson-3.8.2.tar.gz
cd simplejson-3.8.2
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

