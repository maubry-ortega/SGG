import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FileText, Download, ExternalLink, ShieldCheck, Trash2, Clock, CheckCircle, UserPlus } from 'lucide-react';
import axios from 'axios';
import { toast } from 'sonner';

export const ResourceExplorer = ({ refreshTrigger, user, isCorporate }) => {
    const [resources, setResources] = useState([]);
    const [loading, setLoading] = useState(true);
    const [filter, setFilter] = useState('all');

    useEffect(() => {
        fetchResources();
    }, [refreshTrigger]);

    const fetchResources = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/v1/resources/');
            setResources(response.data);
        } catch (err) {
            toast.error("Error al cargar recursos.");
        } finally {
            setLoading(false);
        }
    };

    const handleDeleteResource = async (id) => {
        if (!window.confirm("¿Estás seguro de que deseas eliminar este recurso público?")) return;
        try {
            await axios.delete(`http://localhost:8000/api/v1/resources/${id}`);
            toast.success("Recurso eliminado correctamente.");
            fetchResources();
        } catch (err) {
            toast.error("Error al eliminar el recurso.");
        }
    };

    const categories = [
        { id: 'all', label: 'Todos' },
        { id: 'game', label: 'Gaming' },
        { id: 'tecnologia', label: 'Tecnología' },
        { id: 'agricultura', label: 'Agricultura' },
        { id: 'limpieza', label: 'Limpieza' },
        { id: 'otros', label: 'Otros' }
    ];

    const filteredResources = filter === 'all'
        ? resources
        : resources.filter(res => res.category === filter);

    if (loading) return <div className="text-center py-20 text-slate-500 font-bold">Cargando catálogo...</div>;

    return (
        <div className="space-y-8">
            <div className="flex flex-wrap gap-2">
                {categories.map(cat => (
                    <button
                        key={cat.id}
                        onClick={() => setFilter(cat.id)}
                        className={`px-4 py-2 rounded-xl text-xs font-black uppercase tracking-widest transition-all ${filter === cat.id
                            ? 'bg-cyber-blue text-white shadow-lg shadow-cyber-blue/20'
                            : 'glass text-slate-400 hover:text-white'
                            }`}
                    >
                        {cat.label}
                    </button>
                ))}
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
                {filteredResources.length === 0 ? (
                    <div className="col-span-full glass-card text-center py-20">
                        <FileText className="mx-auto mb-4 text-slate-600" size={48} />
                        <p className="text-slate-400 font-medium">No hay recursos en esta categoría.</p>
                    </div>
                ) : (
                    filteredResources.map((res) => (
                        <ResourceCard
                            key={res.id || res._id}
                            resource={res}
                            isAdmin={user?.role === 'admin'}
                            onDelete={() => handleDeleteResource(res.id || res._id)}
                        />
                    ))
                )}
            </div>
        </div>
    );
};

