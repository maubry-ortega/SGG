import React, { useState, useEffect } from 'react';
import { Settings, Shield, Bell, Eye, Database, Layout, Palette, Lock, Save, Key, X } from 'lucide-react';
import Sidebar from '../components/Sidebar';
import axios from 'axios';
import { toast } from 'sonner';
import useTheme from '../hooks/useTheme';

const SettingsPage = () => {
    const { isCorporate, toggleTheme } = useTheme();
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(false);
    const [highContrast, setHighContrast] = useState(false);
    const [passwordForm, setPasswordForm] = useState({ current_password: '', new_password: '' });

    useEffect(() => {
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
            setUser(JSON.parse(storedUser));
        }
    }, []);

    const handleChangePassword = async (e) => {
        e.preventDefault();
        if (!passwordForm.new_password) return toast.error("La nueva contraseña no puede estar vacía");
        setLoading(true);
        try {
            await axios.post('http://localhost:8000/api/v1/auth/change-password', {
                user_id: user.id,
                ...passwordForm
            });
            toast.success("Contraseña actualizada con éxito");
            setPasswordForm({ current_password: '', new_password: '' });
        } catch (err) {
            toast.error(err.response?.data?.detail || "Error al cambiar contraseña");
        } finally {
            setLoading(false);
        }
    };

    const SettingSection = ({ icon, title, description, children }) => (
        <div className="glass-card p-8 border-white/5 flex flex-col xl:flex-row gap-8 items-start overflow-hidden">
            <div className="w-14 h-14 glass rounded-2xl flex items-center justify-center text-cyber-blue shrink-0 shadow-lg border-white/10">
                {icon}
            </div>
            <div className="flex-1 w-full overflow-hidden">
                <h3 className="text-xl font-black mb-2 tracking-tight break-words">{title}</h3>
                <p className="text-slate-400 text-sm mb-6 max-w-xl break-words">{description}</p>
                <div className="w-full">
                    {children}
                </div>
            </div>
        </div>
    );

    if (!user) return null;

    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} ${highContrast ? 'contrast-125' : ''} transition-all duration-700`}>
            <Sidebar isCorporate={isCorporate} toggleTheme={toggleTheme} />

            <main className="flex-1 p-12 overflow-y-auto relative">
                <header className="mb-16">
                    <h1 className="text-5xl font-black tracking-tight text-gradient">Configuraciones Generales</h1>
                    <p className="text-slate-400 text-lg font-medium italic">Calibra las funciones del sistema SAGGI.</p>
                </header>

                <div className="space-y-8 max-w-5xl pb-20">

                    {/* UI & Appearance */}
                    <SettingSection
                        icon={<Layout size={24} />}
                        title="Interfaz y Apariencia"
                        description="Modifica la calibración visual de tu entorno de trabajo."
                    >
                        <div className="flex flex-wrap gap-4">
                            <button
                                onClick={() => setHighContrast(!highContrast)}
                                className={`px-6 py-3 glass rounded-xl text-sm font-black uppercase tracking-widest transition-all ${highContrast ? 'border-cyan-400 text-cyan-400' : 'opacity-50'}`}
                            >
                                {highContrast ? 'Alto Contraste: ON' : 'Activar Alto Contraste'}
                            </button>
                            <button
                                onClick={toggleTheme}
                                className="px-6 py-3 glass rounded-xl text-sm font-black uppercase tracking-widest border-white/10 hover:border-white/20"
                            >
                                Modo {isCorporate ? 'Comunidad' : 'Corporativo'}
                            </button>
                        </div>
                    </SettingSection>

                    {/* Account Security */}
                    <SettingSection
                        icon={<Lock size={24} />}
                        title="Seguridad y Credenciales"
                        description="Gestiona tus claves de acceso. La información del perfil se edita directamente desde la página de Perfil."
                    >
                        <form onSubmit={handleChangePassword} className="space-y-6 w-full">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                                <div className="w-full">
                                    <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-500 mb-2 block">Contraseña Actual</label>
                                    <input
                                        type="password"
                                        value={passwordForm.current_password}
                                        onChange={(e) => setPasswordForm({ ...passwordForm, current_password: e.target.value })}
                                        className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm focus:border-energy-orange outline-none transition-all"
                                    />
                                </div>
                                <div className="w-full">
                                    <label className="text-[10px] font-black uppercase tracking-[0.2em] text-slate-500 mb-2 block">Nueva Contraseña</label>
                                    <input
                                        type="password"
                                        value={passwordForm.new_password}
                                        onChange={(e) => setPasswordForm({ ...passwordForm, new_password: e.target.value })}
                                        className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm focus:border-energy-orange outline-none transition-all"
                                    />
                                </div>
                            </div>
                            <button type="submit" disabled={loading} className="p-4 glass rounded-2xl text-energy-orange border-energy-orange/20 hover:bg-energy-orange/10 transition-all font-black uppercase tracking-widest text-xs flex items-center gap-2">
                                <Key size={16} /> Cambiar Contraseña
                            </button>
                        </form>
                    </SettingSection>

                    {/* Data Privacy */}
                    <SettingSection
                        icon={<Database size={24} />}
                        title="Estado de la Red"
                        description="Verifica la conexión con los nodos centrales de SAGGI."
                    >
                        <div className="flex items-center gap-4 text-slate-500 font-bold italic">
                            <div className="w-4 h-4 rounded-full bg-green-500 animate-pulse"></div>
                            Bóveda de datos sincronizada y segura
                        </div>
                    </SettingSection>

                    <div className="p-8 border-2 border-dashed border-white/5 rounded-[2.5rem] text-center opacity-40">
                        <p className="text-slate-600 font-bold uppercase tracking-[0.2em] text-xs">
                            SAGGI Professional Edition | Build v1.0.1
                        </p>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default SettingsPage;
