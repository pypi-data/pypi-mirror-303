from setuptools import setup, find_packages

# README.md の内容を読み込む
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='lingustruct',  # パッケージ名
    version='0.1.0',
    description='AI-supported system design framework optimized for usability.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Yasunori Abe',
    author_email='osusume-co@lilseed.jp',
    url='https://pypi.org/project/lingustruct/',
    packages=find_packages(exclude=['templates_server', '*.enc']),
    license='Proprietary',
    install_requires=[
        'fastapi',
        'uvicorn',
        'jinja2',
        'pydantic',
        'weasyprint',
        'markdown',
        'openai',
        'jsonschema',
        'cryptography',
        'requests',
        'redis>=4.0.0',
    ],
    include_package_data=True,  # MANIFEST.in の設定に従う
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
