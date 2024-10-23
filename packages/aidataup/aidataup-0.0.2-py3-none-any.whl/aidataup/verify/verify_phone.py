import phonenumbers
import re

#----- For parse phone number
def phonenum(code,phone):
    y = phonenumbers.parse(phone, code)
    return phonenumbers.is_possible_number(y),phonenumbers.is_valid_number(y)

#----- For mobile in Thailand
def profile_mobile_thai(mobileno_th):
    mobileno_th=str(mobileno_th)
    mobileno_th = mobileno_th.replace(" ", "")
    mobileno_th = mobileno_th.replace("-", "")
    if len(mobileno_th) == 10 :
        if re.findall("[0][8|9|6][0-9]{8}", mobileno_th):
            if mobileno_th.count("0") >= 8:
                return False
            if mobileno_th.count("9") >= 8:
                return False
            y=phonenum("TH", mobileno_th)
            if y[0] == True and y[1] == True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False 

#----- For telephone in Thailand
def profile_telp_thai(telp_th):
    telp_th = str(telp_th)
    main_number, _, extension = telp_th.partition("-")
    main_number = main_number.replace(" ", "").replace("-", "")
    telp_th = main_number + ("-" + extension if extension else "")

    if len(main_number) == 9: 
        if re.findall("[0][2|3|4|5|7][0-9]{7}", main_number):
            if main_number.count("0") >= 7:
                return False
            if main_number.count("9") >= 7:
                return False
            y = phonenum("TH", main_number)
            if y[0] == True and y[1] == True:
                return True 
            else:
                return False
        else:
            return False
    else:
        return False

#----- Verify telephone and mobile number in Thailand
def verify_mobile_number(mobileno):
    result = profile_mobile_thai(mobileno)
    if not result:
        result = profile_telp_thai(mobileno)
    return result

