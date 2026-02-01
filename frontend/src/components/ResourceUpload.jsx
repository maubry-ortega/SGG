import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Upload, X, FileText, CheckCircle, AlertCircle } from 'lucide-react';
import axios from 'axios';
import { toast } from 'sonner';

const ResourceUpload = ({ isOpen, onClose, onUploadSuccess }) => {
    const [file, setFile] = useState(null);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [uploading, setUploading] = useState(false);

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        if (selectedFile && selectedFile.type === 'application/pdf') {
            setFile(selectedFile);
        } else {
            toast.error("Por favor selecciona un archivo PDF válido.");
            e.target.value = null;
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) return toast.error("Selecciona un archivo PDF.");

        setUploading(true);
        const formData = new FormData();
        formData.append('file', file);
        formData.append('title', title);
        formData.append('description', description);
        formData.append('level', 'basic');
        formData.append('tags', 'pdf,recurso');

        // Link with current logged-in user session
        const storedUser = localStorage.getItem('user');
        if (storedUser) {
            const userData = JSON.parse(storedUser);
            formData.append('uploader_id', userData.id);
        }

        try {
            await axios.post('http://localhost:8000/api/v1/resources/upload', formData);
            toast.success("¡Recurso subido!", {
                description: "Un administrador revisará el contenido antes de publicarlo.",
            });
            onUploadSuccess?.();
            onClose();
            // Reset form
            setFile(null);
            setTitle('');
            setDescription('');
        } catch (err) {
            toast.error("Error al subir el archivo.");
        } finally {
            setUploading(false);
        }
    };

    return (
        <AnimatePresence>
            {isOpen && (
                <div className="fixed inset-0 z-50 flex items-center justify-center p-6 bg-midnight/80 backdrop-blur-sm">
                    <motion.div
                        initial={{ opacity: 0, scale: 0.95, y: 20 }}
                        animate={{ opacity: 1, scale: 1, y: 0 }}
                        exit={{ opacity: 0, scale: 0.95, y: 20 }}
                        className="glass-card w-full max-w-xl relative overflow-hidden"
                    >
                        <button onClick={onClose} className="absolute top-6 right-6 text-slate-400 hover:text-white transition-colors">
                            <X size={24} />
                        </button>

                        <div className="flex items-center gap-4 mb-8">
                            <div className="w-12 h-12 bg-cyber-blue/20 rounded-2xl flex items-center justify-center text-cyber-blue">
                                <Upload size={24} />
                            </div>
                            <div>
                                <h2 className="text-2xl font-black">Subir Recurso</h2>
                                <p className="text-slate-400 text-sm">Comparte material PDF con la comunidad.</p>
                            </div>
                        </div>

                        <form onSubmit={handleSubmit} className="space-y-6">
                            <div className="space-y-2">
                                <label className="text-xs font-black uppercase tracking-widest text-slate-500 ml-2">Título del Recurso</label>
                                <input
                                    type="text"
                                    className="input-field"
                                    placeholder="Ej: Guía de Redes Neuronales"
                                    required
                                    value={title}
                                    onChange={(e) => setTitle(e.target.value)}
                                />
                            </div>

                            <div className="space-y-2">
                                <label className="text-xs font-black uppercase tracking-widest text-slate-500 ml-2">Descripción Corta</label>
                                <textarea
                                    className="input-field min-h-[100px] py-4"
                                    placeholder="Resume de qué trata este PDF..."
                                    required
                                    value={description}
                                    onChange={(e) => setDescription(e.target.value)}
                                />
                            </div>

                            <div className="space-y-2">
                                <label className="text-xs font-black uppercase tracking-widest text-slate-500 ml-2">Archivo PDF</label>
                                <div className={`
                                    border-2 border-dashed rounded-2xl p-8 transition-all text-center
                                    ${file ? 'border-green-500/50 bg-green-500/5' : 'border-white/10 hover:border-cyber-blue/50 bg-white/5'}
                                `}>
                                    <input
                                        type="file"
                                        id="pdf-upload"
                                        className="hidden"
                                        accept=".pdf"
                                        onChange={handleFileChange}
                                    />
                                    <label htmlFor="pdf-upload" className="cursor-pointer flex flex-col items-center gap-4">
                                        {file ? (
                                            <>
                                                <FileText size={48} className="text-green-500" />
                                                <div className="text-sm font-bold text-white">{file.name}</div>
                                                <div className="text-xs text-slate-400">Haz clic para cambiar de archivo</div>
                                            </>
                                        ) : (
                                            <>
                                                <Upload size={48} className="text-slate-500" />
                                                <div className="text-sm font-bold text-slate-400">Arrastra o haz clic para subir</div>
                                                <div className="text-xs text-slate-500">Solo archivos .PDF (Máx 10MB)</div>
                                            </>
                                        )}
                                    </label>
                                </div>
                            </div>

                            <button
                                type="submit"
                                disabled={uploading || !file}
                                className="btn-primary w-full h-16 text-lg disabled:opacity-50 disabled:cursor-not-allowed"
                            >
                                {uploading ? 'Subiendo...' : 'Enviar para Validación'}
                            </button>
                        </form>
                    </motion.div>
                </div>
            )}
        </AnimatePresence>
    );
};

export default ResourceUpload;
