import PySimpleGUI as sg
import source
import math
from Calculator import Caalculator as Calc

val1, val2 = 0, 0
enable = 1
flot = 0
whattodo = ""

def res()->float:
    print("=== CALCULATING.... ===")
    print (val1, val2, whattodo)
    
    if whattodo == "+":
        return Calc.add(Calc, val1, val2)
    
    if whattodo == "-":
        return Calc.subtract(Calc, val2, val1)
    
    if whattodo == "/":
        return Calc.divide(Calc, val2, val1)
    
    if whattodo == "*":
        return Calc.multiply(Calc, val1, val2)
    
    
    return 0

if __name__ == "__main__":
    window = sg.Window('Window Title', source.l_top)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print(event, values)

        if event == "C":
            val1, val2 = 0, 0
            enable = 1
            flot = 0
            whattodo = ""
            window["-Value-"].update(val1)
            continue
        
        if event == "+" or event == "-" or event == "/" or event == "*":
            if whattodo == "":
                val2 = val1
                val1 = 0
                whattodo = event
                enable = 1
                flot = 0
            else:
                val1 = res()
                print(val1)
                window["-Value-"].update(val1)
                continue

        if event == "=":
            print(val1, val2)
            val1 = res()  
            print(val1)          
            window["-Value-"].update(val1)
            continue


        
        if event == ",":
            flot = 1

        if not event == "-Value-":
            try:
                value = float(event)
            except ValueError:
                enable = 0
            if enable == 1:
                if flot > 0:
                    val1 = val1 + value/(pow(10, flot))
                    flot = flot + 1
                else:
                    val1 = val1*10 + value
            

        enable = 1
        window["-Value-"].update(val1)



        

    window.close()