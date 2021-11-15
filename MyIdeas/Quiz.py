print ("Bem vindo(o) a empresa Tal")
name = input("Informe seu nome para o cadastro...: ")
print(f"Hello, Mr. {name}")
idade = int(input("Informe seu sua idade...: "))
if idade < 16:
    print ("Você ainda é muito novo para trabalhar ou ser aprendiz")
elif idade <18:
    print ("Você ainda é novo para trabalhar, mas pode ser aprendiz")
    s_n = input ("(OBS: responda com minusculo) Você gostaria de ser aprendiz?...:")
    if s_n == "sim":
        print (f"Pronto! Você foi contratado senhor(a) {name}, seu horário de trabalho será das 12:00pm até 6:00pm ")
    else:
        print ("Ok, vai pra casa da tua mae, tchau")
else:
    print ("Você tem a idade certa para trabalhar")
email = input("Informe-nos com seu gmail...:")
if len(email) <16:
    print ("Por favor, nos informe seu gmail de verdade :c [caso esse for seu email, apenas recoloque-o aqui")
    email = input ("...:")
else:
    print ("Obrigada")
regras = input("(OBS: responda com minusculo) Você ja leu todas as regras e está ciente de nosso contrato?...:")
if regras == "sim":
    print ("perfeito!")
else:
    print ("Entao leia e depois termine de fazer a entrevista")
    regras = input (f"Ao terminar de ler, escreva aqui...:")
experiencia = input ("(OBS: responda com minusculo)Você já teve algum tipo de experiência nessa área?")
if experiencia == "sim":
    print ("Perfeito! Você poderá trabalhar na área e pegar projetos maiores!")
else:
    print ("Tudo bem! Você poderá ser estagiario(a) e depois evoluir para outras áreas!")
fim = input ("(OBS: caso queira, responda [aceito] com minusculo) Parabéns por chegar até aqui, você seria um funcionario qualificado para nossos projetos e trabalhos! Aceita essa vaga?...:")
if fim == "aceito":
        print (f"Muito obrigada por aceitar fazer parte de nossa empresa, {name}! Estaremos lhe enviando seus horários e seu salário como _______ de nossa empresa!!")
else:
    print ("Tudo bem, entendemos sua escolha e esperamos que você tenha bons proveitos em seu novo trabalho! ")