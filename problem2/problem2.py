def date_format(date):
    mm, dd, yyyy = date.split('/')
    return f"{yyyy}-{mm.zfill(2)}-{dd.zfill(2)}"