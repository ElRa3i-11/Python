from tabulate import tabulate
from tkinter import *
from random import randint
#window = Tk()
#photo=PhotoImage(file="icone_pro.png")
#label = Label(window,bg="white",text="CITY SIM",font=("Arial",40,"bold"),relief=RAISED,bd=20,padx=20,pady=20,image=photo,compound="right")
#label.pack()
#button = Button(text="click")
#button.config(command=)
#button.pack()
#window.title("CITYSIM")
#window.geometry("1280x720")
#window.config(background="black")
#from random import randint
print("        -------------------CITY_SIM-------------------")
print("-> In this game you controle a city ")
print("-> Every action has consequences, dependencies etc")
print("-> Each year you make decision")
print("--------> 1 person needs 2 Food , 1 house shelter 5 persons ")
test=True
years=-1
helptest=0
testT=False
helpttt=1
while testT == False:
    Dif = int(input("Choose dificulty : \n Easy(1) , Normal(2) , Hard(3)"))
    testT = Dif == 1 or Dif == 2 or Dif == 3
if Dif == 1:
    Water = 54750
    Farms=5
    Water_infastructure= 5
    electric_infastructure=10
    happiness=70
    population = 1000
    populationGrowth = 0.05
    house = int(population / 5)
    Industry = 100
    foodstorage = 2000
    crimerate = 30
    IndustryFactor = 10
    money=100000
elif Dif == 2 :
    Farms = 2
    Water_infastructure = 3
    electric_infastructure = 5
    happiness=60
    population = 1500
    populationGrowth = 0.01
    house = int(population / 5)
    Industry = 50
    foodstorage = 1500
    crimerate = 50
    IndustryFactor = 0
    money = 50000
else:
    Farms = 0
    Water_infastructure = 1
    electric_infastructure = 2
    happiness=50
    population = 3000
    populationGrowth = 0
    house = int(population / 5)
    Industry = 50
    foodstorage = 500
    crimerate = 70
    IndustryFactor = -10
    money = 25000
