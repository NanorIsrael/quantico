import { useState } from 'react'
import { Menu, X, Phone, Mail, MapPin, ChefHat } from 'lucide-react';
import HomePage from './pages/Home'
import MenuPage from './pages/MenuPage'
import ReservationsPage from './pages/ReservationPage'
import AboutPage from './pages/AboutUsPage'
import GalleryPage from './pages/GalleryPage'
import { Toaster } from 'sonner';

import './App.css'

function App() {
  const [currentPage, setCurrentPage] = useState('home');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navigationItems = [
    { id: 'home', label: 'Home' },
    { id: 'menu', label: 'Menu' },
    { id: 'reservations', label: 'Reservations' },
    { id: 'about', label: 'About Us' },
    { id: 'gallery', label: 'Gallery' }
  ];

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <HomePage setCurrentPage={setCurrentPage} />;
      case 'menu':
        return <MenuPage />;
      case 'reservations':
        return <ReservationsPage />;
      case 'about':
        return <AboutPage />;
      case 'gallery':
        return <GalleryPage />;
      default:
        return <HomePage setCurrentPage={setCurrentPage} />;
    }
  };

  return (
    <div className="min-h-screen bg-stone-50">
      {/* Navigation */}
      <nav className="bg-stone-900 text-white sticky top-0 z-50 shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-20">
            {/* Logo */}
            <div className="flex items-center space-x-2 cursor-pointer" onClick={() => setCurrentPage('home')}>
              <ChefHat className="w-8 h-8 text-amber-500" />
              <div>
                <h1 className="text-2xl font-serif font-bold">The Café Fausse</h1>
                <p className="text-xs text-amber-500">Fine Dining Experience</p>
              </div>
            </div>

            {/* Desktop Navigation */}
            <div className="hidden md:flex space-x-8">
              {navigationItems.map(item => (
                <button
                  key={item.id}
                  onClick={() => setCurrentPage(item.id)}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                    currentPage === item.id
                      ? 'text-amber-500 bg-stone-800'
                      : 'text-white hover:text-amber-500 hover:bg-stone-800'
                  }`}
                >
                  {item.label}
                </button>
              ))}
            </div>

            {/* Mobile menu button */}
            <button
              className="md:hidden p-2"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>

          {/* Mobile Navigation */}
          {mobileMenuOpen && (
            <div className="md:hidden pb-4">
              {navigationItems.map(item => (
                <button
                  key={item.id}
                  onClick={() => {
                    setCurrentPage(item.id);
                    setMobileMenuOpen(false);
                  }}
                  className={`block w-full text-left px-3 py-2 rounded-md text-base font-medium ${
                    currentPage === item.id
                      ? 'text-amber-500 bg-stone-800'
                      : 'text-white hover:text-amber-500 hover:bg-stone-800'
                  }`}
                >
                  {item.label}
                </button>
              ))}
            </div>
          )}
        </div>
      </nav>
      <Toaster
                    duration={4500}
                    position="top-right"
                    toastOptions={{
                      classNames: {
                        //  toast: 'bg-white shadow-lg rounded-lg p-4',
                        success: '!text-primary  border-2',
                        error: '!text-red-600  border-2',
                        warning: '!text-yellow-600  border-2',
                      },
                    }}
                  />
      {/* Page Content */}
      <main>{renderPage()}</main>
      
      {/* Footer */}
      <footer className="bg-stone-900 text-white mt-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <h3 className="text-xl font-serif font-bold mb-4 text-amber-500">The Café Fausse</h3>
              <p className="text-stone-300 text-sm">
                Experience culinary excellence in an elegant atmosphere. Where every meal is a celebration.
              </p>
            </div>
            
            <div>
              <h4 className="text-lg font-semibold mb-4">Contact Us</h4>
              <div className="space-y-3 text-sm text-stone-300">
                <div className="flex items-center space-x-2">
                  <Phone className="w-4 h-4 text-amber-500" />
                  <span>(202) 555-4567</span>
                </div>
                <div className="flex items-center space-x-2">
                  <Mail className="w-4 h-4 text-amber-500" />
                  <span>info@cafefausse.com</span>
                </div>
                <div className="flex items-center space-x-2">
                  <MapPin className="w-4 h-4 text-amber-500" />
                  <span>1234 Culinary Ave, Suite 100, Washington, DC 20002</span>
                </div>
              </div>
            </div>

            <div>
              <h4 className="text-lg font-semibold mb-4">Opening Hours</h4>
              <div className="space-y-2 text-sm text-stone-300">
                <div className="flex justify-between">
                  <span>Monday - Saturday:</span>
                  <span>5:00 PM - 11:00 PM</span>
                </div>
                <div className="flex justify-between">
                  <span>Sunday:</span>
                  <span>5:00 PM - 9:00 PM</span>
                </div>
              </div>
            </div>
          </div>

          <div className="border-t border-stone-800 mt-8 pt-8 text-center text-sm text-stone-400">
            <p>&copy; {new Date().getFullYear()} The Café Fausse. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );

}

export default App
