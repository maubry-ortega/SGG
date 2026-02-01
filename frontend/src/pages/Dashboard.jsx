import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { BookOpen, Info, Zap } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'sonner';
import Sidebar from '../components/Sidebar';

const Dashboard = () => {
    const navigate = useNavigate();
    const [isCorporate, setIsCorporate] = useState(false);
    const [refreshTrigger, setRefreshTrigger] = useState(0);
    const [user, setUser] = useState({ username: 'Invitado', role: 'usuario' });

    useEffect(() => {
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
            setUser(JSON.parse(storedUser));
        } else {
            navigate('/login');
        }
    }, [navigate]);

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
        { label: "Global Guías Completadas", value: user.completed_guides_count || 0, icon: <BookOpen size={20} />, onClick: () => handleSoon("Guías") },
        { label: "Global Recursos Guardados", value: user.saved_resources_count || 0, icon: <Info size={20} />, onClick: () => handleSoon("Recursos") },
        { label: "Global Saggi Points", value: user.points?.toLocaleString() || 0, icon: <Zap size={20} />, accent: true, onClick: () => toast.info("¡Gana puntos compartiendo recursos!") },
    ];

    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} transition-colors duration-700`}>
            {/* Sidebar Component */}
            <Sidebar isCorporate={isCorporate} toggleTheme={toggleTheme} />

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
                        <p className="text-slate-400 text-lg font-medium tracking-tight">
                            Bienvenido de vuelta, <span className="text-white capitalize font-black">{user.username}</span>.
                        </p>
                    </div>

                    <div className="flex items-center gap-6">
                        <div className="text-right hidden sm:block">
                            <p className="text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">{user.role}</p>
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

                {/* Rewards System Info Box */}
                <motion.div
                    initial={{ opacity: 0, y: 10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mb-16 p-8 glass border-cyan-400/20 rounded-[2.5rem] flex flex-col md:flex-row items-center gap-8 relative z-10 overflow-hidden group"
                >
                    <div className="absolute top-0 right-0 w-64 h-64 bg-cyan-400/5 blur-[80px] rounded-full group-hover:bg-cyan-400/10 transition-colors"></div>
                    <div className="w-20 h-20 bg-cyan-400/10 rounded-3xl flex items-center justify-center text-cyan-400 shrink-0 shadow-lg shadow-cyan-400/10">
                        <Zap size={40} className="animate-pulse" />
                    </div>
                    <div className="flex-1 text-center md:text-left">
                        <h4 className="text-xl font-black mb-2 tracking-tight">Ecosistema de Recompensas</h4>
                        <p className="text-slate-400 font-medium leading-relaxed max-w-2xl">
                            ¿Sabías que puedes ganar <span className="text-cyan-400 font-bold">50 Saggi Points</span> por cada PDF que subas?
                            Una vez que un administrador valide tu aporte, los puntos se sumarán a tu perfil global.
                            ¡Pronto podrás canjearlos por insignias y funciones exclusivas!
                        </p>
                    </div>
                    <button
                        onClick={() => navigate('/resources')}
                        className="btn-primary py-4 px-10 shrink-0 shadow-cyan-500/20"
                    >
                        Subir PDF Ahora
                    </button>
                </motion.div>

                <div className="glass-card flex flex-col md:flex-row items-center justify-between gap-8 mb-20 relative z-10">
                    <div className="flex items-center gap-6 text-center md:text-left">
                        <div className="w-16 h-16 glass rounded-2xl flex items-center justify-center text-cyan-400">
                            <BookOpen size={32} />
                        </div>
                        <div>
                            <h3 className="text-2xl font-black mb-1">Navegar por Recursos</h3>
                            <p className="text-slate-400 max-w-sm">Accede al catálogo completo de guías y PDFs validados por la red.</p>
                        </div>
                    </div>
                    <button onClick={() => navigate('/resources')} className="btn-primary py-4 px-10">Explorar Catálogo</button>
                </div>
            </main>
        </div>
    );
};

export default Dashboard;
