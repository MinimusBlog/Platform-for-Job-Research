/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{vue,js,jsx}',
  ],
  theme: {
    extend: {
      colors: {
        mint: {
          DEFAULT: '#00E5A0',
          dark:    '#00C584',
          dim:     'rgba(0,229,160,0.08)',
        },
        bg: {
          DEFAULT: '#0D1117',
          card:    '#161B22',
          elevated:'#1C2333',
        },
        border: {
          DEFAULT: '#30363D',
          light:   '#444C56',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        card: '0 4px 24px rgba(0,0,0,0.4)',
        mint: '0 0 20px rgba(0,229,160,0.2)',
      },
    },
  },
  plugins: [],
}