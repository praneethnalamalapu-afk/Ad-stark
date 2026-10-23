document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Menu Toggle
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  const body = document.body;

  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      menuToggle.setAttribute('aria-expanded', !isExpanded);
      navLinks.classList.toggle('active');
      body.classList.toggle('menu-open');
    });

    // Close menu when clicking nav links
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        body.classList.remove('menu-open');
        menuToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Pre-select service in Enquiry Form when clicking quote links
  const serviceSelect = document.getElementById('service');
  const quoteLinks = document.querySelectorAll('[data-service]');

  quoteLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const serviceName = link.getAttribute('data-service');
      if (serviceSelect && serviceName) {
        for (let option of serviceSelect.options) {
          if (option.value.includes(serviceName) || option.text.includes(serviceName)) {
            option.selected = true;
            break;
          }
        }
      }
    });
  });

  // Handle Enquiry Form Submission (Prepare Mailto Draft)
  const enquiryForm = document.getElementById('enquiry-form');
  const formFeedback = document.querySelector('.form-feedback');

  if (enquiryForm) {
    enquiryForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const phone = document.getElementById('phone').value || 'Not provided';
      const business = document.getElementById('business').value || 'Not provided';
      const service = document.getElementById('service').value;
      const message = document.getElementById('message').value;

      const subject = encodeURIComponent(`New Project Enquiry: ${service} - ${name}`);
      const bodyText = encodeURIComponent(
        `Hello Adstrak Media,\n\n` +
        `I would like to enquire about your services.\n\n` +
        `Name: ${name}\n` +
        `Email: ${email}\n` +
        `Phone/WhatsApp: ${phone}\n` +
        `Business Name: ${business}\n` +
        `Service Interested In: ${service}\n\n` +
        `Project Details:\n${message}\n\n` +
        `Looking forward to hearing from you.`
      );

      // Trigger user mail client with pre-filled content
      window.location.href = `mailto:hello@adstrakmedia.in?subject=${subject}&body=${bodyText}`;

      if (formFeedback) {
        formFeedback.style.color = '#38bdf8';
        formFeedback.textContent = 'Preparing your mail client... If it does not open automatically, please email us directly at hello@adstrakmedia.in.';
      }
    });
  }

  // Dynamic Year in Footer
  const yearSpan = document.getElementById('year');
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }

  const portfolioAssets = [
    { name: 'Hospital Ad', file: 'Hospital Ad.mp4', id: '156hfmCoe-NDJu-YZAN5Pcigi7KZWOU_n', type: 'video' },
    { name: 'Real Estate Ad', file: 'Real-estate Ad video.mp4', id: '1dPjleaci5k6OMRliDx1qtrW56bdhVA7b', type: 'video' },
    { name: 'Promotional Video', file: 'Final c3x.mp4', id: '1h2Y0ieFoSRQd8LsPdT_VSZTQCITccFWR', type: 'video' },
    { name: 'Promotional Video', file: 'lv_0_20260920120310.mp4', id: '1bGNseeGsAiDc0_7UQTByo0Q00mpnsuHJ', type: 'video' },
    { name: 'Promotional Video', file: 'shotcut-20260807-210431.mp4', id: '1HXsTqvZDR7_RY0dMcyzQRYwcfi6YFoo6', type: 'video' },
    { name: 'Video Campaign', file: 'VID_20260725_082124_499_bsl.mp4', id: '10TMoUOfhL0pLQl09j5YNADabqWgmWNK5', type: 'video' },
    { name: 'Video Campaign', file: 'VID_20260725_082750_573_bsl.mp4', id: '1qxF6tr0OSfTGhr9Tsd2upaiTCl9AOxvz', type: 'video' },
    { name: 'Promotional Video', file: 'VID-20260917-WA0002.mp4', id: '1pmr3zS9ubSQR5HdYH52ovkUJMX4VCfGk', type: 'video' },
    { name: 'Campaign Creatives', file: '1787844806151.jpg', id: '1E97_y-mWbmkJIi2Wyb3yvHr3e0iGzRy7', type: 'image' },
    { name: 'Campaign Creatives', file: 'Copy of Ad post 3.webp', id: '1gZPSDsfBeIXgxfmtmDdDdMhaNGFS3nst', type: 'image' },
    { name: 'Campaign Creatives', file: 'Thumbnail 3.jpg', id: '1Serim18tMG3vXmHGyHQdTgiHVyh8bCVM', type: 'image' }
  ];
  const portfolioGrid = document.getElementById('portfolio-grid');
  const portfolioResults = document.getElementById('portfolio-results');
  const previewModal = document.getElementById('preview-modal');
  const previewFrame = document.getElementById('portfolio-preview');
  const previewTitle = document.getElementById('portfolio-preview-title');
  const portfolioDriveLink = document.getElementById('portfolio-drive-link');

  if (portfolioGrid && portfolioResults && previewModal && previewFrame && previewTitle && portfolioDriveLink) {
    portfolioAssets.forEach((asset, index) => {
      const item = document.createElement('article');
      item.className = `portfolio-item reveal${index % 4 ? ` reveal-delay-${index % 4}` : ''}`;
      item.dataset.category = asset.type;

      const media = document.createElement('div');
      media.className = 'portfolio-media';

      const image = document.createElement('img');
      image.src = `https://drive.google.com/thumbnail?id=${asset.id}&sz=w800`;
      image.alt = `${asset.name} preview`;
      image.loading = 'lazy';

      const typeLabel = document.createElement('span');
      typeLabel.className = 'portfolio-type';
      typeLabel.textContent = asset.type === 'video' ? 'Video' : 'Creatives';

      const openButton = document.createElement('button');
      openButton.className = 'portfolio-open';
      openButton.type = 'button';
      openButton.dataset.assetId = asset.id;
      openButton.setAttribute('aria-label', `Open ${asset.name}`);
      const openIcon = document.createElement('span');
      openIcon.setAttribute('aria-hidden', 'true');
      openIcon.textContent = asset.type === 'video' ? '▶' : '↗';
      openButton.append(openIcon);

      media.append(image, typeLabel, openButton);

      const caption = document.createElement('div');
      caption.className = 'portfolio-caption';
      const title = document.createElement('h3');
      title.textContent = asset.name;
      const filename = document.createElement('p');
      filename.textContent = asset.file;
      caption.append(title, filename);

      item.append(media, caption);
      portfolioGrid.append(item);
    });

    document.querySelectorAll('.portfolio-filter-btn').forEach(button => {
      button.addEventListener('click', () => {
        const filter = button.dataset.filter;
        document.querySelectorAll('.portfolio-filter-btn').forEach(filterButton => {
          const isActive = filterButton === button;
          filterButton.classList.toggle('active', isActive);
          filterButton.setAttribute('aria-pressed', String(isActive));
        });
        portfolioGrid.querySelectorAll('.portfolio-item').forEach(item => {
          item.hidden = filter !== 'all' && item.dataset.category !== filter;
        });
        const showResults = filter === 'results';
        portfolioGrid.hidden = showResults;
        portfolioResults.hidden = !showResults;
      });
    });

    portfolioGrid.addEventListener('click', event => {
      const openButton = event.target.closest('.portfolio-open');
      if (!openButton) return;

      const asset = portfolioAssets.find(item => item.id === openButton.dataset.assetId);
      if (!asset) return;

      previewTitle.textContent = asset.name;
      previewFrame.src = `https://drive.google.com/file/d/${asset.id}/preview`;
      portfolioDriveLink.href = `https://drive.google.com/file/d/${asset.id}/view`;
      previewModal.showModal();
    });

    previewModal.querySelector('.portfolio-modal-close').addEventListener('click', () => {
      previewModal.close();
    });
    previewModal.addEventListener('close', () => {
      previewFrame.src = '';
    });
  }

  // Intersection Observer for Scroll Animations
  const revealElements = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => observer.observe(el));
  } else {
    // Fallback if IntersectionObserver is not available
    revealElements.forEach(el => el.classList.add('active'));
  }
});