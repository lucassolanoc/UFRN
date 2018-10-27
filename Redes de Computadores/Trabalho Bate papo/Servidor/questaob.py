# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets
import threading
import time

class minhaThread (threading.Thread):
    # redefine a funcao __init__ para aceitar a passagem parametros de entrada
    def __init__(self, threadID, threadName, threadCounter):
        threading.Thread.__init__(self)
        self.id = threadID
        self.name = threadName
        self.counter = threadCounter
    # a funcao run() e executada por padrao por cada thread 
    def run(self):
        # aviso de inicio da thread
        print('%s se conectou ao servidor.' % (self.name))
        sentencethread = connectionSocket.recv(1024) # recebe dados do cliente
        sentencethread = sentencethread.decode('utf-8') 
        #connectionSocket.send(sentencethread.encode('utf-8'))
        while(sentencethread != 'exit'):
          sentencethread = connectionSocket.recv(1024) # recebe dados do cliente
          sentencethread = sentencethread.decode('utf-8')  
          connectionSocket.send(sentence.encode('utf-8'))
        connectionSocket.close()
        #print ('Iniciando Thread %d [%s] com %d tarefas' % (self.id, self.name, self.counter))
        # chama a funcao a ser executada por cada thread
        #executa_tarefa(self.id, self.name, self.counter)
        # aviso de que a thread terminou de executar suas tarefas
        print ('\nFim da Thread %d [%s]' % (self.id, self.name))

# funcao a ser chamada por cada thread em execucao       
#def executa_tarefa(id, name, counter):
 #   while counter:
  #      time.sleep(2) # atraso em cada thread
   #     print ('\nThread %d [%s] executando a tarefa %d em %s' % (id, name, counter, time.ctime(time.time())))
    #    counter -= 1
 
# criando duas threads
# a classe minhaThread() recebe: identificador da thread, nome da thread, numero de processos
#thread1 = minhaThread (1, 'Alice', 4)
#thread2 = minhaThread (2, 'Bob', 4)
 
# disparando as threads
#thread1.start()
#thread2.start()

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para   'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  print("Novo usuário conectado")
  #thread.start_new_thread(minhaThread, ())


  #sentence = connectionSocket.recv(1024) # recebe dados do cliente
  #sentence = sentence.decode('utf-8')
  thread1 = minhaThread (1, sentence, 4)
  #thread2 = minhaThread (2, sentence, 4)
  thread1.start()
  #thread2.start()
  #capitalizedSentence = sentence.upper() # converte em letras maiusculas
  #print ('Cliente %s enviou: %s, transformando em: %s' % (addr, sentence, capitalizedSentence))
  #connectionSocket.send(sentence.encode('utf-8')) # envia para o cliente o texto transformado
  #connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor