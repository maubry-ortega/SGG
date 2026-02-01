import React, { useState, useEffect } from 'react';
import { BookOpen, Upload, Shield } from 'lucide-react';
import Sidebar from '../components/Sidebar';
import ResourceUpload from '../components/ResourceUpload';
import { ResourceExplorer, AdminResourcePanel } from '../components/Resources';

const ResourcesPage = () => {
    const [isCorporate, setIsCorporate] = useState(false);
    const [isUploadModalOpen, setIsUploadModalOpen] = useState(false);
    const [refreshTrigger, setRefreshTrigger] = useState(0);

    const toggleTheme = () => setIsCorporate(!isCorporate);

    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} transition-colors duration-700`}>
            <Sidebar isCorporate={isCorporate} toggleTheme={toggleTheme} />

            <main className="flex-1 p-12 overflow-y-auto relative">
                <header className="flex justify-between items-start mb-16 relative z-10">
                    <div>
                        <h1 className="text-5xl font-black tracking-tight mb-2 text-gradient">Recursos Académicos</h1>
                        <p className="text-slate-400 text-lg font-medium">Explora, sube y valida material educativo PDF.</p>
                    </div>
                </header>

                <section className="relative z-10 space-y-12 pb-20">
                    <div className="flex justify-between items-center bg-white/5 p-8 rounded-[2rem] border border-white/5">
                        <div>
                            <h2 className="text-2xl font-black italic mb-2 tracking-tight">Gestión de Contenido</h2>
                            <p className="text-slate-500 font-medium">Todos los archivos PDF pasan por una revisión de calidad.</p>
                        </div>
                        <button
                            onClick={() => setIsUploadModalOpen(true)}
                            className="btn-primary py-4 px-8 text-base flex items-center gap-2"
                        >
                            <Upload size={20} /> Subir Nuevo PDF
                        </button>
                    </div>

                    <AdminResourcePanel
                        refreshTrigger={refreshTrigger}
                        onAction={() => setRefreshTrigger(prev => prev + 1)}
                    />

                    <div>
                        <div className="flex items-center gap-3 mb-8 opacity-50">
                            <BookOpen size={20} />
                            <span className="font-black uppercase tracking-[0.2em] text-xs">Catálogo Público</span>
                        </div>
                        <ResourceExplorer refreshTrigger={refreshTrigger} />
                    </div>
                </section>

                <ResourceUpload
                    isOpen={isUploadModalOpen}
                    onClose={() => setIsUploadModalOpen(false)}
                    onUploadSuccess={() => setRefreshTrigger(prev => prev + 1)}
                />
            </main>
        </div>
    );
};

export default ResourcesPage;
