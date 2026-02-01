import React, { useState } from 'react';
import { Settings, Shield, Bell, Eye, Database, Layout, Palette, Lock } from 'lucide-react';
import Sidebar from '../components/Sidebar';

const SettingsPage = () => {
    const [isCorporate, setIsCorporate] = useState(false);
    const toggleTheme = () => setIsCorporate(!isCorporate);

    const SettingSection = ({ icon, title, description, children }) => (
        <div className="glass-card p-8 border-white/5 flex flex-col md:flex-row gap-8 items-start">
            <div className="w-14 h-14 glass rounded-2xl flex items-center justify-center text-cyber-blue shrink-0 shadow-lg border-white/10">
                {icon}
            </div>
            <div className="flex-1">
                <h3 className="text-xl font-black mb-2 tracking-tight">{title}</h3>
                <p className="text-slate-400 text-sm mb-6 max-w-xl">{description}</p>
                {children}
            </div>
        </div>
    );

    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} transition-colors duration-700`}>
            <Sidebar isCorporate={isCorporate} toggleTheme={toggleTheme} />

            <main className="flex-1 p-12 overflow-y-auto relative">
                <header className="mb-16">
                    <h1 className="text-5xl font-black tracking-tight text-gradient">Configuraciones</h1>
                    <p className="text-slate-400 text-lg font-medium">Ajusta el motor SAGGI a tus necesidades.</p>
                </header>

                <div className="space-y-8 max-w-4xl pb-20">
                    <SettingSection
                        icon={<Layout size={24} />}
                        title="Interfaz y Apariencia"
                        description="Modifica cómo visualizas el entorno SGG."
                    >
                        <div className="flex gap-4">
                            <button className="px-6 py-3 glass rounded-xl text-sm font-black uppercase tracking-widest border-cyber-blue/20 text-cyber-blue">
                                Dark Mode
                            </button>
                            <button className="px-6 py-3 glass rounded-xl text-sm font-black uppercase tracking-widest opacity-30 cursor-not-allowed">
                                High Contrast
                            </button>
                        </div>
                    </SettingSection>

                    <SettingSection
                        icon={<Lock size={24} />}
                        title="Seguridad de la Cuenta"
                        description="Protege tus credenciales y sesiones activas."
                    >
                        <button className="btn-primary py-3 px-8 text-sm">Cambiar Contraseña</button>
                    </SettingSection>

                    <SettingSection
                        icon={<Database size={24} />}
                        title="Privacidad de Datos"
                        description="Gestiona qué información compartes con la red comunitaria."
                    >
                        <div className="flex items-center gap-4 text-slate-500 font-bold italic">
                            <div className="w-4 h-4 rounded-full bg-green-500 anim-pulse"></div>
                            Sincronización encriptada activada
                        </div>
                    </SettingSection>

                    <div className="p-8 border-2 border-dashed border-white/5 rounded-[2.5rem] text-center">
                        <p className="text-slate-600 font-bold uppercase tracking-[0.2em] text-xs">
                            SAGGI Engine Alpha v1.0.0
                        </p>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default SettingsPage;
