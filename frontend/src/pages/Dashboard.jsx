import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { LayoutDashboard, BookOpen, Users, Settings, LogOut, Shield, Zap, TrendingUp, Info } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'sonner';

const Dashboard = () => {
    const navigate = useNavigate();
    const [isCorporate, setIsCorporate] = useState(false);

    const toggleTheme = () => {
        const newMode = !isCorporate;
        setIsCorporate(newMode);
        toast.success(`Modo ${newMode ? 'Corporativo' : 'Comunidad'} activado`, {
            description: newMode ? "Interfaz robusta de gestión activada." : "Ambiente de aprendizaje amigable cargado.",
        });
    };

    const handleSoon = (feature) => {
        toast.info(`${feature} llegará pronto.`, {
            description: "Seguimos optimizando el motor SGG.",
        });
    };

    const stats = [
        { label: "Guías Completadas", value: "12", icon: <BookOpen size={20} />, onClick: () => handleSoon("Guías") },
        { label: "Recursos Guardados", value: "45", icon: <Info size={20} />, onClick: () => handleSoon("Recursos") },
        { label: "Puntos Saggi", value: "1,250", icon: <Zap size={20} />, accent: true, onClick: () => handleSoon("Puntos") },
    ];

    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} transition-colors duration-700`}>
            {/* Sidebar */}
            <aside className="w-80 glass border-r border-white/5 flex flex-col p-8 z-20">
                <div className="flex items-center gap-4 mb-16">
                    <div className={`w-12 h-12 rounded-2xl flex items-center justify-center shadow-lg transition-colors ${isCorporate ? 'bg-energy-orange shadow-energy-orange/20' : 'bg-cyber-blue shadow-cyber-blue/20'}`}>
                        <Shield size={24} className="text-white" />
                    </div>
                    <div>
                        <span className="font-black text-2xl tracking-tighter block leading-none">SAGGI</span>
                        <span className={`text-[10px] font-bold uppercase tracking-[0.3em] ${isCorporate ? 'text-energy-orange' : 'text-cyan-400'}`}>
                            {isCorporate ? 'Corporate Engine' : 'Community Shell'}
                        </span>
                    </div>
                </div>

                <nav className="flex-1 space-y-3">
                    <NavItem icon={<LayoutDashboard size={22} />} label="Dashboard" active onClick={() => toast.success("Ya estás en el Dashboard")} />
                    <NavItem icon={<BookOpen size={22} />} label="Recursos" onClick={() => handleSoon("Recursos Explorer")} />
                    <NavItem icon={<Users size={22} />} label="Comunidad" onClick={() => handleSoon("Social Hub")} />
                    <NavItem icon={<TrendingUp size={22} />} label="Analíticas" onClick={() => handleSoon("Advanced Analytics")} />
                </nav>

                <div className="mt-auto space-y-4 pt-8 border-t border-white/5">
                    {/* Theme Toggle Button - For Demo purposes */}
                    <button
                        onClick={toggleTheme}
                        className="w-full flex items-center gap-3 p-4 rounded-2xl bg-white/5 hover:bg-white/10 transition-all border border-white/10 text-sm font-bold"
                    >
                        <div className={`w-3 h-3 rounded-full ${isCorporate ? 'bg-cyan-400' : 'bg-energy-orange'}`}></div>
                        Ver Modo {isCorporate ? 'Comunidad' : 'Corporativo'}
                    </button>

                    <NavItem icon={<Settings size={22} />} label="Configuración" onClick={() => handleSoon("Ajustes de Perfil")} />
                    <div
                        onClick={() => navigate('/')}
                        className="p-4 rounded-2xl flex items-center gap-4 text-red-400 hover:bg-red-500/10 transition-all cursor-pointer font-bold"
                    >
                        <LogOut size={22} /> <span>Cerrar Sesión</span>
                    </div>
                </div>
            </aside>

            {/* Main Content */}
            <main className="flex-1 p-12 overflow-y-auto relative">
                {/* Background Mascot Background - Positioned and transparent */}
                <div className="fixed top-1/2 right-0 -translate-y-1/2 translate-x-1/4 opacity-[0.03] select-none pointer-events-none -z-0">
                    <img
                        src={isCorporate ? "/assets/pulpo_corporativo.png" : "/assets/pulpo_usuarios.png"}
                        alt="Mascot Watermark"
                        className="w-[800px]"
                    />
                </div>

                <header className="flex justify-between items-start mb-16 relative z-10">
                    <div>
                        <motion.h1
                            key={isCorporate ? 'corp' : 'comm'}
                            initial={{ opacity: 0, x: -20 }}
                            animate={{ opacity: 1, x: 0 }}
                            className="text-5xl font-black tracking-tight mb-2"
                        >
                            Panel de {isCorporate ? 'Gestión' : 'Estudio'}
                        </motion.h1>
                        <p className="text-slate-400 text-lg font-medium">Bienvenido de vuelta, <span className="text-white">Maubry</span>.</p>
                    </div>

                    <div className="flex items-center gap-6">
                        <div className="text-right hidden sm:block">
                            <p className="text-xs font-black text-slate-500 uppercase tracking-widest">Nivel 4</p>
                            <p className="font-bold text-gradient">Saggi Expert</p>
                        </div>
                        <div className="w-16 h-16 glass rounded-2xl flex items-center justify-center border-white/20 shadow-xl overflow-hidden">
                            <img src={isCorporate ? "/assets/pulpo_corporativo.png" : "/assets/pulpo_usuarios.png"} alt="avatar" className="w-full h-full object-cover p-2" />
                        </div>
                    </div>
                </header>

                {/* Stats Grid */}
                <section className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-16 relative z-10">
                    {stats.map((stat, idx) => (
                        <motion.div
                            key={idx}
                            onClick={stat.onClick}
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: idx * 0.1 }}
                            className="glass-card group cursor-pointer"
                        >
                            <div className="flex justify-between items-start mb-6">
                                <div className={`p-4 rounded-2xl bg-white/5 transition-colors group-hover:bg-[var(--primary-color)]/10 ${stat.accent ? 'text-gradient' : 'text-slate-400'}`}>
                                    {stat.icon}
                                </div>
                                <div className="text-[10px] font-black uppercase tracking-widest text-slate-500">Global</div>
                            </div>
                            <p className="text-slate-400 text-sm font-bold uppercase tracking-wider mb-1">{stat.label}</p>
                            <div className={`text-5xl font-black italic tracking-tighter ${stat.accent ? 'text-gradient' : ''}`}>{stat.value}</div>
                        </motion.div>
                    ))}
                </section>

                {/* Featured Card */}
                <div className="grid grid-cols-1 xl:grid-cols-2 gap-8 relative z-10">
                    <div className="glass-card overflow-hidden relative">
                        <div className={`absolute top-0 right-0 w-32 h-32 blur-[80px] -z-10 ${isCorporate ? 'bg-energy-orange/40' : 'bg-cyber-blue/40'}`}></div>
                        <h3 className="text-2xl font-black mb-6">Próxima Actividad</h3>
                        <div className="flex items-center gap-6 p-6 glass border-white/5 rounded-[2rem] mb-6">
                            <div className="w-20 h-20 glass rounded-2xl flex items-center justify-center text-cyber-blue">
                                <BookOpen size={32} />
                            </div>
                            <div>
                                <h4 className="font-black text-xl">Arquitectura de Datos</h4>
                                <p className="text-slate-400 text-sm">Módulo 4: Redes Neuronales</p>
                            </div>
                        </div>
                        <button onClick={() => handleSoon("Curso de Arquitectura")} className="btn-primary w-full">Continuar Aprendizaje</button>
                    </div>

                    <div className="glass-card flex flex-col justify-center items-center text-center">
                        <img
                            src={isCorporate ? "/assets/pulpo_corporativo.png" : "/assets/pulpo_usuarios.png"}
                            className="w-40 animate-float mb-6"
                            alt="saggi"
                        />
                        <h3 className="text-2xl font-black mb-2">Saggi IA te ayuda</h3>
                        <p className="text-slate-400 max-w-xs mb-8">Base de datos actualizada. ¿Necesitas ayuda con tu última guía?</p>
                        <button onClick={() => handleSoon("Asistente Saggi")} className="btn-secondary w-full">Abrir Asistente</button>
                    </div>
                </div>
            </main>
        </div>
    );
};

const NavItem = ({ icon, label, active = false, onClick }) => (
    <div
        onClick={onClick}
        className={`
        p-4 rounded-2xl flex items-center gap-4 cursor-pointer transition-all duration-300 font-bold
        ${active ? 'bg-white/10 text-white shadow-xl border border-white/10' : 'text-slate-400 hover:bg-white/5 hover:text-white'}
      `}
    >
        {React.cloneElement(icon, { className: active ? 'text-[var(--primary-color)]' : '' })}
        <span>{label}</span>
    </div>
);

export default Dashboard;
