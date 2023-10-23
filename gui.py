# Introdução à GUI
import PySimpleGUI as psg

layout = [

    [psg.Text('***', size=55, text_color='red', background_color='black'), psg.Text('---------------------------------', size=55, text_color='red', background_color='black'), psg.Text('***', size=55, text_color='red', background_color='black')],
    [psg.Button(' --- Clique aqui --- ', size= (200, 5))],
    [psg.Text('***', size=55, text_color='red', background_color='black'),
     psg.Text('---------------------------------', size=55, text_color='red', background_color='black'),
     psg.Text('***', size=55, text_color='red', background_color='black')]],
window = psg.Window('Minha Primeira Tela Em Python', layout, size=(1280,720),
background_color='black', button_color='red')

while True:
    evento, valor = window.read()

    if evento == psg. WIN_CLOSED:
        break
    else:
        psg.popup('Progamação em Python \n botão clicado!', title='SENAI', button_type=4,
        button_color='red', background_color='black', text_color='red')

window.close()
