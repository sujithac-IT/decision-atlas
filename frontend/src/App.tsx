import { useEffect, useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import { useTranslation } from 'react-i18next'
import './App.css'
import Layout from './layouts/Layout'

function App() {
  const { i18n } = useTranslation()
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Initialize app
    const savedLanguage = localStorage.getItem('language') || 'en'
    i18n.changeLanguage(savedLanguage)
    setLoading(false)
  }, [i18n])

  if (loading) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>
  }

  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<div>Welcome to Decision Atlas</div>} />
      </Route>
    </Routes>
  )
}

export default App
