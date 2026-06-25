# Tabakvest 85 - Modern Student Housing Website

A beautiful, modern website for student housing in Antwerp, built with HTML, CSS (Tailwind), and pure JavaScript.

## 🎯 Features

- **Responsive Design** - Works perfectly on mobile, tablet, and desktop
- **Modern Aesthetics** - Clean, professional design with smooth transitions
- **9 Room Listings** - Detailed pages for each student room with pricing and features
- **Location Page** - Interactive map and location information
- **Performance Optimized** - Fast loading, SEO-friendly
- **Fully Static** - No backend required, perfect for Cloudflare Pages

## 📁 Project Structure

```
tabakvest-85/
├── index.html              # Homepage
├── pages/
│   ├── rooms.html         # Room listing page
│   ├── location.html      # Location & map page
│   ├── room-1.html        # Individual room pages
│   ├── room-2.html
│   └── ...room-9.html
├── src/
│   ├── styles.css         # Tailwind CSS + custom styles
│   └── script.js          # JavaScript utilities
├── public/                # Static assets
├── tailwind.config.js     # Tailwind configuration
├── postcss.config.js      # PostCSS configuration
└── package.json           # Dependencies & scripts
```

## 🚀 Getting Started Locally

### Prerequisites
- Node.js 16+ and npm

### Installation

```bash
# Install dependencies
npm install

# Start development server with CSS watching
npm run dev

# Build for production
npm run build
```

### Local Development

1. Open `index.html` in your browser or use a local server:
```bash
npx http-server
```

2. CSS will automatically compile when you save files (during `npm run dev`)

## 🌐 Deployment to Cloudflare Pages

### Step 1: Prepare Your Repository

```bash
git init
git add .
git commit -m "Initial commit"
```

### Step 2: Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/tabakvest-85.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Cloudflare Pages

1. Go to [Cloudflare Pages](https://pages.cloudflare.com/)
2. Click "Create a project" → "Connect to Git"
3. Select your repository
4. Configure build settings:
   - **Build command:** `npm run build && npm run copy`
   - **Build output directory:** `dist`
   - **Framework preset:** None

### Step 4: Connect Custom Domain

In Cloudflare Pages project settings:
1. Go to "Custom domains"
2. Add your domain
3. Update DNS records in your registrar to point to Cloudflare

## 📝 Content Management

### Update Room Information

Edit individual room pages in `pages/room-X.html`:
- Room description
- Technical specifications
- Pricing information
- Features and amenities

### Update Contact Information

Replace these email addresses and phone numbers throughout:
- Email: `tabakvest85@gmail.com`
- Phone: `0495 91 65 13`
- Facebook: Update social links in footer

## 🎨 Customization

### Colors

Edit `tailwind.config.js` to change the color scheme:
```javascript
colors: {
  primary: '#8B6F47',      // Main brown
  secondary: '#D4A574',    // Light tan
  accent: '#2C3E50',       // Dark blue
}
```

### Typography

Fonts are loaded from Google Fonts (Inter). Change in HTML `<head>` sections.

### Images

Add room photos by replacing gradient backgrounds:
```html
<div style="background: url('path/to/image.jpg')"></div>
```

## 🔍 SEO Optimization

- Meta descriptions on all pages ✓
- Semantic HTML structure ✓
- Mobile-friendly responsive design ✓
- Fast page load times ✓
- Structured content ✓

## ⚡ Performance

- **Static HTML/CSS/JS** - No backend processing
- **Minified CSS** - Optimized file sizes
- **Lazy loading ready** - For future image optimization
- **Zero JavaScript dependencies** - Fast & secure

## 📱 Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari 14+, Chrome Android)

## 📄 License

All rights reserved. Tabakvest 85, 2026.

## 📞 Support

For inquiries about student housing:
- Email: tabakvest85@gmail.com
- Phone: +32 (0)495 91 65 13
- Facebook: [Tabakvest85](https://www.facebook.com/Tabakvest85-103313761715433/)

---

Built with ❤️ using Tailwind CSS
