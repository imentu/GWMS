# GWMS
IMAU软件工程概论大作业
后端框架使用 flask，数据库为 SQLite3。
前端使用 vue + elementUI。

## 打包方式
 * > pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
 * > pyinstaller runserver.py 
 * > pyinstaller create_db.py
 * 找到 app/flask_admin/flask_ckeditor 的 static/templates 文件夹，复制到 dist/runserver/{package_name} 目录。
 * 将 dist/create_db/create_db.exe 复制到 dist/runserver/目录。

## 运行
 * > create_db.exe 
 * create_db.exe 使用 -d 参数时会生成随机数据填充到数据库。
 * > runserver.exe
 * 默认管理员账号为 admin，密码：admin。

