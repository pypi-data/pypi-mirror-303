from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="message_queue_sqlite",
    version="1.0.0",
    author="chakcy",
    author_email="947105045@qq.com",
    description="A simple message queue demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/cai-xinpenge/message_queue",
    include_package_data=True,
    packages=(
        find_packages(where=".")
    ),
    package_dir={
        "": ".",
        "message_queue":"./message_queue_sqlite"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)