#program name: Assignment Group7
#created by: Lee Shu Yan, Duke Chuah Erzhu, Liow Pei Yu, Loke Weng Yan, Ker Ding Wei, Loh Kah Ho
#modified by: Ker Ding Wei, Loh Kah Ho, Lee Shu Yan
#purpose: to check the shortfall of ingredients
#date: 16/12/2021


import datetime as dt
g_currD = dt.date.today()



# Main Menu
def menu():
    import os
    os.system("cls")                                                           #clear to look more tidy 
    #print main menu for user to choose option
    print("\t****************************************************************")  
    print("\t|            ^_^ WELCOME TO DIY HOMEBREAD BAKERY ^_^           |")
    print("\t****************************************************************")
    print("\t       ::Material Planning System" + "( Datetime : %s)" % g_currD) #import date
    print()
    print("\tEnter <1> to Ingredients/Materials Maintenance")
    print("\tEnter <2> to Maintain Recipes")
    print("\tEnter <3> to Create Requirement/Orders ")
    print("\tEnter <4> to Generate Materials Requirements Plan")
    print("\tEnter <0> to Quit")
    print("\n" * 2)
    opt=input("Select Your Option                    >>") #for user to choose either 1,2,3 or 4
    mainProg(opt) # move to the option that according to the user's type



def IM():
    import os   #for clear screen purpose

    def chkFloat(FLOAT):
        isFloat=True
        try:
            float(FLOAT)
        except:
            isFloat=False      #for chkFloat() and chkInt()
        return isFloat         #to check if the entered ingredients' quantity
                                 #is a real number (either a float or an integer)
    def chkInt(INTEGER):
        isInt=True
        try:
            int(INTEGER)
        except:
            isInt=False
        return isInt
            
    def ingDisplay():   #organize and display ingredients on screen
        f1=open("assgnMenu.txt","r")
        f1Lines=f1.read()
        print(f1Lines)                   
        f2=open("Ingredients.txt","r")                 
        f2Lines=f2.readlines()
        for i in range(len(f2Lines)):
            lst1=f2Lines[i].strip("\n").split("|")
            print("\t%-34s%2s%29s"%(lst1[0],lst1[1],lst1[2]))
        print("\t"+"-"*65)

    ing=[] #create an empty list to append ingredients' names from text file into it (always an empty file unless append smtg into it)

    def ingLst():           #open text file and append ingredients' names into ing (list)
        f1=open("Ingredients.txt","r")  #for checking purpose 
        f1Lines=f1.readlines()          #check if entered ingredient already exist or not
        f1.close()                      #doesn't affect the content in Ingredients.txt
        for linesNum in f1Lines:
            lineLst=linesNum.strip("\n").split("|")
            ing.append(lineLst[0])
                    
    def addIng():    #add-ingredient function
        print("\tIngredients List Maintenance -------> Add Ingredients")
        print("\t"+"-"*53)
        loop=True
        step=1
        while loop:
            if step==1:
                ingLst()  #insert ingredients' names into ing
                ingName=input("\tEnter Ingredient          <Q>uit >>>> ").upper()  #user required to input name of new ingredient
                if ingName=="Q":
                    loop=False
                elif ingName in ing:
                    print("\tTHE ENTERED INGREDIENT IS ALREADY EXIST -> PLEASE REENTER")  #must add a new ingredient                
                else:
                    step=2 #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:
                ingUOM=input("\tEnter UOM (g,kg,ml,l)     <Q>uit >>>> ")  #user required to input the UOM of new ingredient
                if ingUOM.upper()=="Q":
                    loop=False
                elif not ingUOM.lower() in ["g","kg","ml","l"]:
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")  #validation: reject values other than g,kg,ml,l
                else:
                    step=3 #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                ingQty=input("\tEnter quantity            <Q>uit >>>> ") #user required to input quantity of new ingredient
                if ingQty.upper()=="Q":
                    loop=False                
                elif chkFloat(ingQty)==False and chkInt(ingQty)==False:     #reject if ingQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:          #ingQty is a real number and can be accepted
                    step=4

            if step==4:
                    print()
                    addCfm=input("\tpress ENTER to confirm adding this ingredient\n\tREMINDER: this action cannot be undone  <B>ack >>>> ")
                    if addCfm.upper()=="B":
                        os.system("cls")                                            #user required to confirm updating the input values
                        ingDisplay()
                        print("\tIngredients List Maintenance -------> Add Ingredients")
                        print("\t"+"-"*53)
                        step=1  #if halfway, user do not want to update it anymore/input the wrong value/any error exist --> back to step 1
                    elif addCfm=="":   #user confirm adding by pressing ENTER ("")
                        ingQty="%.2f"%float(ingQty)         # 2 d.p for all entered quantity, more tidy                   
                        f=open("Ingredients.txt","a+")
                        ingUpd="|".join([ingName,ingUOM,ingQty])+"\n"   #join to become "ingName|ingUOM|ingQty" to be stored in text file
                        f.write(ingUpd)  #added new input values to text file
                        f.close()
                        print("\tINGREDIENT UPDATED AND RECORDED")
                        input("\tpress ENTER to continue")
                        loop=False       #back to Ingredients Maintenance page
                    else:
                        print("\tERROR")

    def delIng():  #delete-ingredient function
        print("\tIngredients List Maintenance -------> Delete Ingredients")
        print("\t"+"-"*56)
        loop=True
        step=1
        while loop:        
            if step==1:
                ingLst()  #insert ingredients' names into ing
                ingName=input("\tEnter Ingredient          <Q>uit >>>> ").upper()   #user input ingredient name that want to be deleted
                if ingName=="Q":
                    loop=False
                elif not ingName in ing:                                                  #if input ingredient's name not in ing
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't delete an ingredient that doesn't exist            
                else:     #entered ingredient exist and can be deleted
                    step=2

            if step==2:
                print()
                delCfm=input("\tpress ENTER to confirm deleting this ingredient\n\tREMINDER: this action cannot be undone  <B>ack >>>> ")
                if delCfm.upper()=="B":                                  #user need to confirm deleting the selected ingredient
                    os.system("cls")
                    ingDisplay()
                    print("\tIngredients List Maintenance -------> Delete Ingredients")
                    print("\t"+"-"*56)
                    step=1      #if halfway, user do not want to delete it anymore/chooses the wrong ingredient/any error exist 
                elif delCfm=="":                                                                   #back to enter ingredient name
                    f=open("Ingredients.txt","r")
                    lines=f.readlines()  #read contents in Ingredients.txt into a list   
                    f.close()
                    f=open("Ingredients.txt","w")  #rewrite Ingredients.txt                  
                    for line in lines:
                        if line.strip("\n").split("|")[0]!=ingName:  
                            f.write(line)       #only rewrite those lines that don't include the ingredient that user want to be deleted
                    f.close()
                    print("\tSELECTED INGREDIENT DELETED")
                    input("\tpress ENTER to continue")
                    loop=False            #back to Ingredients Maintenance page
                else:
                    print("\tERROR")

    def modIng():    #modify-ingredient function
        print("\tIngredients List Maintenance -------> Modify Ingredients")
        print("\t"+"-"*56)
        loop=True
        step=1
        while loop:
            if step==1:
                ingLst()  #insert ingredients' names into ing
                ingName=input("\tEnter Ingredient          <Q>uit >>>> ").upper()   #user input ingredient name that want to be modified
                if ingName=="Q":
                    loop=False
                elif not ingName in ing:                                                  #if input ingredient's name not in ing
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't modify an ingredient that doesn't exist            
                else:
                    step=2   #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:                                                    #user required to input the new UOM of ingredient
                ingUOM=input("\tEnter new UOM (g,kg,ml,l) <Q>uit >>>> ")   #input back current UOM allowed
                if ingUOM.upper()=="Q":                                    #user might only want to modify the quantity 
                    loop=False                                             
                elif not ingUOM.lower() in ["g","kg","ml","l"]:                  #reject values other than g,kg,ml,l
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")
                else:
                    step=3   #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                ingQty=input("\tEnter new quantity        <Q>uit >>>> ")    #user required to input ingredient's quantity to be modified to
                if ingQty.upper()=="Q":
                    loop=False                
                elif chkFloat(ingQty)==False and chkInt(ingQty)==False:             #reject if ingQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:
                    step=4

            if step==4:
                print()
                modCfm=input("\tpress ENTER to confirm modifying this ingredient\n\tREMINDER: this action cannot be undone  <B>ack >>>> ")
                if modCfm.upper()=="B":                                         #user need to confirm modifying the selected ingredient
                    os.system("cls")
                    ingDisplay()
                    print("\tIngredients List Maintenance -------> Modify Ingredients")
                    print("\t"+"-"*56)
                    step=1      #if halfway, user do not want to modify it anymore/input the wrong value/any error exist --> back to step 1
                elif modCfm=="":   #user confirm modifying by pressing ENTER ("")
                    ingQty="%.2f"%float(ingQty)     # 2 d.p.
                    f=open("Ingredients.txt","r+")
                    lines=f.readlines()  #read contents in Ingredients.txt into a list
                    f.seek(0)  #cursor back to starting position
                    ingUpd="|".join([ingName,ingUOM,ingQty])+"\n"   #join to become "ingName|ingUOM|ingQty" to be stored in text file
                    for line in lines:
                        if line.strip("\n").split("|")[0]==ingName:
                            f.write(ingUpd) #if line contains the ingredient name that want to be modified, write ingUpd(modified version)
                        else:
                            f.write(line)   #if line don't contain the ingredient name that want to be modified, write back original line 
                    f.truncate()     #clear all lines underneath the rewrited lines
                    f.close()
                    print("\tSELECTED INGREDIENT MODIFIED")
                    input("\tpress ENTER to continue")
                    loop=False     #back to Ingredients Maintenance page
                else:
                    print("\tERROR")
                                            
    def maintIng():     #combine add, delete, modify functions into 1 page
        loop=True               #whole Ingredient Maintenance function to be added to Main Menu
        step=1       
        while loop:
            if step==1:
                os.system("cls")   #clear screen to be more tidy
                ingDisplay()
                opt=input("\t<A>dd  <M>od  <D>el  <Q>uit  >> ")  #options to be choosen from
                print()
                if opt.upper()=="Q":
                    loop=False
                    menu()
                elif opt.upper()=="A":    #if user enter "A", callout addIng() function
                    addIng()
                elif opt.upper()=="D":    #if user enter "D", callout delIng() function
                    delIng()
                elif opt.upper()=="M":    #if user enter "M", callout modIng() function
                    modIng()
                else:
                    input("\terror in option entered --> press ENTER to continue")
                    step=1    #entered option invalid, back to reenter option
                  
    maintIng()


