- 环境说明
- python==3.9.7 
- django==2.2.4

```bash
pip install -r requirements.txt
```

```bash
  python3 manage.py makemigrations 
  python3 manage.py runserver
  python3 manage.py migrate
```

- 注意修改文件内的绝对路径再运行  将文件夹内的"F:/web_app/uniformer_detection"全部改为"your path/uniformer_detection"即可

- 目前还没有想好使用中文还是英文,所以可能会出现中英文混用的情况
- openh264-1.8.0-win64.dll 视频编码格式H.264的函数库，已下载好
- modelsss文件夹内有多个开源模型供使用（最重要的uniformer模型待添加）--
