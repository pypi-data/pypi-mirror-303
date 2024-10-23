from setuptools import setup, find_packages

__version__ = '1.10.18'

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='MangoUi',
    version=__version__,
    description='UI组件库',
    long_description=long_description,
    # package_data={
    #     'mangokit.mango': ['mango.cp310-win_amd64.pyd'],
    # },
    author='毛鹏',
    author_email='729164035@qq.com',
    url='https://gitee.com/mao-peng/MangoUi',
    packages=find_packages(),
    install_requires=[
        'pydantic~=2.9.2',
        'pyside6~=6.7.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ]
)

r"""
pyside6-rcc D:\GitCode\MangoUi\mango_ui\resources\resources.qrc -o D:\GitCode\MangoUi\mango_ui\resources\app_rc.py

python -m pip install --upgrade setuptools wheel
python -m pip install --upgrade twine

python setup.py check
python setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

"""
