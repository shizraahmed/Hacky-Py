class business:
    prod = ''
    mini = ''
    maxi = ''
    def _init_(self,name,cell_no,prod,mini,maxi):
        self.name = name
        self.cell_no = cell_no
        self.prod = prod
        self.mini = mini
        self.maxi = maxi
    def getprod(self):
        if prod == 'laptop':
            if self.mini <= '25000':
                print('We have these laptops in this price range')
                print('{1:(dell 6578,24800),2:(hp 9900,24999)}')
                l1 = {1:['Model: dell 6578','price: 24800'],2:['Model: hp 9900','price:24999']}
                lap1 = eval(input('Enter no'))
                for x,y in l1.items():
                    if lap1 == x:
                        print(y)
            if self.mini >= '25000' and self.maxi <= '55000':
                print('We have these laptops in this price range')
                print('{1:(dell 6968,48750),2:(hp 9000,54999)}')
                l1 = {1:['Model: dell 6968','price: 48750'],2:['Model: hp 9000','price:54999']}
                lap1 = eval(input('Enter no'))
                for x,y in l1.items():
                    if lap1 == x:
                        print('NAME:',self.name)
                        print('CELL NO',self.cell_no)
                        print(y)
                        print('Company no: 0331-41714714')

name = input('enter your name')
cell_no = input('enter your cell no')
prod = input('Enter item you want: ')
print('Enter your price range')
mini = input('Enter minium amount')
maxi = input('Enter maxium amount')
p1 = business(name,cell_no,prod,mini,maxi)
print(" ")

p1.getprod()
