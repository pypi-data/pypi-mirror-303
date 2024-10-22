from pathlib import Path

from setuptools import find_packages
from setuptools import setup

print('     setup: version:  v1.0.3')
print('     setup: module :  medver_pytest')

# @formatter:off
setup(
    description='Pytest module with Verification Protocol, Verification Report and Trace Matrix',
    keywords=['verification', 'pytest'],
    install_requires=[
        'docx',
        'jsmin',
        'pytest',
        'pytest-check',
        'python-docx',
        'reportlab',
    ],
    classifiers=[
        # Choose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing :: Acceptance',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],

    # common attributes from here on
    name='medver-pytest',
    packages=find_packages(include='./medver_pytest*', ),
    include_package_data=True,
    exclude_package_data={'./medver_pytest/lib': ['.gitignore']},
    version='1.0.3',
    license='MIT',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    author='J. Arrizza',
    author_email='cppgent0@gmail.com',
    url='https://bitbucket.org/arrizza-public/medver-pytest/src/master',
    download_url='https://bitbucket.org/arrizza-public/medver-pytest/get/master.zip',
)
# @formatter:on

print('     setup: done')
