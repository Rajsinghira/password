number=+919523193043

import phonenumbers

from phonenumbers import geocoder

ch_nmber = phonenumbers.parse(number, "CH")

print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier

şervice_nmber = phonenumbers.parse(number, "RO")


print(carrier.name_for_number(service_nmber, "en"))
