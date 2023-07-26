
import PySimpleGUI as sg

from pytube import YouTube

import pytube.exceptions as exceptions

 

class menu:

    def __init__(self): # TELAS DO APLICATIVO

        # TELA PRINCIPAL


        def JanelaPrincipal():

            sg.change_look_and_feel('DarkBlue1')

            layout = [[sg.Text("                                 YOUTUBE VIDEO DOWNLOADER BY: RAULZIN             ")],

                [sg.Text("                                                              APLHA BUILD 2.0")],

                [sg.Text("")],

                [sg.Text("INSIRA LINK DO SEU VIDEO!", text_color='gold'),sg.Input()],

                [sg.Text("                                                                                        ")],

                [sg.Button("Baixar",border_width=5, size=5, button_color="gray", expand_x='true')],

                [sg.Button("Sair",border_width=5 ,button_color='gray', size=(10))]

                ]

            return sg.Window('YOUTUBE VIDEO DOWNLOADER', layout=layout, finalize=True)

        # TELA DE ERRO

        def JanelaErro():

            erro = [[sg.Text("                                                                                        ")],
                [sg.Text("                 POR FAVOR INSIRA UM LINK                 ",text_color='white')],

                [sg.Text("                                                                                        ")],                                                                      

                [sg.Button("Voltar",border_width=5 ,button_color='gray', size=(10))]

                ]

            return sg.Window('Erro !', layout=erro, finalize=True)

 

        try:
            
            while True:
                janela1,janela= JanelaPrincipal(), None
                window, button, values = sg.read_all_windows()
                

                if button == 'Baixar':

                    video = YouTube(values[0])
                    stream = video.streams.get_highest_resolution()

                    stream.download('/home/raulraro/Desktop')
                    break
                    

                elif button == 'Sair' or sg.WINDOW_CLOSE_ATTEMPTED_EVENT:

                    break

        except exceptions.RegexMatchError as a:
             
             while True:
                erroReg,erroReg1 = JanelaErro(), None
                window, button, values = sg.read_all_windows()

                if  window == erroReg and button == 'Voltar':

                    
                    janela1.close()
                    erroReg.close()
                    
                    break

                if window == erroReg and sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
                    break
             menu()

        except exceptions.ExtractError as e:
            
            while True:
                erro1, erro2 = JanelaErro(), None
                window,button, values = sg.read_all_windows()

                if window == erro1 and button == 'Voltar':
                
                    erro1.close()
                    janela1.close()                   

                    break
                                        
                if window == erro1 and sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
                    break
            menu()

            

           
 
tela = menu()
