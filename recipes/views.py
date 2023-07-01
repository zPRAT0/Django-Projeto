from django.shortcuts import render
# Create your views here.


def home(request):
    lista = { 
        'name': [i for i in range(1, 10)] ,
        'receita': "Pastel com caldo de cana",
        'autor': "Gustavo Prates",
        'data': "01/07/2023 às 18:00",
        'conteudo': "O pastel com caldo de cana é tradição nas feiras livres e nos botecos. Uma combinação que resiste ao tempo e se reinventa para conquistar novos paladares.A massa do pastel foi usada por imigrantes japoneses em São Paulo, nos anos 40, para evitar discriminação no país durante a Segunda Guerra Mundial, uma vez que o Japão apoiou a Alemanha. O caldo de cana começou a ser produzido e consumido por pessoas negras escravizadas nos engenhos de cana-de-açúcar.",
        'imagem': "https://i0.wp.com/bernadetealves.com/wp-content/uploads/2021/12/Pastel-e-caldo-de-cana-combinacao-que-resiste-ao-tempo-e-se-reinventa-Bernadete-Alves.jpg?resize=1024%2C683&ssl=1"
        }
    return render(request, 'recipes/pages/home.html', lista)


def contact(request):
    content = "Contact"
    return render(request, 'recipes/contact.html', {'content': content})
