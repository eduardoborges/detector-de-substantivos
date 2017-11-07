# -------------------------------
# Eduardo Borges
# 201500054132
# Universidade Federal de Sergipe - 2017.2
# -------------------------------

import unittest

## Limpa as palavras
def strip(string):
    caractersToScape = [',',';','.','!','?','/','*','-','\\','[',']','}','{','(',')','"','\'']
    for caracter in caractersToScape:
        string = string.replace(caracter,'')
    string = string.replace('\n', ' ')
    return string.lower()

##
## detecta determinantes retornando a posicao do mesmo no texto
##
def findSubTokens(text):
    file = open('_determinantes.cfg', 'r');
    determinantes = file.read().lower().split(';')
    file.close()
    text = strip(text).split(' ');
    matches = []
    i = -1
    for word in text:
        i = i + 1
        if(word in determinantes):
            matches.append( [word, i] )
    return matches

##
## Encontra os tokens com base na posição dos subtokens
##
def findTokens(text):
    text             = strip(text)
    subtokens        = findSubTokens(text)
    textToFindTokens = text.split(' ')
    tokens = []
    for subtoken in subtokens:
        t = textToFindTokens[subtoken[1] + 1]
        tokens.append(t)
    return tokens



##### TESTES #########
class DetectorDeSubstantivosTEST(unittest.TestCase):

    text = "O que é lorem ipsum. lorem ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos."

    # Teste de limpeza de strings
    def testeDeLimpeza(self):
        test = strip(self.text)
        expect = "o que é lorem ipsum lorem ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos"
        self.assertEqual(test, expect)

    # teste de encontro de subtokens
    def testFindSubTokens(self):
        test = findSubTokens(self.text)
        # expect = [0, 9, 11, 13, 17]
        expect = [ ['o',0],['uma',9],['de',11],['da',13],['de',17] ]
        self.assertListEqual(test, expect)
    
    # Teste de Encontro de substantivos
    # @unittest.skip("pule")
    def testFindTokens(self):
        test = findTokens(self.text)
        expect = ["simulação","texto","indústria", "impressos"]
        self.assertListEqual(test, expect)

def test():
    file = open('_txt.txt')
    text = strip(file.read())
    print(text)
    print(findSubTokens(text))

unittest.main()
# test()