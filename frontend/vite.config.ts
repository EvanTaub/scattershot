import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    host: true,
    port : 5173,
    watch : { usePolling: true },
    proxy: {
      '/api' : { target : 'http://backend:8000' },
    },
  },
})