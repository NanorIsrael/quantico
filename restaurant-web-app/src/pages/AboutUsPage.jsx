import { Users, Heart } from "lucide-react";
import NewsletterSignup from "../components/NewLetter";

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
                Founded in 2010 by Chef Antonio Rossi and
				restaurateur Maria Lopez, Café Fausse blends traditional Italian flavors
				with modern culinary innovation. Our mission is to provide an
				unforgettable dining experience that reflects both quality and creativity
              </p>
              
            </div>
          </div>
        </section>

        <section className="bg-white py-16">
        <div className="max-w-7xl mx-auto px-6">
          <h2 className="text-3xl md:text-4xl font-bold text-center text-gray-900 mb-4">Meet Our Founders</h2>
          <p className="text-center text-gray-600 mb-12 text-lg">The visionaries behind Café Fausse</p>
          
          <div className="grid md:grid-cols-2 gap-12">
            {/* Chef Antonio Rossi */}
            <div className="bg-gradient-to-br from-gray-50 to-white rounded-2xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
              <div className="bg-gradient-to-r from-amber-600 to-amber-700 h-48 flex items-center justify-center">
                <div className="w-32 h-32 bg-white rounded-full flex items-center justify-center">
                  <Users className="w-16 h-16 text-amber-700" />
                </div>
              </div>
              <div className="p-8">
                <h3 className="text-2xl font-bold text-gray-900 mb-2">Chef Antonio Rossi</h3>
                <p className="text-amber-600 font-semibold mb-4 text-lg">Co-Founder & Executive Chef</p>
                <div className="space-y-4 text-gray-700">
                  <p>
                    Born and raised in the heart of Tuscany, Chef Antonio Rossi brings over 25 years of culinary expertise to Café Fausse. Trained in the finest kitchens of Italy and France, Antonio's passion for authentic Italian cuisine is matched only by his innovative spirit.
                  </p>
                  <p>
                    His philosophy is simple yet profound: respect the ingredients, honor the traditions, and never stop innovating. Under his guidance, our kitchen has become a laboratory of flavors where classic recipes are reimagined with contemporary flair.
                  </p>
                  <p>
                    Antonio's dedication to his craft has earned him numerous accolades, but his greatest joy comes from seeing the delight on our guests' faces with every bite.
                  </p>
                </div>
              </div>
            </div>

            {/* Maria Lopez */}
            <div className="bg-gradient-to-br from-gray-50 to-white rounded-2xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
              <div className="bg-gradient-to-r from-amber-600 to-amber-700 h-48 flex items-center justify-center">
                <div className="w-32 h-32 bg-white rounded-full flex items-center justify-center">
                  <Heart className="w-16 h-16 text-amber-700" />
                </div>
              </div>
              <div className="p-8">
                <h3 className="text-2xl font-bold text-gray-900 mb-2">Maria Lopez</h3>
                <p className="text-amber-600 font-semibold mb-4 text-lg">Co-Founder & Managing Director</p>
                <div className="space-y-4 text-gray-700">
                  <p>
                    With a background in hospitality management and a lifelong passion for creating memorable experiences, Maria Lopez is the heart and soul of Café Fausse's warm, welcoming atmosphere.
                  </p>
                  <p>
                    Maria's vision extends beyond excellent food—she believes that every guest should feel like family from the moment they walk through our doors. Her attention to detail and commitment to service excellence has shaped every aspect of the Café Fausse experience.
                  </p>
                  <p>
                    A champion of sustainability and community engagement, Maria has forged strong relationships with local farmers and suppliers, ensuring that we serve only the finest, freshest ingredients while supporting our local economy.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
		{/* Call to Action */}
      {/* <section className="max-w-7xl mx-auto px-6 py-16 text-center">
        <div className="bg-gradient-to-br from-amber-50 to-orange-50 rounded-2xl p-12 shadow-lg">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Experience Café Fausse</h2>
          <p className="text-xl text-gray-700 mb-8 max-w-2xl mx-auto">
            Join us for an unforgettable culinary journey where tradition meets innovation, and every meal is a celebration.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="bg-amber-600 hover:bg-amber-800 text-white font-semibold px-8 py-4 rounded-lg transition-colors shadow-md hover:shadow-lg">
              Make a Reservation
            </button>
            <button className="bg-white hover:bg-gray-50 text-amber-700 font-semibold px-8 py-4 rounded-lg border-2 border-stone-300 transition-colors">
              View Our Menu
            </button>
          </div>
        </div>
      </section> */}

		<NewsletterSignup/>
	</div>
	</div>
  )}
  export default AboutPage;