usuario_correto = 'admin'
senha_correta = '1234'

tentativas = 3

while tentativas > 0:
  usuario = input('digite o nome de usuario:')
  senha = input ('digite a senha:')

  if usuario == usuario_correto and senha == senha_correta:
    print ('acesso concedido!')
    break 

  elif usuario != usuario_correto or senha != senha_correta:
    tentativas -= 1
    print(f'usuario ou senha incorreta! voce tem {tentativas} restantes.')

  if tentativas == 0:
    print('acesso bloqueado!')