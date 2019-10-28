print ("\033c") #console ro clear mikone !!!!
try:
    k = int(input("'K' Ra Vared Konid :"))
except NameError:
    print("Lotfan ADAD Vared Konid!")
else:    
    if k >= 1 and k <= 100 :
        mod = divmod(k,2)
        x = mod[1]
        if x is 0 :
            print("Payin Barare")
        else :
            print("Bala Barare")
    else :
        print("invalid number!")
        exit