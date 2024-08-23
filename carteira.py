from bitcoinlib.keys import Key

def gerar_carteira():
  """Gera um par de chaves pública e privada Bitcoin."""
  chave_privada = Key.generate()
  chave_publica = chave_privada.pub
  endereco_bitcoin = chave_publica.address
  return chave_privada, chave_publica, endereco_bitcoin

# Gerando uma nova carteira
chave_privada, chave_publica, endereco_bitcoin = gerar_carteira()

# Imprimindo os detalhes da carteira
print(f"Chave Privada: {chave_privada.hex()}")
print(f"Chave Pública: {chave_publica.hex()}")
print(f"Endereço Bitcoin: {endereco_bitcoin}")
