import React, { useState } from 'react';
import { X, ChevronLeft, ChevronRight, Award, Star, Quote } from 'lucide-react';
import ImageGallery from '../components/ImageGallery';
import galleryCafeInterior from '../assets/images/gallery/gallery-cafe-interior.webp';
import gallerySpecialEvent from '../assets/images/gallery/gallery-special-event.webp';
import galleryRibeyesteak from '../assets/images/gallery/gallery-ribeye-steak.webp';
import homeCafeFausse from '../assets/images/gallery/home-cafe-fausse.webp';

export default function RestaurantGallery() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0);

  const internalGallery = [galleryCafeInterior, gallerySpecialEvent, galleryRibeyesteak, homeCafeFausse]
  const galleryImages = [
    {
      id: 1,
      category: 'interior',
      title: 'Main Dining Hall',
      url: 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
      description: 'Elegant dining space with ambient lighting'
    },
    {
      id: 2,
      category: 'interior',
      title: 'Private Dining Room',
      url: 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80',
      description: 'Intimate setting for special occasions'
    },
    {
      id: 3,
      category: 'interior',
      title: 'Bar Area',
      url: 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800&q=80',
      description: 'Sophisticated bar with premium selection'
    },
    {
      id: 4,
      category: 'dishes',
      title: 'Signature Steak',
      url: 'https://images.unsplash.com/photo-1544025162-d76694265947?w=800&q=80',
      description: 'Perfectly grilled to perfection'
    },
    // {
    //   id: 5,
    //   category: 'dishes',
    //   title: 'Seafood Platter',
    //   url: 'https://images.unsplash.com/photo-1559737558-2f5a70d6e4c5?w=800&q=80',
    //   description: 'Fresh catch of the day'
    // },
    {
      id: 6,
      category: 'dishes',
      title: 'Gourmet Dessert',
      url: 'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=800&q=80',
      description: 'Artisanal sweet creations'
    },
    {
      id: 7,
      category: 'dishes',
      title: 'Pasta Specialty',
      url: 'https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=800&q=80',
      description: 'House-made pasta with seasonal ingredients'
    },
    {
      id: 8,
      category: 'events',
      title: 'Wine Tasting Event',
      url: 'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800&q=80',
      description: 'Exclusive wine pairing evenings'
    },
    {
      id: 9,
      category: 'events',
      title: 'Chef\'s Table Experience',
      url: 'https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=800&q=80',
      description: 'Behind-the-scenes culinary journey'
    },
    {
      id: 10,
      category: 'events',
      title: 'Kitchen in Action',
      url: 'https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=800&q=80',
      description: 'Our talented chefs at work'
    },
    {
      id: 11,
      category: 'interior',
      title: 'Outdoor Terrace',
      url: 'https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800&q=80',
      description: 'Al fresco dining under the stars'
    },
    {
      id: 12,
      category: 'dishes',
      title: 'Chef\'s Tasting Menu',
      url: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&q=80',
      description: 'Multi-course culinary experience'
    },
    // {
    //   id: 13,
    //   category: 'interior',
    //   title: 'Indoor Illustration',
    //   url: ``,
    //   description: 'Indoor Illustration'
    // }
  ];

  const awards = [
    {
      id: 1,
      title: 'Culinary Excellence Award',
      year: '2022',
      icon: Award
    },
    {
      id: 2,
      title: 'Restaurant of the Year',
      year: '2023',
      icon: Award
    },
    {
      id: 3,
      title: 'Best Fine Dining Experience',
      year: '2023',
      source: 'Foodie Magazine',
      icon: Star
    }
  ];

  const reviews = [
    {
      id: 1,
      text: 'Exceptional ambiance and unforgettable flavors.',
      author: 'Gourmet Review',
      rating: 5
    },
    {
      id: 2,
      text: 'A must-visit restaurant for food enthusiasts.',
      author: 'The Daily Bite',
      rating: 5
    }
  ];

  const openLightbox = (index) => {
    setCurrentIndex(index);
    setSelectedImage(galleryImages[index]);
  };

  const closeLightbox = () => {
    setSelectedImage(null);
  };

  const navigateImage = (direction) => {
    const newIndex = direction === 'next' 
      ? (currentIndex + 1) % galleryImages.length
      : (currentIndex - 1 + galleryImages.length) % galleryImages.length;
    
    setCurrentIndex(newIndex);
    setSelectedImage(galleryImages[newIndex]);
  };

  const handleKeyDown = (e) => {
    if (selectedImage) {
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowRight') navigateImage('next');
      if (e.key === 'ArrowLeft') navigateImage('prev');
    }
  };

  React.useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [selectedImage, currentIndex]);

  return (
    <div className="min-h-screen  from-slate-50 to-slate-100">
      {/* Hero Section */}
      <div className=" text-stone-900 py-16 px-6">
        <div className="max-w-7xl mx-auto">
          <h1 className="text-5xl font-bold mb-4 text-center">Our Gallery</h1>
          <p className="text-xl text-amber-600 text-center max-w-2xl mx-auto">
            Experience the essence of fine dining through our curated collection of moments
          </p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-6 py-12">
		<div className='mb-6'>
			<img
				src={galleryCafeInterior}
				alt={'previewing the restaurant interior'}
				className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
        	/>
		</div>
		<div className='grid md:grid-cols-2 gap-2 mb-6'>
			<figure>
			<img
				src={galleryRibeyesteak}
				alt={'previewing the restaurant interior'}
				className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
        	/>	
			</figure>
			<figure>
			<img
				src={gallerySpecialEvent}
				alt={'previewing the restaurant interior'}
				className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
        	/>	
			</figure>
		</div>
		<div className='mb-6'>
			<img
				src={homeCafeFausse}
				alt={'previewing the restaurant interior'}
				className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
        	/>
		</div>
		<ImageGallery images={galleryImages}/>

        {/* Gallery Grid */}
        <section className="mb-16">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {galleryImages.map((image, index) => (
              <div
                key={image.id}
                className="group relative overflow-hidden rounded-lg shadow-lg hover:shadow-2xl transition-all duration-300 cursor-pointer aspect-square"
                onClick={() => openLightbox(index)}
              >
                <img
                  src={image.url}
                  alt={image.title}
                  className="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  <div className="absolute bottom-0 left-0 right-0 p-4">
                    <h3 className="text-white font-semibold text-lg mb-1">{image.title}</h3>
                    <p className="text-gray-200 text-sm">{image.description}</p>
                  </div>
                </div>
                <div className="absolute top-3 right-3 bg-amber-600 text-white text-xs px-2 py-1 rounded-full opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  {image.category}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Awards Section */}
        <section className="mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-8 text-center">Awards & Recognition</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {awards.map((award) => (
              <div
                key={award.id}
                className="bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 p-8 text-center"
              >
                <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-amber-400 to-amber-600 rounded-full mb-4">
                  <award.icon className="w-8 h-8 text-white" />
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-2">{award.title}</h3>
                <p className="text-amber-600 font-semibold text-lg mb-1">{award.year}</p>
                {award.source && (
                  <p className="text-gray-600 text-sm italic">{award.source}</p>
                )}
              </div>
            ))}
          </div>
        </section>

        {/* Customer Reviews */}
        <section>
          <h2 className="text-4xl font-bold text-gray-900 mb-8 text-center">What Our Guests Say</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {reviews.map((review) => (
              <div
                key={review.id}
                className="bg-white rounded-xl shadow-md hover:shadow-xl transition-shadow duration-300 p-8"
              >
                <Quote className="w-10 h-10 text-amber-500 mb-4" />
                <div className="flex mb-3">
                  {[...Array(review.rating)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 fill-amber-400 text-amber-400" />
                  ))}
                </div>
                <p className="text-gray-700 text-lg italic mb-4 leading-relaxed">
                  "{review.text}"
                </p>
                <p className="text-gray-900 font-semibold">— {review.author}</p>
              </div>
            ))}
          </div>
        </section>
      </div>

      {/* Lightbox Modal */}
      {selectedImage && (
        <div
          className="fixed inset-0 bg-black/95 z-50 flex items-center justify-center p-4"
          onClick={closeLightbox}
        >
          {/* Close Button */}
          <button
            onClick={closeLightbox}
            className="absolute top-4 right-4 text-white hover:text-amber-400 transition-colors z-10"
          >
            <X className="w-8 h-8" />
          </button>

          {/* Previous Button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              navigateImage('prev');
            }}
            className="absolute left-4 text-white hover:text-amber-400 transition-colors z-10"
          >
            <ChevronLeft className="w-12 h-12" />
          </button>

          {/* Next Button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              navigateImage('next');
            }}
            className="absolute right-4 text-white hover:text-amber-400 transition-colors z-10"
          >
            <ChevronRight className="w-12 h-12" />
          </button>

          {/* Image Container */}
          <div
            className="max-w-6xl max-h-[90vh] flex flex-col items-center"
            onClick={(e) => e.stopPropagation()}
          >
            <img
              src={selectedImage.url}
              alt={selectedImage.title}
              className="max-w-full max-h-[80vh] object-contain rounded-lg shadow-2xl"
            />
            <div className="mt-6 text-center text-white">
              <h3 className="text-2xl font-bold mb-2">{selectedImage.title}</h3>
              <p className="text-gray-300">{selectedImage.description}</p>
              <p className="text-sm text-gray-400 mt-2">
                {currentIndex + 1} / {galleryImages.length}
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}