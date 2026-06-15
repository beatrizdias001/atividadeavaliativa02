from django.shortcuts import render, redirect

def index(request):
    """Renderiza a página inicial com o formulário de avaliação"""
    return render(request, 'index.html')

def avaliacao(request):
    """Processa a avaliação do livro com validação de dados"""
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        comentario = request.POST.get('comentario', '').strip()
        nota = request.POST.get('nota', '').strip()
        
        # Validações
        erros = []
        
        if len(nome) < 3:
            erros.append('O nome deve ter pelo menos 3 caracteres.')
        
        if len(comentario) < 10:
            erros.append('O comentário deve ter pelo menos 10 caracteres.')
        
        try:
            nota_int = int(nota)
            if nota_int < 1 or nota_int > 5:
                erros.append('A nota deve estar entre 1 e 5.')
        except (ValueError, TypeError):
            erros.append('A nota é inválida.')
        
        # Se houver erros, redireciona para página inicial
        if erros:
            return redirect('/')
        
        # Se todos os dados estão válidos, exibe página de sucesso
        context = {
            'nome': nome,
            'comentario': comentario,
            'nota': nota
        }
        return render(request, 'sucesso.html', context)
    
    # Se não for POST, redireciona para página inicial
    return redirect('/')
