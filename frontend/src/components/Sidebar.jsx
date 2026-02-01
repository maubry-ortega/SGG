import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { LayoutDashboard, BookOpen, Users, Settings, LogOut, Shield, User } from 'lucide-react';
import { toast } from 'sonner';

const Sidebar = ({ isCorporate, toggleTheme }) => {
    const navigate = useNavigate();
    const location = useLocation();

    const NavItem = ({ icon, label, path, active = false, onClick }) => {
        const isActive = location.pathname === path || active;
        return (
            <div
                onClick={onClick || (() => navigate(path))}
                className={`
                    p-4 rounded-2xl flex items-center gap-4 cursor-pointer transition-all duration-300 font-bold
                    ${isActive ? 'bg-white/10 text-white shadow-xl border border-white/10' : 'text-slate-400 hover:bg-white/5 hover:text-white'}
                `}
            >
                {React.cloneElement(icon, { className: isActive ? 'text-[var(--primary-color)]' : '' })}
                <span>{label}</span>
            </div>
        );
    };

    const handleLogout = () => {
        localStorage.removeItem('user');
        localStorage.removeItem('access_token');
        navigate('/');
        toast.info("Sesión cerrada correctamente");
    };

    return (
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
                <NavItem icon={<LayoutDashboard size={22} />} label="Dashboard" path="/dashboard" />
                <NavItem icon={<BookOpen size={22} />} label="Recursos" path="/resources" />
                <NavItem icon={<Users size={22} />} label="Comunidad" path="/community" onClick={() => toast.info("Comunidad próximamente")} />
                <NavItem icon={<TrendingUp size={22} />} label="Analíticas" path="/analytics" onClick={() => toast.info("Analíticas próximamente")} />
            </nav>

            <div className="mt-auto space-y-4 pt-8 border-t border-white/5">
                <button
                    onClick={toggleTheme}
                    className="w-full flex items-center gap-3 p-4 rounded-2xl bg-white/5 hover:bg-white/10 transition-all border border-white/10 text-sm font-bold"
                >
                    <div className={`w-3 h-3 rounded-full ${isCorporate ? 'bg-cyan-400' : 'bg-energy-orange'}`}></div>
                    Ver Modo {isCorporate ? 'Comunidad' : 'Corporativo'}
                </button>

                <NavItem icon={<Settings size={22} />} label="Configuración" path="/settings" />
                <NavItem icon={<User size={22} />} label="Mi Perfil" path="/profile" />
                <div
                    onClick={handleLogout}
                    className="p-4 rounded-2xl flex items-center gap-4 text-red-400 hover:bg-red-500/10 transition-all cursor-pointer font-bold"
                >
                    <LogOut size={22} /> <span>Cerrar Sesión</span>
                </div>
            </div>
        </aside>
    );
};

// Internal icons helper since TrendingUp was missing in some places
const TrendingUp = ({ size, className }) => (
    <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>
);

export default Sidebar;
