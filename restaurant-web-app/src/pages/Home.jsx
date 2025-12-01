import {Phone, MapPin, Clock, Star, Award, Users, ChefHat } from 'lucide-react';
import heroImage from "../assets/images/hero-bg.avif";

function HomePage({ setCurrentPage }) {
  return (
    <div>
      {/* Hero Section */}
      <section
      style={{ backgroundImage: `url(${heroImage})` }}
      className="relative bg-cover h-screen flex items-center justify-center bg-gradient-to-br from-stone-800 to-stone-900 text-white"
      >
        <div className="absolute inset-0 bg-black opacity-40"></div>
        <div className="relative z-10 text-center px-4 max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-7xl font-serif font-bold mb-6">Welcome to The Café Fausse</h1>
          <p className="text-xl md:text-2xl mb-8 text-stone-200">Where Culinary Art Meets Elegance</p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button
              onClick={() => setCurrentPage('menu')}
              className="bg-amber-600 hover:bg-amber-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors"
            >
              View Menu
            </button>
            <button
              onClick={() => setCurrentPage('reservations')}
              className="bg-white hover:bg-stone-100 text-stone-900 px-8 py-3 rounded-lg font-semibold transition-colors"
            >
              Make a Reservation
            </button>
          </div>
        </div>
      </section>

      {/* Quick Info Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center p-6">
              <div className="inline-flex items-center justify-center w-16 h-16 bg-amber-100 rounded-full mb-4">
                <Phone className="w-8 h-8 text-amber-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Call Us</h3>
              <p className="text-stone-600">(202) 555-4567</p>
              <p className="text-sm text-stone-500 mt-2">Available 9 AM - 9 PM</p>
            </div>

            <div className="text-center p-6">
              <div className="inline-flex items-center justify-center w-16 h-16 bg-amber-100 rounded-full mb-4">
                <MapPin className="w-8 h-8 text-amber-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Visit Us</h3>
              <p className="text-stone-600">1234 Culinary Ave, Suite 100</p>
              <p className="text-stone-600"> Washington, DC 20002</p>
            </div>

            <div className="text-center p-6">
              <div className="inline-flex items-center justify-center w-16 h-16 bg-amber-100 rounded-full mb-4">
                <Clock className="w-8 h-8 text-amber-600" />
              </div>
              <h3 className="text-xl font-semibold mb-2">Opening Hours</h3>
              <p className="text-stone-600">Mon-Sat: 5 PM - 11 PM</p>
              <p className="text-stone-600">Sun: 5 PM - 9 PM</p>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Section */}
      <section className="py-16 bg-stone-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-serif font-bold text-stone-900 mb-4">Why Choose Us</h2>
            <p className="text-lg text-stone-600">Experience the finest dining in the heart of the city</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-xl transition-shadow">
              <div className="text-amber-600 mb-4">
                <Award className="w-12 h-12 mx-auto" />
              </div>
              <h3 className="text-xl font-semibold text-center mb-3">Award Winning</h3>
              <p className="text-stone-600 text-center">
                Recognized with multiple culinary awards for our exceptional cuisine and service excellence.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-xl transition-shadow">
              <div className="text-amber-600 mb-4">
                <ChefHat className="w-12 h-12 mx-auto" />
              </div>
              <h3 className="text-xl font-semibold text-center mb-3">Expert Chefs</h3>
              <p className="text-stone-600 text-center">
                Our master chefs bring years of international experience to create unforgettable dishes.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-xl transition-shadow">
              <div className="text-amber-600 mb-4">
                <Users className="w-12 h-12 mx-auto" />
              </div>
              <h3 className="text-xl font-semibold text-center mb-3">Premium Service</h3>
              <p className="text-stone-600 text-center">
                Attentive and professional staff dedicated to making your dining experience perfect.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Preview */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-serif font-bold text-stone-900 mb-4">What Our Guests Say</h2>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="bg-stone-50 p-6 rounded-lg">
              <div className="flex mb-4">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} className="w-5 h-5 fill-amber-500 text-amber-500" />
                ))}
              </div>
              <p className="text-stone-700 mb-4 italic">
                "Absolutely wonderful experience! The food was exquisite and the atmosphere was perfect for our anniversary dinner."
              </p>
              <p className="font-semibold">- Sarah Johnson</p>
            </div>

            <div className="bg-stone-50 p-6 rounded-lg">
              <div className="flex mb-4">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} className="w-5 h-5 fill-amber-500 text-amber-500" />
                ))}
              </div>
              <p className="text-stone-700 mb-4 italic">
                "The best restaurant in Washington! Every dish is prepared to perfection. Highly recommend the chef's special."
              </p>
              <p className="font-semibold">- Michael Mensah</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
export default HomePage;