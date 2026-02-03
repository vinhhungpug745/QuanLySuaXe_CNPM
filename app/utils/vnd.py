def vnd(value):
    try:
        return "{:,.0f}".format(value)
    except:
        return "0"