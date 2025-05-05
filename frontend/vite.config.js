import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    host: 'localhost',            // ensure Vite listens where you’re calling
    proxy: {
      '/api': {
        target: 'http://localhost:8000',  // your FastAPI server
        changeOrigin: true,               // mimic an actual request
        secure: false,                    // if you ever use HTTPS dev certs
      },
    },
  },
});