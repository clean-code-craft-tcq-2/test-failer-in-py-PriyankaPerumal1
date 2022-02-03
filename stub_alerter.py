def network_ok():
    return 1

def network_not_ok():
    return 0

def network_alert_stub(celcius, network_func):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    if(network_func()):
      return 200
    else:
      return 500
