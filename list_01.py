
def get_month_name(wee):
    Month = [ "Jan","Feb" ,"March","Apr" ,"May", "June","July","Sep"," Oct" ,"Nov" ,"Dec"]
    return print(Month[wee-1])


while True:
    score = int(input( "Please Key input ===="))
    if ( score < 12  ):
        get_month_name(score)
    else:
        print (" Please input again" )
