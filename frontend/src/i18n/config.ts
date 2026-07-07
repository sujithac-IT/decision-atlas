import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'

const resources = {
  en: {
    translation: {
      'nav.home': 'Home',
      'nav.about': 'About',
      'nav.contact': 'Contact',
      'common.loading': 'Loading...',
      'common.error': 'An error occurred',
    },
  },
  es: {
    translation: {
      'nav.home': 'Inicio',
      'nav.about': 'Acerca de',
      'nav.contact': 'Contacto',
      'common.loading': 'Cargando...',
      'common.error': 'Ocurrió un error',
    },
  },
  fr: {
    translation: {
      'nav.home': 'Accueil',
      'nav.about': 'À propos',
      'nav.contact': 'Contact',
      'common.loading': 'Chargement...',
      'common.error': 'Une erreur est survenue',
    },
  },
}

i18n.use(initReactI18next).init({
  resources,
  lng: 'en',
  interpolation: {
    escapeValue: false,
  },
})

export default i18n
