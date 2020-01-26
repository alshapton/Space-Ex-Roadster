import inflect

AU_KM = 149597871
AU_MI = 92955807

def km_to_au(km):
    return km / AU_KM  

def mi_to_au(mi):
    return mi / AU_MI

def au_to_km(au):
    return au * AU_KM  

def au_to_mi(au):
    return au * AU_MI  

def num_to_month(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[month-1]    

def convert_date_to_speech(longlaunchdateutc="No date",fmt="short"):
    p = inflect.engine()
    
    if (longlaunchdateutc == "No date"):
        return longlaunchdateutc
    # 2018-02-06T20:45:00.000Z

    launchyear  = p.number_to_words(int(longlaunchdateutc[0:4]))
    launchmonth = num_to_month(int(longlaunchdateutc[6:7]))
    launchday   = p.ordinal(int(longlaunchdateutc[9:10]))
    
    launchhour  = p.number_to_words(int(longlaunchdateutc[11:13]))
    if (int(longlaunchdateutc[11:13]) < 10):
        launchhour = "oh " + launchhour
        
    launchmin  =  p.number_to_words(int(longlaunchdateutc[14:16]))
    if (int(longlaunchdateutc[14:16]) < 10):
        launchmin = "oh " + launchmin
    
    launchsec   = p.number_to_words(longlaunchdateutc[17:18])
    launchtz    = "You Tee See"
    
    if (fmt == "long"):
        # Long stuff 
        launchdatetime = launchday + " of " + launchmonth + " " + launchyear + " at " + launchhour + " " + launchmin + " hours and " + launchsec + " seconds " + launchtz
    
    if (fmt == "short"):
        # Short stuff 
        
        launchdatetime = launchday + " of " + launchmonth + " " + launchyear 
        
    return launchdatetime