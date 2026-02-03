import { useState, useEffect } from 'react';
import { toast } from 'sonner';

const useTheme = () => {
    const [isCorporate, setIsCorporate] = useState(() => {
        const saved = localStorage.getItem('sggi_theme');
        return saved ? JSON.parse(saved) : false;
    });

    const toggleTheme = () => {
        const newMode = !isCorporate;
        setIsCorporate(newMode);
        localStorage.setItem('sggi_theme', JSON.stringify(newMode));

        toast.success(`Modo ${newMode ? 'Corporativo' : 'Comunidad'} activado`, {
            description: newMode ? "Interfaz robusta de gestión activada." : "Ambiente de aprendizaje amigable cargado.",
        });
    };

    return { isCorporate, toggleTheme };
};

export default useTheme;