export const AdminResourcePanel = ({ refreshTrigger, onAction, user, isCorporate }) => {
    const [pending, setPending] = useState([]);

    useEffect(() => {
        if (isCorporate && user?.role === 'admin') {
            fetchPending();
        }
    }, [refreshTrigger, isCorporate, user]);

    const fetchPending = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/v1/resources/pending');
            setPending(response.data);
        } catch (err) {
            console.error(err);
        }
    };

    const handleApprove = async (id) => {
        try {
            await axios.patch(`http://localhost:8000/api/v1/resources/${id}/approve`);
            toast.success("Recurso aprobado correctamente.");
            onAction?.();
            fetchPending();
        } catch (err) {
            toast.error("Error al aprobar.");
        }
    };

    const handleDelete = async (id) => {
        try {
            await axios.delete(`http://localhost:8000/api/v1/resources/${id}`);
            toast.info("Recurso rechazado y eliminado.");
            onAction?.();
            fetchPending();
        } catch (err) {
            toast.error("Error al eliminar.");
        }
    };

    if (!isCorporate || user?.role !== 'admin' || pending.length === 0) return null;

    return (
        <div className="mb-12">
            <h2 className="text-2xl font-black mb-6 flex items-center gap-3">
                <ShieldCheck className="text-energy-orange" />
                Validación de Recursos ({pending.length})
            </h2>
            <div className="space-y-4">
                {pending.map((res) => (
                    <div key={res.id || res._id} className="glass border-energy-orange/20 p-6 rounded-3xl flex flex-col md:flex-row justify-between items-center gap-6">
                        <div className="flex items-center gap-4">
                            <div className="w-12 h-12 glass rounded-2xl flex items-center justify-center text-energy-orange">
                                <FileText size={20} />
                            </div>
                            <div>
                                <h4 className="font-bold text-lg">{res.title}</h4>
                                <p className="text-xs text-slate-400 line-clamp-1">{res.description}</p>
                            </div>
                        </div>
                        <div className="flex items-center gap-3">
                            <a
                                href={res.file_url.startsWith('http') ? res.file_url : `http://localhost:8000/${res.file_url}`}
                                target="_blank"
                                className="p-3 glass rounded-xl text-slate-300 hover:text-white"
                            >
                                <ExternalLink size={18} />
                            </a>
                            <button onClick={() => handleDelete(res.id || res._id)} className="p-3 glass rounded-xl text-red-400 hover:bg-red-500/10">
                                <Trash2 size={18} />
                            </button>
                            <button onClick={() => handleApprove(res.id || res._id)} className="btn-primary py-3 px-6 text-sm">
                                Aprobar PDF
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export const AdminUserPanel = ({ refreshTrigger, user, isCorporate }) => {
    const [pendingUsers, setPendingUsers] = useState([]);

    useEffect(() => {
        if (isCorporate && user?.role === 'admin') {
            fetchPendingUsers();
        }
    }, [refreshTrigger, isCorporate, user]);

    const fetchPendingUsers = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/v1/users/pending');
            setPendingUsers(response.data);
        } catch (err) {
            console.error(err);
        }
    };

    const handleActivate = async (userId) => {
        try {
            await axios.patch(`http://localhost:8000/api/v1/users/${userId}/activate`);
            toast.success("Usuario activado correctamente.");
            fetchPendingUsers();
        } catch (err) {
            toast.error("Error al activar usuario.");
        }
    };

    if (!isCorporate || user?.role !== 'admin' || pendingUsers.length === 0) return null;

    return (
        <div className="mb-12">
            <h2 className="text-2xl font-black mb-6 flex items-center gap-3">
                <UserPlus className="text-cyan-400" />
                Aprobación de Usuarios ({pendingUsers.length})
            </h2>
            <div className="space-y-4">
                {pendingUsers.map((u) => (
                    <div key={u.id} className="glass border-cyan-400/20 p-6 rounded-3xl flex flex-col md:flex-row justify-between items-center gap-6">
                        <div className="flex items-center gap-4">
                            <div className="w-12 h-12 glass rounded-2xl flex items-center justify-center text-cyan-400">
                                <UserPlus size={20} />
                            </div>
                            <div>
                                <h4 className="font-bold text-lg">{u.full_name}</h4>
                                <p className="text-xs text-slate-400">@{u.username} • {u.email}</p>
                            </div>
                        </div>
                        <button onClick={() => handleActivate(u.id)} className="btn-primary py-3 px-8 text-sm shrink-0">
                            Activar Acceso
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
};

const ResourceCard = ({ resource, isAdmin, onDelete }) => (
    <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-card group hover:scale-[1.02] transition-all"
    >
        <div className="flex justify-between items-start mb-6">
            <div className="w-12 h-12 bg-cyber-blue/10 rounded-2xl flex items-center justify-center text-cyber-blue">
                <FileText size={24} />
            </div>
            <div className="flex gap-2">
                {resource.category && (
                    <span className="text-[10px] uppercase font-black tracking-widest text-cyber-blue bg-cyber-blue/10 px-2 py-1 rounded-md">
                        {resource.category}
                    </span>
                )}
                {resource.tags.slice(0, 1).map((tag, i) => (
                    <span key={i} className="text-[10px] uppercase font-black tracking-widest text-slate-500 bg-white/5 px-2 py-1 rounded-md">
                        {tag}
                    </span>
                ))}
            </div>
        </div>
        <h3 className="text-xl font-black mb-2 line-clamp-1">{resource.title}</h3>
        <p className="text-slate-400 text-sm mb-8 line-clamp-2 h-10">{resource.description}</p>

        <div className="flex items-center justify-between pt-4 border-t border-white/5">
            <div className="flex items-center gap-2">
                <div className="flex items-center gap-2 text-xs text-slate-500 font-bold">
                    <CheckCircle size={14} className="text-green-500" /> Público
                </div>
                {isAdmin && (
                    <button
                        onClick={onDelete}
                        className="ml-2 p-2 rounded-lg text-red-400 hover:bg-red-500/10 transition-colors"
                        title="Eliminar Recurso"
                    >
                        <Trash2 size={14} />
                    </button>
                )}
            </div>
            <a
                href={resource.file_url.startsWith('http') ? resource.file_url : `http://localhost:8000/${resource.file_url}`}
                target="_blank"
                download
                className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-cyber-blue hover:text-white transition-colors"
            >
                Ver <Download size={14} />
            </a>
        </div>
    </motion.div>
);
