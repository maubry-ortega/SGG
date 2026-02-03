import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Trophy, Users, Activity, Zap, Star, MessageSquare, BookOpen } from 'lucide-react';
import axios from 'axios';
import Sidebar from '../components/Sidebar';
import useTheme from '../hooks/useTheme';

const CommunityPage = () => {
    const { isCorporate, toggleTheme } = useTheme();
    const [leaderboard, setLeaderboard] = useState([]);
    const [activities, setActivities] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const [lbRes, actRes] = await Promise.all([
                    axios.get('http://localhost:8000/api/v1/users/leaderboard'),
                    axios.get('http://localhost:8000/api/v1/resources/')
                ]);
                setLeaderboard(lbRes.data);
                setActivities(actRes.data.slice(0, 5)); // Only top 5 recent
            } catch (err) {
                console.error("Error fetching community data", err);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);


    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} transition-colors duration-700`}>
            <Sidebar isCorporate={isCorporate} toggleTheme={toggleTheme} />

            <main className="flex-1 p-12 overflow-y-auto relative">
                <header className="mb-16">
                    <h1 className="text-5xl font-black tracking-tight text-gradient">Hub de Comunidad</h1>
                    <p className="text-slate-400 text-lg font-medium">Conecta, colabora y destaca en el ecosistema SGG.</p>
                </header>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
                    {/* Leaderboard (Hall of Fame) */}
                    <section className="lg:col-span-2 space-y-8">
                        <div className="flex items-center gap-4 mb-8">
                            <div className="w-12 h-12 glass rounded-2xl flex items-center justify-center text-energy-orange">
                                <Trophy size={24} />
                            </div>
                            <h2 className="text-3xl font-black tracking-tight">Hall of Fame</h2>
                        </div>

                        <div className="space-y-4">
                            {leaderboard.map((user, idx) => (
                                <motion.div
                                    key={user.id}
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    transition={{ delay: idx * 0.1 }}
                                    className="glass-card group flex items-center justify-between p-6 border-white/5 hover:border-energy-orange/30 transition-all hover:scale-[1.01]"
                                >
                                    <div className="flex items-center gap-6">
                                        <div className={`text-2xl font-black italic w-8 ${idx < 3 ? 'text-energy-orange' : 'text-slate-600'}`}>
                                            #{idx + 1}
                                        </div>
                                        <div className="w-12 h-12 glass rounded-xl flex items-center justify-center">
                                            <Users size={20} className="text-slate-400" />
                                        </div>
                                        <div>
                                            <h4 className="font-bold text-lg capitalize">{user.username}</h4>
                                            <p className="text-xs text-slate-500 uppercase font-black tracking-widest">{user.role}</p>
                                        </div>
                                    </div>
                                    <div className="text-right">
                                        <div className="flex items-center gap-2 text-gradient text-2xl font-black italic">
                                            {user.points?.toLocaleString()} <Zap size={18} className="text-cyan-400" />
                                        </div>
                                        <p className="text-[10px] text-slate-500 uppercase font-bold tracking-tighter">Saggi Points</p>
                                    </div>
                                </motion.div>
                            ))}
                        </div>
                    </section>

                    {/* Sidebar: Activity & Stats */}
                    <aside className="space-y-12">
                        <div>
                            <div className="flex items-center gap-4 mb-8 text-cyan-400">
                                <Activity size={24} />
                                <h2 className="text-2xl font-black tracking-tight">Actividad Reciente</h2>
                            </div>
                            <div className="space-y-6">
                                {activities.map((act, idx) => (
                                    <div key={idx} className="flex gap-4 relative">
                                        {idx !== activities.length - 1 && (
                                            <div className="absolute left-[1.15rem] top-10 bottom-[-1.5rem] w-[2px] bg-white/5"></div>
                                        )}
                                        <div className="w-10 h-10 glass rounded-full flex items-center justify-center shrink-0 border-white/10">
                                            <BookOpen size={16} className="text-slate-500" />
                                        </div>
                                        <div className="pb-4">
                                            <p className="text-sm text-slate-200 font-bold leading-tight mb-1">
                                                Nuevo recurso: <span className="text-cyan-400">{act.title}</span>
                                            </p>
                                            <p className="text-[10px] text-slate-500 font-black uppercase tracking-widest leading-none">
                                                Validado hace poco
                                            </p>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>

                        <div className="glass-card p-8 border-cyan-400/20 bg-cyan-400/5">
                            <h4 className="font-black italic text-lg mb-2">¿Quieres aparecer aquí?</h4>
                            <p className="text-slate-400 text-sm mb-6">Sube recursos útiles y gana aprobación para escalar en el Hall of Fame.</p>
                            <button className="btn-primary w-full py-3">Ir a Recursos</button>
                        </div>
                    </aside>
                </div>
            </main>
        </div>
    );
};

export default CommunityPage;
