# 说明
playwright助手，内置函数

win系统如需控制隐藏窗口，需安装pywin32


## 试一试
```python
from easy_pyweb.wb_helpers import WebHelper

def open_page():
    wb = WebHelper(cookie_path='cookies.txt')
    page = wb.new_page()
    page.goto('https://tool.lu/timestamp/')
    print(page.title())
    assert page.title() == '时间戳(Unix timestamp)转换工具 - 在线工具'
```

# 打包操作
需要安装包
pip install build twine

执行打包
python -m build

推送分支`[testpypi|pypi]`

python -m twine upload --repository testpypi dist/*