from setuptools import setup

package_name = 'pub_sub_tests'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/pub_sub_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ipa-hsd',
    maintainer_email='harshavardhan.deshpande@ipa.fraunhofer.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = pub_sub_tests.pub_sub:main',
        ],
    },
)
