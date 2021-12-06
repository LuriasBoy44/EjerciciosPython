from io import open

class Fibonacci():
    def __init__(self):
        self.__sec1,self.__sec2= 0,1        

    def ejecutaSecuencia(self,n):
        while self.__sec1 < n:
           # print(f'\t{a}',end='\n')
           print('\t',self.__sec1 , end='\n')   
           # print('\t',self.__sec1 , self.points(self.__sec1), end='\n')     
           # self.sumaValores()
           self.guardaValores(self.__sec1)
           self.__sec1,self.__sec2 = self.__sec2, (self.__sec1+self.__sec2)

    def guardaValores(self, dato):
        archivo_texto=open("ArchivoDeTexto.txt","a")
        archivo_texto.write(str(dato)+'\n')
        archivo_texto.close()

    def sumaValores(self):
        res=0
        if self.__sec1>9:
             valor=str(self.__sec1) 
             for i in  range (len(valor)):
                   res=res+int(valor[i])
        else:
           res=self.__sec1
                   
        print('\t>>>>',res)
        
    def points(self,n):  
        txt=''
        if n>0:
            x = txt.rjust(n, '.')
            return x
        else:
            return ''


