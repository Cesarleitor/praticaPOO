from cliente import Cliente

cliente = Cliente("Cesar", "cesar@gmail.com", "basic")
print(cliente.nome)
cliente.mudar_plano("premium")

print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")
