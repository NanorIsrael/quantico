import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { ClientProvider } from './context/HTTPClientProvider.js'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ClientProvider>
      
      <App />
    </ClientProvider>
  </StrictMode>,
)
