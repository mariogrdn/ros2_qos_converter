from setuptools import setup

package_name = 'qos_converter'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mariogrdn',
    maintainer_email='mariogrdn@gmail.com',
    description='By changing topic and qos profile, allow to convert qos of messages',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'converter = qos_converter.qos_converter:main',
        ],
    },
)
