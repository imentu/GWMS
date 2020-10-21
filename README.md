# GWMS
IMAU软件工程概论大作业

## 打包方式
 * > pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
 * > pyinstaller runserver.py -y --add-data ./resources/app;./app --add-data ./resources/flask_admin;./flask_admin --add-data ./resources/flask_ckeditor;./flask_ckeditor 
 * > pyinstaller create_db.py
 * 将 dist/create_db/create_db.exe 复制到 dist/runserver/目录。

## 运行
 * > create_db.exe 
 * create_db.exe 使用 -d 参数时会生成随机数据填充到数据库。
 * > runserver.exe
 * 默认管理员账号为 admin，密码：admin。

