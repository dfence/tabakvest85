# Tabakvest 85 - Student Housing Website

Professional student housing website built with **GitHub Pages** for Tabakvest 85 in Antwerp, Belgium.

## 📂 Folder Structure

```
tabakvest85/
├── index.html              ← Home page
├── rooms.html              ← Rooms overview (grid layout)
├── room-1.html             ← Room 1 details (template for rooms 2-9)
├── css/
│   └── style.css           ← Professional corporate design
├── js/
│   └── script.js           ← Interactivity & navigation
├── pictures/               ← All images
│   ├── gevel.jpg           ← Building photo
│   ├── student.jpg         ← Student header photo
│   └── kamer 1/            ← Room 1 photos (1.jpg - 6.jpg)
│       ├── 1.jpg through 6.jpg
├── .git/                   ← GitHub repository (hidden)
├── .gitignore              ← Git configuration
└── README.md               ← This file
```

## 🚀 Getting Started

### **Local Development**
1. Open `index.html` in your browser to preview
2. Edit HTML files with any text editor
3. CSS is in `css/style.css` - modify colors, fonts, spacing here
4. JavaScript is in `js/script.js` - add interactivity here

### **Publishing to GitHub Pages**
1. Make changes locally in your folder
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your message here"
   git push
   ```
3. Site automatically deploys to: `https://dfence.github.io/tabakvest85/`

## 📝 Next Steps

### **1. Add Content (Fill in placeholders)**
Replace all `[PLACEHOLDER TEXT]` in HTML files with actual content from www.tabakvest85.be:
- Home page headline and description
- Room features and amenities
- Contact information

### **2. Add More Room Photos**
Create subdirectories for each room:
```
pictures/
├── kamer 2/  (add 1.jpg, 2.jpg, 3.jpg, ...)
├── kamer 3/
├── kamer 4/
... etc
└── kamer 9/
```

### **3. Create Room Pages (2-9)**
Copy `room-1.html` to `room-2.html` through `room-9.html` and update:
- Room number and status
- Image paths (change `pictures/kamer 1/` to `pictures/kamer 2/`, etc.)
- Description and features

### **4. Update Links in rooms.html**
Change placeholder room cards from disabled "Coming Soon" to working links pointing to the new room pages.

## 💻 Local vs GitHub Best Practice

### **Local Folder** (Your Computer)
- ✅ Working space where you make edits
- ✅ Test changes before publishing
- ✅ Keep a backup of all files
- ✅ Never edit directly on GitHub website

### **GitHub Repository** (Cloud Backup & Publishing)
- ✅ Backup of all your files
- ✅ Automatic publishing to GitHub Pages
- ✅ Version history (can revert changes)
- ✅ Only push when you're ready to publish

### **Workflow**
```
Edit locally → Test in browser → git add/commit/push → GitHub Pages updates
```

## 🎨 Customization

### **Colors**
Edit the CSS variables at the top of `css/style.css`:
```css
:root {
  --primary: #1e3a5f;        /* Deep blue */
  --secondary: #2d5a8c;      /* Medium blue */
  --accent: #f39c12;         /* Gold */
  /* ... more colors ... */
}
```

### **Fonts**
Change fonts in the `body` selector:
```css
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
```

### **Images**
- Replace `pictures/gevel.jpg` with your building photo
- Replace `pictures/student.jpg` with your student photo
- Add room photos to subdirectories

## 📱 Responsive Design
The site automatically adapts to:
- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1200px)
- ✅ Mobile (under 768px)

No additional work needed - CSS handles all screen sizes.

## 🔗 Custom Domain (Later)
When ready to use your Vimexx domain instead of github.io:
1. Add a CNAME file to this folder with your domain
2. Configure DNS settings at Vimexx
3. Update GitHub Pages settings

## 📞 Support
Questions? Edit `index.html` to see how HTML works, or ask for help!

---

**Current Status:** ✅ Ready for content and photos  
**Last Updated:** June 2026
