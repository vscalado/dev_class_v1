// Funções de autenticação
async function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    const errorElement = document.getElementById('loginError');
    const submitButton = event.target.querySelector('button[type="submit"]');

    try {
        // Desabilita o botão durante o processo
        submitButton.disabled = true;
        submitButton.textContent = 'Entrando...';

        console.log('Tentando login com:', { email }); // Log para debug
        const response = await apiCall('auth/login', 'POST', { email, password });
        console.log('Resposta do login:', response); // Log para debug
        
        // Salva o token no localStorage
        localStorage.setItem('token', response.access_token);
        
        // Limpa mensagem de erro e redireciona
        errorElement.textContent = '';
        showPage('dashboardPage');
    } catch (error) {
        console.error('Erro detalhado do login:', error); // Log para debug
        errorElement.textContent = error.message || 'Erro ao fazer login';
    } finally {
        // Reabilita o botão
        submitButton.disabled = false;
        submitButton.textContent = 'Entrar';
    }
}

async function handleRegister(event) {
    event.preventDefault();
    
    const name = document.getElementById('registerName').value;
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const errorElement = document.getElementById('registerError');
    const submitButton = event.target.querySelector('button[type="submit"]');

    // Validações básicas
    if (password !== confirmPassword) {
        errorElement.textContent = 'As senhas não coincidem';
        return;
    }

    // Validações adicionais
    if (!name || !email || !password) {
        errorElement.textContent = 'Todos os campos são obrigatórios';
        return;
    }

    if (password.length < 6) {
        errorElement.textContent = 'A senha deve ter pelo menos 6 caracteres';
        return;
    }

    try {
        // Desabilita o botão durante o processo
        submitButton.disabled = true;
        submitButton.textContent = 'Cadastrando...';

        console.log('Tentando cadastrar:', { email, name }); // Log para debug
        const userData = { 
            name: name.trim(), 
            email: email.trim(), 
            password: password 
        };
        console.log('Dados do cadastro:', userData); // Log para debug

        const response = await apiCall('auth/register', 'POST', userData);
        console.log('Resposta do cadastro:', response); // Log para debug

        // Limpa mensagem de erro e redireciona para login
        errorElement.textContent = '';
        alert('Cadastro realizado com sucesso! Faça login para continuar.');
        
        // Limpa o formulário
        event.target.reset();
        
        showPage('loginPage');
    } catch (error) {
        console.error('Erro detalhado do cadastro:', error); // Log para debug
        let mensagemErro = error.message || 'Erro ao fazer cadastro';
        
        // Trata mensagens específicas
        if (mensagemErro === 'Email já registrado') {
            mensagemErro = 'Este email já está cadastrado. Por favor, use outro email ou faça login.';
        }
        
        errorElement.textContent = mensagemErro;
    } finally {
        // Reabilita o botão
        submitButton.disabled = false;
        submitButton.textContent = 'Cadastrar';
    }
}