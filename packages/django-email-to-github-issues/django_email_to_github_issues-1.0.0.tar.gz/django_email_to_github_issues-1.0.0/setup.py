from setuptools import setup, find_packages

setup(
    name='django-email-to-github-issues',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
        'celery>=5.0',
        'requests',
        'imaplib2',
    ],
    license='MIT',
    description='Django app to create GitHub issues from emails, with attachments.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/django-email-to-github-issues',
)
