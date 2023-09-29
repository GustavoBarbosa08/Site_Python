#flet - flutter

# Botão de iniciar site
# Pop-up para entrar no chat
# Mostrar mensagem quando você entrar no chat, além do campo e botão de enviar mensagem
# A cada mensagem que vocÊ envia aparece
     # Nome: texto da mensagem
# Isso deve aparecer para todos

# produto = {
#      "produto": "iphone",
#      "preço": 6500
# }
# produto.get("produto")
# produto["preço"]



import flet as ft



def main(pagina):   

     texto = ft.Text("Seja bem-vindo ao Zap 2.0!")
     
     chat = ft.Column()

     nome_usuario = ft.TextField(label="Digite o seu nome")

     def enviar_mensagem_tunel(mensagem):
          tipo = mensagem["tipo"]

          if tipo == "mensagem":
               texto_mensagem = mensagem["texto"]
               usuario_mensagem = mensagem["usuario"]
               #adicionar a mensagem ao chat
               chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
          else:
               usuario_mensagem = mensagem["usuario"]
               chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12, italic=True, color=ft.colors.RED))

          pagina.update()



     #PUBSUB -> publish and subscribe

     pagina.pubsub.subscribe(enviar_mensagem_tunel)


     def enviar_mensagem(evento):
          pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})

          #limpar o campo de mensagem
          campo_mensagem.value = ""
          pagina.update()

     campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
     botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

     def entrar_popup(evento):
          pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
          # adcionar o chat
          pagina.add(chat)
          # Fechar o popup
          popup.open = False
          # deletar o iniciar chat
          pagina.remove(botao)
          pagina.remove(texto)
          # criar o campo de mensagem do usuário # criar botão de enviar mensagem   
          pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem]))
            
          pagina.update()

     popup = ft.AlertDialog(
          open=False,
          modal=True, 
          title=ft.Text("Bem-vindo ao Zap"),
          content= nome_usuario,
          actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
          )
     
     
     def entrar_chat(evento):
          # texto_entrou = ft.Text("Entrou")
          # pagina.add(texto_entrou)
          pagina.dialog = popup
          popup.open = True
          pagina.update()

     botao = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat)#TextButton
     pagina.add(texto)
     pagina.add(botao)



ft.app(target=main, view=ft.WEB_BROWSER, port=8080)