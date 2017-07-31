import sys
import os









def ArthGeo(args):

    
    args = args.split(',')

    list1 =[]
    
    total = 0

    
    


    for i in args:
        args1=int(i)
        list1.append(args1)

    Arth = [list1[i+1]-list1[i] for i in range(len(list1)-1)]

    for i in range(len(Arth)-1):
        if Arth[i] == Arth[i+1]:
            print ("Arth")
            
        elif Arth[i] != Arth[i+1]:

            for i in args:
                args1=int(i)
                list1.append(args1)

                Arth = [list1[i+1]/list1[i] for i in range(len(list1)-2)]
                
                for i in range(len(Arth)-1):
                    if Arth[i] == Arth[i+1]:
                        return (print("Geo"))
        else:
            return 0
            
                    
           

                    
                    

    
            
        
        






        

        
    #print(sum(list))

    






ArthGeo('2,6,168,58')


ArthGeo('1,2,3')








