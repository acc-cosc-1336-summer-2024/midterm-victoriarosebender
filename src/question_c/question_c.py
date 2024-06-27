#write functions here, don't add input('') statements here!

def get_fahrenheit(celsius):
    fahren = celsius*9/5 + 32

    return fahren

def run_table():

    for celsius in range(0,21):
        fahren = get_fahrenheit(celsius)
        print(celsius,"C","-",fahren,"F")


    
