from abc import ABC
import pygame
from tela import Tela


class Objeto(pygame.sprite.Sprite, ABC):
    def __init__(self,
                 posicao: list,
                 nome: str,
                 tela: Tela,
                 anim: list,
                 velocidade: int):
        super().__init__()
        self.__posicao = posicao
        self.__nome = nome
        self.__tela = tela
        self.__anim = anim
        self.__velocidade = velocidade

        #Vão ser implementados nas subclasses
        self.__img_atual = None

        self.__spriteNum = 0
        self.__spriteNumMax = 0

        self.__spriteTimer = 0
        self.__spriteTimerMax = 0

        #Colocar isso no init das subclasses
        # self.pos_inicial()

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    @property
    def tela(self):
        return self.__tela

    @property
    def img_atual(self):
        return self.__img_atual

    @img_atual.setter
    def img_atual(self, img):
        self.__img_atual = img

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def anim(self):
        return self.__anim

    @anim.setter
    def anim(self, anim):
        self.__anim = anim

    @property
    def spriteNum(self):
        return self.__spriteNum

    @spriteNum.setter
    def spriteNum(self, spriteNum):
        self.__spriteNum = spriteNum

    @property
    def spriteNumMax(self):
        return self.__spriteNumMax

    @spriteNumMax.setter
    def spriteNumMax(self, spriteNumMax):
        self.__spriteNumMax = spriteNumMax

    @property
    def spriteTimer(self):
        return self.__spriteTimer

    @spriteTimer.setter
    def spriteTimer(self, spriteTimer):
        self.__spriteTimer = spriteTimer
    
    @property
    def spriteTimerMax(self):
        return self.__spriteTimerMax

    @spriteTimerMax.setter
    def spriteTimerMax(self, spriteTimerMax):
        self.__spriteTimerMax = spriteTimerMax

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    def pos_inicial(self):
        if len(self.__posicao) >= 2:
            self.__rect.x = self.__posicao[0]
            self.__rect.y = self.__posicao[1]
        else:
            self.__rect.x = 0
            self.__rect.y = 0

    def animacao(self):
        self.__spriteTimer +=1
        if self.__spriteTimer>=self.__spriteTimerMax:
            self.__spriteNum +=1
            self.__spriteTimer = 0

        if self.__spriteNum >= self.__spriteNumMax:
            self.__spriteNum = 0

        self.img_atual = self.__anim[self.__spriteNum]

    def blitme(self):
        self.tela.tela.blit(self.__img_atual, self.__rect)

    def update(self):
        pass