import os
from .parser.parser import parse
from .engine.game import init_game, play_game
from .engineP5.p5_export import export_for_p5  # Agora estamos importando da pasta engineP5

import argparse
import subprocess

__version__ = "0.1.8"

def game_parse_arguments():
    '''Define and parse arguments using argparse'''
    parser = argparse.ArgumentParser(description='Engine')
    parser.add_argument('--input','-i'             ,type=str, nargs=1                                , help='Input file')
    parser.add_argument("--engine", '-e', choices=["pygame", "p5"], default="pygame", help="Escolha a engine do jogo: pygame ou p5.js")
    return parser.parse_args()



def erpl_parse_arguments():
    '''Define and parse arguments using argparse'''
    parser = argparse.ArgumentParser(description='ERPL Parser')
    parser.add_argument('--output','-o'            ,type=str, nargs=1,required=False                                , help='Output file')
    parser.add_argument('--input','-i'             ,type=str, nargs=1,required=True                                 , help='Input file')
    parser.add_argument('--args','-args'           ,nargs='+'                                                       , help='Args')
    parser.add_argument("--engine", '-e', choices=["pygame", "p5"], default="pygame", help="Escolha a engine do jogo: pygame ou p5.js")
    return parser.parse_args()

def parser_parse_arguments():
    '''Define and parse arguments using argparse'''
    parser = argparse.ArgumentParser(description='ERPL Parser')
    parser.add_argument('--output','-o'            ,type=str, nargs=1,required=False                                , help='Output file')
    parser.add_argument('--input','-i'             ,type=str, nargs=1,required=True                                 , help='Input file')
    parser.add_argument('--args','-args'           ,nargs='+'                                                       , help='Args')
    return parser.parse_args()



def erpl():
    args = erpl_parse_arguments()
    
    # Gerar o arquivo JSON temporário
    if args.output:
        print("ERROR!")
    args.output = ['tmp.json']  # TODO: Gerar nome de arquivo baseado na data e hora
    parse(args)
    
    # Escolher a engine
    args.input = ['tmp.json']
    if args.engine == "pygame":
        screen, room, inventory, state = init_game(args)
        os.remove('tmp.json')
        # Joga usando o Pygame
        play_game(screen, room, inventory, state)
    elif args.engine == "p5":
        # Exportar os dados do jogo para o formato p5.js
        export_for_p5(args.input[0])
        os.remove('tmp.json')

        # Opcional: rodar o jogo em um servidor local para testar
        print("Rodando jogo com engine p5.js. Iniciando em http://localhost:3000")
        subprocess.run(["python", "-m", "http.server", "3000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def erparse():
    args = parser_parse_arguments()
    parse(args)
    

def erengine():
    args = game_parse_arguments()

    if args.engine == "pygame":
        screen, room, inventory, state = init_game(args)
        play_game(screen, room, inventory, state)
    elif args.engine == "p5":
        export_for_p5(args.input[0])
        print("Rodando jogo com engine p5.js. Iniciando em http://localhost:3000")
        subprocess.run(["python", "-m", "http.server", "3000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
