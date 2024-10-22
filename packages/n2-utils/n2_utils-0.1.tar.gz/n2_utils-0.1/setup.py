from setuptools import setup, find_packages

setup(
    name='n2_utils',  # Paket adınız
    version='0.1',  # Paket versiyonu
    packages=find_packages(),  # Paketlenecek modülleri bulur
    include_package_data=True,  # Statik dosyaların da dahil edilmesini sağlar
    install_requires=[
        'django>=3.2',  # Django versiyonunu belirtebilirsiniz
        # Diğer bağımlılıklar
    ],
    license='MIT',  # Lisans
    description='My Django App as a pip package',  # Kısa açıklama
    long_description='Test',  # README.md içeriği paket açıklaması olarak kullanılır
    long_description_content_type='text/markdown',  # Markdown formatında açıklama
    url='https://github.com/yourusername/my_django_app',  # Paketinizin URL'si
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
    ],
)