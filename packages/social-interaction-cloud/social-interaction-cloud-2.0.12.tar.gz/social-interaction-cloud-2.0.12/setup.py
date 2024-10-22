from setuptools import setup, find_packages

# Basic (bare minimum) requirements for local machine
requirements = [
    'numpy',
    'Pillow',
    'PyTurboJPEG',
    'redis',
    'six',
    'opencv-python',
    'paramiko',
    'pyaudio',
    'pyspacemouse',
    'scp',
]

# Dependencies specific to each component or server
extras_require = {
    'dialogflow': [
        'google-cloud-dialogflow',
    ],
    'face-detection-dnn': [
        'matplotlib',
        'pandas',
        'pyyaml',
        'torch',
        'torchvision',
        'tqdm',
    ],
    'face-recognition-dnn': [
        'scikit-learn',
        'torch',
        'torchvision',
    ],
}

setup(
    name='social-interaction-cloud',
    version='2.0.12',
    author='Koen Hindriks',
    author_email='k.v.hindriks@vu.nl',
    packages=find_packages(),
    package_data={
        'sic_framework.services.face_detection': [
            'haarcascade_frontalface_default.xml',
        ],
        'lib.libturbojpeg.lib32': [
            'libturbojpeg.so.0',
        ],
    },
    install_requires=requirements,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'run-dialogflow=sic_framework.services.dialogflow:main',
            'run-face-detection=sic_framework.services.face_detection:main',
            'run-face-recognition=sic_framework.services.face_recognition_dnn:main',
        ],
    },
)
