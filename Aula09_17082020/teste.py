# from conta import Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

conta_ze = ContaCorrente("Zé", 1500.0)
conta_lu = ContaPoupanca("Lu")

print("")
print("Antes de transferir -------------")
print(conta_ze)
print(conta_lu)

conta_ze.transferir(500.0, conta_lu)

print("")
print("Depois de transferir ------------")
print(conta_ze)
print(conta_lu)

conta_lu.render()

print("")
print("Depois do rendimento ------------")
print(conta_lu)

conta_ze.sacar(100)

# conta_ze.__saque(100)

print("")
print("Depois do Saque ------------")
print(conta_ze)



