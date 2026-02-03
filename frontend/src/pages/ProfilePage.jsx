import React, { useState, useEffect } from 'react';
import { User, Mail, Shield, Zap, Award, Edit3, Calendar, Save, X } from 'lucide-react';
import Sidebar from '../components/Sidebar';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';
import { toast } from 'sonner';
import useTheme from '../hooks/useTheme';

const ProfilePage = () => {
    const { isCorporate, toggleTheme } = useTheme();
    const [user, setUser] = useState(null);
    const [isEditing, setIsEditing] = useState(false);
    const [loading, setLoading] = useState(false);
    const [profileForm, setProfileForm] = useState({ full_name: '', email: '' });

    useEffect(() => {
        fetchUserData();
    }, []);

    const fetchUserData = async () => {
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
            const basicUser = JSON.parse(storedUser);
            try {
                const response = await axios.get(`http://localhost:8000/api/v1/users/${basicUser.id}`);
                setUser(response.data);
                setProfileForm({
                    full_name: response.data.full_name || '',
                    email: response.data.email || ''
                });
                localStorage.setItem('user', JSON.stringify({ ...basicUser, ...response.data }));
            } catch (err) {
                console.error("Error fetching fresh user data", err);
                setUser(basicUser);
                setProfileForm({
                    full_name: basicUser.full_name || '',
                    email: basicUser.email || ''
                });
            }
        }
    };

    const handleUpdateProfile = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            const response = await axios.patch(`http://localhost:8000/api/v1/users/${user.id}`, profileForm);
            setUser({ ...user, ...response.data });
            localStorage.setItem('user', JSON.stringify({ ...user, ...response.data }));
            toast.success("Perfil actualizado");
            setIsEditing(false);
        } catch (err) {
            toast.error("Error al actualizar");
        } finally {
            setLoading(false);
        }
    };

    if (!user) return null;

    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} transition-colors duration-700`}>
            <Sidebar isCorporate={isCorporate} toggleTheme={toggleTheme} />

            <main className="flex-1 p-12 overflow-y-auto relative">
                <header className="mb-16">
                    <h1 className="text-5xl font-black tracking-tight text-gradient">Tu Perfil</h1>
                    <p className="text-slate-400 text-lg font-medium">Gestiona tu identidad en el ecosistema SGG.</p>
                </header>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
                    {/* Profile Card */}
                    <div className="lg:col-span-1">
                        <div className="glass-card flex flex-col items-center text-center p-10 border-white/5">
                            <div className="w-32 h-32 glass rounded-[2.5rem] flex items-center justify-center border-white/10 shadow-2xl mb-6 overflow-hidden">
                                <img
                                    src={isCorporate ? "/assets/pulpo_corporativo.png" : "/assets/pulpo_usuarios.png"}
                                    alt="Profile"
                                    className="w-full h-full object-cover p-4"
                                />
                            </div>
                            <h2 className="text-3xl font-black tracking-tight mb-1 capitalize truncate w-full px-2" title={user.username}>
                                {user.username}
                            </h2>
                            <p className="text-cyan-400 font-bold uppercase tracking-widest text-xs mb-6">{user.role}</p>

                            <div className="w-full grid grid-cols-2 gap-4">
                                <div className="p-4 glass rounded-2xl border-white/5">
                                    <div className="text-cyan-400 mb-2 flex justify-center"><Zap size={20} /></div>
                                    <div className="text-2xl font-black italic">{user.points || 0}</div>
                                    <div className="text-[10px] text-slate-500 uppercase font-bold tracking-wider">Points</div>
                                </div>
                                <div className="p-4 glass rounded-2xl border-white/5">
                                    <div className="text-energy-orange mb-2 flex justify-center"><Award size={20} /></div>
                                    <div className="text-2xl font-black italic">Exp.</div>
                                    <div className="text-[10px] text-slate-500 uppercase font-bold tracking-wider">Status</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Details Column */}
                    <div className="lg:col-span-2 space-y-8">
                        <section className="glass-card p-10 border-white/5 relative">
                            <div className="flex justify-between items-center mb-10">
                                <h3 className="text-2xl font-black italic tracking-tight">Información de Cuenta</h3>
                                <button
                                    onClick={() => setIsEditing(true)}
                                    className="p-3 glass rounded-xl text-slate-400 hover:text-white transition-colors"
                                >
                                    <Edit3 size={18} />
                                </button>
                            </div>

                            <div className="space-y-8 overflow-hidden">
                                <div className="flex items-start gap-6">
                                    <div className="w-12 h-12 glass rounded-2xl flex items-center justify-center text-slate-500">
                                        <User size={20} />
                                    </div>
                                    <div className="overflow-hidden">
                                        <p className="text-xs font-black uppercase tracking-widest text-slate-500 mb-1">Nombre Completo</p>
                                        <p className="text-lg font-bold text-slate-200 break-words" title={user.full_name}>
                                            {user.full_name || 'Sin nombre configurado'}
                                        </p>
                                    </div>
                                </div>

                                <div className="flex items-start gap-6">
                                    <div className="w-12 h-12 glass rounded-2xl flex items-center justify-center text-slate-500">
                                        <Mail size={20} />
                                    </div>
                                    <div className="overflow-hidden">
                                        <p className="text-xs font-black uppercase tracking-widest text-slate-500 mb-1">Email</p>
                                        <p className="text-lg font-bold text-slate-200 break-words" title={user.email}>
                                            {user.email || 'Email No Configurado'}
                                        </p>
                                    </div>
                                </div>

                                <div className="flex items-start gap-6 border-t border-white/5 pt-8 mt-8">
                                    <div className="w-12 h-12 glass rounded-2xl flex items-center justify-center text-slate-500">
                                        <Shield size={20} />
                                    </div>
                                    <div>
                                        <p className="text-xs font-black uppercase tracking-widest text-slate-500 mb-1">Nivel de Seguridad</p>
                                        <p className="text-lg font-bold text-green-400 flex items-center gap-2">
                                            Protegido <Shield size={16} />
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <div className="glass-card p-8 border-cyan-400/10 text-center opacity-50">
                            <p className="text-sm font-medium italic text-slate-500">
                                Sincronizado con SAGGI Core v1.0.1
                            </p>
                        </div>
                    </div>
                </div>

                <AnimatePresence>
                    {isEditing && (
                        <div className="fixed inset-0 z-50 flex items-center justify-center p-6 bg-black/60 backdrop-blur-sm">
                            <motion.div
                                initial={{ opacity: 0, scale: 0.95 }}
                                animate={{ opacity: 1, scale: 1 }}
                                exit={{ opacity: 0, scale: 0.95 }}
                                className="glass-card w-full max-w-lg p-10 border-white/10"
                            >
                                <div className="flex justify-between items-center mb-8">
                                    <h3 className="text-2xl font-black italic">Editar Perfil</h3>
                                    <button onClick={() => setIsEditing(false)} className="text-slate-500 hover:text-white">
                                        <X size={24} />
                                    </button>
                                </div>

                                <form onSubmit={handleUpdateProfile} className="space-y-6">
                                    <div>
                                        <label className="text-[10px] font-black uppercase tracking-widest text-slate-500 mb-2 block">Nombre Completo</label>
                                        <input
                                            type="text"
                                            value={profileForm.full_name}
                                            onChange={(e) => setProfileForm({ ...profileForm, full_name: e.target.value })}
                                            className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm focus:border-cyan-400 outline-none transition-all"
                                            autoFocus
                                        />
                                    </div>
                                    <div>
                                        <label className="text-[10px] font-black uppercase tracking-widest text-slate-500 mb-2 block">Email Público</label>
                                        <input
                                            type="email"
                                            value={profileForm.email}
                                            onChange={(e) => setProfileForm({ ...profileForm, email: e.target.value })}
                                            className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm focus:border-cyan-400 outline-none transition-all"
                                        />
                                    </div>
                                    <button
                                        type="submit"
                                        disabled={loading}
                                        className="btn-primary w-full py-4 flex items-center justify-center gap-3"
                                    >
                                        <Save size={18} /> {loading ? 'Guardando...' : 'Guardar Cambios'}
                                    </button>
                                </form>
                            </motion.div>
                        </div>
                    )}
                </AnimatePresence>
            </main>
        </div>
    );
};

export default ProfilePage;