def MR():

    def chkFloat(FLOAT):
        isFloat=True
        try:
            float(FLOAT)
        except:
            isFloat=False      #for chkFloat() and chkInt()
        return isFloat         #to check if the entered ingredients' quantity
                                 #is a real number (either a float or an integer)
    def chkInt(INTEGER):
        isInt=True
        try:
            int(INTEGER)
        except:
            isInt=False
        return isInt



    def toraB():              #display ingredients of tora bread
        print("\t"+"-"*64)
        print("\tTora Bread")
        print("\t"+"-"*64)
        print("\tIngredient(s)     \tUnit/UOM     \tQuantity")
        print("\t"+"-"*13+"\t\t"+"-"*9+"\t"+"-"*9)
        tb=open("toraBread.txt","r")        
        tbLines=tb.readlines()
        for t in range (len(tbLines)):
            lst1=tbLines[t].strip("\n").split("|")
            print("\t%-25s%2s%18.1f"%(lst1[0],lst1[1],float(lst1[2])))
        print("\t"+"-"*64)
        opt=input("\t<A>dd  <M>od  <D>el  <Q>uit  >> ")
        print()
        if opt.upper()=="Q":
            print("\tExiting system")
            ingred()
        elif opt.upper()=="A":      #add new ingredient to tora bread
            addTb()
        elif opt.upper()=="D":      #delete exist ingredient from tora bread
            delTb()
        elif opt.upper()=="M":      #delete exist ingredient from tora bread
            modTb()
        else:
            input("\terror in option entered.Please ENTER to continue ")

    tbread=[]

    def tbLst():           #open text file and append ingredients' names into tbread (list)
        tb=open("toraBread.txt","r")
        tbLines=tb.readlines()          #check if entered ingredient already exist or not
        tb.close()                      #doesn't affect the content in toraBread.txt
        for linesNum in tbLines:
            lineLst=linesNum.strip("\n").split("|")
            tbread.append(lineLst[0])
            
    def addTb():    
        print("\tTora Bread -------------------------> Add Ingredients")
        print("\t-----------------------------------------------------")
        loop=True
        step=1
        while loop:
            if step==1:
                tbLst()  #insert ingredients' names into tbread
                addName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user required to input name of new ingredient
                if addName.upper()=="Q":
                    toraB()
                elif addName in tbread:
                    print("\tTHE ENTERED INGREDIENT IS ALREADY EXIST ")
                    toraB()
                else:
                    step=2 #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:
                addUOM=input("\tEnter UOM (g,kg,ml,l)     <Q>uit >>>> ")  #user required to input the UOM of new ingredient
                if addUOM.upper()=="Q":
                    toraB()
                elif not addUOM.lower() in ["g","kg","ml","l"]:
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")  #validation: reject values other than g,kg,ml,l
                else:
                    step=3 #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                addQty=input("\tEnter quantity            <Q>uit >>>> ") #user required to input quantity of new ingredient
                if addQty.upper()=="Q":
                    toraB()               
                elif chkFloat(addQty)==False and chkInt(addQty)==False:     #reject if addQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:          #addQty is a real number and can be accepted
                    addQty="%.1f"%float(addQty)         # 1 d.p for all entered quantity, more tidy                   
                    tb=open("toraBread.txt","a+")
                    addUpd="|".join([addName,addUOM,addQty])+"\n"  #join to become "addName|addUOM|addQty" to be stored in text file
                    tb.write(addUpd)  #added new input values to text file
                    tb.close()
                    print("\tINGREDIENT UPDATED AND RECORDED")
                    toraB()       

    def delTb():
        print("\tTora Bread  -------------------------> Delete Ingredients")
        print("\t--------------------------------------------------------")
        loop=True
        step=1
        while loop:        
            if step==1:
                tbLst()  #insert ingredients' names into tbread
                delName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user input ingredient name that want to be deleted
                if delName.upper()=="Q":
                    toraB()
                elif not delName in tbread:                                                  #if input ingredient's name not in tbread
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't delete an ingredient that doesn't exist            
                elif delName in tbread:     #entered ingredient exist and can be deleted         
                    tb=open("toraBread.txt","r")
                    tbLines=tb.readlines() 
                    tb.close()
                    tb=open("toraBread.txt","w")#rewrite toraBread.txt                  
                    for line in tbLines:
                        if line.strip("\n").split("|")[0]!=delName:  
                            tb.write(line)       #only rewrite those lines that don't include the ingredient that user want to be deleted
                    tb.close()
                    print("\tSELECTED INGREDIENT DELETED")
                    toraB()      

    def modTb():
        print("\tTora Bread -------------------------> Modify Ingredients")
        print("\t--------------------------------------------------------")
        loop=True
        step=1
        while loop:
            if step==1:
                tbLst()  #insert ingredients' names into tbread
                modName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user input ingredient name that want to be modified
                if modName.upper()=="Q":
                    toraB()
                elif not modName in tbread:                                                  #if input ingredient's name not in tbread
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't modify an ingredient that doesn't exist            
                else:
                    step=2   #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:                                                    #user required to input the new UOM of ingredient
                modUOM=input("\tEnter new UOM (g,kg,ml,l) <Q>uit >>>> ")   #input back current UOM allowed
                if modUOM.upper()=="Q":                                    #user might only want to modify the quantity 
                    toraB()                                             
                elif not modUOM.lower() in ["g","kg","ml","l"]:                  #reject values other than g,kg,ml,l
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")
                else:
                    step=3   #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                modQty=input("\tEnter new quantity        <Q>uit >>>> ")    #user required to input ingredient's quantity to be modified to
                if modQty.upper()=="Q":
                    toraB()               
                elif chkFloat(modQty)==False and chkInt(modQty)==False:             #reject if modQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:
                    modQty="%.1f"%float(modQty)     # 1 d.p.
                    tb=open("toraBread.txt","r+")
                    tbLines=tb.readlines()   #read contents in toraBread.txt into a list
                    tb.seek(0)  #cursor back to starting position
                    modUpd="|".join([modName,modUOM,modQty])+"\n"   #join to become "modName|modUOM|modQty" to be stored in text file
                    for line in tbLines:
                        if line.strip("\n").split("|")[0]==modName:
                            tb.write(modUpd) #if line contains the ingredient name that want to be modified, write modUpd(modified version)
                        else:
                            tb.write(line)   #if line don't contain the ingredient name that want to be modified, write back original line 
                    tb.truncate()     #clear all lines underneath the rewrited lines
                    tb.close()
                    print("\tSELECTED INGREDIENT MODIFIED")
                    toraB()

        
    def cheeseL():  #display ingredients of cheese loaf
        print("\t"+"-"*64)
        print("\tCheese Loaf")
        print("\t"+"-"*64)
        print("\tIngredient(s)     \tUnit/UOM     \tQuantity")
        print("\t"+"-"*13+"\t\t"+"-"*9+"\t"+"-"*9)
        c1=open("cheeseLoaf.txt","r")
        c1Lines=c1.readlines()
        for l in range(len(c1Lines)):
            lst2=c1Lines[l].strip("\n").split("|")
            print("\t%-25s%2s%18.1f"%(lst2[0],lst2[1],float(lst2[2])))
        print("\t"+"-"*64)
        opt=input("\t<A>dd  <M>od  <D>el  <Q>uit  >> ")
        print()
        if opt.upper()=="Q":
            print("\tExiting system")
            print()
            ingred()
        elif opt.upper()=="A":  #add new ingredient to cheese loaf
            addC1()
        elif opt.upper()=="D":  #delete exist ingredient from cheese loaf
            delC1()
        elif opt.upper()=="M":  #modify exist ingredient from cheese loaf
            modC1()
        else:
            input("\terror in option entered.Plese ENTER to continue")

    cloaf=[]

    def c1Lst():           #open text file and append ingredients' names into cloaf (list)
        c1=open("cheeseLoaf.txt","r")
        c1Lines=c1.readlines()          #check if entered ingredient already exist or not
        c1.close()                      #doesn't affect the content in cheeseLoaf.txt
        for linesNum in c1Lines:
            lineLst=linesNum.strip("\n").split("|")
            cloaf.append(lineLst[0])

    def addC1():
        print("\tCheese Loaf ------------------------> Add Ingredients")
        print("\t-----------------------------------------------------")
        loop=True
        step=1
        while loop:
            if step==1:
                c1Lst()  #insert ingredients' names into cloaf
                addName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user required to input name of new ingredient
                if addName.upper()=="Q":
                    cheeseL()
                elif addName in cloaf:
                    print("\tTHE ENTERED INGREDIENT IS ALREADY EXIST ")
                    cheeseL()
                else:
                    step=2 #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:
                addUOM=input("\tEnter UOM (g,kg,ml,l)     <Q>uit >>>> ")  #user required to input the UOM of new ingredient
                if addUOM.upper()=="Q":
                    cheeseL()
                elif not addUOM.lower() in ["g","kg","ml","l"]:
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")  #validation: reject values other than g,kg,ml,l
                else:
                    step=3 #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                addQty=input("\tEnter quantity            <Q>uit >>>> ") #user required to input quantity of new ingredient
                if addQty.upper()=="Q":
                    cheeseL()               
                elif chkFloat(addQty)==False and chkInt(addQty)==False:     #reject if addQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:          #addQty is a real number and can be accepted
                    addQty="%.1f"%float(addQty)         # 1 d.p for all entered quantity, more tidy                   
                    c1=open("cheeseLoaf.txt","a+")
                    addUpd="|".join([addName,addUOM,addQty])+"\n"  #join to become "addName|addUOM|addQty" to be stored in text file
                    c1.write(addUpd)  #added new input values to text file
                    c1.close()
                    print("\tINGREDIENT UPDATED AND RECORDED")
                    cheeseL()      

    def delC1():
        print("\tCheese Loaf  -----------------------> Delete Ingredients")
        print("\t--------------------------------------------------------")
        loop=True
        step=1
        while loop:        
            if step==1:
                c1Lst()  #insert ingredients' names into cloaf
                delName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user input ingredient name that want to be deleted
                if delName.upper()=="Q":
                    cheeseL()
                elif not delName in cloaf:                                                  #if input ingredient's name not in cloaf
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't delete an ingredient that doesn't exist            
                elif delName in cloaf:     #entered ingredient exist and can be deleted         
                    c1=open("cheeseLoaf.txt","r")
                    c1Lines=c1.readlines() 
                    c1.close()
                    c1=open("cheeseLoaf.txt","w")#rewrite cheeseLoaf.txt                  
                    for line in c1Lines:
                        if line.strip("\n").split("|")[0]!=delName:  
                            c1.write(line)       #only rewrite those lines that don't include the ingredient that user want to be deleted
                    c1.close()
                    print("\tSELECTED INGREDIENT DELETED")
                    cheeseL()      

    def modC1():
        print("\tCheese Loaf ------------------------> Modify Ingredients")
        print("\t--------------------------------------------------------")
        loop=True
        step=1
        while loop:
            if step==1:
                c1Lst()  #insert ingredients' names into cloaf
                modName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user input ingredient name that want to be modified
                if modName.upper()=="Q":
                    cheeseL()
                elif not modName in cloaf:                                                  #if input ingredient's name not in cloaf
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't modify an ingredient that doesn't exist            
                else:
                    step=2   #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:                                                    #user required to input the new UOM of ingredient
                modUOM=input("\tEnter new UOM (g,kg,ml,l) <Q>uit >>>> ")   #input back current UOM allowed
                if modUOM.upper()=="Q":                                    #user might only want to modify the quantity 
                    cheeseL()                                             
                elif not modUOM.lower() in ["g","kg","ml","l"]:                  #reject values other than g,kg,ml,l
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")
                else:
                    step=3   #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                modQty=input("\tEnter new quantity        <Q>uit >>>> ")    #user required to input ingredient's quantity to be modified to
                if modQty.upper()=="Q":
                    cheeseL()               
                elif chkFloat(modQty)==False and chkInt(modQty)==False:             #reject if modQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:
                    modQty="%.1f"%float(modQty)     # 1 d.p.
                    c1=open("cheeseLoaf.txt","r+")
                    c1Lines=c1.readlines()   #read contents in cheeseLoaf.txt into a list
                    c1.seek(0)  #cursor back to starting position
                    modUpd="|".join([modName,modUOM,modQty])+"\n"   #join to become "modName|modUOM|modQty" to be stored in text file
                    for line in c1Lines:
                        if line.strip("\n").split("|")[0]==modName:
                            c1.write(modUpd) #if line contains the ingredient name that want to be modified, write modUpd(modified version)
                        else:
                            c1.write(line)   #if line don't contain the ingredient name that want to be modified, write back original line 
                    c1.truncate()     #clear all lines underneath the rewrited lines
                    c1.close()
                    print("\tSELECTED INGREDIENT MODIFIED")
                    cheeseL()
        
    def custardR(): #display ingredients of custard cream roll
        print("\t"+"-"*64)
        print("\tCustard Cream Roll")
        print("\t"+"-"*64)
        print("\tIngredient(s)     \tUnit/UOM     \tQuantity")
        print("\t"+"-"*13+"\t\t"+"-"*9+"\t"+"-"*9)
        c2=open("custardRoll.txt","r")
        c2Lines=c2.readlines()
        for r in range(len(c2Lines)):
            lst3=c2Lines[r].strip("\n").split("|")
            print("\t%-25s%2s%18.1f"%(lst3[0],lst3[1],float(lst3[2])))
        print("\t"+"-"*64)
        opt=input("\t<A>dd  <M>od  <D>el  <Q>uit  >> ")
        print()
        if opt.upper()=="Q":
            print("\tExiting system")
            ingred()
        elif opt.upper()=="A":  #add new ingredient to custard cream roll
            addC2()
        elif opt.upper()=="D":  #delete exist ingredient from custard cream roll
            delC2()
        elif opt.upper()=="M":  #modify exist ingredient from custard cream roll
            modC2()
        else:
            input("\terror in option entered.Please ENTER to continue")

    croll=[]

    def c2Lst():           #open text file and append ingredients' names into croll (list)
        c2=open("custardRoll.txt","r")
        c2Lines=c2.readlines()          #check if entered ingredient already exist or not
        c2.close()                      #doesn't affect the content in custardRoll.txt
        for linesNum in c2Lines:
            lineLst=linesNum.strip("\n").split("|")
            croll.append(lineLst[0])

    def addC2():
        print("\tCustard Cream Roll -----------------> Add Ingredients")
        print("\t-----------------------------------------------------")
        loop=True
        step=1
        while loop:
            if step==1:
                c2Lst()  #insert ingredients' names into croll
                addName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user required to input name of new ingredient
                if addName.upper()=="Q":
                    custardR()
                elif addName in croll:
                    print("\tTHE ENTERED INGREDIENT IS ALREADY EXIST ")
                    custardR()
                else:
                    step=2 #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:
                addUOM=input("\tEnter UOM (g,kg,ml,l)     <Q>uit >>>> ")  #user required to input the UOM of new ingredient
                if addUOM.upper()=="Q":
                    custardR()
                elif not addUOM.lower() in ["g","kg","ml","l"]:
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")  #validation: reject values other than g,kg,ml,l
                else:
                    step=3 #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                addQty=input("\tEnter quantity            <Q>uit >>>> ") #user required to input quantity of new ingredient
                if addQty.upper()=="Q":
                    custardR()               
                elif chkFloat(addQty)==False and chkInt(addQty)==False:     #reject if addQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:          #addQty is a real number and can be accepted
                    addQty="%.1f"%float(addQty)         # 1 d.p for all entered quantity, more tidy                   
                    c2=open("custardRoll.txt","a+")
                    addUpd="|".join([addName,addUOM,addQty])+"\n"  #join to become "addName|addUOM|addQty" to be stored in text file
                    c2.write(addUpd)  #added new input values to text file
                    c2.close()
                    print("\tINGREDIENT UPDATED AND RECORDED")
                    custardR()      

    def delC2():
        print("\tCustard Cream Roll  ----------------> Delete Ingredients")
        print("\t--------------------------------------------------------")
        loop=True
        step=1
        while loop:        
            if step==1:
                c2Lst()  #insert ingredients' names into croll
                delName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user input ingredient name that want to be deleted
                if delName.upper()=="Q":
                    custardR()
                elif not delName in croll:                                                  #if input ingredient's name not in croll
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't delete an ingredient that doesn't exist            
                elif delName in croll:     #entered ingredient exist and can be deleted         
                    c2=open("custardRoll.txt","r")
                    c2Lines=c2.readlines() 
                    c2.close()
                    c2=open("custardRoll.txt","w")#rewrite custardRoll.txt                  
                    for line in c2Lines:
                        if line.strip("\n").split("|")[0]!=delName:  
                            c2.write(line)       #only rewrite those lines that don't include the ingredient that user want to be deleted
                    c2.close()
                    print("\tSELECTED INGREDIENT DELETED")
                    custardR()     

    def modC2():
        print("\tCustard Crean Roll ------------------> Modify Ingredients")
        print("\t--------------------------------------------------------")
        loop=True
        step=1
        while loop:
            if step==1:
                c2Lst()  #insert ingredients' names into croll
                modName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user input ingredient name that want to be modified
                if modName.upper()=="Q":
                    custardR()
                elif not modName in croll:                                                  #if input ingredient's name not in croll
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't modify an ingredient that doesn't exist            
                else:
                    step=2   #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:                                                    #user required to input the new UOM of ingredient
                modUOM=input("\tEnter new UOM (g,kg,ml,l) <Q>uit >>>> ")   #input back current UOM allowed
                if modUOM.upper()=="Q":                                    #user might only want to modify the quantity 
                    custardR()                                             
                elif not modUOM.lower() in ["g","kg","ml","l"]:                  #reject values other than g,kg,ml,l
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")
                else:
                    step=3   #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                modQty=input("\tEnter new quantity        <Q>uit >>>> ")    #user required to input ingredient's quantity to be modified to
                if modQty.upper()=="Q":
                    custardR()               
                elif chkFloat(modQty)==False and chkInt(modQty)==False:             #reject if modQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:
                    modQty="%.1f"%float(modQty)     # 1 d.p.
                    c2=open("custardRoll.txt","r+")
                    c2Lines=c2.readlines()   #read contents in cheeseLoaf.txt into a list
                    c2.seek(0)  #cursor back to starting position
                    modUpd="|".join([modName,modUOM,modQty])+"\n"   #join to become "modName|modUOM|modQty" to be stored in text file
                    for line in c2Lines:
                        if line.strip("\n").split("|")[0]==modName:
                            c2.write(modUpd) #if line contains the ingredient name that want to be modified, write modUpd(modified version)
                        else:
                            c2.write(line)   #if line don't contain the ingredient name that want to be modified, write back original line 
                    c2.truncate()     #clear all lines underneath the rewrited lines
                    c2.close()
                    print("\tSELECTED INGREDIENT MODIFIED")
                    custardR()
        
    def burgerB():  #display ingredients of burger & hot-dog Bun
        print("\t"+"-"*64)
        print("\tBurger & Hot-dog Bun")
        print("\t"+"-"*64)
        print("\tIngredient(s)     \tUnit/UOM     \tQuantity")
        print("\t"+"-"*13+"\t\t"+"-"*9+"\t"+"-"*9)
        bb=open("burgerBun.txt","r")
        bbLines=bb.readlines()
        for b in range(len(bbLines)):
            lst4=bbLines[b].strip("\n").split("|")
            print("\t%-25s%2s%18.1f"%(lst4[0],lst4[1],float(lst4[2])))
        print("\t"+"-"*64)
        opt=input("\t<A>dd  <M>od  <D>el  <Q>uit  >> ")
        print()
        if opt.upper()=="Q":
            print("\tExiting system")
            ingred()
        elif opt.upper()=="A":  #add new ingredient to burger & hot-dog bun
            addBb()
        elif opt.upper()=="D":  #delete exist ingredient from burger & hot-dog bun
            delBb()
        elif opt.upper()=="M":  #modify exist ingredient from burger & hot-dog bun
            modBb()
        else:
            input("\terror in option entered.Please ENTER to continue")

    bbun=[]

    def bbLst():           #open text file and append ingredients' names into bBun (list)
        bb=open("burgerBun.txt","r")
        bbLines=bb.readlines()          #check if entered ingredient already exist or not
        bb.close()                      #doesn't affect the content in burgerBun.txt
        for linesNum in bbLines:
            lineLst=linesNum.strip("\n").split("|")
            bbun.append(lineLst[0])

    def addBb():
        print("\tBurger & Hot-dog Bun ---------------> Add Ingredients")
        print("\t-----------------------------------------------------")
        loop=True
        step=1
        while loop:
            if step==1:
                bbLst()  #insert ingredients' names into bBun
                addName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user required to input name of new ingredient
                if addName.upper()=="Q":
                    burgerB()
                elif addName in bbun:
                    print("\tTHE ENTERED INGREDIENT IS ALREADY EXIST ")
                    burgerB()
                else:
                    step=2 #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:
                addUOM=input("\tEnter UOM (g,kg,ml,l)     <Q>uit >>>> ")  #user required to input the UOM of new ingredient
                if addUOM.upper()=="Q":
                    burgerB()
                elif not addUOM.lower() in ["g","kg","ml","l"]:
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")  #validation: reject values other than g,kg,ml,l
                else:
                    step=3 #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                addQty=input("\tEnter quantity            <Q>uit >>>> ") #user required to input quantity of new ingredient
                if addQty.upper()=="Q":
                    burgerB()               
                elif chkFloat(addQty)==False and chkInt(addQty)==False:     #reject if addQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:          #addQty is a real number and can be accepted
                    addQty="%.1f"%float(addQty)         # 1 d.p for all entered quantity, more tidy                   
                    bb=open("burgerBun.txt","a+")
                    addUpd="|".join([addName,addUOM,addQty])+"\n"  #join to become "addName|addUOM|addQty" to be stored in text file
                    bb.write(addUpd)  #added new input values to text file
                    bb.close()
                    print("\tINGREDIENT UPDATED AND RECORDED")
                    burgerB()   

    def delBb():
        print("\tBurger & Hot-dog Bun  --------------> Delete Ingredients")
        print("\t--------------------------------------------------------")
        loop=True
        step=1
        while loop:        
            if step==1:
                bbLst()  #insert ingredients' names into bBun
                delName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user input ingredient name that want to be deleted
                if delName.upper()=="Q":
                    burgerB()
                elif not delName in bbun:                                                  #if input ingredient's name not in ing
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't delete an ingredient that doesn't exist            
                elif delName in bbun:     #entered ingredient exist and can be deleted         
                    bb=open("burgerBun.txt","r")
                    bbLines=bb.readlines() 
                    bb.close()
                    bb=open("burgerBun.txt","w")#rewrite burgerBun.txt                  
                    for line in bbLines:
                        if line.strip("\n").split("|")[0]!=delName:  
                            bb.write(line)       #only rewrite those lines that don't include the ingredient that user want to be deleted
                    bb.close()
                    print("\tSELECTED INGREDIENT DELETED")
                    burgerB()

    def modBb():
        print("\tBurger & Hot-dog Bun ---------------> Modify Ingredients")
        print("\t--------------------------------------------------------")
        loop=True
        step=1
        while loop:
            if step==1:
                bbLst()  #insert ingredients' names into ing
                modName=input("\tEnter Ingredient          <Q>uit >>>> ")  #user input ingredient name that want to be modified
                if modName.upper()=="Q":
                    burgerB()
                elif not modName in bbun:                                                  #if input ingredient's name not in ing
                    print("\tTHE ENTERED INGREDIENT DOES NOT EXIST -> PLEASE REENTER")    #can't modify an ingredient that doesn't exist            
                else:
                    step=2   #if meet criteria, proceed to step 2, if not, then remain in this loop

            if step==2:                                                    #user required to input the new UOM of ingredient
                modUOM=input("\tEnter new UOM (g,kg,ml,l) <Q>uit >>>> ")   #input back current UOM allowed
                if modUOM.upper()=="Q":                                    #user might only want to modify the quantity 
                    burgerB()                                             
                elif not modUOM.lower() in ["g","kg","ml","l"]:                  #reject values other than g,kg,ml,l
                    print("\tTHE ENTERED UOM IS NOT VALID -> PLEASE REENTER")
                else:
                    step=3   #if meet criteria, proceed to step 3, if not, then remain in this loop

            if step==3:
                modQty=input("\tEnter new quantity        <Q>uit >>>> ")    #user required to input ingredient's quantity to be modified to
                if modQty.upper()=="Q":
                    burgerB()                
                elif chkFloat(modQty)==False and chkInt(modQty)==False:             #reject if modQty is not a real number
                    print("\tTHE ENTERED QUANTITY IS NOT VALID -> PLEASE REENTER")
                else:
                    modQty="%.1f"%float(modQty)     # 2 d.p.
                    bb=open("burgerBun.txt","r+")
                    bbLines=bb.readlines()   #read contents in burgerBun.txt into a list
                    bb.seek(0)  #cursor back to starting position
                    modUpd="|".join([modName,modUOM,modQty])+"\n"   #join to become "modName|modUOM|modQty" to be stored in text file
                    for line in bbLines:
                        if line.strip("\n").split("|")[0]==modName:
                            bb.write(modUpd) #if line contains the ingredient name that want to be modified, write modUpd(modified version)
                        else:
                            bb.write(line)   #if line don't contain the ingredient name that want to be modified, write back original line 
                    bb.truncate()     #clear all lines underneath the rewrited lines
                    bb.close()
                    print("\tSELECTED INGREDIENT MODIFIED")
                    burgerB()


    def ingred():   #user can add,modify and delete ingredients of recipes
        opt="C"
        loop=True   
        while opt!="Q":
            recipe()    #display recipe
            opt=input("\t<T>ora Bread  <C1>heese Loaf  <C2>ustard Cream Roll  \n\t<B>urger & Hot-dog Bun  <Q>uit  >>")
            print()
            if opt.upper()=="Q":    #back to recipe()
                print("\tExiting system")
                print()
                maintRec()
            elif opt.upper()=="T":  #add,modify and delete ingredients of tora bread
                toraB()
            elif opt.upper()=="C1": #add,modify and delete ingredients of cheese loaf
                cheeseL()
            elif opt.upper()=="C2": #add,modify and delete ingredients of custard cream roll
                custardR()
            elif opt.upper()=="B":  #add,modify and delete ingredients of burger & hot-dog bun
                burgerB()
            else:
                input("\terror in option entered.Please ENTER to continue")

                    
    def recipe():               #display recipes
        os.system("cls")  
        print("\t"+"-"*64)
        print("\tRecipe")
        print("\t"+"-"*64)
        f=open("recipes.txt","r")
        recipes=f.readlines()
        for i in range (len(recipes)):  
            lst=recipes[i].strip("\n").split("|")
            print("\t%s"%(lst[1]))
        print("\t"+"-"*64)

    rec=[]  #create an empty list to append recipes' names from text file into it (always an empty file unless append smtg into it)

    def recLst():#open text file and append recipes' names into ing (list) 
        f1=open("recipes.txt","r")  #for checking purpose 
        f1Lines=f1.readlines()          #check if entered ingredient already exist or not
        f1.close()                      #doesn't affect the content in recipes.txt
        for linesNum in f1Lines:
            lineLst=linesNum.strip("\n").split("|")
            rec.append(lineLst[1])

    def maintRec():
        opt="C"
        while opt!="Q":             #return to recipe()
            loop=False
            recipe()
            opt=input("\t<Q>uit  <I>ngredients>> ")
            print()
            if opt.upper()=="Q":
                print("\tExiting system")
                menu()
            elif opt.upper()=="I":
                ingred()                    #to add,modify and delete ingredients of recipe
            else:
                input("\terror in option entered.Please ENTER to continue")

    maintRec()





