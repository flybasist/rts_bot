def checkuser(userid, vipuser):

    if userid not in vipuser:
        vip = 0
    else:
        vip = 100
    return(vip)

def checkvacuumcleaner(userid, vipuser):

    if userid not in vipuser:
        vip = 0
    else:
        vip = 1
    return(vip)
