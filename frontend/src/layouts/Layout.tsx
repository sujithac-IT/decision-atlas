import { Outlet } from 'react-router-dom'
import { useTranslation } from 'react-i18next'

export default function Layout() {
  const { t } = useTranslation()

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-blue-600">Decision Atlas</h1>
          <div className="flex gap-4">
            <button className="px-4 py-2 text-gray-700 hover:text-blue-600">
              {t('nav.home')}
            </button>
            <button className="px-4 py-2 text-gray-700 hover:text-blue-600">
              {t('nav.about')}
            </button>
          </div>
        </nav>
      </header>
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <Outlet />
      </main>
      <footer className="bg-gray-900 text-white mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 text-center">
          <p>&copy; 2024 Decision Atlas. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}
