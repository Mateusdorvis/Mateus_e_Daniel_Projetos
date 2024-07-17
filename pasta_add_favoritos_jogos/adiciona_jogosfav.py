

class CatalogoJogosDisponiveis:
    def __init__(self, titulo_do_jogo : str , version : str):
        self.titulo_do_jogo = titulo_do_jogo
        self.version = version
    
    def dcionario_lista_de_jogos_disponiveis(self):
        var_lista_dic_jogos_disponiveis = [{f'titulo do jogo ' : 'Resident Evil 4', 
                                           'Versão ' : 'Região: NTSC (América do Norte)'
                                            },
                                        
                                          {f'titulo do jogo ' : 'Silent Hill', 
                                            'Versão ' : 'Região: NTSC (América do Norte)'
                                            }, 
                                          
                                          {f'titulo do jogo ' : 'Resident Evil Outbreak', 
                                            'Versão ' : 'Região: NTSC (América do Norte)'
                                            }
                                        ]
        
        #o titulo vai para o menu e se caso o menu for igual ao titulo vai mostrar a id e mostra
        

#teste = CatalogoJogosDisponiveis(None, None)
#teste.dcionario_de_jogos_disponiveis()