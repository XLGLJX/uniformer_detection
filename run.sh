
##网上搜到到一个tips，不能直接跑
adduser acs          # 创建普通用户acs
usermod -aG sudo acs          # 给用户acs分配sudo权限
su -acs          # 可切换到用户acs中
#将镜像加载到本地，创建并运行镜像（这里的开放的端口就是我们上面自己服务器开放的端口），接着进入自己创建的docker容器内，设置好root密码，我们就可以使用docker容器，也可以挂起容器。
ssh server_name         # 登录自己的云端服务器
docker load -i django_lesson_1_0.tar         # 将镜像加载到本地
docker run -p 20000:22 -p 8000:8000 --name django_server -itd  django_lesson:1.0        #创建并运行django_lesson:1.0镜像 (端口要自己去云平台放行)
docker attach django_server         # 进入创建的docker容器
passwd         # 设置root密码
ctrl p + ctrl q         #挂起容器
#配置git,先在docker 容器内生成ssh密钥，等下连接git用。
django-admin startproject acapp #创建django项目acapp
ssh-keygen # 生成密钥用于连接到ac git上面
#在git偏好设置中，打开ssh密钥，添加一下刚才生成的公钥
git init # 进到acapp中将其配置成git仓库
#打开git，在git上创建一个仓库（项目）按照下面的提示在acs里面配置一下gitgit config --global user.name xxx
git config --global user.email xxx@xxx.com
git add .
git commit -m "xxx"
git remote add origin git@git.acwing.com:xxx/XXX.git #建立连接
git push --set-upstream origin master
#再打开一个tmux，(一个tmux用于维护控制台，另一个tmux用于开发)跑一下我们的项目 python3 manage.py runserver 0.0.0.0:8000
ag ALLOWED-HOSTS #全文搜索
python3 manage.py startapp game # 创建gameapp
ctrl c #先关掉控制台
python3 manage.py migrate #同步一下数据库的修改
python3 manage.py createsuperuser # 创建管理员账号
pyhton3 manage.py runserver 0.0.0.0:8000 # 启动控制台（8000就是我们开放的端口号）