(preview here)[https://quantico-bistro.netlify.app/]


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