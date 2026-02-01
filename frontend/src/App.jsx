import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import LandingPage from './pages/LandingPage'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import ResourcesPage from './pages/ResourcesPage'
import ProfilePage from './pages/ProfilePage'
import SettingsPage from './pages/SettingsPage'
import CommonPage from './pages/CommonPage'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/resources" element={<ResourcesPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="/community" element={<CommonPage title="Comunidad" description="Conecta con otros estudiantes en el ecosistema SGG." />} />
        <Route path="/analytics" element={<CommonPage title="Analíticas" description="Visualiza tu progreso y estadísticas de aprendizaje avanzadas." />} />
      </Routes>
    </Router>
  )
}

export default App
