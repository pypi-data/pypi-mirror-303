import os
import setuptools

# 获取当前文件所在目录的绝对路径
this_directory = os.path.abspath(os.path.dirname(__file__))
long_description = "使用说明"

# 尝试读取 README.md 文件
readme_file_paths = [
    os.path.join(this_directory, "README.MD"),
    os.path.join(this_directory, "easy_pyweb/README.MD")
]

for readme_file in readme_file_paths:
    if os.path.exists(readme_file):
        with open(readme_file, "r", encoding="utf-8") as fh:
            long_description = fh.read()
        break  # 找到文件后退出循环

# easy_pyweb项目
setuptools.setup(
    name="easy_pyweb",
    version="1.0",
    author="xiaoxi",
    author_email="xiaoxiggnet@gmail.com",
    url="https://github.com/xiaoxigithub",
    description="web helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,  # 包含所有包数据
    package_data={
        'easy_pyweb': ['js/*'],  # 包含 js 文件夹中的所有文件
    },
    install_requires=[
        "requests",
        "playwright",
    ],
    python_requires=">=3.6",
)