def CRO():

    import os 

    def chkInt(INTEGER):            #to check the quantity is an integer
        chkStatus=True
        try:
            int(INTEGER)
        except:
            chkStatus=False
        return chkStatus


    def orderDisplay():             #display the list of recipes and existing orders
        print("\n")
        f1=open("recipeH.txt","r")
        f1Lines=f1.read()
        print(f1Lines)
        f2=open("recipes.txt","r")  #display lists of recipes
        f2Lines=f2.readlines()
        for i in range(len(f2Lines)):
            lst1=f2Lines[i].strip("\n").split("|")
            print("\t%s. %-25s"%(lst1[0],lst1[1]))
        f3=open("orderH.txt","r")
        f3Lines=f3.read()
        print(f3Lines)
        f4=open("orders.txt","r")   #display lists of orders          
        f4Lines=f4.readlines()
        for i in range(len(f4Lines)):
            lst2=f4Lines[i].strip("\n").split("|")
            print("\t%-25s%-20s%15s"%(lst2[0],lst2[1],lst2[2]))
        print()
        print("\t"+"-"*64)


    order=[]                        #create a empty list for list of orders
    orderD=[]                       #create a empty list for lists of orders' descriptions


    def recipeLst():                #open text file to add the recipe
        f1=open("recipes.txt","r")
        f1Lines=f1.readlines()          
        f1.close()                      
        for linesNum in f1Lines:
            lineLst=linesNum.strip("\n")
            recipes.append(lineLst[0])


    def orderLst():                 #open text file to add,del and mod the orders
        f1=open("orders.txt","r")
        f1Lines=f1.readlines()          
        f1.close()                      
        for linesNum in f1Lines:
            lineLst=linesNum.strip("\n").split("|")
            order.append(lineLst[0])


    def orderDescripLst():          #open text file to add and mod the orders' descriptions
        f1=open("recipes.txt","r")
        f1Lines=f1.readlines()          
        f1.close()                      
        for linesNum in f1Lines:
            lineLst=linesNum.strip("\n").split("|")
            orderD.append(lineLst[1])


    def addOrder():                 #add new orders 
        print("\tOrder Requirement Plan >> ")
        loop=True
        step=1
        while loop:
            if step==1:
                orderLst()
                orderName=input("\tRecipe          <Q>uit >> ").upper()
                if orderName=="Q":
                    loop=False      
                elif orderName in order:
                    print("\tThe order already exist.")
                    error = input("\tPlease try it again by enter ENTER key. ")
                else:
                    step=2
                    
            #to make sure the input step 1 correct to continue step 2 and so on
            if step==2:
                orderDescrip=input("\tDescription     <Q>uit >> ").upper()
                if orderDescrip=="Q":
                    loop=False
                else:
                    step=3
                    
            if step==3:
                orderQty=input("\tQuantity        <Q>uit >> ")
                if orderQty=="Q":
                    loop=False
                elif chkInt(orderQty)==False:
                    print("\tThe quantity is not an integer.")
                    error = input("\tPlease try it again by enter ENTER key. ")
                else:
                    print()
                    #confirm adding the order
                    addCfm=input("\tEnter key to confirm adding this order\n \tREMINDER: This action cannot be undone  <B>ack >>>> ")
                    if addCfm.upper()=="B":
                        os.system("cls")
                        
                        orderDisplay()
                        print("\tOrder Requirement Plan >> ")
                        step=1
                        
                    elif addCfm=="":   
                        orderQty="%d"%int(orderQty)                           
                        f=open("orders.txt","a+")
                        orderAdd="|".join([orderName,orderDescrip,orderQty])+"\n"   
                        f.write(orderAdd)  
                        f.close()
                        print()
                        print("\tOrder added and recorded")
                        input("\tpress ENTER to continue")
                        loop=False       
                        

    def modOrder():                 #modify the existing orders
        print("\tOrder Requirement Plan >> ")
        loop=True
        step=1
        while loop:
            if step==1:
                orderLst()
                orderName=input("\tRecipe          <Q>uit >> ").upper()
                if orderName=="Q":
                    loop=False
                elif not orderName in order:
                    print("\tThe order does not exist.")
                    error = input("\tPlease try it again by enter ENTER key. ")          
                else:
                    step=2   

            #to make sure the input step 1 correct to continue step 2 and so on
            if step==2:                                                    
                orderDescrip=input("\tDescription     <Q>uit >> ").upper()   
                if orderDescrip=="Q":                                     
                    loop=False
                else:
                    step=3

            if step==3:
                orderQty=input("\tQuantity        <Q>uit >> ")
                if orderQty.upper()=="Q":
                    loop=False
                elif chkInt(orderQty)==False:
                    print("\tThe quantity is not an integer.")
                    error = input("\tPlease try it again by enter ENTER key. ")
                else:
                    print()
                    #confirm modifying the order
                    modCfm=input("\tEnter key to confirm modifying this order\n \tREMINDER: This action cannot be undone  <B>ack >>>> ")
                    if modCfm.upper()=="B":
                        os.system("cls")
                        orderDisplay()
                        print("\tOrder Requirement Plan >> ")
                        step=1
                    elif modCfm=="":   
                        orderQty="%d"%int(orderQty)
                        f=open("orders.txt","r+")
                        lines=f.readlines() 
                        f.seek(0)  
                        orderUpd="|".join([orderName,orderDescrip,orderQty])+"\n"   
                        for line in lines:
                            if line.strip("\n").split("|")[0]==orderName:
                                f.write(orderUpd) 
                            else:
                                f.write(line)
                        f.truncate()     #clear all lines underneath the rewrited lines
                        f.close()
                        print()
                        print("\tOrder modified and recorded")
                        input("\tpress ENTER to continue")
                        loop=False



    def delOrder():                 #delete the existing orders
        print("\tOrder Requirement Plan >> ")
        loop=True
        step=1
        while loop:
            if step==1:
                orderLst()
                orderName=input("\tRecipe          <Q>uit >> ").upper()
                if orderName=="Q":
                    loop=False
                elif not orderName in order:
                    print("\tThe order does not exist.")
                    error = input("\tPlease try it again by enter ENTER key. ")
                elif orderName in order:
                    print()
                    #confirm deleting the order
                    delCfm=input("\tEnter key to confirm deleting this order\n \tREMINDER: This action cannot be undone  <B>ack >>>> ")
                    if delCfm.upper()=="B":                                 
                        os.system("cls")
                        orderDisplay()
                        print("\tOrder Requirement Plan >> ")
                        step=1      
                    elif delCfm=="":                                                                
                        f=open("orders.txt","r")
                        lines=f.readlines()     
                        f.close()
                        f=open("orders.txt","w")                   
                        for line in lines:
                            if line.strip("\n").split("|")[0]!=orderName:  
                                f.write(line)       
                        f.close()
                        print()
                        print("\tOrder deleted and recorded")
                        input("\tpress ENTER to continue")
                        loop=False 

    def resOrder():                 #reseting all the existing orders
        #confirm reseting all the existing order
        resCfm=input("\tEnter key to confirm reseting all the existing order\n \tREMINDER: This action cannot be undone  <B>ack >>>> ")
        if resCfm.upper()=="B":                                 
            os.system("cls")
            orderDisplay()
            opt=input("\t<A>dd  <M>od  <D>el  <Q>uit  <R>esetFile  >> ") 
        else:
            f=open("orders.txt","r")
            lines=f.readlines()     
            f.close()
            f=open("orders.txt","w") 
            f.close()
            print()
            print("\tOrder reseted and recorded")
            input("\tpress ENTER to continue")


    def createRO():                 #function of add, mod, del, reset orders and quit the section in one page
        loop=True
        step=1
        while loop:
            if step==1:
                os.system("cls")   
                orderDisplay()
                opt=input("\t<A>dd  <M>od  <D>el  <Q>uit  <R>esetFile  >> ")  
                print()
                if opt.upper()=="Q":
                    loop=False
                    menu()
                elif opt.upper()=="A":    
                    addOrder()
                elif opt.upper()=="M":   
                    modOrder()
                elif opt.upper()=="D":
                    delOrder()
                elif opt.upper()=="R":
                    resOrder()
                else:
                    print("\tERROR option. Only letters A,M,D,Q,R are allowed. ")
                    error = input("\tPlease try it again by enter any keys. ")
                    step=1    
                  
                    
    createRO()



