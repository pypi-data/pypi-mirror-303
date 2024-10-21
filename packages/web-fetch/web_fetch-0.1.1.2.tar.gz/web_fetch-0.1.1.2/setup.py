from setuptools import setup, find_packages

setup(
    name='web_fetch',
    version='0.1.1.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'beautifulsoup4',
        'diskcache',
        'python-dotenv',
        'htmldate',
        'pydantic',
    ],
    entry_points={
        
    },
    author='li-xiu-qi',
    author_email='lixiuqixiaoke@qq.com',
    description='A package to fetch web resources and cache HTML content.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/li-xiu-qi/web_fetch',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)