import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite';

import path from 'path';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    port: 9000,
  },
  build: {
    outDir: 'dist', // Make sure this matches your expected output
    rollupOptions: {
      input: {
        main: './index.html', // Explicitly specify the HTML entry point
      },
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },

})
