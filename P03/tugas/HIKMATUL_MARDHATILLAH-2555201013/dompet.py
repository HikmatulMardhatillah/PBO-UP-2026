
class Dompet:
    def __init__(self, saldo: int) -> None:
        self.__saldo = saldo

    @property
    def saldo(self) -> int:
        return self.__saldo


d = Dompet(100000)

try:
    print(d.__saldo)
except AttributeError as e:
    print("Akses langsung : ditolak ->", e)

d._Dompet__saldo = -1
print("Lewat nama asli : berhasil ->", d.saldo)
print("Isi objek        :", list(vars(d)))
