Welcome to Juham™ - Juha's Ultimate Home Automation Masterpiece
===============================================================


Project Status and Current State
--------------------------------

This release introduces bug fixes and a couple of new features,
most notably the module that records log messages, e.g. warnings and errors,
to InfluxDB time series database. 

For a full list of changes in this release, consult the :doc:`CHANGELOG <CHANGELOG>`

The software development status has been elevated to 2 - "Pre-Alpha".

In its current state, you might call it merely a home automation mission, 
rather than masterpiece, but I'm working hard to turn it into a masterpiece! 


Goals
-----

Develop a decent home automation framework that can control all the
apparatuses in my home, and maybe also other homes.


Install
-------

1. pip install juham. This installs all the dependencies as well, I hope.

2. Set up InfluxDB 3.0 and Crafana cloud. Not an absolute requirement, Juham™ can
   live fine without them. However, I strongly recommend them, as they allow you to
   monitor your home from anywhere in the world.

3. Configure Juham™. When started all classes attempt to initialize themselves from their
   JSON configuration files, located in the `config` sub folder. The  files to pay attention to
   are:
   
   * `config/Base.json` - fill with your MQTT host and port information. 
   * `config/JDatabase.json` - fill with your InfluxDB account information. 
   * `config/RVisualCrossing.json` - you need API key to fetch the weather forecast from the Visual Crossing site.
   * `config/Shelly*.json` - in case you happen to have Shellies at your home.
  
4. Configure `myhome.py` to run as a service, or as a quick test from console: `python3 myhome.py`. 
   No two homes are alike, but this program is fully functional and serves as a good starting point for your real home.
   



Design
------

The design is based on object-oriented paradigm, a modular plugin architecture, full abstraction, 
and overall robustness of design. If you appreciate these concepts, look no further — you've come to the right place!

In Juham™, the fundamental units of control are called "masterpieces". Each masterpiece is an object designed 
to master a specific home apparatus. Whether it's controlling the lights, managing the thermostat, 
or operating the security system, masterpieces are the building blocks of your smart home.

Big part of the architectural patterns arise from the 'Object' base class. Just like all creatures on Earth share a common 
ancestor, all components of Juham™ trace their lineage back to this first life form of software (okay, maybe 
that’s a bit too dramatic, but you get the idea).

More magic emerges from the modular plugin architecture:  new features can be plugged in as independent components,
without touching (read breaking) the existing code.

The 'Object' base class plus a few others in the 'juham.base' module
are generic by nature, any software could be built on top of them. I'm planning to publish them as a separate 
python packages (yet another task to be added into :doc:`TODO <TODO>`).

The actual home automation specific classes revolve around  the MQTT broker and standardized Juham™ MQTT messages.
Data acquisition clients, such as those reading temperature sensors, electricity prices, and power levels from solar panels, 
to name a few, publish data to respective MQTT topics. Automation clients listening to these topics can then perform their 
designated tasks, such as control the temperature of a hot water boiler.


Developer Documentation
-----------------------

The documentation is still a work in progress. Originally, the documentation was generated using Doxygen, 
a tool primarily used for generating developer documentation in the C++ ecosystem. To feel more like a Python 
professional, I replaced it with Python's native documentation tool, Sphinx. After several frustrating 
hours (okay, days), I finally got it working, but it will require a few more hours (okay, days) of effort to be really usable.


Special Thanks
--------------

This project would not have been possible without the generous support of two extraordinary gentlemen: my best friend, Teppo K., 
and my son, `Mahi.fi <https://mahi.fi>`_. The project began with Teppo's donation of a Raspberry Pi computer, a temperature sensor, and an inspiring 
demonstration of his own home automation system. My ability to translate my automation ideas into Python is greatly due to my son, Mahi.
His support and encouragement have been invaluable in bringing this project to life. 
Thank you both!
