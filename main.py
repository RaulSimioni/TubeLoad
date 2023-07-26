
import PySimpleGUI as sg

from pytube import YouTube

import pytube.exceptions as exceptions

import os

 

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

        def GetWindowsPath():
            try:
                from winreg import HKEY_CURRENT_USER, ConnectRegistry, OpenKey, QueryValueEx
                key = r"Software\\Microsoft\Windows\\CurrentVersion\\Explorer\\Shell Folders"
                with OpenKey(ConnectRegistry(None, HKEY_CURRENT_USER), key) as reg_key:
                    download_dir = QueryValueEx(reg_key, "{374DE290-123F-4565-9164-39C4925E467B}")[0]
                    return download_dir
            except Exception as e:
                print("Erro!! OS LINUX!!", e)
                return GetLinuxPath()
        
        def GetLinuxPath():
            try:
                download_dir = os.path.expanduser("~/Downloads")
                return download_dir
            except Exception as e:
                print("Erro ao obter diretório de download no Linux:", e)
            return None

        try:
            
            while True:
                janela1,janela= JanelaPrincipal(), None
                window, button, values = sg.read_all_windows()
                download_dir = GetWindowsPath()
                

                if button == 'Baixar':

                    video = YouTube(values[0])
                    stream = video.streams.get_highest_resolution()

                    stream.download(download_dir)
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
