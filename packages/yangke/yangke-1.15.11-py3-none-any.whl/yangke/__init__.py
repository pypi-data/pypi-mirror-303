# encoding=utf8
"""
制作*.whl的安装文件
"""
import sys
import os

__version__ = "1.15.11"
extras_require = {  # 额外依赖项，安装方法“pip install yangke[Database]”
    "Database": [
        'pymysql>=0.9.3',
        'DBUtils>=1.3',  # 用于创建数据库连接池
        'cryptography>=3.1.1',  # 用于mysql8以上版本的连接加密，必须安装，否则无法解析密码
        'python-docx',
        'mysql-connector-python>=8.0.24',
        'sqlalchemy<=1.4.39',  # 2.0版本的sqlalchemy存在很多兼容性问题，还需要进一步解决
    ],
    "windows": [
        'pypiwin32',
    ],
    "web": [
        'flask>=1.1.2',
        'Flask-Cors>=3.0.8',
        'waitress',
    ],
    "Stock": [
        # 'torch>=1.4.0', # pytorch需要单独安装，pypi里版本太老
        'tushare>=1.2.48',
        'scrapy>=2.0.0',
        # 'sxtwl>=1.0.7',  # 该库是用于农历节假日计算的，从2022年开始已经停止更新了，因此新版python不适用
        'pymysql>=0.9.3',
        'DBUtils>=1.3',
        'selenium>=3.141.0',
        'mysql-connector-python>=8.0.24',
        'selenium>=3.141.0',
        'sqlalchemy>=1.3.23',
    ],
    "ImageRecognition": [
        'opencv-python>=4.2.0',
        'cmake>=3.18.2',
        'boost',
        # 'dlib>=19.17.0',  # dlib需要单独安装，涉及到cmake和boost
        'pillow>=7.0.0',
        'requests>=2.22.0',
        # 'tensorflow>=2.8.0',
        # 'torch>=1.11.0',
        'optuna',
        'plotly',
        'paddlepaddle',

    ],

    "GameServer": [
        'twisted>=20.3.0',
        'flask>=1.1.2',
        'flask_cors>=3.0.8',
        'requests>=2.22.0',
        'gevent>=20.5.0',
        'gevent-websocket',
        'waitress>=1.4.4',
        'lxml',
    ],
    "Performance": [
        'iapws>=1.5.2',
        'pygame',
        # 'PyQt5',
        # 安装PyQt5时如果出现ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied:
        # ‘C:\Users\zhangbin\AppData\Roaming\Python\Python39\site-packages\PyQt5\Qt5\bin\d3dcompiler_47.dll’，
        # 说明d3dcompiler_47.dll文件占用，禁止无关应用开机启动，重启安装尝试。
        # 'PyQtWebEngine',  # 用于显示pyecharts图形
        'PyQt6',
        "PyQt6-WebEngine",
        'PyQt6-QScintilla'
        'PyQt6-WebEngine',
        # 'PySide6'
    ],

}

module_name_list = list(extras_require.keys())


def info():
    from yangke.common.config import printInColor
    printInColor(" module 'yangke' installed successfully ", color_fg='white', color_bg='cyan', mode=1)
    printInColor(" version is {} ".format(__version__), color_fg="white", color_bg="yellow", mode=1)
    print("The optional submodules are: ", end="")

    for mod in module_name_list[:-1]:
        printInColor('[{}]'.format(mod), mode=1, color_bg='', end='')
        print(", ", end='')
    printInColor('[{}]'.format(module_name_list[-1]), color_bg='', mode=1)

    print("Use command ", end="")  # end设置不换行输出
    printInColor("pip install yangke", color_fg='red', color_bg='yellow', end='', mode=1)
    printInColor("[Database]", color_bg='yellow', end="", mode=1)
    print("/", end='')
    printInColor("pip install *.whl", color_fg='red', color_bg='yellow', end='', mode=1)
    printInColor("[Database]", color_bg='yellow', end="", mode=1)
    print(" to install the selected submodule.")

    print("Use command ", end="")
    printInColor("pip install *.whl[All]", color_fg='red', color_bg='yellow', end='', mode=1)
    printInColor("[Database]", color_bg='yellow', end="", mode=1)
    print(" to install all the submodule.")


def yangke_test():
    info()


def version():
    info()


def test():
    info()


def start_restful_mysql(mysql_user, mysql_password, mysql_host='localhost', mysql_port=3306, mysql_db='sges',
                        rest_port=5000):
    from yangke.dataset.YKSqlalchemy import SqlOperator
    from sqlalchemy import create_engine
    from yangke.web.flaskserver import start_server_app
    sql = SqlOperator(
        create_engine(f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}'))

    def deal(args):
        action = args.get('Action')  # 因为下方use_action=True，所以这里的action必然有值，避免eval函数出错
        result = eval("{}(args)".format(action))
        return result

    def login(args):
        username = args['username']
        password = args['password']
        res = sql.exists_in_table('user', condition_dict={'user_name': username, 'password': password})
        return {
            "success": True,
            "login_info": res
        }

    def register(args):
        username = args['username']
        password = args['password']
        email = args['email']
        sql.insert_item('user', values=[username, email, password], col_names=['user_name', 'email', 'password'])
        return {"success": True}

    app = start_server_app(deal=deal, allow_action=['login', 'register'], host='0.0.0.0', port=rest_port,
                           example_url=[f'http://localhost:{rest_port}/?Action=login&username=杨可&password=test'],
                           single_thread=True)

# yangke_test()
