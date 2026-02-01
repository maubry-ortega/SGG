import React, { useState } from 'react';
import axios from 'axios';
import { User, Mail, UserPlus, CheckCircle, ArrowRight, ArrowLeft, HeartHandshake } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';

const Register = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        full_name: '',
        email: '',
        username: ''
    });
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const response = await axios.post('http://localhost:8000/api/v1/users/', formData);
            setSuccess(true);
        } catch (err) {
            const message = err.response?.data?.detail || 'Error al conectar con el servidor';
            setError(typeof message === 'string' ? message : 'Error en el registro');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center p-8 bg-midnight relative overflow-hidden">
            {/* Background Decor */}
            <div className="absolute -top-24 -left-24 w-[600px] h-[600px] bg-cyan-500/5 blur-[120px] rounded-full -z-10"></div>
            <div className="absolute -bottom-24 -right-24 w-[600px] h-[600px] bg-cyber-purple/5 blur-[120px] rounded-full -z-10"></div>

            <div className="max-w-6xl w-full flex flex-col lg:flex-row-reverse items-center gap-16">

                {/* Left Side (Actually Right on Desktop): Mascot & Welcome */}
                <motion.div
                    initial={{ opacity: 0, x: 50 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="flex-1 hidden lg:flex flex-col items-center text-center space-y-8"
                >
                    <div className="mascot-container w-full max-w-sm relative">
                        <div className="mascot-glow scale-150 opacity-10 bg-cyan-400"></div>
                        <img src="/assets/pulpo_usuarios.png" className="w-full animate-float scale-x-[-1]" alt="Saggi Welcome" />
                    </div>
                    <div>
                        <h2 className="text-4xl font-black mb-4">¡Únete a la Red!</h2>
                        <p className="text-slate-400 max-w-sm mx-auto font-medium">
                            Comienza tu viaje en SAGGI. Un solo registro para acceder a un mundo de conocimiento organizado.
                        </p>
                    </div>
                </motion.div>

                {/* Content Side */}
                <motion.div
                    initial={{ opacity: 0, x: -50 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="w-full max-w-md"
                >
                    <div className="glass-card shadow-[0_50px_100px_-20px_rgba(0,0,0,0.5)] border-white/5 relative">
                        <button
                            onClick={() => navigate('/')}
                            className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-slate-500 hover:text-white mb-10 transition-colors"
                        >
                            <ArrowLeft size={14} /> Volver
                        </button>

                        <div className="mb-10 text-center lg:text-left">
                            <div className="inline-flex items-center gap-3 px-4 py-1.5 glass rounded-full mb-6 border-cyan-400/20">
                                <HeartHandshake size={14} className="text-cyan-400" />
                                <span className="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-400">Bienvenido a la Comunidad</span>
                            </div>
                            <h1 className="text-4xl font-black mb-2 tracking-tighter">Crear Cuenta</h1>
                            <p className="text-slate-400 font-medium">Regístrate para obtener tus credenciales.</p>
                        </div>

                        <AnimatePresence mode="wait">
                            {success ? (
                                <motion.div
                                    key="success"
                                    initial={{ opacity: 0, scale: 0.9 }}
                                    animate={{ opacity: 1, scale: 1 }}
                                    className="text-center space-y-8 py-8"
                                >
                                    <div className="w-24 h-24 bg-green-500/10 border border-green-500/20 rounded-3xl flex items-center justify-center mx-auto mb-6 rotate-12">
                                        <CheckCircle size={48} className="text-green-500" />
                                    </div>
                                    <div>
                                        <h2 className="text-3xl font-black mb-4 tracking-tight">¡Genial! Ya casi estás.</h2>
                                        <p className="text-slate-400 leading-relaxed font-medium">
                                            Hemos enviado tu contraseña generada a <strong className="text-white bg-white/5 px-2 py-1 rounded-lg">{formData.email}</strong>.
                                        </p>
                                    </div>
                                    <button onClick={() => navigate('/login')} className="btn-primary w-full h-16 text-lg">
                                        Ir al Login <ArrowRight size={20} className="inline ml-2" />
                                    </button>
                                </motion.div>
                            ) : (
                                <motion.form
                                    key="form"
                                    onSubmit={handleSubmit}
                                    className="space-y-6"
                                >
                                    {error && (
                                        <div className="bg-red-500/10 border border-red-500/20 text-red-400 p-4 rounded-2xl text-sm font-bold text-center">
                                            {error}
                                        </div>
                                    )}

                                    <div className="space-y-2">
                                        <label className="text-xs font-black uppercase tracking-widest text-slate-500 ml-2">Nombre Completo</label>
                                        <div className="relative">
                                            <User className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-500" size={18} />
                                            <input
                                                type="text"
                                                className="input-field pl-14"
                                                placeholder="Juan Pérez"
                                                required
                                                value={formData.full_name}
                                                onChange={(e) => setFormData({ ...formData, full_name: e.target.value })}
                                            />
                                        </div>
                                    </div>

                                    <div className="space-y-2">
                                        <label className="text-xs font-black uppercase tracking-widest text-slate-500 ml-2">Correo Electrónico</label>
                                        <div className="relative">
                                            <Mail className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-500" size={18} />
                                            <input
                                                type="email"
                                                className="input-field pl-14"
                                                placeholder="hola@ejemplo.com"
                                                required
                                                value={formData.email}
                                                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                                            />
                                        </div>
                                    </div>

                                    <div className="space-y-2">
                                        <label className="text-xs font-black uppercase tracking-widest text-slate-500 ml-2">Nombre de Usuario</label>
                                        <div className="relative">
                                            <UserPlus className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-500" size={18} />
                                            <input
                                                type="text"
                                                className="input-field pl-14"
                                                placeholder="juanperez123"
                                                required
                                                value={formData.username}
                                                onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                                            />
                                        </div>
                                    </div>

                                    <div className="pt-4">
                                        <button type="submit" disabled={loading} className="btn-primary w-full h-16 text-lg">
                                            {loading ? 'Preparando Red...' : 'Registrarme ahora'}
                                        </button>
                                    </div>

                                    <p className="text-center text-sm text-slate-500 font-medium pt-4">
                                        ¿Ya tienes cuenta? <a href="#" onClick={(e) => { e.preventDefault(); navigate('/login'); }} className="text-gradient font-black">Inicia sesión</a>
                                    </p>
                                </motion.form>
                            )}
                        </AnimatePresence>
                    </div>
                </motion.div>
            </div>
        </div>
    );
};

export default Register;
