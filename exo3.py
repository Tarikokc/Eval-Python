class Exo:
    def puissance(self, x, n):
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n < 0:
            return 1 / self.puissance(x, -n)
        
        
        if n % 2 == 0:
            carre = self.puissance(x, n // 2)
            return carre * carre
        else:
            return x * self.puissance(x, n - 1)

exo = Exo()
print(exo.puissance(2, 3))   
print(exo.puissance(2, 1))   
print(exo.puissance(2, 0))   
print(exo.puissance(2, -3))  
 