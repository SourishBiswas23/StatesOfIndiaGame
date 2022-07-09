
states = {'Andhra Pradesh': (-101.0, -198.0), 'Arunachal Pradesh': (306.0, 208.0), 'Assam': (233.0, 144.0), 'Bihar': (81.0, 119.0), 'Chhattisgarh': (-9.0, 2.0), 'Goa': (-235.0, -200.0), 'Gujarat': (-309.0, 36.0), 'Haryana': (-166.0, 219.0), 'Himachal Pradesh': (-144.0, 303.0), 'Jammu And Kashmir': (-206.0, 359.0), 'Jharkhand': (69.0, 52.0), 'Karnataka': (-188.0, -222.0), 'Kerala': (-170.0, -347.0), 'Ladakh': (-209.0, 417.0), 'Madhya Pradesh': (-126.0, 43.0),
          'Maharashtra': (-204.0, -65.0), 'Manipur': (303.0, 105.0), 'Meghalaya': (224.0, 107.0), 'Mizoram': (282.0, 48.0), 'Nagaland': (320.0, 146.0), 'Odisha': (54.0, -30.0), 'Punjab': (-192.0, 276.0), 'Rajasthan': (-264.0, 149.0), 'Sikkim': (156.0, 165.0), 'Tamil Nadu': (-114.0, -320.0), 'Telangana': (-96.0, -115.0), 'Tripura': (247.0, 71.0), 'Uttarakhand': (-94.0, 256.0), 'Uttar Pradesh': (-48.0, 150.0), 'West Bengal': (140.0, 28.0)}


def check_states(state_name):
    if state_name in states:
        return states[state_name]
    else:
        return False


def total_number_of_states():
    return len(states)
