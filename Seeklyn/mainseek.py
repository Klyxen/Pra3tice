#!/usr/bin/env python

import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from colorama import init, Fore, Style
import socket
init(autoreset=True)

def online():
  try:
    socket.create_connection(("8.8.8.8", 53), timeout=3)
    return True
  except OSError:
    return False

def info(number):
  try:
    parsed = phonenumbers.parse(number)

    country = geocoder.description_for_number(parsed, "en")
    sim_carrier = carrier.name_for_number(parsed, "en")

    return country, sim_carrier
  except phonenumbers.phonenumberutil.NumberParseException:
    return "Invalid Number", None

geolocator = Nominatim(user_agent="geoapi")
tf = TimezoneFinder()

try:
  while True:
    try:
      phone_number = input("Enter Phone Number : ")
    except EOFError:
      print("Input Interrupted...")
      break

    if not online():
      print("No Internet, Please check or turn on the internet")
      continue

    country, sim_carrier = info(phone_number)
    if country == "Invalid Number":
      print("Invalid Phone Number")
      continue

    location = geolocator.geocode(country)
    if not location:
      print("Could not locate the country")
      continue

    timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)

    print(f"Country : {country}")
    print(f"Carrier : {sim_carrier}")
    print(f"Timezone : {timezone_str}")
except KeyboardInterrupt:
  print("Exiting...")
