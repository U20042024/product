class Produit:
    _nbr_produit = 0
    
    def _init_(self, reference, designation, prix_achat, prix_vente, stock):
        self.__reference = reference
        self.__designation = designation
        self.__prix_achat = prix_achat
        self.__prix_vente = prix_vente 
        self.__stock = stock
        Produit._nbr_produit += 1
    
    @property
    def get_reference(self): 
        return self.__reference
    
    def set_reference(self, newreference) :
        self.__reference = newreference

    @property
    def get_prix_achat(self):
        return self.__prix_achat
    
    def set_prix_achat(self, newprix):
        self.__prix_achat = newprix

    @property
    def get_prix_vente(self):
        return self.__prix_vente

    def set_prix_vente(self, newprix):
        self.__prix_vente = newprix

    @property
    def get_stock(self):
        return self.__stock
    
    def set_stock(self, newstock):
        if newstock >= 0 :
            self.__stock += newstock
        elif newstock < 0 :
            if abs(newstock) <= self.__stock :
                self.__stock -= abs(newstock)
            else :
                print("Erreur de saisie du stock")


    def _str_(self):
        return f"""Référence: {self.__reference},
                Désignation: {self.__designation},
                Prix d'achat: {self.__prix_achat},
                Prix de vente: {self.__prix_vente},
                Stock: {self.__stock}"""

    def _eq_(self, other):
        if (self.get_reference == other.get_reference) :
            return True
        else:
            return False

class Commande:
    def _init_(self, date, produit, quantite):
        self.__date = date
        self.__produit = produit
        self.__quantite = quantite
    @property

    def get_date(self):
        return self.__date
    @property

    def get_produit(self):
        return self.__produit
    @property

    def get_quantite(self):
        return self.__quantite

    def Set_Produit(self, prod):
        self.__produit = prod

    def Set_Quantite(self, qte):
        self.__quantite = qte

    def _str_(self):
        return f"""Date : {self.__date},
                Produit : {self.__produit},
                Quantité : {self.__quantite}"""
    
    def _eq_(self, other):
        if (self.get_date == other.get_date) and (self.get_produit == other.get_produit) and (self.get_quantite == self.get_quantite):
            return True
        else:
            return False


#Test des classes

prd1 = Produit(332762, "laptob", 758, 67, 80)
prd2 = Produit(332762, "tablette", 250, 100, 5)
cmd1 = Commande("10/09/2021", prd1, 2)
cmd2 = Commande("11/09/2021", prd2, 5)


print(prd1)

print("nombres des produit :", Produit._nbr_produit)

print(prd1._eq_(prd2))