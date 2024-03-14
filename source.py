import PySimpleGUI as sg

FL_top = [[sg.Image(sg.EMOJI_BASE64_BLANK_STARE, subsample= 2, background_color= "#C1C1C1"), 
           sg.Text("Hackathone 12-14 y.o.", background_color= "#C1C1C1", text_color= "#000000"), 
           sg.Image(sg.EMOJI_BASE64_BLANK_STARE, subsample= 2, background_color= "#C1C1C1") ]]

FL_input = [[sg.Text("0", size= (35, 3), enable_events= True, key= "-Value-")]]

FL_erasers = [[sg.Button("C", size= [8, 3], pad= 0), ]]
FL_keyboard = [[sg.Button("7", size= [8, 3], pad= 0), sg.Button("8", size=[8,3], pad= 0), sg.Button("9", size=[8,3], pad= 0)],
               [sg.Button("4", size=[8,3], pad= 0), sg.Button("5", size=[8,3], pad= 0), sg.Button("6", size=[8,3], pad= 0)],
               [sg.Button("1", size=[8,3], pad= 0), sg.Button("2", size=[8,3], pad= 0), sg.Button("3", size=[8,3], pad= 0)],
               [sg.Button(" ", size=[8,3], pad= 0), sg.Button("0", size=[8,3], pad= 0), sg.Button(",", size=[8,3], pad= 0)]
               ]

FL_operators = [[sg.Button("/", size= (8, 3), pad= 0)],
                [sg.Button("*", size= (8, 3), pad= 0)],
                [sg.Button("+", size= (8, 3), pad= 0)],
                [sg.Button("-", size= (8, 3), pad= 0)],
                [sg.Button("=", size= (8, 3), pad= 0)]
]

l_top = [[sg.Frame("", FL_top, pad= 0, background_color= "#C1C1C1", border_width= 5)],
         [sg.Frame("", FL_input, pad= 0, background_color= "#C1C1C1")],
         [sg.Frame("", FL_erasers, pad= 0, background_color= "#C1C1C1")],
         [sg.Frame("", FL_keyboard, background_color= "#C1C1C1", border_width= 5, pad= 0), sg.Frame("", FL_operators, background_color= "#C1C1C1", border_width= 5, pad= 0)] ]

