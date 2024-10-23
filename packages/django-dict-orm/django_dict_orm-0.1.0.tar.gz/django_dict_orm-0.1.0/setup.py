from setuptools import setup, find_packages

setup(
    name='django_dict_orm',
    version='0.1.0',
    packages=find_packages(),
    install_requires=["bcrypt==4.2.0", "setuptools==75.2.0"],  # Add dependencies if there are any
    author='Mirahmad',
    author_email='mirahmadhacker2007@gmail.com',
    description='A lightweight ORM for JSON data storage in Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/mirahmadhacker2007/django-dict-orm.git',  # Update with your GitLab URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
