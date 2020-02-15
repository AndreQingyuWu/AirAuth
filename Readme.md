![avatar](https://geecatswc.github.io/source/AirAuth/ReadmePage/AirAuth.png)

# AirAuth 轻验

## 背景介绍
AirAuth 要提供一种可以在多场景调用，通过可靠的生物认证方式和授权协议，生成生物ID的隐式实时身份认证，以及授权管理功能的身份认证服务框架。最终实现不依赖账号密码和设备绑定，以人为本的身份认证方式；并利用快应用实现 页面和智能设备的认证调用接口，达到万物互融，即开即用，即用即走的效果。  



## 项目介绍  
AirAuth是一款提供有页面和智能设备调用接口，基于快应用开发的生物身份认证授权服务。利用生物识别和深度学习技术，提供检测，识别，对比，认证等完整的端到端技术能力，可广泛应用于APP登录，网页登录，安全认证，智能音箱， 闸机门禁等认证场景。可以避免传统认证方法的不安全性和认证的繁琐性。    
  
具体功能包括：  
        1. 多场景调用接口：可在登录页面中，以第三方登录的形式（类似QQ第三方登录，微信第三方登录）提供认证授权服务接口；并且同理在智能硬件中也嵌入蓝牙或二维码的认证调用接口，利用快应用弹出认证页面，提供给用户多场景身份认证服务的入口。  
        2. 面部认证功能：AirAuth采用快应用作为认证服务的载体，由于快应用不支持读取指纹等数据，所以为了在用户不佩戴腕部认证手环的情况下能够进行认证，我们采集面部特征作为一种生物认证途径。在用户选择使用人脸认证时，提供基于前置摄像头的人脸识别和采集，以达到识别用户的功能。  
        3. 生物手环认证功能：在用户佩戴有腕部生物骨纹手环时，AirAuth可在用户调用认证功能时，利用快应用通过蓝牙自动读取手环数据，实现真正的隐式的持续身份认证功能。  
        4. 授权管理功能：AirAuth 提供基于快应用的权限管理功能，用户可增添或删除被授权方，并且设置认证方式及权限。  
        5. 快应用卡片快速入口：AirAuth提供权限管理和一键直达的快速入口，利用快应用卡片在手机的负一屏展现权限管理的快应用卡片，用户不仅可以快速管理自己的授权，还可以直接点击被授权方一键快速登陆并且直达链接页面。  
        
## 环境依赖  

### 服务器环境：  
	asn1crypto==0.24.0  
	certifi==2018.10.15  
	cffi==1.11.5  
	chardet==3.0.4  
	cryptography==2.3.1  
	Django==2.1.2  
	idna==2.7  
	pycparser==2.19  
	PyMySQL==0.9.2  
	pytz==2018.5  
	requests==2.19.1  
	six==1.11.0  
	urllib3==1.23  

### 快应用环境：  
    node==8.10.0  
    npm==3.5.2  
    hap-tooikit==2.1.1  

## 部署步骤
运行/Script/init.sh脚本

## 使用说明
本项目需要在快应用服务框架版本1010+的安卓手机运行  

## 目录结构描述  
<pre><code>.
├── Readme.md                 //readme  
│  
├── Script  
│   └── init.sh               //部署脚本  
│  
├── Model                     //腕部骨骼声纹身份认证模型  
│   ├── modified_vgg16.py     //基于vgg16修改的模型训练  
│   ├── model.h5              //模型文件  
│   └── Preprocessed_data     //存放预处理可视化数据  
│  
├── Server                    //AirAuth认证服务 基于Django2服务器代码  
│   ├── READEME               //server端 readme  
│   ├── sql.py                //数据库设置代码  
│   ├── env                   //存放server端 python环境  
│   ├── test_client           //模拟第三方登录接口的测试客户端网站  
│   │   ├── db.sqlite3  
│   │   ├── client  
│   │   ├── oauthClient  
│   │   ├── templates  
│   │   └── manage.py         //Django项目管理部署文件  
│   │  
│   └── auther                //AirAuth认证服务代码  
│       ├── .idea  
│       ├── auther  
│       ├── oauthServer  
│       ├── static  
│       ├── templates  
│       └── manage.py         //Django项目管理部署文件  
│     
└── QuickApp                  //存放快应用代码  
    ├── airauth               //AirAuth快应用客户端  
    │   ├── .ide  
    │   ├── build  
    │   ├── dist  
    │   ├── node_modules  
    │   ├── sign  
    │   ├── .eslintrc.json  
    │   ├── babel.config.js   
    │   ├── package.json  
    │   ├── package-lock.json  
    │   ├── package-lock.json  
    │   └── src  
    │       ├── AcousticAuth  //腕部骨骼声纹认证页面  
    │       ├── FaceAuth      //人脸认证页面  
    │       ├── Management    //授权管理页面  
    │       ├── CardPage      //快应用卡片模拟页面  
    │       ├── Auth          //认证选项  
    │       ├── BLEDevice     //蓝牙调用页面  
    │       ├── AuthResult    //认证结果页面  
    │       ├── Common        //资源文件  
    │       ├── app.ux  
    │       ├── util.js  
    │       └── manifest.json //快应用配置文件  
    │  
    └── testweb  
        ├── .ide  
        ├── build  
        ├── dist  
        ├── node_modules  
        ├── sign  
        ├── .eslintrc.json   
        ├── babel.config.js  
        ├── package.json  
        ├── package-lock.json  
        ├── package-lock.json  
        └── src  
            ├── TestWeb       //测试网站webview调用  
            ├── Common        //资源文件  
            ├── app.ux    
            ├── util.js  
            └── manifest.json //快应用配置文件  
</code></pre>

## 作者列表
![avatar](https://geecatswc.github.io/source/AirAuth/ReadmePage/GeeCat.jpg)  
本项目由GeeCat团队开发  
    
## V1.0.0
1. 完善项目，优化项目可部署性  
2. 提高了生物声纹认证方式的准确率  
3. 增加快应用卡片授权管理入口  

## 开源协议
本项目您可以根据Apache Licence 2.0 进行使用  
