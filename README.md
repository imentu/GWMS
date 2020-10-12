# GWMS
Software Engineering Homework

## 打包方式
 * > pip install -r requirement.txt
 * 找到 flask_admin 的包文件夹，复制到项目目录。
 * > pyinstaller runserver.py --add-data "./app/static/*;./app/static" --add-data "./app/templates/*;./app/templates"
 * > pyinstaller create_db.py
 * 将 dist/create_db/create_db.exe 复制到 dist/runserver/目录下。

## 运行
 * > create_db.exe 
 * create_db.exe 使用 -d 参数时会生成随机数据填充到数据库。
 * > runserver.exe
 * 默认管理员账号为 admin，密码：admin。

