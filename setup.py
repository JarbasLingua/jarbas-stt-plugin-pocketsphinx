#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'pocketsphinx_stt_plug = ' \
                     'jarbas_stt_plugin_pocketsphinx:PocketSphinxSTTPlugin'
setup(
    name='jarbas-stt-plugin-pocketsphinx',
    version='0.1',
    description='A pocketsphinx stt plugin for mycroft',
    url='https://github.com/JarbasLingua/jarbas-stt-plugin-pocketsphinx',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['jarbas_stt_plugin_pocketsphinx'],
    install_requires=["pocketsphinx>=0.1.3", "speechrecognition>=3.8.1"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin stt',
    entry_points={'mycroft.plugin.stt': PLUGIN_ENTRY_POINT}
)
