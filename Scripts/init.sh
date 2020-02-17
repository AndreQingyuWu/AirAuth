#!/bin/bash
#Desc : 项目部署脚本
#Author : GeeCat
#Version: 1.0
#Create : 2019-12-30

cd ./../Server/auther/
nohup python3 manage.py runserver 0.0.0.0:8002 > server.log 2>&1 &
cd ./../test_client/
nohup python3 manage.py runserver 0.0.0.0:8001 > client.log 2>&1 &
cd ./../../QuickApp/airauth
npm run build
npm run server
exit 0