def GMRP():
    import os
    
    def chkShortFall(num):    #check is there a short fall
        chkStatus=True
        try:
            float(num)
        except:
            chkStatus=False
        return chkStatus

    def chkNewRecipe(num):    #check is there a new recipe
        chkStatus=True
        try:
            orderNumLst[num]
        except:
            chkStatus=False
        return chkStatus

    def Diff(li1, li2):       #get the list that include element exist in li1 but not in li2 or vice versa
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif


    def order():
        os.system("cls")
        import datetime as dt
        now=dt.datetime.now()
        date=now.strftime("%Y-%m-%d") #get the date of today


        print("\t"+" "*14,"Materials Requirement Plan run ("+date+")") #print title with date of today and decoration
        print("\t"+"_"*73)  #decoration
        print()
        print("\t"+"<>"*14+":Production Plan:"+"<>"*14)  #print the title and decoration
        print()

        order=open("orders.txt","r") #read orders.txt
        orderLst=order.readlines() #read order in list form
        for i in range(len(orderLst)):  
            planLst=orderLst[i].strip("\n").split("|")  #strip away "\n" and create plan list by spliting "|"
            recipes=planLst[0]  
            Description=planLst[1]
            orderNumber=planLst[2]
            print("\t"+f"{recipes:<27}{Description:<17}{orderNumber:>17}",end="") #to print  recipes, description of the order and number of order
            print()
        print()
        print("\t"+"-"*73)  #decoration
        print("\t"+"-"*73)

    order()



    def MRP():
        import os
        
        order=open("orders.txt","r")  #read orders.txt
        orderLst=order.readlines()    #read order in list form
        orderNumLst=[]
        recipeLst=[]
        for i in range(len(orderLst)):
            planLst=orderLst[i].strip("\n").split("|")
            orderNumber=planLst[2] #number of order
            orderNumLst.append(orderNumber) #append number of order into orderNumLst
            recipe=planLst[0]
            recipeLst.append(recipe)

            

        ingreLst=[]

        recipeBunLst=open("burgerBun.txt","r")   #read burgerBun.txt
        recipeBun=recipeBunLst.readlines()       #read recipe in burgerBun.txt in list form
        bunOrderNum=int(orderNumLst[recipeLst.index("BURGER & HOT-DOG BUN")])    #obtaining order number of Burger & Hot-Dog Bun
        bunRecipeLst=[]

        for lines in range(len(recipeBun)):
            bunIngreLst=[] #[ingreBun,demandBun,uomBun]
            ingreBun=recipeBun[lines].strip("\n").split("|")[0].upper() #obtaining ingredient to make Burger & Hot-Dog Bun
            demandBun=float(recipeBun[lines].strip("\n").split("|")[2])*bunOrderNum  #obtaining the demand of ingredient to make Burger & Hot-Dog Bun
            uomBun=recipeBun[lines].strip("\n").split("|")[1]   #obtaining ingredient's uom for Burger & Hot-Dog Bun
            bunIngreLst.append(ingreBun)
            bunIngreLst.append(demandBun)
            bunIngreLst.append(uomBun)
            bunRecipeLst.append(bunIngreLst)


        recipeLoafLst=open("cheeseLoaf.txt","r")  #read cheeseLoaf.txt
        recipeLoaf=recipeLoafLst.readlines()      #read recipe in cheeseLoaf.txt in list form
        loafOrderNum=int(orderNumLst[recipeLst.index("CHEESE LOAF")])    #obtaining order number of Cheese Loaf
        loafRecipeLst=[]

        for lines in range(len(recipeLoaf)):    #repeat until all lines in recipeLoaf already processed
            loafIngreLst=[]
            ingreLoaf=recipeLoaf[lines].strip("\n").split("|")[0].upper()   #obtaining ingredient to make Cheese Loaf
            demandLoaf=float(recipeLoaf[lines].strip("\n").split("|")[2])*loafOrderNum #obtaining the demand of ingredient to make Cheese Loaf
            uomLoaf=recipeLoaf[lines].strip("\n").split("|")[1]  #obtaining ingredient's uom for Cheese Loaf
            loafIngreLst.append(ingreLoaf)
            loafIngreLst.append(demandLoaf)
            loafIngreLst.append(uomLoaf)
            loafRecipeLst.append(loafIngreLst)


        recipeRollLst=open("custardRoll.txt","r")  #read custardRoll.txt
        recipeRoll=recipeRollLst.readlines()       #read recipe in custardRoll.txt in list form
        rollOrderNum=int(orderNumLst[recipeLst.index("CUSTARD CREAM ROLL")])   #obtaining order number of Custard Roll
        rollRecipeLst=[]

        for lines in range(len(recipeRoll)):    #repeat until all lines in recipeRoll already processed
            rollIngreLst=[]
            ingreRoll=recipeRoll[lines].strip("\n").split("|")[0].upper()  #obtaining ingredient to make Custard Roll
            demandRoll=float(recipeRoll[lines].strip("\n").split("|")[2])*rollOrderNum  #obtaining the demand of ingredient to make Custard Roll
            uomRoll=recipeRoll[lines].strip("\n").split("|")[1]    #obtaining ingredient's uom for Custard Roll
            rollIngreLst.append(ingreRoll)
            rollIngreLst.append(demandRoll)
            rollIngreLst.append(uomRoll)
            rollRecipeLst.append(rollIngreLst)


        recipeBreadLst=open("toraBread.txt","r") #read toraBread.txt 
        recipeBread=recipeBreadLst.readlines()   #read recipe in toraBread.txt in list form
        breadOrderNum=int(orderNumLst[recipeLst.index("TORA BREAD")])   #obtaining order number of Tora Bread
        breadRecipeLst=[]

        for lines in range(len(recipeBread)):   #repeat until all lines in recipeBread already processed
            breadIngreLst=[]
            ingreBread=recipeBread[lines].strip("\n").split("|")[0].upper()  #obtaining ingredient to make Tora Bread
            demandBread=float(recipeBread[lines].strip("\n").split("|")[2])*breadOrderNum  #obtaining the demand of ingredient to make Tora Bread
            uomBread=recipeBread[lines].strip("\n").split("|")[1]    #obtaining ingredient's uom for Tora Bread
            breadIngreLst.append(ingreBread)
            breadIngreLst.append(demandBread)
            breadIngreLst.append(uomBread)
            breadRecipeLst.append(breadIngreLst)


        if chkNewRecipe(4)==True:   #if newRecipe exist, run the program
            NRLst=open("newRecipe.txt","r")   #read newRecipe.txt
            NR=NRLst.readlines()     #read recipe in newRecipe.txt in list form
            NROrderNum=int(orderNumLst[4])
            NRLst=[]

            for lines in range(len(NR)):   #repeat until all lines in NR already processed
                NRIngreLst=[]
                ingreNR=NR[lines].strip("\n").split("|")[0].upper()  #obtaining ingredient to make the new recipe
                demandNR=NR[lines].strip("\n").split("|")[2]*NROrderNum  #obtaining the demand of ingredient to make new recipe
                uomNR=NR[lines].strip("\n").split("|")[1]    #obtaining ingredient's uom for new recipe
                NRIngreLst.append(ingreNR)
                NRIngreLst.append(demandNR)
                NRIngreLst.append(uomNR)
                NRLst.append(NRIngreLst)


        if chkNewRecipe(4)==True:   #if newRecipe exist, run this program
            ingreLst=breadRecipeLst+loafRecipeLst+bunRecipeLst+rollRecipeLst+NRLst
            demandIngreLst=[]
            demandUomLst=[]
            for i in range(len(ingreLst)):
                demandIngre=ingreLst[i][0]
                if demandIngre not in demandIngreLst:  #append all ingredients into a new list without repetition
                    demandUom=ingreLst[i][2]
                    demandUomLst.append(demandUom)
                    demandIngreLst.append(demandIngre)
                    demandIngreLst.sort()
            demandLevelLst=[0]*len(demandIngreLst)
            for x in range(len(ingreLst)):
                demandLevel=ingreLst[x][1]
                demandLevelLst[demandIngreLst.index(ingreLst[i])]+=demandLevel  #calculate the demand of ingredient
                            
        else:
            ingreLst=breadRecipeLst+loafRecipeLst+bunRecipeLst+rollRecipeLst
            demandIngreLst=[]
            demandUomLst=[]
            for i in range(len(ingreLst)):
                demandIngre=ingreLst[i][0]
                if demandIngre not in demandIngreLst:    #append all ingredients into a new list without repetition
                    demandUom=ingreLst[i][2]
                    demandUomLst.append(demandUom)
                    demandIngreLst.append(demandIngre)
                    demandIngreLst.sort()
            demandLevelLst=[0]*len(demandIngreLst)
            for x in range(len(ingreLst)):
                demandLevel=ingreLst[x][1]
                demandLevelLst[demandIngreLst.index(ingreLst[x][0])]+=demandLevel    #calculate the demand of ingredient


        #To get the stocklevel of ingredient
        stock=open("Ingredients.txt","r")  #read Ingredients.txt
        stockLst=stock.readlines()   #read stock in Ingredients.txt in list form
        allStockIngreLst=[]
        for lines in range(len(stockLst)): #repeat until all lines in stockLst already processed
            stockIngreLst=[]
            stockIngre=stockLst[lines].strip("\n").split("|")[0].upper() 
            stockLevel=stockLst[lines].strip("\n").split("|")[2]  
            stockUom=stockLst[lines].strip("\n").split("|")[1]
            stockIngreLst.append(stockIngre)
            stockIngreLst.append(stockLevel)
            stockIngreLst.append(stockUom)
            allStockIngreLst.append(stockIngreLst)


        #Add ingredient in demand into stock list if it does not in the list
        chkIngreLst=[]
        for i in range(len(allStockIngreLst)):
            chkIngreLst.append(allStockIngreLst[i][0])

        for i in range(len(demandIngreLst)):
            if demandIngreLst[i] not in chkIngreLst:
                allStockIngreLst.append([demandIngreLst[i],0])


        #decoration
        print("\tIngredient(s)        Stocklevel           Demand          Shortfall")
        print("\t"+"-"*13 + " "*6 + "-"*14 + " "*7 + "-"*10 + " "*6 + "-"*13)


        #calculate short fall
        shortFallLst=[]
        for i in range(len(allStockIngreLst)):
            if allStockIngreLst[i][0] in demandIngreLst:
                idx=demandIngreLst.index(allStockIngreLst[i][0])
                shortFall=demandLevelLst[idx]-float(allStockIngreLst[i][1])
                uom=demandUomLst[idx]
                demandLevel=demandLevelLst[idx]
                if shortFall>0:  #if short fall exist, append it in 
                    shortFallLst.append([allStockIngreLst[i][0],allStockIngreLst[i][1],demandLevel,uom,shortFall])
                else:   #no short fall, append NA
                    shortFallLst.append([allStockIngreLst[i][0],allStockIngreLst[i][1],demandLevel,uom,"NA"])
            else:
                shortFallLst.append([allStockIngreLst[i][0],allStockIngreLst[i][1],0,allStockIngreLst[i][2],"NA"])


        #print out ingredient, stocklevel, unit of ingredient, demand level and short fall
        for i in range(len(shortFallLst)):
            ingredient=shortFallLst[i][0]
            stockLevel=float(shortFallLst[i][1])
            demandLevel=shortFallLst[i][2]
            uom=shortFallLst[i][3]
            shortFall=shortFallLst[i][4]
            if shortFall=="NA":
                print("\t%-20s%9.2f%2s%17.2f%2s%15s"%(ingredient,stockLevel,uom,demandLevel,uom,shortFall))
            else:
                print("\t%-20s%9.2f%2s%17.2f%2s%16.2f%2s"%(ingredient,stockLevel,uom,demandLevel,uom,shortFall,uom))

        print("\t"+"-"*73)
        print("\t"+"-"*73)


        option=input("\t<S>aveFile"+" "*3+"<Q>uit  >>")
        #input again if option is invalid
        while option.upper() not in ["Q","S"]: #if option are not Q,q,S or s
            err=input("\tERROR Option\nPlease Enter <5> to continue:")
            while err!="5": #repeat until err="5"
                err=input("\tERROR Option\nPlease Enter <5> to continue:")
            else: #if err="5"
                option=input("\t<S>aveFile"+" "*3+"<Q>uit  >>")
                
        if option.upper()=="S": #if option is S or s, save the result into MRP.txt
            MRPFile=open("MRP.txt","w")
            MRPLst=[]
            title="\tIngredient(s)        Stocklevel           Demand          Shortfall\n\t"+"-"*13 + " "*6 + "-"*14 + " "*7 + "-"*10 + " "*6 + "-"*13+"\n"   
            print("\tMRP run result is saved into file named (MRP.txt)")
            MRPFile.write(title)
            for i in range(len(shortFallLst)):
                ingredient=shortFallLst[i][0]
                stockLevel=float(shortFallLst[i][1])
                demandLevel=shortFallLst[i][2]
                uom=shortFallLst[i][3]
                shortFall=shortFallLst[i][4]
                if shortFall=="NA":
                    MRP="\t%-20s%9.2f%2s%17.2f%2s%15s\n"%(ingredient,stockLevel,uom,demandLevel,uom,shortFall)
                    MRPFile.write(MRP)
                else:
                    MRP="\t%-20s%9.2f%2s%17.2f%2s%16.2f%2s\n"%(ingredient,stockLevel,uom,demandLevel,uom,shortFall,uom)
                    MRPFile.write(MRP)

            MRPFile.close()

            err=input("\tPlease Enter <5> to continue:")
            while err!="5": #repeat until err="5"
                err=input("\tERROR Option\nPlease Enter <5> to continue:")
            else: #if err="5"
                os.system("cls")  #clear screen
                menu() #back to main menu


                
        elif option.upper()=="Q":  #if option is Q or q
            os.system("cls") #clear screen
            menu() #back to main menu


                    
    MRP()







