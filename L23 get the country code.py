country_code = {'india': '0091',
                'australia': '0025',
                'indonesia' : '0062',
                'Nepal' : "0977"
                }

#search dictionary for country of indonesia 
print("Country code for indonesia: ")
print(country_code.get('indonesia', "not found"))

#Search dictionalry for country code of Nepal
print("Country code for Nepal: ")
print(country_code.get('Nepal', "not found"))

#Search dictionalry for country code of Japan
print("Country code for Japan: ")
print(country_code.get('Japan', "not found"))