from distutils.core import setup

with open('README.md', 'r') as README:
    README_md = README.read()

setup(
    name = 'pygvideo',
    version = '1.0.0',
    author = 'azzammuhyala',
    author_email = 'azzammuhyala@gmail.com',
    description = 'pygvideo, video for pygame. Using moviepy video module to read and organize videos.',
    url = 'https://github.com/azzammuhyala/pygvideo.git',
    # packages = find_packages(),
    install_requires = [
        "pygame>=2.5.0",
        "moviepy>=1.0.3"
    ],
    keywords = [
        'pygvideo', 'pygamevid', 'pyvidplayer', 'pygame vid', 'pygame video', 'video player', 'vid player',
        'python pygame video', 'pgvideo', 'pgvid', 'video', 'player'
    ],
    packages = ['pygvideo'],
    long_description_content_type = 'text/markdown',
    long_description = README_md,
    python_requires ='>=3.10',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)