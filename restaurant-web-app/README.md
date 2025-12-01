

function ReservationsPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    date: '',
    time: '',
    guests: '2',
    specialRequests: ''
  });
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
    setTimeout(() => {
      setSubmitted(false);
      setFormData({
        name: '',
        email: '',
        phone: '',
        date: '',
        time: '',
        guests: '2',
        specialRequests: ''
      });
    }, 3000);
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="py-16">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-serif font-bold text-stone-900 mb-4">Make a Reservation</h1>
          <p className="text-lg text-stone-600">Reserve your table for an unforgettable dining experience</p>
        </div>

        {submitted ? (
          <div className="bg-green-50 border-l-4 border-green-500 p-6 rounded-lg text-center">
            <h3 className="text-2xl font-semibold text-green-800 mb-2">Reservation Confirmed!</h3>
            <p className="text-green-700">
              Thank you for your reservation. We'll send a confirmation email shortly.
            </p>
          </div>
        ) : (
          <div className="bg-white rounded-lg shadow-lg p-8">
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-semibold text-stone-700 mb-2">
                    Full Name *
                  </label>
                  <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-transparent"
                    placeholder="John Doe"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-stone-700 mb-2">
                    Email Address *
                  </label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-transparent"
                    placeholder="john@example.com"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-stone-700 mb-2">
                    Phone Number *
                  </label>
                  <input
                    type="tel"
                    name="phone"
                    value={formData.phone}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-transparent"
                    placeholder="+233 123 456 789"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-stone-700 mb-2">
                    Number of Guests *
                  </label>
                  <select
                    name="guests"
                    value={formData.guests}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-transparent"
                  >
                    {[...Array(12)].map((_, i) => (
                      <option key={i + 1} value={i + 1}>
                        {i + 1} {i === 0 ? 'Guest' : 'Guests'}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-semibold text-stone-700 mb-2">
                    Date *
                  </label>
                  <input
                    type="date"
                    name="date"
                    value={formData.date}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-transparent"
                  />
                </div>

                <div>
                  <label className="block text-sm font-semibold text-stone-700 mb-2">
                    Time *
                  </label>
                  <select
                    name="time"
                    value={formData.time}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-transparent"
                  >
                    <option value="">Select a time</option>
                    <option value="11:00">11:00 AM</option>
                    <option value="11:30">11:30 AM</option>
                    <option value="12:00">12:00 PM</option>
                    <option value="12:30">12:30 PM</option>
                    <option value="13:00">1:00 PM</option>
                    <option value="13:30">1:30 PM</option>
                    <option value="14:00">2:00 PM</option>
                    <option value="18:00">6:00 PM</option>
                    <option value="18:30">6:30 PM</option>
                    <option value="19:00">7:00 PM</option>
                    <option value="19:30">7:30 PM</option>
                    <option value="20:00">8:00 PM</option>
                    <option value="20:30">8:30 PM</option>
                    <option value="21:00">9:00 PM</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-sm font-semibold text-stone-700 mb-2">
                  Special Requests
                </label>
                <textarea
                  name="specialRequests"
                  value={formData.specialRequests}
                  onChange={handleChange}
                  rows="4"
                  className="w-full px-4 py-2 border border-stone-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-transparent"
                  placeholder="Any dietary restrictions, allergies, or special occasions we should know about?"
                ></textarea>
              </div>

              <button
                type="submit"
                className="w-full bg-amber-600 hover:bg-amber-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors"
              >
                Confirm Reservation
              </button>
            </form>
          </div>
        )}

        <div className="mt-12 grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-stone-100 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-3">Reservation Policy</h3>
            <ul className="text-stone-700 space-y-2 text-sm">
              <li>• Reservations are held for 15 minutes</li>
              <li>• Please call to cancel or modify</li>
              <li>• Groups of 8+ please call directly</li>
              <li>• Smart casual dress code</li>
            </ul>
          </div>

          <div className="bg-stone-100 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-3">Contact Us</h3>
            <div className="text-stone-700 space-y-2 text-sm">
              <p className="flex items-center">
                <Phone className="w-4 h-4 mr-2 text-amber-600" />
                +233 (0) 123 456 789
              </p>
              <p className="flex items-center">
                <Mail className="w-4 h-4 mr-2 text-amber-600" />
                reservations@cafefausse.com
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function AboutPage() {
  const owners = [
    {
      name: 'Chef Pierre Dubois',
      role: 'Executive Chef & Co-Founder',
      bio: 'With over 25 years of culinary experience in France and across Europe, Chef Pierre brings authentic French cuisine to Ghana with a modern twist.'
    },
    {
      name: 'Marie Dubois',
      role: 'Restaurant Manager & Co-Founder',
      bio: 'Marie\'s passion for hospitality and attention to detail ensures every guest receives an exceptional dining experience.'
    }
  ];

  return (
    <div className="py-16">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-serif font-bold text-stone-900 mb-4">About Us</h1>
          <p className="text-lg text-stone-600">Our Story, Our Passion</p>
        </div>

        {/* History Section */}
        <section className="mb-16">
          <div className="bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-3xl font-serif font-bold text-amber-600 mb-6">Our History</h2>
            <div className="prose prose-lg max-w-none text-stone-700">
              <p className="mb-4">
                Founded in 2015, The Café Fausse was born from a dream to bring authentic French culinary 
                traditions to the vibrant city of Accra. Our founders, Chef Pierre and Marie Dubois, 
                left their successful restaurant in Lyon, France, to create something truly special in Ghana.
              </p>
              <p className="mb-4">
                What started as a small bistro has grown into one of Accra's most beloved fine dining 
                establishments. We've maintained our commitment to quality, authenticity, and exceptional 
                service while embracing local flavors and ingredients.
              </p>
              <p>
                Today, The Café Fausse stands as a testament to the universal language of great food and 
                the power of hospitality to bring people together from all walks of life.
              </p>
            </div>
          </div>
        </section>

        {/* Mission Section */}
        <section className="mb-16">