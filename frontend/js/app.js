// Gerenciamento de páginas
function showPage(pageId) {
    // Esconde todas as páginas
    document.querySelectorAll('.form-container, .dashboard').forEach(page => {
        page.classList.add('hidden');
    });
    
    // Mostra a página solicitada
    document.getElementById(pageId).classList.remove('hidden');
}

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    console.log('Aplicação inicializando...');
    
    // Configura os listeners dos formulários
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    
    if (loginForm) {
        console.log('Configurando evento do formulário de login');
        loginForm.addEventListener('submit', handleLogin);
    } else {
        console.error('Formulário de login não encontrado!');
    }
    
    if (registerForm) {
        console.log('Configurando evento do formulário de registro');
        registerForm.addEventListener('submit', handleRegister);
    } else {
        console.error('Formulário de registro não encontrado!');
    }

    // Verifica se já está logado
    const token = localStorage.getItem('token');
    if (token) {
        console.log('Token encontrado, redirecionando para dashboard');
        showPage('dashboardPage');
    } else {
        console.log('Sem token, mostrando página de login');
        showPage('loginPage');
    }
});

// Função de logout
function logout() {
    localStorage.removeItem('token');
    showPage('loginPage');
}