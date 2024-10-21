from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='nonebot-plugin-partner-join',
    version='0.1.2.1',
    description='NoneBot2 plugin used to generate maimaiDX travel companion add pictures (rotating gif) and can also be used to generate pictures similar to embed the corresponding circular frame (such as embedding the picture into the school badge).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='YuuzukiRin',
    author_email='yuuzukirin@outlook.com',
    url='https://github.com/YuuzukiRin/nonebot_plugin_partner_join',
    packages=find_packages(),
    install_requires=[
        "nonebot2>=2.0.0",
        "nonebot-adapter-onebot",
        "nonebot-plugin-alconna.uniseg",
        "nonebot-plugin-apscheduler",
        "Pillow",
        "httpx",
        "imageio",
        "python-dotenv",
        "tarina"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    package_data={
        'nonebot_plugin_partner_join': ['background/*.gif'],      
    },
    include_package_data=True,  
)


