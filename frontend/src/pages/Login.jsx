import React, { useState } from 'react';
import axios from 'axios';
import { Lock, User, Rocket, ArrowLeft, ShieldCheck } from 'lucide-react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        username: '',
        password: ''
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [loginMode, setLoginMode] = useState('community'); // 'community' or 'corporate'

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const response = await axios.post('http://localhost:8000/api/v1/auth/login', formData);
            console.log('Login successful:', response.data);

            // Store session data
            localStorage.setItem('user', JSON.stringify(response.data.user));
            localStorage.setItem('access_token', response.data.access_token);

            // Set theme based on selected login mode
            localStorage.setItem('sggi_theme', JSON.stringify(loginMode === 'corporate'));

            navigate('/dashboard');
        } catch (err) {
            setError('Usuario o contraseña incorrectos');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center p-8 bg-midnight relative overflow-hidden">
            {/* Background Decor */}
            <div className={`absolute top-0 right-0 w-[500px] h-[500px] blur-[120px] rounded-full -z-10 animate-pulse transition-colors duration-1000 ${loginMode === 'corporate' ? 'bg-energy-orange/10' : 'bg-cyber-blue/10'}`}></div>
            <div className={`absolute bottom-0 left-0 w-[500px] h-[500px] blur-[120px] rounded-full -z-10 transition-colors duration-1000 ${loginMode === 'corporate' ? 'bg-energy-orange/5' : 'bg-cyber-purple/5'}`}></div>

            <div className="max-w-6xl w-full flex flex-col lg:flex-row items-center gap-16">

                {/* Left Side: Mascot & Info */}
                <motion.div
                    key={loginMode}
                    initial={{ opacity: 0, x: -50 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="flex-1 hidden lg:flex flex-col items-center text-center space-y-8"
                >
                    <div className="mascot-container w-full max-w-sm relative">
                        <div className={`mascot-glow scale-150 ${loginMode === 'corporate' ? 'after:bg-energy-orange/30' : ''}`}></div>
                        <img
                            src={loginMode === 'corporate' ? "/assets/pulpo_corporativo.png" : "/assets/pulpo_usuarios.png"}
                            className="w-full animate-float transition-all duration-500"
                            alt="Saggi Welcome"
                        />
                    </div>
                    <div>
                        <h2 className="text-4xl font-black mb-4">
                            {loginMode === 'corporate' ? 'Gestión SGG' : 'Acceso Seguro'}
                        </h2>
                        <p className="text-slate-400 max-w-sm mx-auto font-medium">
                            {loginMode === 'corporate'
                                ? 'Entra para administrar los recursos y validar contenido de la red.'
                                : 'Saggi está listo para cargar tus recursos. Ingresa tus credenciales para continuar tu progreso.'}
                        </p>
                    </div>
                </motion.div>

                {/* Right Side: Login Card */}
                <motion.div
                    initial={{ opacity: 0, x: 50 }}
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
                            <div className="flex gap-2 mb-8 p-1 glass rounded-2xl border-white/5">
                                <button
                                    onClick={() => setLoginMode('community')}
                                    className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-xl text-[10px] font-black uppercase tracking-widest transition-all ${loginMode === 'community' ? 'bg-cyber-blue text-white shadow-lg shadow-cyber-blue/20' : 'text-slate-500 hover:text-white'}`}
                                >
                                    <Rocket size={14} /> Comunidad
                                </button>
                                <button
                                    onClick={() => setLoginMode('corporate')}
                                    className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-xl text-[10px] font-black uppercase tracking-widest transition-all ${loginMode === 'corporate' ? 'bg-energy-orange text-white shadow-lg shadow-energy-orange/20' : 'text-slate-500 hover:text-white'}`}
                                >
                                    <ShieldCheck size={14} /> Corporativo
                                </button>
                            </div>

                            <div className="inline-flex items-center gap-3 px-4 py-1.5 glass rounded-full mb-6 border-white/5">
                                {loginMode === 'corporate' ? (
                                    <>
                                        <ShieldCheck size={14} className="text-energy-orange" />
                                        <span className="text-[10px] font-black uppercase tracking-[0.2em] text-energy-orange">SGG Management Node</span>
                                    </>
                                ) : (
                                    <>
                                        <Rocket size={14} className="text-cyan-400" />
                                        <span className="text-[10px] font-black uppercase tracking-[0.2em] text-cyan-400">SGG Community Access</span>
                                    </>
                                )}
                            </div>
                            <h1 className="text-4xl font-black mb-2 tracking-tighter">Bienvenido</h1>
                            <p className="text-slate-400 font-medium">
                                {loginMode === 'corporate' ? 'Accede al panel de administración.' : 'Ingresa a tu entorno de aprendizaje.'}
                            </p>
                        </div>

                        <form onSubmit={handleSubmit} className="space-y-6">
                            {error && (
                                <motion.div
                                    initial={{ opacity: 0, scale: 0.95 }}
                                    animate={{ opacity: 1, scale: 1 }}
                                    className="bg-red-500/10 border border-red-500/20 text-red-400 p-4 rounded-2xl text-sm font-bold text-center"
                                >
                                    {error}
                                </motion.div>
                            )}

                            <div className="space-y-2">
                                <label className="text-xs font-black uppercase tracking-widest text-slate-500 ml-2">Usuario</label>
                                <div className="relative">
                                    <User className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-500" size={18} />
                                    <input
                                        type="text"
                                        className="input-field pl-14"
                                        placeholder="Tu nombre de usuario"
                                        required
                                        value={formData.username}
                                        onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                                    />
                                </div>
                            </div>

                            <div className="space-y-2">
                                <label className="text-xs font-black uppercase tracking-widest text-slate-500 ml-2">Contraseña</label>
                                <div className="relative">
                                    <Lock className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-500" size={18} />
                                    <input
                                        type="password"
                                        className="input-field pl-14"
                                        placeholder="••••••••"
                                        required
                                        value={formData.password}
                                        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                                    />
                                </div>
                            </div>

                            <div className="pt-4">
                                <button
                                    type="submit"
                                    disabled={loading}
                                    className={`w-full h-16 text-lg font-black uppercase tracking-widest rounded-2xl border-none transition-all duration-300 shadow-lg ${loginMode === 'corporate'
                                            ? 'bg-energy-orange text-white hover:bg-orange-600 shadow-energy-orange/20'
                                            : 'bg-cyber-blue text-white hover:bg-cyan-500 shadow-cyber-blue/20'
                                        }`}
                                >
                                    {loading ? 'Accediendo...' : (loginMode === 'corporate' ? 'Entrar como Admin' : 'Entrar a la Comunidad')}
                                </button>
                            </div>

                            <p className="text-center text-sm text-slate-500 font-medium tracking-tight">
                                ¿No tienes cuenta? <a href="#" onClick={(e) => { e.preventDefault(); navigate('/register'); }} className="text-gradient font-black">Únete ahora</a>
                            </p>
                        </form>
                    </div>
                </motion.div>
            </div>
        </div>
    );
};

export default Login;
