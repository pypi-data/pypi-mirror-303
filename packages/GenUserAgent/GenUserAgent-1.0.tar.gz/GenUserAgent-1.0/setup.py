from setuptools import setup, find_packages
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
    name='GenUserAgent',  # Tên thư viện của bạn
    version='1.0',  # Phiên bản đầu tiên
    packages=find_packages('src'),  # Tìm tất cả các packages trong thư mục src
    package_dir={'': 'src'},  # Chỉ định thư mục chứa các packages
    author='Lam',
    author_email='ldl.contact.booking@gmail.com',
    description='Thư Viện Hỗ Trợ Tạo UserAgent',
    long_description=open('README.md','r',encoding='utf-8').read(),  # Đọc nội dung README nếu có
    long_description_content_type='text/markdown',  # Định dạng của long description
    url='',  # URL tới nguồn của bạn
    classifiers=classifiers,
    python_requires='>=3.6',  # Phiên bản Python yêu cầu
    install_requires=[  # Các phụ thuộc, nếu có
        # 'some_dependency',
    ],
    test_suite='tests',  # Thư mục chứa các bài kiểm tra
)
