from tkinter import*
import time

window = Tk()
window.title("Fractional Knapsacks")
window.geometry("520x400")
window.configure(bg="#D3E0EC")

######################################################
##################### Functions ######################
######################################################

#function to Reset
def reset():
    Max_Weight_Input.delete(0,END)
    No_Items_Input.delete(0,END)
    Weight_input.delete(0,END)
    Benefit_input.delete(0,END)

    ShowBox_Items.delete(0,END)
    ShowBox_Weight.delete(0,END)
    ShowBox_Benefit.delete(0,END)
    ShowBox_benefit_By_Weight.delete(0,END)
    ShowBox_Maximum_Benefit.delete(0,END)

#function to submit 
def submit_Items_total_Weight():
    # clear the boxes when clicking of submit for the second time

    ShowBox_Items.delete(0,END)
    ShowBox_Weight.delete(0,END)
    ShowBox_Benefit.delete(0,END)
    ShowBox_benefit_By_Weight.delete(0,END)
    ShowBox_Maximum_Benefit.delete(0,END)

    global Total_Weight
    global lenght
    global weight
    global benefit
    
    Items =  No_Items_Input.get()
    Total_Weight1 = Max_Weight_Input.get()
    weight1 = Weight_input.get().split(" ")
    benefit1 = Benefit_input.get().split(" ")

    lenght = int(Items)
    Total_Weight = float(Total_Weight1)
    weight = weight1
    benefit = benefit1
    
    #Print Items
    lenght1=[]
    for i in range (lenght):
        lenght1.append(i+1)
    ShowBox_Items.insert(0, lenght1)

    #print Weight
    weight_Input = []
    for i in range (lenght):
        a = int(weight[i])
        weight_Input.append(a)

    ShowBox_Weight.insert(0, weight_Input)

    #print Benefit
    Benefit_Input = []
    for i in range (lenght):
        a = int(benefit[i])
        Benefit_Input.append(a)

    ShowBox_Benefit.insert(0, Benefit_Input)


    #print Benefit By Weight
    benefit_By_Weight = []

    for i in range (lenght):
        a = float(benefit[i])
        b = float(weight[i])
        benefit_By_Weight1 = round(a/b, 2)

        benefit_By_Weight.append(benefit_By_Weight1)

    ShowBox_benefit_By_Weight.insert(0, benefit_By_Weight)

    # get the indexes from the biggest to smallest number in benefit_By_Weight list

    benefit_By_Weight_temp = benefit_By_Weight.copy()
    benefit_sorted = benefit_By_Weight.copy()
    benefit_sorted.sort()

    benefit_index = []

    for x in benefit_sorted:
        benefit_index.insert(0,benefit_By_Weight_temp.index(x))
        benefit_By_Weight_temp[benefit_By_Weight_temp.index(x)] = -1

    # Calculate the Maximum Benefit

    Total_Benefit = 0

    for i in  range(lenght):
        Total_Weight = Total_Weight - weight_Input[benefit_index[i]]
        if Total_Weight >= 0 :
            Total_Benefit = Total_Benefit + Benefit_Input[benefit_index[i]]
        else:
            Total_Weight = Total_Weight + weight_Input[benefit_index[i]]
            Total_Benefit = round(Total_Benefit + ((Benefit_Input[benefit_index[i]])*(Total_Weight))/(weight_Input[benefit_index[i]]),2)
    
    ShowBox_Maximum_Benefit.insert(0, Total_Benefit)  
        


#####################################################


# Ask for the Input of Total Weight
Max_Weight = Label(window,text="what is the total/Max weight: ",font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
Max_Weight.grid(row=0, column=0)
Max_Weight_Input = Entry(window, width = 10, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
Max_Weight_Input.grid(row=0, column=1, columnspan = 2)

# Ask for the Input of The total Number of Items Which will be the Lenght or or lists
No_Items = Label(window,text="how many items you Have: ", font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
No_Items.grid(row=1, column=0)
No_Items_Input = Entry(window, width = 10, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
No_Items_Input.grid(row=1, column=1, columnspan = 2)

# Ask for the Input of weight of the Items
Weight = Label(window,text="please enter the weight of the items: ", font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
Weight.grid(row=2, column=0)
Weight_input = Entry(window, width = 45, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
Weight_input.grid(row=2, column=1, columnspan=2, padx=10)

# Ask for the Input of benefit
Benefit = Label(window,text="please enter the benefit of the items: ", font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
Benefit.grid(row=3, column=0)
Benefit_input = Entry(window, width = 45, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
Benefit_input.grid(row=3, column=1, columnspan=2, padx=10)

#give some space
Benefit = Label(window,text=" ", bg="#D3E0EC")
Benefit.grid(row=4, column=0, padx=10, pady=5)

#Show Box for Items
ShowBox_Items1 = Label(window,text="The Items Numbers are: ", font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
ShowBox_Items1.grid(row=5, column=0)
ShowBox_Items = Entry(window, width=45, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
ShowBox_Items.grid(row=5, column=1, columnspan=2, padx=10)

#Show Box for Weight
ShowBox_Weight1 = Label(window,text="The Weight is: ", font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
ShowBox_Weight1.grid(row=6, column=0)
ShowBox_Weight = Entry(window, width=45, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
ShowBox_Weight.grid(row=6, column=1, columnspan=2, padx=10)

#Show Box for Benefit
ShowBox_Benefit1 = Label(window,text="The Benefit is: ", font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
ShowBox_Benefit1.grid(row=7, column=0)
ShowBox_Benefit = Entry(window, width=45, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
ShowBox_Benefit.grid(row=7, column=1, columnspan=2, padx=10)

#Show Box for Benefit / Weight
ShowBox_benefit_By_Weight1 = Label(window,text="The Ration Benefit By Weight is: ", font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
ShowBox_benefit_By_Weight1.grid(row=8, column=0)
ShowBox_benefit_By_Weight = Entry(window, width=45, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
ShowBox_benefit_By_Weight.grid(row=8, column=1, columnspan=2, padx=10)

#Show Box for Maximum Benefit
ShowBox_Maximum_Benefit1 = Label(window,text="The Max Benefit is: ", font=("Times", 10, "bold"), width = 30, bg="#B9CBDC", fg = "#102539")
ShowBox_Maximum_Benefit1.grid(row=9, column=0)
ShowBox_Maximum_Benefit = Entry(window, width=45, borderwidth = 5, font=("Times", 9, "bold"), fg = "#102539")
ShowBox_Maximum_Benefit.grid(row=9, column=1, columnspan=2, padx=10)



#give some space
Benefit = Label(window,text=" ", bg="#D3E0EC")
Benefit.grid(row=10, column=0, padx=10, pady=10)

#button for submission And to Reset
button_Submit =Button(window, text="Submit", padx=11, pady=5, font=("Times", 10, "bold"), bg = "#102539", fg = "White", command = submit_Items_total_Weight)
button_Submit.grid(row=11, column=0, columnspan = 2)
button_Reset =Button(window, text="Reset", padx=11, pady=5, font=("Times", 10, "bold"), bg = "#102539", fg = "White", command= reset)
button_Reset.grid(row=11, column=1, columnspan = 1)


window.mainloop()