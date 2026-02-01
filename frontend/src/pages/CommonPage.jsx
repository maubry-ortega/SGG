import React, { useState } from 'react';
import Sidebar from '../components/Sidebar';

const CommonPage = ({ title, description }) => {
    const [isCorporate, setIsCorporate] = useState(false);
    const toggleTheme = () => setIsCorporate(!isCorporate);

    return (
        <div className={`flex min-h-screen ${isCorporate ? 'theme-corporate bg-[#0a0f1e]' : 'bg-midnight'} transition-colors duration-700`}>
            <Sidebar isCorporate={isCorporate} toggleTheme={toggleTheme} />
            <main className="flex-1 p-12 flex flex-col items-center justify-center text-center">
                <h1 className="text-6xl font-black mb-4 text-gradient">{title}</h1>
                <p className="text-slate-400 text-xl max-w-lg">{description}</p>
                <div className="mt-12 p-8 glass rounded-3xl border-white/5 opacity-50 italic">
                    Esta sección del motor SAGGI se encuentra actualmente en fase de calibración.
                </div>
            </main>
        </div>
    );
};

export default CommonPage;
