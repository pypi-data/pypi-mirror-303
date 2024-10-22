from setuptools import setup, find_packages

setup(
    name="django-snart",
    version="0.0.1",
    description="A Django app for text translation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Gregory Zhizhilkin",
    author_email="gregory@stopdesign.ru",
    url="https://github.com/stopdesign/django-snart",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[
        "Django>=3.2",
        "django-modeltranslation",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
