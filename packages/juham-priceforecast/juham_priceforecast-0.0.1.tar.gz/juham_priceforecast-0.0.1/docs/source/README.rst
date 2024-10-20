juham_priceforecast
====================

`juham-priceforecast` plugs electricity price forecast service to Juham - Juha's Ultimate
Home Automation Masterpiece applications.



Features
--------

This plugin allows users to configure multiple electricity sources, such as solar panels, aggregates, and
the grid, each with its respective price expectations. It generates electricity price forecasts by calculating cost 
for a specific amount of power. This functionality is crucial for many home automation applications, answering the
question: how much would I have to pay for electricity if I consumed a specific amount of additional power.
For example, how much would it cost if I switched on my 7 kW sauna right now. 



Installation
------------

The installation is two stage process

1. To install:

.. code-block:: python

    pip install juham-priceforecast


2. Configure

   PriceForecast can be configured just like all the other masterpieces, through its
   json configuration file: '~/.[app]/config/PriceForecast.json' 
   file.



License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.
