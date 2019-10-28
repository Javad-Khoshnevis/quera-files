#By Javad Khoshnevis
#Github : Javad-Khoshnevis
#------------------------------------------------

print ("\033c") #console ro clear mikone !!!!
while 1 :
    try:
        k = int(input("'K' Ra Vared Konid :"))
    except ValueError:
        print("Lotfan ADAD Vared Konid!")
    except NameError :
        print("Lotfan ADAD Vared Konid!")
    except SyntaxError :
        print("Lotfan ADAD Vared Konid!")
    except TypeError :
        print("Lotfan ADAD Vared Konid!")
    else:    
        if k >= 1 and k <= 100 :
            mod = divmod(k,2)
            x = mod[1]
            if x is 0 :
                print("Payin Barare")
                break
            else :
                print("Bala Barare")
                break
        else :
            print("invalid number!")

#------------------------------------------------
#By Javad Khoshnevis
#Github : Javad-Khoshnevis