import React from 'react';
import { motion } from 'framer-motion';
import { BookOpen, Users, Zap, Rocket, ArrowRight, MousePointer2 } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'sonner';

const LandingPage = () => {
    const navigate = useNavigate();

    const handleSoon = (feature) => {
        toast.info(`${feature} estará disponible próximamente.`, {
            description: "Estamos trabajando en ello.",
        });
    };

    const features = [
        {
            icon: <BookOpen />,
            title: "Guías Académicas",
            description: "Organización modular de tus recursos de estudio con un diseño pensado para aprender mejor.",
            onClick: () => navigate('/register')
        },
        {
            icon: <Zap />,
            title: "IA Saggi",
            description: "Tu pulpo tecnológico te acompaña y recomienda rutas de aprendizaje personalizadas.",
            onClick: () => handleSoon("IA Saggi")
        },
        {
            icon: <Users />,
            title: "Comunidad",
            description: "Comparte conocimientos en un entorno amigable y colaborativo.",
            onClick: () => handleSoon("Comunidad")
        }
    ];

    return (
        <div className="min-h-screen selection:bg-cyan-500/30">
            {/* Navbar */}
            <nav className="p-8 flex justify-between items-center max-w-7xl mx-auto relative z-10">
                <div className="flex items-center gap-3">
                    <div className="w-12 h-12 bg-gradient-to-br from-cyber-blue to-cyan-400 rounded-2xl flex items-center justify-center shadow-lg shadow-cyber-blue/20">
                        <Rocket className="text-white" size={24} />
                    </div>
                    <span className="text-3xl font-black tracking-tighter text-gradient">SAGGI</span>
                </div>
                <div className="flex gap-6 items-center">
                    <button onClick={() => navigate('/login')} className="font-bold text-slate-300 hover:text-white transition-colors">Login</button>
                    <button onClick={() => navigate('/register')} className="btn-primary">Registrarse</button>
                </div>
            </nav>

            {/* Hero Section */}
            <header className="max-w-7xl mx-auto px-8 pt-10 pb-32 flex flex-col lg:flex-row items-center gap-16 relative">
                <div className="flex-1 text-center lg:text-left z-10">
                    <motion.div
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        className="inline-flex items-center gap-2 px-6 py-2 glass rounded-full mb-8"
                    >
                        <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
                        <span className="text-xs font-black uppercase tracking-[0.2em] text-cyan-300">Asistente de Aprendizaje Inteligente</span>
                    </motion.div>

                    <motion.h1
                        initial={{ opacity: 0, y: 30 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="text-6xl md:text-8xl font-black tracking-tighter mb-8 leading-[0.9]"
                    >
                        Aprende con <br />
                        <span className="text-gradient">Inteligencia.</span>
                    </motion.h1>

                    <motion.p
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.1 }}
                        className="text-xl text-slate-400 max-w-xl mb-12 leading-relaxed font-medium"
                    >
                        Descubre una forma más organizada y dinámica de estudiar.
                        Saggi, tu compañero tecnológico, simplifica tus procesos académicos.
                    </motion.p>

                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.2 }}
                        className="flex flex-col sm:flex-row gap-6 justify-center lg:justify-start"
                    >
                        <button onClick={() => navigate('/register')} className="btn-primary text-lg">Empezar a Estudiar</button>
                        <button onClick={() => handleSoon("Explorador de Recursos")} className="btn-secondary text-lg flex items-center gap-2 group">
                            Explorar Recursos <ArrowRight size={20} className="group-hover:translate-x-1 transition-transform" />
                        </button>
                    </motion.div>
                </div>

                {/* Mascot Column */}
                <div className="flex-1 mascot-container">
                    <div className="mascot-glow"></div>
                    <motion.div
                        initial={{ opacity: 0, scale: 0.8, rotate: -5 }}
                        animate={{ opacity: 1, scale: 1, rotate: 0 }}
                        transition={{ duration: 0.8, type: 'spring' }}
                        className="animate-float"
                    >
                        <img
                            src="/assets/pulpo_usuarios.png"
                            alt="Saggi Mascot Community"
                            className="max-w-[500px] drop-shadow-[0_0_50px_rgba(59,130,246,0.3)]"
                        />
                    </motion.div>

                    {/* Floating UI elements decoration */}
                    <motion.div
                        animate={{ y: [0, -10, 0] }}
                        transition={{ duration: 4, repeat: Infinity }}
                        className="absolute top-10 right-0 glass p-4 rounded-2xl shadow-xl border-cyan-400/20"
                    >
                        <MousePointer2 className="text-cyan-400" />
                    </motion.div>
                </div>
            </header>

            {/* Stats / Features */}
            <section className="bg-white/5 py-32 border-y border-white/5">
                <div className="max-w-7xl mx-auto px-8 grid md:grid-cols-3 gap-12">
                    {features.map((feature, idx) => (
                        <div key={idx} onClick={feature.onClick} className="flex flex-col items-center text-center cursor-pointer group">
                            <div className="w-16 h-16 bg-white/5 rounded-3xl flex items-center justify-center mb-8 text-cyan-400 shadow-inner group-hover:scale-110 transition-transform">
                                {React.cloneElement(feature.icon, { size: 32 })}
                            </div>
                            <h3 className="text-2xl font-black mb-4">{feature.title}</h3>
                            <p className="text-slate-400 font-medium">{feature.description}</p>
                        </div>
                    ))}
                </div>
            </section>

            {/* Footer */}
            <footer className="py-16 text-center text-slate-500 text-sm font-bold uppercase tracking-widest border-t border-white/5 mx-8">
                <div className="flex justify-center gap-8 mb-4">
                    <a href="#" onClick={(e) => { e.preventDefault(); handleSoon("Privacidad"); }} className="hover:text-white transition-colors">Privacidad</a>
                    <a href="#" onClick={(e) => { e.preventDefault(); handleSoon("Términos"); }} className="hover:text-white transition-colors">Términos</a>
                    <a href="#" onClick={(e) => { e.preventDefault(); handleSoon("Contacto"); }} className="hover:text-white transition-colors">Contacto</a>
                </div>
                &copy; 2026 SAGGI GRID GOVERNANCE - AMPIU TEAM
            </footer>
        </div>
    );
};

export default LandingPage;
