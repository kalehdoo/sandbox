from random import randrange, uniform

def get_device_data():    
    return {
        "high_blood_pressure": randrange(80, 120), 
        "low_blood_pressure": randrange(40, 60)
    }

if __name__ == '__main__':
    print(get_device_data())