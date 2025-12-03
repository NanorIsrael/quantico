import { useEffect, useState } from 'react'
import { Phone, Mail } from 'lucide-react';
import ReservationSuccessDialog from '../components/ReservationSuccessDialog'
import { useClient } from '../api/client';
import { toast } from 'sonner';
import LoadingSpinner from '../components/LoadingSpinner';
import { to12Hour } from '../lib/util';

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
  const [isSuccess, setIsSuccess] = useState(false);
  const [slots, setSlots] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const httpClient = useClient()
  const isSunday = new Date(formData.date).toLocaleDateString('en-US', {weekday: 'long'})
                  .toLowerCase() === 'sunday';
  const today = new Date();
  const localDate = new Date(today.getTime() - today.getTimezoneOffset() * 60000)
  .toISOString()
  .split("T")[0]; 

  const handleSubmit = async(e) => {
    e.preventDefault();
    setSubmitted(true);

	const response = await httpClient.post('reservations', formData);
	if (response.success) {
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
      setIsSuccess(true)
    }, 300);
		toast.success(response.data.message)
	} else {
		toast.success(response.error.message)
	}
	
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  useEffect(() => {
    setIsLoading(true)
    const fetchTimeSlots = async () => {
      try {
        const response = await httpClient.get(`slots${(formData.date).length > 0 ? `?date=${formData.date}`: ''}`);
        if (response.success) {
          console.log('response.data', response.data.data)
          setSlots(response.data.data)
        } else {
          setSlots([])
        }
      } finally {
        setIsLoading(false)
      }
    }
    fetchTimeSlots()
  }, [formData.date])

  if (!slots) {
    return <LoadingSpinner text="Loading page contents..."/>
  }

  return (
    <div className="py-16">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-serif font-bold text-stone-900 mb-4">Make a Reservation</h1>
          <p className="text-lg text-stone-600">Reserve your table for an unforgettable dining experience</p>
        </div>

        { (
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
                    min={localDate}
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
                    <option value="">{slots.length > 0 ? 'Select a time' : 'No time slots available for selected date'}</option>
                    {(isSunday ? slots.slice(0, 5) : slots).map(slot => <option key={slot} value={slot}>{to12Hour(slot)}</option>)}
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
	  {isSuccess && <ReservationSuccessDialog openModal={true}/>}
    </div>
  );
}
export default ReservationsPage