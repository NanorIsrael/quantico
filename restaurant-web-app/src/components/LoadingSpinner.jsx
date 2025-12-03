import React from 'react';



const LoadingSpinner = ({
  size = 'md',
  color = 'yellow',
  text = 'Loading...',
  fullScreen = false,
  overlay = false,
}) => {
  const sizeClasses = {
    sm: 'w-4 h-4',
    md: 'w-8 h-8',
    lg: 'w-12 h-12',
    xl: 'w-16 h-16',
  };

  const colorClasses = {
    blue: 'text-blue-600',
    gray: 'text-gray-600',
    green: 'text-green-600',
    red: 'text-red-600',
    yellow: 'text-yellow-600',
    purple: 'text-purple-600',
  };

  const textSizeClasses = {
    sm: 'text-sm',
    md: 'text-base',
    lg: 'text-lg',
    xl: 'text-xl',
  };

  const SpinnerIcon = () => (
    <svg
      className={`animate-spin ${sizeClasses[size]} ${colorClasses[color]}`}
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle
        className="opacity-25"
        cx="12"
        cy="12"
        r="10"
        stroke="currentColor"
        strokeWidth="4"
      ></circle>
      <path
        className="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
      ></path>
    </svg>
  );

  const content = (
    <div className="min-h-screen flex flex-col items-center justify-center space-y-4">
      <SpinnerIcon />
      {text && (
        <p
          className={`${colorClasses[color]} ${textSizeClasses[size]} font-medium animate-pulse`}
        >
          {text}
        </p>
      )}
    </div>
  );

  if (fullScreen) {
    return (
      <div
        className={`
        fixed inset-0 z-50 flex items-center justify-center
        ${overlay ? 'bg-black bg-opacity-50' : 'bg-white'}
      `}
      >
        {content}
      </div>
    );
  }

  return <div className="flex items-center justify-center p-8">{content}</div>;
};

// Alternative skeleton loading component for more sophisticated loading states
export const SkeletonLoader = ({
  lines = 3,
  width = 'w-full',
}) => {
  return (
    <div className="animate-pulse space-y-4">
      {Array.from({ length: lines }).map((_, index) => (
        <div key={index} className="space-y-3">
          <div className={`h-4 bg-gray-200 rounded ${width}`}></div>
          {index === 0 && <div className="h-4 bg-gray-200 rounded w-3/4"></div>}
          {index === lines - 1 && (
            <div className="h-4 bg-gray-200 rounded w-1/2"></div>
          )}
        </div>
      ))}
    </div>
  );
};

// Dashboard skeleton for your budget dashboard
export const DashboardSkeleton = () => {
  return (
    <div className="bg-gray-50 p-6 min-h-screen animate-pulse">
      {/* Navigation skeleton */}
      <div className="mb-8 flex space-x-8">
        <div className="h-4 bg-gray-200 rounded w-24"></div>
        <div className="h-4 bg-gray-200 rounded w-16"></div>
        <div className="h-4 bg-gray-200 rounded w-32"></div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-8">
          {/* Chart skeleton */}
          <div className="bg-white rounded-lg p-6 shadow-sm">
            <div className="h-6 bg-gray-200 rounded w-48 mb-6"></div>
            <div className="h-64 bg-gray-100 rounded"></div>
          </div>

          {/* Two column charts skeleton */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="bg-white rounded-lg p-6 shadow-sm">
              <div className="h-5 bg-gray-200 rounded w-32 mb-4"></div>
              <div className="space-y-3">
                {[1, 2, 3, 4].map((i) => (
                  <div key={i} className="h-6 bg-gray-100 rounded"></div>
                ))}
              </div>
            </div>
            <div className="bg-white rounded-lg p-6 shadow-sm">
              <div className="h-5 bg-gray-200 rounded w-32 mb-4"></div>
              <div className="w-32 h-32 bg-gray-100 rounded-full mx-auto mb-4"></div>
              <div className="space-y-2">
                {[1, 2, 3, 4, 5].map((i) => (
                  <div key={i} className="flex justify-between">
                    <div className="h-4 bg-gray-100 rounded w-16"></div>
                    <div className="h-4 bg-gray-100 rounded w-12"></div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Stats skeleton */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            {[1, 2, 3, 4].map((i) => (
              <div key={i} className="bg-white rounded-lg p-4 shadow-sm">
                <div className="h-3 bg-gray-200 rounded w-24 mb-2"></div>
                <div className="h-5 bg-gray-200 rounded w-20"></div>
              </div>
            ))}
          </div>
        </div>

        {/* Sidebar skeleton */}
        <div className="bg-white rounded-lg p-6 shadow-sm h-fit">
          <div className="h-5 bg-gray-200 rounded w-32 mb-4"></div>
          <div className="space-y-3">
            {[1, 2, 3, 4].map((i) => (
              <div key={i} className="h-4 bg-gray-100 rounded"></div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

// Loading overlay for existing content
export const LoadingOverlay = ({ isLoading, children }) => {
  return (
    <div className="relative">
      {children}
      {isLoading && (
        <div className="absolute inset-0 bg-white bg-opacity-75 flex items-center justify-center z-10">
          <LoadingSpinner size="lg" text="Updating..." />
        </div>
      )}
    </div>
  );
};

export default LoadingSpinner;
