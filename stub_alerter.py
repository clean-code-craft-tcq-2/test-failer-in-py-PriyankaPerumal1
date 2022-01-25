
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    if(celcius < float(100)):
      return 200
    else:
      return 500
