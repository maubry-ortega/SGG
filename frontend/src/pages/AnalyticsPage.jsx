import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { BarChart3, TrendingUp, Target, Award, Info, Zap, Download, Eye } from 'lucide-react';
import Sidebar from '../components/Sidebar';
import useTheme from '../hooks/useTheme';

const AnalyticsPage = () => {
    const { isCorporate, toggleTheme } = useTheme();
    const [user, setUser] = useState(null);

    useEffect(() => {
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
            setUser(JSON.parse(storedUser));
        }
    }, []);

    if (!user) return null;

    // Mock data for visualizations
    const momentumData = [40, 60, 45, 80, 70, 90, 100];
    const categories = [
        { name: "Desarrollo PDF", value: 85, color: "bg-cyan-400" },
        { name: "Colaboración", value: 65, color: "bg-energy-orange" },
        { name: "Gestión SGG", value: 45, color: "bg-cyber-blue" },
        { name: "Consistencia", value: 95, color: "bg-green-400" },
    ];

    const StatCard = ({ icon, label, value, sublabel }) => (
        <div className="glass-card p-8 border-white/5 relative overflow-hidden group hover:scale-[1.02] transition-transform">
            <div className="absolute top-0 right-0 w-32 h-32 bg-white/5 blur-3xl rounded-full translate-x-10 -translate-y-10 group-hover:bg-white/10 transition-colors"></div>
            <div className="flex items-center gap-4 mb-4">
                <div className="w-10 h-10 glass rounded-xl flex items-center justify-center text-cyber-blue">
                    {icon}
                </div>
                <span className="text-xs font-black uppercase tracking-widest text-slate-500">{label}</span>
            </div>
            <div className="text-4xl font-black italic mb-1">{value}</div>
            <p className="text-[10px] text-slate-500 font-bold">{sublabel}</p>
        </div>
    );

    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} transition-colors duration-700`}>
            <Sidebar isCorporate={isCorporate} toggleTheme={toggleTheme} />

            <main className="flex-1 p-12 overflow-y-auto relative">
                <header className="mb-16">
                    <h1 className="text-5xl font-black tracking-tight text-gradient">Analíticas Avanzadas</h1>
                    <p className="text-slate-400 text-lg font-medium">Visualiza tu crecimiento e impacto en la red SGG.</p>
                </header>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-16">
                    <StatCard icon={<Zap size={20} />} label="Total Puntos" value={user.points || 0} sublabel="Potencia acumulada" />
                    <StatCard icon={<TrendingUp size={20} />} label="Progreso" value="84%" sublabel="Hacia el próximo rango" />
                    <StatCard icon={<Eye size={20} />} label="Impacto" value="1.2k" sublabel="Visualizaciones totales" />
                    <StatCard icon={<Award size={20} />} label="Rango" value="Master" sublabel="Nivel de contribución" />
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
                    {/* Momentum Chart */}
                    <section className="glass-card p-10 border-white/5">
                        <div className="flex items-center justify-between mb-10">
                            <h3 className="text-2xl font-black italic tracking-tight flex items-center gap-3">
                                <ActivityIcon size={24} className="text-cyan-400" /> Momentum Semanal
                            </h3>
                            <div className="flex gap-2">
                                <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
                                <span className="text-[10px] font-black text-slate-500 uppercase">Live Data</span>
                            </div>
                        </div>

                        <div className="h-64 flex items-end gap-2 px-2">
                            {momentumData.map((val, i) => (
                                <motion.div
                                    key={i}
                                    initial={{ height: 0 }}
                                    animate={{ height: `${val}%` }}
                                    transition={{ duration: 1, delay: i * 0.1 }}
                                    className="flex-1 bg-gradient-to-t from-cyber-blue/20 to-cyan-400/40 rounded-t-xl border-t border-cyan-400/30 group relative"
                                >
                                    <div className="opacity-0 group-hover:opacity-100 absolute -top-10 left-1/2 -translate-x-1/2 glass px-2 py-1 rounded text-[10px] font-black transition-opacity">
                                        {val}pts
                                    </div>
                                </motion.div>
                            ))}
                        </div>
                        <div className="flex justify-between mt-6 px-1 text-[10px] font-black text-slate-600 uppercase tracking-widest">
                            <span>Lun</span><span>Mar</span><span>Mie</span><span>Jue</span><span>Vie</span><span>Sab</span><span>Dom</span>
                        </div>
                    </section>

                    {/* Skill Distribution */}
                    <section className="glass-card p-10 border-white/5">
                        <h3 className="text-2xl font-black italic tracking-tight flex items-center gap-3 mb-10">
                            <Target size={24} className="text-energy-orange" /> Distribución de Habilidades
                        </h3>
                        <div className="space-y-8">
                            {categories.map((cat, i) => (
                                <div key={i}>
                                    <div className="flex justify-between mb-2">
                                        <span className="text-xs font-black uppercase tracking-widest text-slate-400">{cat.name}</span>
                                        <span className="text-xs font-black italic">{cat.value}%</span>
                                    </div>
                                    <div className="h-2 w-full bg-white/5 rounded-full overflow-hidden">
                                        <motion.div
                                            initial={{ width: 0 }}
                                            animate={{ width: `${cat.value}%` }}
                                            transition={{ duration: 1.5, delay: i * 0.2 }}
                                            className={`h-full ${cat.color} shadow-[0_0_15px_rgba(34,211,238,0.3)]`}
                                        ></motion.div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </section>
                </div>

                <div className="mt-16 p-8 glass border-white/5 rounded-[2.5rem] flex items-center justify-between opacity-60">
                    <div className="flex items-center gap-6">
                        <div className="w-14 h-14 glass rounded-2xl flex items-center justify-center text-slate-500">
                            <Info size={24} />
                        </div>
                        <div>
                            <p className="font-black italic text-lg leading-tight text-slate-300">Generación de Reportes</p>
                            <p className="text-sm text-slate-500 font-medium">Exportación avanzada disponible para perfiles Verificados.</p>
                        </div>
                    </div>
                    <button className="px-8 py-3 glass rounded-xl text-xs font-black uppercase tracking-widest opacity-50 cursor-not-allowed border-white/10">
                        Descargar PDF Log
                    </button>
                </div>
            </main>
        </div>
    );
};

const ActivityIcon = ({ size, className }) => (
    <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
);

export default AnalyticsPage;
