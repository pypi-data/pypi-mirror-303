from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# with open('requirements.txt', "r", encoding="utf-8") as f:
#     required = f.read().splitlines()

setup(
    name="Industrial_time_series_analysis",                                # 包名
    version="1.11.6",                                                       # 版本号
    author="PYJ",                                                          # 作者
    author_email="3463146475@qq.com",                                      # 邮箱
    description="A time series data analysis algorithm library for industrial scenarios",               # 简短描述
    long_description=long_description,                                     # 详细说明
    package_data={'Industrial_time_series_analysis': ['**/*.json','**/*.csv', '**/*.pdf', '**/*.txt',  '**/*.pth', '**/*.ckpt'],
        # 包含特定目录下的.joblib文件
        'Industrial_time_series_analysis.Forecast.forecast_utils.STD_Phy_util.save.gas_improve': ['*.joblib'],},

    long_description_content_type="text/markdown",                         # 详细说明使用标记类型
    # url="https://github.com/Lvan826199/mwjApiTest",                      # 项目主页
    packages=find_packages(),                                              # 需要打包的部分
    python_requires=">=3.6",                                               # 项目支持的Python版本
    # install_requires=required,                                           # 项目必须的依赖
    # include_package_data=True,                                           # 打包包含静态文件标识
)