#Data Validation
import os
def mainProg(mainmode):     
    # Go to Ingredients Maintenence
    if mainmode == "1":
        IM()   

    # Go to Maintain Recipe
    elif mainmode == "2":
        MR()

    #Go to Create Requirement/Orders
    elif mainmode == "3":
        CRO()

    # Go to MRP Run
    elif mainmode == "4":
       GMRP()
       
   #Quit
    elif mainmode == "0":
        stopprogram = input("Are you sure you want to quit ? ( Y, N ) >> ")
        if (stopprogram == "y") or (stopprogram == "Y"): 
            print()
            input("\t\tTHANKS FOR VISITING DIY HOMEBREAD BAKERY =)\n \t\t\t    SEE YOU NEXT TIME!\n \t\t\t   PLEASE ENTER TO EXIT")
            exit()                                                   #kill the running program
        elif (stopprogram == "n") or (stopprogram == "N"):
            os.system("cls")                                   #clear screen to look more tidy 
            menu()                                             #return to main menu
        else:
            print("Please type either Y or N")                 #ERROR 
            mainProg(mainmode)                                
          
    #Option != 1,2,3,4 or 0 
    else:
        print("ERROR OPTION!Only numbers 1,2,3,4,0 allowed!") #ERROR
        rptProg()   
    
           
               
    

import os
#data validation
def rptProg():
    mode=input("Please Enter <5> to continue :")   

    if mode == "5" :
        menu()                 #return to main menu
    elif mode != "5":
        rptProg()              #repeat 
        

menu()
