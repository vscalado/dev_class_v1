/* Importa o tema */
import { theme } from './theme';

/* Injeta as variáveis CSS globalmente */
document.documentElement.style.setProperty('--bg-primary', theme.background);
document.documentElement.style.setProperty('--bg-surface', theme.surface);
document.documentElement.style.setProperty('--color-primary', theme.primary);
document.documentElement.style.setProperty('--text-primary', theme.textPrimary);
document.documentElement.style.setProperty('--text-secondary', theme.textSecondary);
document.documentElement.style.setProperty('--input-bg', theme.inputBg);
document.documentElement.style.setProperty('--input-border', theme.inputBorder);
document.documentElement.style.setProperty('--input-text', theme.inputText);
document.documentElement.style.setProperty('--button-primary', theme.buttonPrimary);
document.documentElement.style.setProperty('--button-secondary', theme.buttonSecondary);
document.documentElement.style.setProperty('--button-hover', theme.buttonHover);
document.documentElement.style.setProperty('--color-success', theme.success);
document.documentElement.style.setProperty('--color-error', theme.error);
document.documentElement.style.setProperty('--color-warning', theme.warning);