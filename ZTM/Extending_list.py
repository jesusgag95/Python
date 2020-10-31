class SuperList(list):
    def __len__(self):
        return 1000


superlist1 = SuperList()
superlist1.append(5)
superlist1.append(6)
superlist1.append(7)
superlist1.append(8)
print(superlist1[3])
print(len(superlist1))
