from contaBancaria import ContaCorrente,CartaoCredito

conta_lira = ContaCorrente("Lira", "111.222.333-45", "Banco do Brasil", "212121")

cartao_lira = CartaoCredito("Lira", conta_lira)

print(cartao_lira.conta_corrente._num_conta)

print(cartao_lira.numero,
      cartao_lira.titular,
      cartao_lira.validade,
      cartao_lira.cod_seguranca,
      cartao_lira.limite)

#conta_lira.depositar_dinheiro(1000)
#conta_lira.consultar_saldo()

#conta_lira.sacar_dinheiro(3000)
#conta_lira.consultar_saldo()

#conta_lira.consultar_historico_transacoes()

#conta_maeLira = ContaCorrente("Beth", "222.333.444-555", "Itaum", "656565")

#conta_lira.transferir(1000, conta_maeLira)