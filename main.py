from cliente import Cliente

cliente = Cliente("Cesar", 17, "cesar@gmail.com", "basic")
print(cliente.nome)
cliente.mudar_plano("premium")

print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")

print(cliente.idade)
cliente.restricao(17)



