from django.shortcuts import render
# Create your views here.


def home(request):
    lista = {'lista': [{
        'receita': "Pão de Queijo",
        'autor': "Luara Vasconcelos",
        'data': "02/07/2023 às 19:00",
        'conteudo': "O pão de queijo é uma iguaria oriunda de Minas Gerais, muito difundida em todo o Brasil. Embora não haja registro de local e época exata de sua criação, há consenso de que tenha se originado em Minas Gerais em meados do Século XVIII.Em meados de 2023, foi eleito uma das melhores comidas do mundo por um site estrangeiro de gastronomia, ficando em terceiro na categoria café da manhã.",
        'imagem': "https://amopaocaseiro.com.br/wp-content/uploads/2022/08/yt-069_pao-de-queijo_receita.jpg",
        'tempo': "1 hora",
        'porcao': "15 unidades"
    }, {
        'receita': "Pastel com caldo de cana",
        'autor': "Gustavo Prates",
        'data': "01/07/2023 às 18:00",
        'conteudo': "O pastel com caldo de cana é tradição nas feiras livres e nos botecos. Uma combinação que resiste ao tempo e se reinventa para conquistar novos paladares.A massa do pastel foi usada por imigrantes japoneses em São Paulo, nos anos 40, para evitar discriminação no país durante a Segunda Guerra Mundial, uma vez que o Japão apoiou a Alemanha. O caldo de cana começou a ser produzido e consumido por pessoas negras escravizadas nos engenhos de cana-de-açúcar.",
        'imagem': "https://i0.wp.com/bernadetealves.com/wp-content/uploads/2021/12/Pastel-e-caldo-de-cana-combinacao-que-resiste-ao-tempo-e-se-reinventa-Bernadete-Alves.jpg?resize=1024%2C683&ssl=1",
        'tempo': "40 minutos",
        'porcao': "5 unidades"
    }, {
        'receita': "Feijoada",
        'autor': "Gustavo Prates",
        'data': "02/07/2023 às 18:18",
        'conteudo': "Um dos pratos mais deliciosos do Brasil é com certeza a feijoada. Feita em várias partes do país é a pedida perfeita para os dias mais frios mas também bem vinda com refrescos. A receita vem do tempo da escravidão. É, com certeza uma das comidas brasileiras mais famosas! Geralmente se come às quartas ou aos sábados. ",
        'imagem': "https://assets.turismocity.com/cdn-cgi/image/format=auto,width=1400,fit=scale-down/feijoada-comida-tipica-brasileira.jpg",
        'tempo': "2 horas",
        'porcao': "20 porções"
    }, {
        'receita': "Farofa",
        'autor': "Gustavo Prates",
        'data': "02/07/2023 às 18:34",
        'conteudo': "Farofa é uma receita versátil que combina com o almoço, jantar e também com a ceia de Natal. Feita com farinha de mandioca, a receita fica bastante temperada com ingredientes como bacon, linguiça, uva-passa, salsinha e hortelã.",
        'imagem': "https://s2-receitas.glbimg.com/TIY_7fKDaUMPuXRCwYs6kqjk0rg=/0x0:1920x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_1f540e0b94d8437dbbc39d567a1dee68/internal_photos/bs/2022/y/k/phJx1yS5Gm7ea2NydVUA/farofa.jpg",
        'tempo': "30 minutos",
        'porcao': "10 porções"
    }]}

    return render(request, 'recipes/pages/home.html', lista)


def contact(request):
    content = "Contact"
    return render(request, 'recipes/contact.html', {'content': content})
