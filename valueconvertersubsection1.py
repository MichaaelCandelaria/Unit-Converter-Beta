# Welcome message
print("Welcome to Michael's number converter!")
print(' 1. Imperial only \n 2. Metric only \n 3. Imperial to metric \n 4. Metric to Imperial')
unit_system = int(input('First, please select what conversion type you wish to use here:'))
# Imperial only
if unit_system == 1:
    print('  1. Length \n  2. Mass')
    unit_type = int(input('Enter unit type here: '))
# Imperial Length
    if unit_type == 1:
        print('Below is a list of IMPERIAL LENGTH conversions')
        print('    1. Feet to Inches \n    2. Feet to Miles \n    3. Feet to Yards \n    4. Inches to Feet')
        print('    5. Inches to Miles \n    6. Inches to Yards \n    7. Miles to Feet \n    8. Miles to Inches')
        print('    9. Miles to Yards \n    10. Yards to Feet \n    11. Yards to Inches \n    12. Yards to Miles')
        conversion = int(input('Please input what IMPERIAL LENGTH measurement you would like to convert: '))
    # Feet to Inches
        if conversion == 1:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(12), 'Inches')
    # Feet to Miles
        elif conversion == 2:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(5280), 'Miles')
    # Feet to Yards
        elif conversion == 3:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(3), 'Yards')
    # Inches to Feet
        elif conversion == 4:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(12), 'Feet')
    # Inches to Miles
        elif conversion == 5:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(63360), 'Miles')
    # Inches to Yards
        elif conversion == 6:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(36), 'Yards')
    # Miles to Feet
        elif conversion == 7:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(5280), 'Feet')
    # Miles to Inches
        elif conversion == 8:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(63360), 'Inches')
    # Miles to Yards
        elif conversion == 9:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(1760), 'Yards')
    # Yards to Feet
        elif conversion == 10:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(3), 'Feet')
    # Yards to Inches
        elif conversion == 11:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(36), 'Inches')
    # Yards to Miles
        elif conversion == 12:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(1760), 'Miles')
# Imperial Mass
    elif unit_type == 2:
        print('Below is a list of IMPERIAL MASS conversions')
        print('    1. Pounds to Ounces \n    2. Ounces to Pounds \n    3. Pounds to Tons \n    4. Tons to Pounds')
        print('     5. Ounces to Tons')
        conversion = int(input('Please input what IMPERIAL MASS measurement you would like to convert: '))
    # Pounds to Ounces
        if conversion == 1:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(16), 'Ounces')
    # Ounces to Pounds
        elif conversion == 2:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(16), 'Pounds')
    # Pounds to Tons
        elif conversion == 3:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(2000), 'Tons')
    # Tons to Pounds
        elif conversion == 4:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(2000), 'Pounds')
    # Ounces to Tons
        elif conversion == 5:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(32000), 'Tons')
# Metric only
elif unit_system == 2:
    print('  1. Length \n  2. Mass')
    unit_type = int(input('Enter METRIC unit type here: '))
    # Metric Length
    if unit_type == 1:
        print('Below is a list of METRIC LENGTH conversions')
        print('     1. Centimeters to Kilometers \n     2. Centimeters to Meter \n     3. Centimeters to Millimeters')
        print('     4. Kilometers to Centimeters \n     5. Kilometers to Meters \n     6. Kilometers to Millimeters')
        print('     7. Meters to Centimeters \n     8. Meters to Kilometers \n     9. Meters to Millimeters')
        conversion = int(input('Please enter the METRIC LENGTH you wish to convert: '))
        # Centimeters to Kilometers
        if conversion == 1:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(100000), 'Kilometers')
        # Centimeter to Meter
        elif conversion == 2:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(100), 'Meters')
        # Centimeters to Millimeters
        elif conversion == 3:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(X) * int(10), 'Millimeters')
        # Kilometers to Centimeters
        elif conversion == 4:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(100000), 'Centimeters')
        # Kilometers to Meters
        elif conversion == 5:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(1000), 'Meters')
        # Kilometers to Millimeters
        elif conversion == 6:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(1000000), 'Millimeters')
        # Meters to Centimeters
        elif conversion == 7:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(100), 'Centimeters')
        # Meters to Kilometers
        elif conversion == 8:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) / int(1000), 'Kilometers')
        # Meters to Millimeters
        elif conversion == 9:
            x = float(input('Please enter the value you wish to convert: '))
            print(float(x) * int(1000), 'Millimeters')
    # Metric Length
    elif unit_type == 2:
        print('Below is a list of METRIC MASS conversions')
        print('     1. ')
