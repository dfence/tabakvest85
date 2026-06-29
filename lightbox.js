/**
 * Simple Lightbox - Pure JavaScript image gallery
 * No external dependencies, works on GitHub Pages
 */

class SimpleLightbox {
  constructor(selector = '[data-lightbox]') {
    this.selector = selector;
    this.currentIndex = 0;
    this.images = [];
    this.galleries = {};
    this.init();
  }

  init() {
    const images = document.querySelectorAll(this.selector);
    
    // Group images by gallery
    images.forEach(img => {
      const gallery = img.getAttribute('data-glightbox')?.split('=')[1] || 'default';
      if (!this.galleries[gallery]) {
        this.galleries[gallery] = [];
      }
      this.galleries[gallery].push(img);
    });

    // Add click handlers
    images.forEach((img, idx) => {
      img.style.cursor = 'pointer';
      img.addEventListener('click', (e) => {
        e.preventDefault();
        const gallery = img.getAttribute('data-glightbox')?.split('=')[1] || 'default';
        this.currentIndex = this.galleries[gallery].indexOf(img);
        this.open(gallery);
      });
    });

    // Create lightbox modal
    this.createModal();
  }

  createModal() {
    if (document.getElementById('simple-lightbox-modal')) return;

    const modal = document.createElement('div');
    modal.id = 'simple-lightbox-modal';
    modal.style.cssText = `
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.95);
      z-index: 9999;
      padding: 20px;
      box-sizing: border-box;
      overflow: auto;
    `;

    modal.innerHTML = `
      <div style="position: relative; display: flex; align-items: center; justify-content: center; height: 100%; min-height: 300px;">
        <img id="lightbox-image" src="" style="max-width: 90%; max-height: 90vh; object-fit: contain;">
        
        <button id="lightbox-prev" style="position: absolute; left: 20px; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.3); border: none; color: white; font-size: 30px; padding: 10px 15px; cursor: pointer; border-radius: 3px; transition: 0.3s;">❮</button>
        
        <button id="lightbox-next" style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.3); border: none; color: white; font-size: 30px; padding: 10px 15px; cursor: pointer; border-radius: 3px; transition: 0.3s;">❯</button>
        
        <button id="lightbox-close" style="position: absolute; top: 20px; right: 20px; background: rgba(255,255,255,0.3); border: none; color: white; font-size: 30px; width: 40px; height: 40px; cursor: pointer; border-radius: 3px; transition: 0.3s;">✕</button>
        
        <div id="lightbox-counter" style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: white; font-size: 14px; background: rgba(0,0,0,0.5); padding: 8px 16px; border-radius: 3px;"></div>
      </div>
    `;

    document.body.appendChild(modal);

    // Event listeners
    document.getElementById('lightbox-close').addEventListener('click', () => this.close());
    document.getElementById('lightbox-prev').addEventListener('click', () => this.prev());
    document.getElementById('lightbox-next').addEventListener('click', () => this.next());

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (modal.style.display === 'none') return;
      if (e.key === 'Escape') this.close();
      if (e.key === 'ArrowLeft') this.prev();
      if (e.key === 'ArrowRight') this.next();
    });

    // Close on background click
    modal.addEventListener('click', (e) => {
      if (e.target === modal) this.close();
    });

    // Hover effects
    const buttons = modal.querySelectorAll('button');
    buttons.forEach(btn => {
      btn.addEventListener('mouseover', () => btn.style.background = 'rgba(255,255,255,0.5)');
      btn.addEventListener('mouseout', () => btn.style.background = 'rgba(255,255,255,0.3)');
    });
  }

  open(gallery) {
    this.currentGallery = gallery;
    this.showImage();
    document.getElementById('simple-lightbox-modal').style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  close() {
    document.getElementById('simple-lightbox-modal').style.display = 'none';
    document.body.style.overflow = 'auto';
  }

  showImage() {
    const images = this.galleries[this.currentGallery];
    if (!images || images.length === 0) return;

    const img = images[this.currentIndex];
    document.getElementById('lightbox-image').src = img.src;
    document.getElementById('lightbox-counter').textContent = `${this.currentIndex + 1} / ${images.length}`;
  }

  next() {
    const images = this.galleries[this.currentGallery];
    this.currentIndex = (this.currentIndex + 1) % images.length;
    this.showImage();
  }

  prev() {
    const images = this.galleries[this.currentGallery];
    this.currentIndex = (this.currentIndex - 1 + images.length) % images.length;
    this.showImage();
  }
}

// Initialize on DOM ready or immediately if already loaded
(function() {
  function init() {
    new SimpleLightbox();
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else if (document.readyState === 'interactive' || document.readyState === 'complete') {
    // Use setTimeout to ensure DOM is fully ready
    setTimeout(init, 0);
  }
})();
