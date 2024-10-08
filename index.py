import os
import flet
from flet import *

class ModernNavBar(UserControl):
    def __init__(self, on_select_option, user_name, selected_image=None):
        super().__init__()
        self.on_select_option = on_select_option
        self.user_name = user_name
        self.selected_image = selected_image

    def UserData(self, initials: str, name: str, description: str):
        return Container(
            content=Column(
                controls=[
                    Text(
                        value=self.user_name,
                        size=18,
                        weight='bold',
                        color="white",
                    ),
                    Row(
                        controls=[
                            Container(
                                width=84,
                                height=84,
                                bgcolor="white",
                                alignment=alignment.center,
                                border_radius=84,
                                content=Image(
                                    src=self.selected_image if self.selected_image else "",
                                    fit="cover",
                                    width=84,
                                    height=84,
                                ) if self.selected_image else Text(
                                    value=initials,
                                    size=30,
                                    weight="bold",
                                ),
                            ),
                            Column(
                                spacing=1,
                                alignment="start",
                                controls=[
                                    Text(
                                        value=name,
                                        size=15,
                                        weight='bold',
                                        color="blue",
                                    ),
                                    Text(
                                        value=description,
                                        size=9,
                                        weight='w400',
                                        color="white70",
                                        opacity=1,
                                        animate_opacity=200,
                                    ),
                                ],
                            ),
                        ]
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name: str, text: str, option: int):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            padding=padding.all(10),
            on_click=lambda e: self.on_select_option(option),
            content=Row(
                controls=[
                    Icon(name=icon_name, size=30),
                    Text(value=text, size=16, weight="bold"),
                ]
            ),
        )

    def build(self):
        return Container(
            width=200,
            height=580,
            alignment=alignment.center,
            content=Column(
                controls=[
                    self.UserData("RL", self.user_name, "Seja Bem-vindo!"),
                    Divider(height=5, color="transparent"),
                    self.ContainedIcon("home", "Home", 1),
                    self.ContainedIcon("menu", "Menu", 2),
                    self.ContainedIcon("settings", "Settings", 3),
                    self.ContainedIcon("info", "Info", 4),
                    self.ContainedIcon("exit_to_app", "Sair", 5),
                ]
            ),
        )

def main(page: Page):
    page.title = "Tutor inteligente"
    page.bgcolor = "black"

    # Centralizar o conteúdo na página
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    selected_image = None

    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Preencha o seu nome"
            page.update()
            return
        if not entrada_senha.value:
            entrada_senha.error_text = "Campo de senha obrigatório"
            page.update()
            return

        nome = entrada_nome.value
        senha = entrada_senha.value
        print(f"Nome: {nome}\nSenha: {senha}")

        page.clean()
        menu_lateral(nome)

    def menu_lateral(nome):
        def opcao_selecionada(opcao):
            if opcao == 1:
                exibir_home(nome)
            elif opcao == 2:
                exibir_menu_principal(nome)
            elif opcao == 3:
                exibir_settings(nome)
            elif opcao == 4:
                exibir_texto("Info", nome)
            elif opcao == 5:
                page.clean()
                page.add(Text("Saindo do programa.", size=30))
            else:
                page.add(Text("Opção inválida. Tente novamente.", size=30))
            page.update()

        # Adicionar o menu lateral e a página Home diretamente após o login
        page.add(
            Row(
                controls=[
                    ModernNavBar(opcao_selecionada, nome, selected_image),  # Menu lateral
                    Container(
                        alignment=alignment.center,
                        expand=True,
                        content=Column(
                            controls=[
                                Text(f"Olá, {nome}!\nSeja bem-vindo ao Tutor Inteligente", size=30, color="white"),
                                Text("O Tutor Inteligente é uma ferramenta interativa para ajudar no aprendizado.", size=20, color="white"),
                            ],
                            alignment="center",
                            horizontal_alignment="center"
                        )
                    )
                ]
            )
        )
        page.update()

    def exibir_texto(texto, nome):
        page.clean()
        page.add(Text(texto, size=20, color="white"))
        page.add(ElevatedButton("Voltar", on_click=lambda e: exibir_menu_principal(nome)))
        page.update()

    def exibir_home(nome):
        page.clean()
        menu_lateral(nome)  # Recarregar o layout com o menu lateral
        page.update()

    def exibir_settings(nome):
        def atualizar_imagem(src):
            nonlocal selected_image
            selected_image = src
            exibir_home(nome)

        # Caminho da pasta onde estão as imagens
        images_folder = os.path.expanduser("~/Downloads/Tutor inteligente")

        page.clean()
        page.add(
            Column(
                alignment="center",
                horizontal_alignment="center",
                controls=[
                    Text("Escolha uma imagem para o perfil:", size=20, color="white"),
                    Row(
                        controls=[
                            Container(
                                width=100,
                                height=100,
                                border_radius=50,  # Torna o botão redondo
                                content=Image(
                                    src=os.path.join(images_folder, "imagem1.jpg"),
                                    fit="cover",
                                    width=100,
                                    height=100,
                                ),
                                on_click=lambda e: atualizar_imagem(os.path.join(images_folder, "imagem1.jpg")),
                            ),
                            Container(
                                width=100,
                                height=100,
                                border_radius=50,  # Torna o botão redondo
                                content=Image(
                                    src=os.path.join(images_folder, "imagem2.jpg"),
                                    fit="cover",
                                    width=100,
                                    height=100,
                                ),
                                on_click=lambda e: atualizar_imagem(os.path.join(images_folder, "imagem2.jpg")),
                            ),
                            Container(
                                width=100,
                                height=100,
                                border_radius=50,  # Torna o botão redondo
                                content=Image(
                                    src=os.path.join(images_folder, "imagem3.jpg"),
                                    fit="cover",
                                    width=100,
                                    height=100,
                                ),
                                on_click=lambda e: atualizar_imagem(os.path.join(images_folder, "imagem3.jpg")),
                            ),
                            Container(
                                width=100,
                                height=100,
                                border_radius=50,  # Torna o botão redondo
                                content=Image(
                                    src=os.path.join(images_folder, "imagem4.jpg"),
                                    fit="cover",
                                    width=100,
                                    height=100,
                                ),
                                on_click=lambda e: atualizar_imagem(os.path.join(images_folder, "imagem4.jpg")),
                            ),
                            Container(
                                width=100,
                                height=100,
                                border_radius=50,  # Torna o botão redondo
                                content=Image(
                                    src=os.path.join(images_folder, "imagem5.jpg"),
                                    fit="cover",
                                    width=100,
                                    height=100,
                                ),
                                on_click=lambda e: atualizar_imagem(os.path.join(images_folder, "imagem5.jpg")),
                            ),
                        ]
                    ),
                    ElevatedButton("Voltar", on_click=lambda e: exibir_home(nome))
                ]
            )
        )
        page.update()

    def exibir_menu_principal(nome):
        page.clean()
        page.add(
            ElevatedButton("O que é equação do segundo grau?", width=500, height=50, on_click=lambda 
            e: exibir_texto(
                "Equação do segundo grau\n\n"
                "A equação do segundo grau recebe esse nome porque é uma equação polinomial cujo termo de maior grau está elevado ao quadrado.\n"
                "Também chamada de equação quadrática, é representada por:\n\n ax² + bx + c\n\n"
                "Em uma equação do 2º grau, 'x' é a incógnita e representa um valor desconhecido. As letras 'a', 'b' e 'c' são chamadas coeficientes da equação.\n"
                "Os coeficientes são números reais e o coeficiente 'a' deve ser diferente de zero, caso contrário, passa a ser uma equação do 1º grau."
            , nome)),
            ElevatedButton("Como calcular as raízes?", width=500, height=50, on_click=lambda e: exibir_texto(
                "Como calcular as raízes\n\n"
                "As raízes de uma equação do segundo grau são os valores de 'x' nos quais a função definida pela equação cruza o eixo 'x',\n"
                "ou seja, onde o valor da função é igual a zero\n\n"
                "Para resolver uma equação do segundo grau, você pode utilizar a fórmula de Bhaskara. Siga os seguintes passos:\n"
                "1 - Determine os coeficientes 'a', 'b' e 'c' da equação.\n\n"
                "2 - Calcule o discriminante (Δ) usando a fórmula Δ = b² - 4ac\n\n"
                "Se Δ > 0, a equação tem duas raízes reais diferentes.\n"
                "Se Δ = 0, a equação tem uma raiz real.\n"
                "Se Δ < 0, a equação não possui raízes reais.\n\n"
                "3 - Calcule as raízes usando a fórmula de Bhaskara:\n"
                "x1 = (-b + √Δ) / 2a\n"
                "x2 = (-b - √Δ) / 2a"
            , nome)),
            ElevatedButton("Exemplo 1 ", width=500, height=50, on_click=lambda e: exibir_exemplo1(nome)),
            ElevatedButton("Exemplo 2", width=500, height=50, on_click=lambda e: exibir_exemplo(nome)),
            ElevatedButton("Voltar", width=500, height=50, on_click=lambda e: exibir_home(nome))
        )
        page.update()

    entrada_nome = TextField(label="Digite o seu nome", width=300)
    entrada_senha = TextField(label="Digite a sua senha", password=True, width=300)
    
    page.add(
        Column(
            alignment="center",  # Centralizar verticalmente
            horizontal_alignment="center",  # Centralizar horizontalmente
            controls=[
                entrada_nome,
                entrada_senha,
                ElevatedButton("Entrar", on_click=login)
            ]
        )
    )
    
    def exibir_exemplo1(nome):
        page.clean()

        # Título e instruções do exercício
        exercise_title1 = Text(value="Indique os coeficientes da equação", size=20, color='white')
        instructions1 = Text(value="\nDetermine os coeficientes 'a', 'b' e 'c' da equação: 2x² - 6x - 8 = 0", size=16, color='white')

        coef_a1 = TextField(label="Coeficiente 'a'", width=200)
        coef_b1 = TextField(label="Coeficiente 'b'", width=200)
        coef_c1 = TextField(label="Coeficiente 'c'", width=200)

        correct_a1 = "2"
        correct_b1 = "-6"
        correct_c1 = "-8"

        feedback = Text(value="", size=16, color='red')

        # Função para verificar se os valores são numéricos
        def is_numeric(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        # Função para verificar as respostas
        def check_answers(e):
            # Verificar se todos os valores inseridos são numéricos
            if not is_numeric(coef_a1.value) or not is_numeric(coef_b1.value) or not is_numeric(coef_c1.value):
                feedback.value = "Por favor, insira apenas números nos coeficientes."
            elif coef_a1.value != correct_a1:
                feedback.value = "Coeficiente 'a' incorreto. Lembre-se que o sinal acompanha os coeficientes. Tente novamente."
            elif coef_b1.value != correct_b1:
                feedback.value = "Coeficiente 'b' incorreto. Lembre-se que o sinal acompanha os coeficientes. Tente novamente."
            elif coef_c1.value != correct_c1:
                feedback.value = "Coeficiente 'c' incorreto. Lembre-se que o sinal acompanha os coeficientes. Tente novamente."
            else:
                feedback.value = "Você acertou!"

            page.update()

        # Botões de verificação e voltar
        check_button = ElevatedButton(text="Verificar Respostas", on_click=check_answers)
        back_button = ElevatedButton(text="Voltar", on_click=lambda e: exibir_menu_principal(nome))

        # Adicionar todos os elementos à página
        page.add(
            Column(
                controls=[
                    exercise_title1,
                    instructions1,
                    coef_a1,
                    coef_b1,
                    coef_c1,
                    check_button,
                    feedback,
                    back_button
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )

        page.update()

        
    def exibir_exemplo(nome):
        page.clean()

        # Título e instruções do exercício
        exercise_title = Text(value="Calcule as raízes da equação x² - 5x + 6 = 0", size=20, color='white')
        instructions = Text(value="\nDetermine os coeficientes 'a', 'b' e 'c' da equação:", size=16, color='white')

        # Campos de entrada
        coef_a = TextField(label="Coeficiente 'a'", width=200)
        coef_b = TextField(label="Coeficiente 'b'", width=200)
        coef_c = TextField(label="Coeficiente 'c'", width=200)
        delta_input = TextField(label="Valor do discriminante (Δ)", width=200)
        x1_input = TextField(label="Valor de x1", width=200)
        x2_input = TextField(label="Valor de x2", width=200)
        feedback = Text(value="", size=16, color='red')

        # Respostas corretas
        correct_a = "1"
        correct_b = "-5"
        correct_c = "6"
        correct_delta = "1"
        correct_x1 = "3"
        correct_x2 = "2"

        # Função para verificar se os valores são numéricos
        def is_numeric(value):
            try:
                float(value)  # Tenta converter para float
                return True
            except ValueError:
                return False

        # Função para verificar as respostas
        def check_answers(e):
            # Verificar se todos os valores inseridos são numéricos
            if not is_numeric(coef_a.value) or not is_numeric(coef_b.value) or not is_numeric(coef_c.value):
                feedback.value = "Por favor, insira apenas números nos coeficientes."
            elif not is_numeric(delta_input.value) or not is_numeric(x1_input.value) or not is_numeric(x2_input.value):
                feedback.value = "Por favor, insira apenas números no discriminante e nas raízes."
            elif coef_a.value != correct_a:
                feedback.value = "Coeficiente 'a' incorreto. Lembre-se que o sinal acompanha os coeficientes. Tente novamente."
            elif coef_b.value != correct_b:
                feedback.value = "Coeficiente 'b' incorreto. Lembre-se que o sinal acompanha os coeficientes. Tente novamente."
            elif coef_c.value != correct_c:
                feedback.value = "Coeficiente 'c' incorreto. Lembre-se que o sinal acompanha os coeficientes. Tente novamente."
            elif delta_input.value != correct_delta:
                feedback.value = "Valor do discriminante (Δ) incorreto. Lembre-se que Δ = b² - 4ac. Tente novamente."
            elif (x1_input.value != correct_x1 and x1_input.value != correct_x2) or (x2_input.value != correct_x2 and x2_input.value != correct_x1):
                feedback.value = "Valores de x1 ou x2 incorretos. Lembre-se que x1 = (-b + √Δ) / 2a e x2 = (-b - √Δ) / 2a. Tente novamente."
            else:
                feedback.value = "Você acertou as raízes."

            # Atualizar a página para exibir o feedback
            page.update()

        # Botões de verificação e voltar
        check_button = ElevatedButton(text="Verificar Respostas", on_click=check_answers)
        back_button = ElevatedButton(text="Voltar", on_click=lambda e: exibir_menu_principal(nome))

        # Adicionar todos os elementos à página
        page.add(
            Column(
                controls=[
                    exercise_title,
                    instructions,
                    coef_a,
                    coef_b,
                    coef_c,
                    delta_input,
                    x1_input,
                    x2_input,
                    check_button,
                    feedback,
                    back_button
                ],
                alignment="center",
                horizontal_alignment="center"
            )
        )

        # Atualizar a página
        page.update()
        
flet.app(target=main)