happinessF = "0"
happinessP = "0"
happinessT = "0"
happinessS= "0"
happinessC= "0"
electricty_bill=0
electrictyGenerated=electric_infastructure * 500
industryincome = 0
Adultpopulation = population * (60 / 100)
Adultpopulation = int(Adultpopulation)
debt=0
while test :
    WaterGenerated=Water_infastructure*15000
    WaterNeed=population*150*365/1000
    randomevent=randint(0,5)
    if helpttt == 1:
        while helptest == False:
            help_input = input("do you want to see the game mechanics ? (n), (y) : ")
            help_input = help_input.upper()
            helptest = help_input == "Y" or help_input == "YES" or help_input == "N" or help_input == "NO"
            if help_input in ["Y", "YES"]:
                print("--------> 1 person needs 2 Food , 1 house shelter 5 persons")
                print("--------> tax rate is divide by 10 , so tax rate : 15,is 1.5%")
                print("--------> every factory needs 120 workers / every Farm need 250 Workers")
                print("--------> each house consume 3 to 5 KW , Factory consume 25 to 27 KW ,Farms consume 0.2 KW ")
                print("--------> 3% of your tax income goes to health care , 5% go to Government , and for each citizen that is not an adult you pay them 250$ a year")
                print("--------> crime rate , average salary , food , houses , electricity , unemployment , each one affect Happiness And population Growth")
                helptest = True
            elif help_input in ["N", "NO"]:
                helpttY = input("do you want this message to not show again ?")
                helpttY = helpttY.upper()
                if helpttY in ["Y", "YES"]:
                    helpttt = 0
                    helptest = True
                elif helpttY in ["N", "NO"]:
                    helpttt = 1
                    helptest = True
                helptest = True
    debttimer=0
    Avsalary=0
    Water=0
    Water_bill=0
    WaterIn = 0
    WaterInM = 0
    waterTest = False
    electricty_bill=0
    houseStatus=""
    crimerateStatus=""
    foodStatus=""
    populationGrowth=0
    Education=0
    healthcare=0
    Government=0
    foodIn=0
    foodInM=0
    FarmIn = 0
    FarmInM = 0
    houseIn=0
    houseInM = 0
    policeIn=0
    IndustryIn=0
    IndustryInM=0
    ElectricityIn = 0
    ElectricityInM = 0
    FarmTest = False
    ElectricityTest = False
    houseTest= False
    foodTest = False
    policeTest = False
    IndustryTest = False
    decisiontest= False
    Choosetest= False
    years=years+1
    electricty = house * randint(3,5) + Industry * randint(25,27) + Farms * 0.2
    electrictyGenerated = electric_infastructure * 500
    Adultpopulation = population * (60/100)
    Adultpopulation = int(Adultpopulation)
    print("        -------------------What are going to do this year-------------------")
    print("Happiness: ",happiness," // Money: ",f"{int(money):,}","$ //","Food: ",foodstorage," //","Population: ",population,"Electricity: ",int(electricty/1000),"MW")
    tax = int(input("tax rate: "))
    while decisiontest == False :
        while foodTest == False:
            foodIn = int(input("Food import(1food=6$): "))
            foodInM = foodIn * 6
            if 0 < money < foodInM:
                print("!! not enough money !!")
                print("You have :", money, "$")
            foodTest = money >= foodInM or foodInM == 0
        money = money - foodInM
        while policeTest == False:
            policeIn = int(input("Police founding: "))
            if 0 < money < policeIn:
                print("!! not enough money !!")
                print("You have :", money)
            policeTest = money > policeIn or policeIn == 0
        Avsalary = int(input("Average salary: "))
        while Choosetest == False :
            Choose = input("are you going to build ? (no) , (yes) : \n")
            Choose=Choose.upper()
            Choosetest = Choose == "Y" or Choose == "YES" or Choose == "N" or Choose == "NO"
        if Choose in ["Y","YES"]:
            while houseTest == False:
                houseIn = int(input("housing investment(1 House = 100$): "))
                houseInM = houseIn * 100
                if 0 < money < houseInM:
                    print("!! not enough money !!")
                    print("You have :", money)
                houseTest = money >= houseInM or houseInM == 0
            while IndustryTest == False:
                IndustryIn = int(input("Industry investment(1 Factory = 500$): "))
                IndustryInM = IndustryIn * 500
                if 0 < money < IndustryInM:
                    print("!! not enough money !!")
                    print("You have :", money)
                IndustryTest = money > IndustryInM or IndustryInM == 0
            while FarmTest == False:
                FarmIn = int(input("Farms investment(1Farm=750$): "))
                FarmInM = FarmIn * 750
                if 0 < money < FarmInM:
                    print("!! not enough money !!")
                    print("You have :", money)
                FarmTest = money > FarmInM or FarmInM == 0
            while ElectricityTest == False:
                ElectricityIn = int(input("Electrical infrastructure investment(1 Coal_Power_Plant = 5000$): "))
                ElectricityInM = ElectricityIn * 5000
                if 0 < money < ElectricityInM:
                    print("!! not enough money !!")
                    print("You have :", money)
                ElectricityTest = money > ElectricityInM or ElectricityInM == 0
            while waterTest == False:
                WaterIn = int(input("Water infrastructure investment(1 Pump = 2500$): "))
                WaterInM = WaterIn * 2500
                if 0 < money < WaterInM:
                    print("!! not enough money !!")
                    print("You have :", money)
                waterTest = money > WaterInM or WaterInM == 0
            decisiontest = True
        elif Choose in ["N","NO"] :
            decisiontest = True
    money = money - ElectricityInM
    money = money - WaterInM
    money = money - houseInM
    money = money - FarmInM
    Farms = Farms + FarmIn
    Water_infastructure = Water_infastructure + WaterIn
    electric_infastructure = electric_infastructure + ElectricityIn
    house = house + houseIn
    Industry = Industry + IndustryIn
    money = money - IndustryInM
    foodstorage = foodstorage + Farms*250
    if policeIn < population * (20/100):
        crimerate=crimerate+10
    else :
        crimerate=crimerate-5
    if crimerate < 0 :
        crimerate = 0
    money = money - policeIn
    policeIn=policeIn-policeIn*(30/100)
    tax=tax/10
    taxincome=(Adultpopulation*Avsalary) * tax * 50/100
    WorkersSalary=Adultpopulation*Avsalary*0.15
    money= money - WorkersSalary
    money = money + taxincome
    healthcare =healthcare+ (taxincome*3/100)
    Government= Government + (taxincome*5/100)
    Education=Education + ((population - Adultpopulation) * 250)
    money= money - (Education+Government+healthcare)
    money = money + industryincome
    Maintenance=Industry*100+house*50
    money=money-Maintenance
    total_jobs=Industry*120+Farms*250
    electricty = house * randint(3, 5) + Industry * randint(25, 27) + Farms * 0.2
    if electricty > electrictyGenerated :
        electricty_bill = electricty * 5
    money=money - electricty_bill

    if WaterNeed > WaterGenerated :
        happiness = happiness -2
        happinessS= "-2"
        IndustryFactor = IndustryFactor -5
    if WaterNeed < WaterGenerated :
        happiness = happiness +2
        happinessS= "+2"
        IndustryFactor=IndustryFactor + 20

    if Avsalary < 500 :
        happiness = happiness -1
        happinessS= "-1"
        IndustryFactor = IndustryFactor -5
    if Avsalary >= 500 :
        happiness = happiness +1
        happinessS= "+1"
        IndustryFactor=IndustryFactor + 20
    if total_jobs >= Adultpopulation :
        unemployment=0
        employment=Adultpopulation
    else:
        employment = total_jobs
        unemployment = Adultpopulation - total_jobs
    if 4.0 > tax > 2.0:
        taxStatus="! High Taxes !"
        happiness = happiness -3
        happinessT="-3"
        IndustryFactor = IndustryFactor +10
        populationGrowth = populationGrowth - 0.001
    elif tax <= 2.0:
        taxStatus = "Low Taxes"
        happiness = happiness + 0
        happinessT="+0"
        IndustryFactor = IndustryFactor + 20
        populationGrowth = populationGrowth + 0.001
    elif tax == 0:
        taxStatus = "No Taxes"
        happiness = happiness + 2
        happinessT="+2"
        IndustryFactor = IndustryFactor + 30
        populationGrowth = populationGrowth + 0.009
    elif tax > 4.0 :
        taxStatus = "! Very High Taxes !"
        happiness = happiness - 7
        happinessT = "-7"
        populationGrowth = populationGrowth - 0.01
        IndustryFactor = IndustryFactor -50
    foodstorage=foodstorage+foodIn
    foodstorage=foodstorage - population*2
    if foodstorage < 0:
        happiness = happiness-2
        happinessF="-2"
        foodStatus="Shortage"
        IndustryFactor = IndustryFactor - 10
        populationGrowth = populationGrowth - 0.02
    elif foodstorage > population*2 :
        happiness=happiness+1
        happinessF = "+1"
        foodStatus="Balanced"
        IndustryFactor = IndustryFactor + 10
        populationGrowth= populationGrowth + 0.01
    if 10 > population / house > 5 :
        happiness = happiness -2
        happinessP="-2"
        houseStatus = "NOT ENOUGH HOUSES"
        IndustryFactor = IndustryFactor - 10
        populationGrowth = populationGrowth - 0.01
    elif population / house >= 10 :
        happiness = happiness - 4
        happinessP = "-4"
        houseStatus = "YOU NEED TO BUILD HOUSES !!!"
        IndustryFactor = IndustryFactor - 30
        populationGrowth = populationGrowth - 0.03
    elif population / house < 5 :
        houseStatus = "Far more Enough Houses for all citizens"
        happiness = happiness +2
        happinessP = "+2"
        IndustryFactor = IndustryFactor + 20
        populationGrowth = populationGrowth + 0.02
    if 80 > crimerate > 50 :
        crimerateStatus="HIGH CRIME RATE"
        populationGrowth = populationGrowth - 0.01
        happiness= happiness -2
        happinessC="-2"
        IndustryFactor = IndustryFactor - 10
    elif crimerate < 50 :
        crimerateStatus="Stale Crime Rate"
        happiness= happiness +2
        happinessC="+2"
        IndustryFactor = IndustryFactor + 20
    elif crimerate > 80 :
        crimerateStatus="VERY HIGH CRIME RATE"
    if happiness > 100 :
        happiness = 100
    if IndustryFactor > 300 :
        IndustryFactor = 300
    if Adultpopulation * 50/100 >= unemployment >= Adultpopulation * 20/100 :
        crimerate = crimerate + 10
    elif unemployment > Adultpopulation * 50/100 :
        crimerate = crimerate + 30
    if employment == 0 :
        IndustryFactor = 0
    IndustryFactorStatus=""
    if IndustryFactor <= 0 :
        IndustryFactor = 0
        IndustryFactorStatus="NO ONE WANT TO WORK"
    elif IndustryFactor >= 200 :
        IndustryFactorStatus="Good conditions"
    elif IndustryFactor < 200 :
        IndustryFactorStatus="Balanced"
    if 40 >= happiness > 30:
        industryincome = employment * IndustryFactor * 1.1
    elif 60 >= happiness > 40:
        industryincome = employment * IndustryFactor * 1.2
    else:
        industryincome = employment * IndustryFactor * 1.5

    TotalExpense=Maintenance+IndustryInM+foodInM+houseInM+WorkersSalary+healthcare+Government+Education+electricty_bill
    TotalIncome=taxincome+industryincome
    population=int(population+populationGrowth*population)
    AlldataHappiness=[
        ["Food",happinessF,foodStatus],
        ["Housing", happinessP,houseStatus],
        ["Tax", happinessT,""],
        ["Aevrage_Salary", happinessS,""],
        ["Happiness", happiness,""]

    ]
    HappinessHeadrs=["Type","Value","Status"]
    taxincomeW=str(taxincome)+"$"
    industryincomeW = str(industryincome) + "$"
    AlldataIncome = [
        ["Tax", f"{int(taxincomeW):,}"],
        ["Industry", f"{int(industryincomeW):,}",IndustryFactorStatus],
        ["Total", f"{int(TotalIncome):,}"]

    ]
    IncomeHeadrs = ["Type", "Value","Status"]
    AlldataExpense = [
        ["Maintenance", str("{:,}".format(Maintenance)) + "$"],
        ["Industry ", str("{:,}".format(IndustryInM)) + "$"],
        ["Electricity infrastructure ", str("{:,}".format(ElectricityInM)) + "$"],
        ["Water infrastructure ", str("{:,}".format(WaterInM)) + "$"],
        ["Farms ", str("{:,}".format(FarmInM)) + "$"],
        ["Food ", str("{:,}".format(foodInM)) + "$"],
        ["Housing ", str("{:,}".format(houseInM)) + "$"],
        ["Workers salary ", str("{:,}".format(WorkersSalary)) + "$"],
        ["Health care ", str("{:,}".format(healthcare)) + "$"],
        ["Government ", str("{:,}".format(Government)) + "$"],
        ["Education ", str("{:,}".format(Education)) + "$"],
        ["Total ", str("{:,}".format(TotalExpense)) + "$"],
    ]

    ExpenseHeadrs = ["Type", "Value"]
    AlldataStatus = [
        ["Population", f"{int(population):,}", ""],
        ["Population Growth Rate", str(populationGrowth) + "%", ""],
        ["Unemployed", f"{int(unemployment):,}", ""],
        ["Employed", f"{int(employment):,}", ""],
        ["Houses", f"{int(house):,}", ""],
        ["Factories", f"{int(Industry):,}", ""],
        ["Tax", str(tax) + "%", ""],
        ["Crime Rate", str(crimerate) + "%", crimerateStatus],
        ["Water consumption", f"{int(WaterNeed):,}m³/year", ""],
        ["Water Generated", f"{int(WaterGenerated):,}m³/year", ""],
        ["Electricity consumption", f"{int(electricty / 1000):,}MW", ""],
        ["Electricity Generated", f"{int(electrictyGenerated / 1000):,}MW", ""]
    ]

    StatusHeadrs = ["Type", "Value","Status"]
    print("================ Year",years," ================")
    print("====HAPPINESS====")
    print(tabulate(AlldataHappiness, headers=HappinessHeadrs, tablefmt="grid"))
    print("====INCOME====")
    print(tabulate(AlldataIncome, headers=IncomeHeadrs, tablefmt="grid"))
    print("====EXPENSES====")
    print(tabulate(AlldataExpense, headers=ExpenseHeadrs, tablefmt="grid"))
    print()
    print("------------------>MONEY: ", f"{int(money):,}", "$")
    print()
    if money < 10000 :
        print("!! WARNING !!")
        print("LOW ON MONEY")
    elif money <= 0 :
        print("!! WARNING !!!!!!!!")
    print("====CITY STATUS====")
    print(tabulate(AlldataStatus, headers=StatusHeadrs, tablefmt="grid"))
    print("hello world")
