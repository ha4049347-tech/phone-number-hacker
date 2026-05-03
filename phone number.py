import phonenumbers
from phonenumbers import geocoder, carrier
print("Welcome to Hamid's phonenumber Hacker! make sure to a + at the start")
number = input("Enter your phone number and make sure to start with +: ")

try:
    parsed_number = phonenumbers.parse(number)

    # This gets the short code like 'US'
    location_code = phonenumbers.region_code_for_number(parsed_number)
    print("Location:", location_code)

    # This gets the service provider
    service_provider = carrier.name_for_number(parsed_number, "en")
    print("Carrier:", service_provider)

except:
    print("The string supplied did not seem to be a phone number.")
