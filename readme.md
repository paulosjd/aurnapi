A repository of the underlying code for the JSON API available at air-aware.com which was built using the Flask framework and 
the flask-SQLAlchemy extension. The API exposes hourly air quality monitoring
measurements for 123 sites across the UK which form part of AURN, the automatic monitoring network. The API
facilitates visualization of real-time and historical data, and provides a more convenient means for accessing data 
than by submitting web forms in the government body (DEFRA) website.

In addition to the functionality exposing data from the database, the repository contains modules which enable a database 
to be constructed and populated using data scraped from a webpage which is updated with the latest air quality measurements
once an hour (but does not provide any historical data). The functionality to scrape and insert the most recent data can
be run manually but should ideally be setup to run automatically on a server.
