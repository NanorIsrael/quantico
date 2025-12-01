import { useEffect, useState } from 'react';
import { ChevronLeft, ChevronRight, Eye, X } from 'lucide-react';

export default function ImageGallery({images}) {
  const [previewImage, setPreviewImage] = useState(0);
  const [isPreviewOpen, setIsPreviewOpen] = useState(false);

  // Handle keyboard arrow navigation
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'ArrowRight' && previewImage < images.length - 1) {
        setPreviewImage((prev) => prev + 1);
      } else if (e.key === 'ArrowLeft' && previewImage > 0) {
        setPreviewImage((prev) => prev - 1);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [previewImage, images?.length]);

  const handlePrev = () => {
    if (previewImage > 0) setPreviewImage((prev) => prev - 1);
  };

  const handleNext = () => {
    if (previewImage < images.length - 1) setPreviewImage((prev) => prev + 1);
  };

  useEffect(() => {
    if (!images?.length) return;

    const timer = setInterval(() => {
      setPreviewImage(Math.floor(Math.random() * images.length))
    }, 5000);
    return () => clearInterval(timer)
  }, [images.length])

  return (
    <div className="mb-6 w-full">
      {/* Main preview image */}
      <div className="mb-4 relative">
        <button
          onClick={() => setIsPreviewOpen(true)}
          className={`relative group w-full`}
        >
          <img
            src={images[previewImage].url}
            alt={images[previewImage].description}
            className="w-full h-72 object-cover rounded-lg shadow-sm"
          />
          <div className="absolute inset-0 bg-transparent bg-opacity-0 group-hover:bg-opacity-30 transition-all duration-200 rounded-lg flex items-center justify-center">
            <Eye className="w-6 h-6 text-white opacity-0 group-hover:opacity-100 transition-opacity duration-200 cursor-pointer" />
          </div>
        </button>

        {/* Left Chevron (only show if not first) */}
        {previewImage > 0 && (
          <ChevronLeft
            size={40}
            className="absolute left-2 top-1/2 -translate-y-1/2 text-white bg-black/50 rounded-full p-1 cursor-pointer"
            onClick={handlePrev}
          />
        )}

        {/* Right Chevron (only show if not last) */}
        {previewImage < images.length - 1 && (
          <ChevronRight
            size={40}
            className="absolute right-2 top-1/2 -translate-y-1/2 text-white bg-black/50 rounded-full p-1 cursor-pointer"
            onClick={handleNext}
          />
        )}
        {/* <div className='absolute top-2 right-1' >
			<p className='flex items-center gap-1 text-sm text-primary border border-black bg cursor-pointer bg-transparent p-1 rounded-lg'>
				<Eye size={15}/>
			<span className='text-primary'>Preview</span>
			</p>
		</div> */}
      </div>

      {/* Thumbnail previews */}
      
      {isPreviewOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-95 z-50 flex items-center justify-center p-6">
          <button
            onClick={() => setIsPreviewOpen(false)}
            className="absolute top-6 right-6 text-white hover:text-gray-300 transition-colors z-10 bg-black bg-opacity-50 rounded-full p-2"
          >
            <X className="w-6 h-6" />
          </button>

          <div className="relative max-w-6xl max-h-full">
            <img
              src={images[previewImage]}
              alt={`previewing ${images[previewImage]}`}
              className="max-w-full max-h-full object-contain rounded-lg"
            />
          </div>
        </div>
      )}
    </div>
  );
}
