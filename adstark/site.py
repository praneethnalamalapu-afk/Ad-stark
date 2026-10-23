import os, zipfile, textwrap, shutil

base = "/mnt/data/adstrak-media-business-growth"
if os.path.exists(base):
    shutil.rmtree(base)
os.makedirs(base + "/css", exist_ok=True)
os.makedirs(base + "/js", exist_ok=True)
os.makedirs(base + "/assets", exist_ok=True)

files = {
"index.html": r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#0b5cff" />
  <meta name="description" content="Adstrak Media helps businesses grow through creative promotional videos and practical marketing solutions. Build. Grow. Scale." />
  <title>Adstrak Media | Build. Grow. Scale.</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <div class="announcement"><span class="announcement-dot"></span> Promotional video creation is available now <a href="#video-service">Explore the service <span aria-hidden="true">↗</span></a></div>
  <header class="site-header" id="top">
    <nav class="nav container" aria-label="Main navigation">
      <a class="brand" href="#top" aria-label="Adstrak Media home"><span class="brand-mark">A<span>+</span></span><span class="brand-copy">adstrak<span>media</span></span></a>
      <button class="menu-toggle" aria-label="Open navigation menu" aria-expanded="false"><span></span><span></span><span></span></button>
      <div class="nav-links">
        <a href="#services">Services</a><a href="#work">Our Work</a><a href="#about">About</a><a href="#process">How It Works</a>
        <a class="nav-cta" href="#contact">Let's Talk <span>↗</span></a>
      </div>
    </nav>
  </header>

  <main>
    <section class="hero section-pad">
      <div class="hero-orb orb-one"></div><div class="hero-orb orb-two"></div>
      <div class="container hero-grid">
        <div class="hero-copy reveal">
          <div class="eyebrow"><span class="eyebrow-line"></span> YOUR BUSINESS GROWTH PARTNER</div>
          <h1>Build. Grow.<br><span>Scale.</span></h1>
          <p class="hero-lead">Good businesses deserve to be seen.</p>
          <p class="hero-desc">We help businesses strengthen their online presence and grow through creative content and practical marketing solutions.</p>
          <div class="hero-actions"><a class="btn btn-primary" href="#services">Explore Our Services <span>↗</span></a><a class="btn btn-secondary" href="#contact">Contact Us</a></div>
          <div class="hero-proof"><div class="proof-avatars"><span>A</span><span>+</span><span>↗</span></div><p><strong>Creative ideas. Clear communication.</strong><br>Built around your business goals.</p></div>
        </div>
        <div class="hero-visual reveal reveal-delay">
          <div class="visual-window">
            <div class="window-top"><div class="window-dots"><i></i><i></i><i></i></div><span>YOUR NEXT BIG IDEA</span><span class="window-menu">•••</span></div>
            <div class="visual-content">
              <div class="visual-label">MAKE YOUR BRAND</div><div class="visual-title">Impossible<br><span>to ignore.</span></div>
              <div class="visual-bottom"><span>CONTENT THAT CONNECTS</span><span class="play-button">▶</span></div>
              <div class="visual-shape shape-a"></div><div class="visual-shape shape-b"></div>
            </div>
          </div>
          <div class="floating-card floating-card-top"><span class="float-icon">✳</span><div><strong>Creative first</strong><small>Ideas with purpose</small></div></div>
          <div class="floating-card floating-card-bottom"><span class="float-icon blue">↗</span><div><strong>Growth minded</strong><small>Focused on your goals</small></div></div>
          <div class="hero-spark spark-one">✳</div><div class="hero-spark spark-two">✦</div>
        </div>
      </div>
      <div class="container hero-bottom"><span>CREATIVE CONTENT</span><i></i><span>BRAND VISIBILITY</span><i></i><span>BUSINESS GROWTH</span></div>
    </section>

    <section class="services section-pad" id="services">
      <div class="container">
        <div class="section-heading reveal"><div><div class="eyebrow"><span class="eyebrow-line"></span> WHAT WE DO</div><h2>Creative solutions.<br><span>Real business goals.</span></h2></div><p>Start with what your business needs today. As we grow, our services will grow with you.</p></div>
        <div class="service-grid">
          <article class="service-card service-featured reveal" id="video-service">
            <div class="service-card-top"><span class="service-icon">▶</span><span class="status status-live"><i></i> AVAILABLE NOW</span></div>
            <div class="service-art video-art"><div class="art-play">▶</div><span class="art-caption">YOUR BRAND, IN MOTION</span><div class="art-slab"></div></div>
            <h3>Promotional Video Creation</h3><p>Make your product, service or business stand out with a polished promotional video designed to catch attention.</p>
            <div class="service-price"><span>Starting at</span><strong>₹1,499</strong></div>
            <a class="text-link" href="#contact" data-service="Promotional Video Creation">Get a quote <span>↗</span></a>
          </article>
          <article class="service-card reveal reveal-delay-1">
            <div class="service-card-top"><span class="service-icon pale">◉</span><span class="status status-soon">COMING SOON</span></div>
            <div class="service-art social-art"><div class="social-tile tile-one">◎</div><div class="social-tile tile-two">f</div><div class="social-tile tile-three">▶</div><div class="social-orbit"></div></div>
            <h3>Social Media Management</h3><p>Consistent, thoughtful social content to help your brand stay active and connected with its audience.</p>
            <div class="service-footnote">Planned service</div><span class="text-link disabled-link">Launching in the future <span>→</span></span>
          </article>
          <article class="service-card reveal reveal-delay-2">
            <div class="service-card-top"><span class="service-icon pale">↗</span><span class="status status-soon">COMING SOON</span></div>
            <div class="service-art leads-art"><div class="lead-chart"><span></span><span></span><span></span><span></span><span></span><b>↗</b></div><div class="lead-chip">REACH MORE</div></div>
            <h3>Digital Marketing &amp; Lead Generation</h3><p>Future solutions focused on reaching the right audience and creating more opportunities for your business.</p>
            <div class="service-footnote">Planned service</div><span class="text-link disabled-link">Launching in the future <span>→</span></span>
          </article>
          <article class="service-card service-planned reveal reveal-delay-1">
            <div class="service-card-top"><span class="service-icon pale">✳</span><span class="status status-planned">PLANNED</span></div>
            <div class="service-art brand-art"><div class="brand-monogram">A<span>+</span></div><div class="brand-lines"><i></i><i></i><i></i></div><div class="brand-ring"></div></div>
            <h3>Brand Building &amp; Marketing Strategy</h3><p>A future offering to help businesses define their message, strengthen their identity and plan for growth.</p>
            <div class="service-footnote">In development</div><span class="text-link disabled-link">More details coming <span>→</span></span>
          </article>
        </div>
        <p class="availability-note"><span>ⓘ</span> Only promotional video creation is currently advertised as available. Other services are clearly marked as future offerings.</p>
      </div>
    </section>

    <section class="work section-pad" id="work">
      <div class="container">
        <div class="section-heading reveal"><div><div class="eyebrow"><span class="eyebrow-line"></span> THE CREATIVE PLAYGROUND</div><h2>Ideas made to<br><span>make an impact.</span></h2></div><p>Concept samples show the kind of creative directions we can explore. We’ll add completed client projects as our portfolio grows.</p></div>
        <div class="work-grid">
          <article class="work-card work-large reveal"><div class="work-image work-food"><span class="concept-label">CONCEPT SAMPLE</span><div class="food-sticker">FRESH<br><b>EVERY DAY</b></div><div class="food-copy"><small>MADE WITH LOVE</small><strong>Good food.<br>Good mood.</strong></div><div class="food-circle"></div></div><div class="work-meta"><div><span>FOOD &amp; BEVERAGE</span><h3>A delicious first impression</h3></div><span class="work-arrow">↗</span></div></article>
          <article class="work-card reveal reveal-delay-1"><div class="work-image work-product"><span class="concept-label">CONCEPT SAMPLE</span><div class="product-sun"></div><div class="product-bottle"><span>PURE<br>FORM</span></div><div class="product-word">LESS,<br>BETTER.</div></div><div class="work-meta"><div><span>PRODUCT PROMOTION</span><h3>Product spotlight</h3></div><span class="work-arrow">↗</span></div></article>
          <article class="work-card reveal reveal-delay-2"><div class="work-image work-retail"><span class="concept-label">CONCEPT SAMPLE</span><div class="retail-bag">YOUR<br><b>STORE</b></div><div class="retail-copy">STYLE THAT<br><strong>STANDS OUT.</strong></div><div class="retail-spark">✳</div></div><div class="work-meta"><div><span>RETAIL &amp; FASHION</span><h3>Make your brand memorable</h3></div><span class="work-arrow">↗</span></div></article>
          <article class="work-card reveal"><div class="work-image work-service"><span class="concept-label">CONCEPT SAMPLE</span><div class="service-circle">YOUR<br><b>SERVICE</b><br><small>YOUR NEXT CHAPTER</small></div><div class="service-side-text">BUILT AROUND YOU</div></div><div class="work-meta"><div><span>LOCAL SERVICES</span><h3>Trust starts with visibility</h3></div><span class="work-arrow">↗</span></div></article>
        </div>
        <div class="work-foot reveal"><span>These are illustrative concept samples, not completed client campaigns.</span><a class="text-link" href="#contact">Create something for your business <span>↗</span></a></div>
      </div>
    </section>

    <section class="about section-pad" id="about">
      <div class="container about-grid">
        <div class="about-visual reveal"><div class="about-backdrop"></div><div class="about-note note-top"><span>01</span> Creativity with purpose</div><div class="about-note note-bottom"><span>02</span> Practical, clear solutions</div><div class="about-main-card"><span class="about-plus">✳</span><small>THE ADSTRAK APPROACH</small><strong>Make every<br>brand moment<br><em>count.</em></strong><div class="about-card-line"></div><span class="about-card-foot">BUILD • GROW • SCALE</span></div></div>
        <div class="about-copy reveal reveal-delay-1"><div class="eyebrow"><span class="eyebrow-line"></span> A LITTLE ABOUT US</div><h2>We’re here to help<br>your business <span>move forward.</span></h2><p>Adstrak Media is your business growth partner—helping brands communicate clearly, show up confidently online and connect with the people who matter.</p><p>We believe good marketing starts with understanding your business. That means creative thinking, honest communication and practical solutions that fit your goals.</p><div class="values-list"><div><span>✓</span><p><strong>Creativity</strong><small>Ideas that help your brand stand out.</small></p></div><div><span>✓</span><p><strong>Clear communication</strong><small>Simple conversations, aligned expectations.</small></p></div><div><span>✓</span><p><strong>Practical thinking</strong><small>Solutions shaped around your business.</small></p></div></div><a class="btn btn-dark" href="#contact">Let’s work together <span>↗</span></a></div>
      </div>
    </section>

    <section class="video-offer section-pad">
      <div class="container offer-panel reveal" id="offer">
        <div class="offer-copy"><div class="eyebrow eyebrow-light"><span class="eyebrow-line"></span> OUR AVAILABLE SERVICE</div><h2>Promotional videos<br>for your <span>business.</span></h2><p>Turn your product or service into a story people want to watch. Let’s discuss the right approach for your brand and budget.</p><div class="offer-price"><span>Packages starting at</span><strong>₹1,499</strong><small>Final quote depends on your requirements.</small></div><a class="btn btn-white" href="#contact" data-service="Promotional Video Creation">Get a Quote <span>↗</span></a></div>
        <div class="offer-visual"><div class="offer-screen"><div class="offer-screen-top"><span>ADSTRAK MEDIA</span><span>01 / 04</span></div><div class="offer-screen-big">YOUR<br><em>STORY.</em></div><div class="offer-screen-bottom"><span>MADE TO CONNECT</span><span class="offer-play">▶</span></div></div><div class="offer-sticker">MAKE<br>IT <b>MOVE</b> ↗</div><div class="offer-orbit"></div></div>
      </div>
      <div class="container deliverables">
        <div class="deliverable-intro reveal"><div class="eyebrow"><span class="eyebrow-line"></span> WHAT TO EXPECT</div><h2>Clear expectations.<br><span>Better collaboration.</span></h2><p>We’ll confirm the scope before work begins, so you know what’s included in your quote.</p></div>
        <div class="deliverable-list reveal reveal-delay-1">
          <div class="deliverable-row"><span class="deliverable-number">01</span><div><h3>Video length &amp; format</h3><p>Agreed to suit your platform, message and creative brief.</p></div><span class="deliverable-icon">↗</span></div>
          <div class="deliverable-row"><span class="deliverable-number">02</span><div><h3>Editing &amp; revisions</h3><p>Editing scope and number of revision rounds confirmed in your quote.</p></div><span class="deliverable-icon">✳</span></div>
          <div class="deliverable-row"><span class="deliverable-number">03</span><div><h3>Footage &amp; production</h3><p>We’ll clarify whether you provide footage or whether any shooting is included before confirming the project.</p></div><span class="deliverable-icon">▣</span></div>
          <div class="deliverable-row"><span class="deliverable-number">04</span><div><h3>Timeline &amp; delivery</h3><p>Delivery date, final file format and payment milestones agreed upfront.</p></div><span class="deliverable-icon">✓</span></div>
        </div>
      </div>
    </section>

    <section class="process section-pad" id="process">
      <div class="container">
        <div class="section-heading reveal"><div><div class="eyebrow"><span class="eyebrow-line"></span> SIMPLE FROM START TO FINISH</div><h2>Four steps to your<br><span>next great video.</span></h2></div><p>A straightforward process with clear communication at every step.</p></div>
        <div class="process-grid">
          <article class="process-step reveal"><span class="step-num">01</span><div class="step-icon">↗</div><h3>Tell us about your business</h3><p>Share your business, audience and what you want your video to achieve.</p><span class="step-line"></span></article>
          <article class="process-step reveal reveal-delay-1"><span class="step-num">02</span><div class="step-icon">☷</div><h3>Discuss your requirements</h3><p>We align on the concept, deliverables, pricing and timeline.</p><span class="step-line"></span></article>
          <article class="process-step reveal reveal-delay-2"><span class="step-num">03</span><div class="step-icon">▶</div><h3>We create and edit</h3><p>We bring the agreed creative direction to life and share it for review.</p><span class="step-line"></span></article>
          <article class="process-step reveal reveal-delay-3"><span class="step-num">04</span><div class="step-icon">✓</div><h3>Review and receive</h3><p>After review and agreed payment milestones, receive the final deliverable.</p><span class="step-line"></span></article>
        </div>
      </div>
    </section>

    <section class="contact section-pad" id="contact">
      <div class="container contact-grid">
        <div class="contact-copy reveal"><div class="eyebrow eyebrow-light"><span class="eyebrow-line"></span> LET’S START A CONVERSATION</div><h2>Have a business<br>to <span>grow?</span></h2><p>Tell us what you’re working on. We’ll get back to you to understand your needs and discuss the next step.</p>
          <div class="contact-links">
            <a href="mailto:hello@adstrakmedia.in"><span class="contact-link-icon">✉</span><span><small>EMAIL US</small><strong>hello@adstrakmedia.in</strong></span><span class="contact-link-arrow">↗</span></a>
            <a href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer"><span class="contact-link-icon">◎</span><span><small>FOLLOW ALONG</small><strong>Instagram</strong></span><span class="contact-link-arrow">↗</span></a>
            <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer"><span class="contact-link-icon">f</span><span><small>FIND US ON</small><strong>Facebook</strong></span><span class="contact-link-arrow">↗</span></a>
          </div>
          <a class="whatsapp-link" href="https://wa.me/?text=Hi%20Adstrak%20Media%2C%20I%27d%20like%20to%20enquire%20about%20a%20promotional%20video." target="_blank" rel="noopener noreferrer"><span>◉</span> Enquire on WhatsApp <b>↗</b></a>
        </div>
        <form class="contact-form reveal reveal-delay-1" id="enquiry-form">
          <div class="form-heading"><span>YOUR NEXT STEP</span><h3>Tell us a little about it.</h3><p>Fields marked * are required.</p></div>
          <label for="name">Your name *</label><input id="name" name="name" type="text" placeholder="e.g. Priya Sharma" required>
          <div class="form-row"><div><label for="email">Email address *</label><input id="email" name="email" type="email" placeholder="you@business.com" required></div><div><label for="phone">Phone / WhatsApp</label><input id="phone" name="phone" type="tel" placeholder="+91 00000 00000"></div></div>
          <label for="business">Business name</label><input id="business" name="business" type="text" placeholder="Your brand or business">
          <label for="service">What are you interested in? *</label><select id="service" name="service" required><option value="">Choose a service</option><option>Promotional Video Creation</option><option>Social Media Management (future service)</option><option>Digital Marketing &amp; Lead Generation (future service)</option><option>Brand Building &amp; Marketing Strategy (planned)</option><option>Something else</option></select>
          <label for="message">Tell us about your project *</label><textarea id="message" name="message" rows="4" placeholder="What do you want to promote? What are your goals?" required></textarea>
          <button class="btn btn-primary form-submit" type="submit">Prepare Enquiry <span>↗</span></button>
          <p class="form-note">This demo prepares an email enquiry in your email app. Connect a form service or backend before publishing to receive submissions automatically.</p>
          <p class="form-feedback" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-main"><a class="brand brand-footer" href="#top"><span class="brand-mark">A<span>+</span></span><span class="brand-copy">adstrak<span>media</span></span></a><p>Build. Grow. Scale.<br><span>Your Business Growth Partner.</span></p><a class="footer-top" href="#top">BACK TO TOP ↑</a></div>
    <div class="container footer-bottom"><span>© <span id="year"></span> Adstrak Media. All rights reserved.</span><span>Built for ideas that move businesses forward.</span></div>
  </footer>
  <a class="floating-whatsapp" href="https://wa.me/?text=Hi%20Adstrak%20Media%2C%20I%27d%20like%20to%20enquire." target="_blank" rel="noopener noreferrer" aria-label="Enquire on WhatsApp">◉</a>
  <script src="js/main.js"></script>
</body>
</html>
''',
"css/style.css": r''' :root{--blue:#0b5cff;--blue-dark:#0844c7;--ink:#101522;--muted:#667085;--paper:#f7f9fc;--line:#e7ebf2;--white:#fff;--radius:22px;--font:'DM Sans',sans-serif;--display:'Manrope',sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;font-family:var(--font);color:var(--ink);background:#fff;line-height:1.6;-webkit-font-smoothing:antialiased}body.menu-open{overflow:hidden}a{color:inherit;text-decoration:none}button,input,select,textarea{font:inherit}.container{width:min(1160px,calc(100% - 48px));margin-inline:auto}.section-pad{padding:110px 0}.announcement{min-height:36px;display:flex;align-items:center;justify-content:center;gap:9px;background:#0b1325;color:#dbe5ff;font-size:11px;letter-spacing:.02em;padding:8px 20px;text-align:center}.announcement a{color:#fff;font-weight:700;text-decoration:underline;text-underline-offset:3px;margin-left:6px}.announcement-dot,.status i{width:7px;height:7px;background:#5ee1a0;border-radius:50%;display:inline-block;flex-shrink:0}.site-header{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.93);backdrop-filter:blur(16px);border-bottom:1px solid rgba(16,21,34,.06)}.nav{height:78px;display:flex;align-items:center;justify-content:space-between}.brand{display:flex;align-items:center;gap:10px}.brand-mark{width:38px;height:38px;border-radius:12px;background:var(--blue);color:#fff;display:grid;place-items:center;font:800 20px var(--display);position:relative;letter-spacing:-2px}.brand-mark>span{font-size:10px;position:absolute;right:5px;top:4px;letter-spacing:0}.brand-copy{font:800 17px/1 var(--display);letter-spacing:-.8px}.brand-copy span{display:block;color:var(--blue);font-size:10px;letter-spacing:3px;text-transform:uppercase;margin-top:5px}.nav-links{display:flex;align-items:center;gap:32px;font-size:13px;font-weight:600;color:#485064}.nav-links>a:not(.nav-cta):hover{color:var(--blue)}.nav-cta{background:var(--blue);color:white;border-radius:10px;padding:12px 18px;display:flex;align-items:center;gap:18px;transition:.25s}.nav-cta:hover,.btn-primary:hover{background:var(--blue-dark);transform:translateY(-2px)}.menu-toggle{display:none;border:0;background:none;padding:8px}.menu-toggle span{width:24px;height:2px;background:var(--ink);display:block;margin:5px}
.hero{padding:90px 0 26px;position:relative;overflow:hidden;background:radial-gradient(ellipse at 82% 35%,#eef4ff 0,rgba(239,245,255,.4) 35%,transparent 65%),#fff}.hero-grid{display:grid;grid-template-columns:1fr .95fr;align-items:center;gap:65px;min-height:470px;position:relative;z-index:1}.eyebrow{display:flex;align-items:center;gap:10px;font-size:10px;font-weight:800;letter-spacing:2px;color:var(--blue);margin-bottom:24px}.eyebrow-line{height:2px;width:23px;background:var(--blue);display:inline-block}.hero h1{font:800 clamp(58px,7vw,91px)/.99 var(--display);letter-spacing:-6px;margin:0 0 22px}.hero h1 span{color:var(--blue)}.hero-lead{font:700 21px var(--display);margin:0 0 8px}.hero-desc{font-size:15px;line-height:1.85;color:var(--muted);max-width:480px;margin:0}.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:29px}.btn{min-height:48px;padding:0 20px;border-radius:10px;display:inline-flex;align-items:center;justify-content:center;gap:22px;font-size:12px;font-weight:700;border:1px solid transparent;transition:transform .25s,background .25s,border-color .25s;cursor:pointer}.btn-primary{background:var(--blue);color:#fff}.btn-secondary{border-color:#dce2eb;background:rgba(255,255,255,.8)}.btn-secondary:hover{border-color:var(--blue);color:var(--blue)}.hero-proof{display:flex;align-items:center;gap:12px;margin-top:34px}.proof-avatars{display:flex}.proof-avatars span{width:29px;height:29px;border-radius:50%;background:#e5edff;border:2px solid white;display:grid;place-items:center;color:var(--blue);font-size:11px;font-weight:800;margin-left:-5px}.proof-avatars span:first-child{margin-left:0;background:#111a30;color:white}.proof-avatars span:nth-child(2){background:#d9f6e8;color:#116c46}.hero-proof p{font-size:10px;line-height:1.55;color:#8a92a3;margin:0}.hero-proof strong{font-size:11px;color:#30394a}.hero-visual{position:relative;padding:20px 8px 28px 22px}.visual-window{position:relative;z-index:2;background:#101727;border-radius:18px;padding:12px;box-shadow:0 28px 70px #1a3e8524;transform:rotate(1deg)}.window-top{height:32px;display:flex;align-items:center;justify-content:space-between;color:#8490a8;font-size:8px;letter-spacing:1.6px;padding:0 6px 10px}.window-dots{display:flex;gap:4px}.window-dots i{width:6px;height:6px;background:#667085;border-radius:50%}.window-dots i:first-child{background:#ff7676}.window-dots i:nth-child(2){background:#ffd36c}.window-dots i:nth-child(3){background:#5ee1a0}.window-menu{font-size:13px}.visual-content{min-height:310px;border-radius:10px;overflow:hidden;position:relative;padding:34px 30px;background:linear-gradient(135deg,#0b5cff,#0939a9 65%,#061b54);color:white}.visual-label{font-size:9px;font-weight:700;letter-spacing:2px;position:relative;z-index:2}.visual-title{font:800 clamp(36px,4.5vw,57px)/1.08 var(--display);letter-spacing:-2.8px;margin-top:38px;position:relative;z-index:2}.visual-title span{color:#b7ccff}.visual-bottom{display:flex;align-items:center;justify-content:space-between;position:absolute;bottom:22px;left:30px;right:24px;font-size:8px;letter-spacing:1.5px;font-weight:700;z-index:2}.play-button{width:38px;height:38px;border-radius:50%;background:white;color:var(--blue);display:grid;place-items:center;font-size:10px;padding-left:2px}.visual-shape{position:absolute;border:1px solid #ffffff2c;border-radius:50%;width:280px;height:280px;right:-90px;top:65px}.shape-b{width:210px;height:210px;right:-55px;top:100px;border-color:#ffffff45}.floating-card{display:flex;align-items:center;gap:10px;position:absolute;background:#fff;box-shadow:0 12px 36px #1b35661a;border:1px solid #edf0f7;border-radius:13px;padding:12px 15px;z-index:3}.floating-card strong,.floating-card small{display:block}.floating-card strong{font-size:11px}.floating-card small{font-size:9px;color:#8a92a3;margin-top:2px}.floating-card-top{top:0;right:-8px}.floating-card-bottom{bottom:0;left:0}.float-icon{width:30px;height:30px;background:#e5f8ef;color:#17865a;border-radius:9px;display:grid;place-items:center;font-size:17px}.float-icon.blue{background:#e8efff;color:var(--blue)}.hero-spark{position:absolute;color:var(--blue);font-size:28px}.spark-one{right:-8px;top:36px}.spark-two{left:-4px;bottom:62px;font-size:18px}.hero-bottom{display:flex;align-items:center;gap:15px;color:#9aa2b2;font-size:9px;letter-spacing:1.7px;font-weight:700;margin-top:75px}.hero-bottom i{width:4px;height:4px;background:#aeb7c7;border-radius:50%}.hero-orb{position:absolute;border:1px solid #e9effb;border-radius:50%;pointer-events:none}.orb-one{width:550px;height:550px;right:-220px;top:40px}.orb-two{width:410px;height:410px;right:-150px;top:110px}
.section-heading{display:flex;align-items:end;justify-content:space-between;gap:35px;margin-bottom:44px}.section-heading h2,.about-copy h2,.deliverable-intro h2{font:800 clamp(32px,4vw,47px)/1.16 var(--display);letter-spacing:-2px;margin:0}.section-heading h2 span,.about-copy h2 span,.deliverable-intro h2 span{color:var(--blue)}.section-heading>p{max-width:360px;color:var(--muted);font-size:13px;line-height:1.8;margin:0 0 4px}.services{background:#f8faff}.service-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:15px}.service-card{background:#fff;border:1px solid #e9edf5;border-radius:18px;padding:20px;min-width:0;transition:transform .3s,box-shadow .3s,border-color .3s}.service-card:hover{transform:translateY(-6px);box-shadow:0 18px 45px #1e3a6a0d;border-color:#d6e2ff}.service-featured{border-color:#bcd0ff;box-shadow:0 10px 35px #0b5cff0b}.service-card-top{display:flex;align-items:center;justify-content:space-between;gap:8px}.service-icon{width:35px;height:35px;background:var(--blue);color:white;border-radius:10px;display:grid;place-items:center;font-size:15px}.service-icon.pale{background:#edf3ff;color:var(--blue)}.status{display:flex;align-items:center;gap:6px;font-size:8px;font-weight:800;letter-spacing:.7px;white-space:nowrap}.status-live{color:#17865a}.status-live i{width:6px;height:6px}.status-soon{color:#7c8494;background:#f0f2f6;border-radius:5px;padding:5px 7px}.status-planned{color:#9b6a14;background:#fff5df;border-radius:5px;padding:5px 7px}.service-art{height:142px;border-radius:12px;margin:18px 0;position:relative;overflow:hidden}.video-art{background:linear-gradient(135deg,#0c5cff,#062d87);display:flex;align-items:center;justify-content:center}.art-play{width:43px;height:43px;border-radius:50%;background:#fff;color:var(--blue);display:grid;place-items:center;font-size:12px;z-index:2;box-shadow:0 6px 20px #001c5d40}.art-caption{position:absolute;bottom:13px;left:14px;color:#dce7ff;font-size:7px;letter-spacing:1.7px}.art-slab{position:absolute;width:160px;height:160px;border:1px solid #ffffff2d;border-radius:50%;right:-45px;top:-50px}.social-art{background:#f2f5fc}.social-tile{position:absolute;width:50px;height:50px;display:grid;place-items:center;color:white;font-size:24px;border-radius:14px;box-shadow:0 12px 22px #12204420}.tile-one{background:#e04f9c;left:22%;top:34px;transform:rotate(-12deg)}.tile-two{background:#2263df;left:43%;top:52px;transform:rotate(8deg)}.tile-three{background:#e44d42;left:63%;top:28px;transform:rotate(13deg)}.social-orbit{position:absolute;width:160px;height:160px;border:1px dashed #b9c9e9;border-radius:50%;left:calc(50% - 80px);top:-10px}.leads-art{background:#edf4ff;display:grid;place-items:center}.lead-chart{height:80px;width:180px;display:flex;align-items:end;gap:10px;border-bottom:1px solid #c8d6f0;position:relative;padding:0 10px}.lead-chart span{width:20px;background:linear-gradient(#4f91ff,#0b5cff);border-radius:5px 5px 0 0}.lead-chart span:nth-child(1){height:24px}.lead-chart span:nth-child(2){height:39px}.lead-chart span:nth-child(3){height:32px}.lead-chart span:nth-child(4){height:55px}.lead-chart span:nth-child(5){height:72px}.lead-chart b{position:absolute;right:0;top:-14px;font-size:24px;color:var(--blue)}.lead-chip{position:absolute;bottom:12px;right:12px;background:#fff;padding:5px 8px;border-radius:5px;font-size:7px;letter-spacing:1px;font-weight:800;color:var(--blue)}.brand-art{background:#11192d;display:flex;align-items:center;justify-content:center;gap:15px}.brand-monogram{font:800 52px var(--display);color:#fff;letter-spacing:-5px;position:relative}.brand-monogram span{font-size:15px;color:#8db1ff;position:absolute;right:-5px;top:0}.brand-lines{display:grid;gap:7px}.brand-lines i{display:block;width:45px;height:4px;background:#6e94ec;border-radius:4px}.brand-lines i:nth-child(2){width:32px;opacity:.7}.brand-lines i:nth-child(3){width:22px;opacity:.4}.brand-ring{position:absolute;width:130px;height:130px;border:1px solid #ffffff20;border-radius:50%;right:-38px;top:15px}.service-card h3{font:800 16px/1.35 var(--display);letter-spacing:-.4px;margin:0 0 10px}.service-card>p{font-size:11px;line-height:1.8;color:var(--muted);margin:0;min-height:80px}.service-price{display:flex;align-items:baseline;gap:8px;border-top:1px solid #edf0f5;padding-top:15px;margin-top:18px}.service-price span{font-size:10px;color:#8b94a5}.service-price strong{font:800 21px var(--display);color:var(--blue)}.text-link{display:inline-flex;align-items:center;justify-content:space-between;gap:15px;font-size:11px;font-weight:800;color:var(--blue);margin-top:16px}.text-link span{font-size:15px;transition:transform .2s}.text-link:hover span{transform:translate(3px,-3px)}.service-footnote{border-top:1px solid #edf0f5;padding-top:15px;margin-top:18px;color:#9aa1af;font-size:10px}.disabled-link{color:#9299a7;cursor:default}.availability-note{font-size:10px;color:#7d8798;display:flex;align-items:center;gap:7px;margin:24px 0 0}.availability-note span{color:var(--blue);font-size:14px}
.work{background:#fff}.work-grid{display:grid;grid-template-columns:1.15fr 1fr 1fr;gap:20px}.work-card{min-width:0}.work-large{grid-row:span 2}.work-image{height:230px;border-radius:16px;position:relative;overflow:hidden}.work-large .work-image{height:490px}.concept-label{position:absolute;left:13px;top:13px;background:#ffffffdd;backdrop-filter:blur(8px);border-radius:5px;padding:6px 8px;font-size:7px;font-weight:800;letter-spacing:1px;z-index:4}.work-food{background:linear-gradient(145deg,#f8be6c,#f16f49 65%,#d94540)}.food-circle{position:absolute;width:300px;height:300px;border-radius:50%;background:#ffdf9a;right:-55px;bottom:35px;box-shadow:inset 0 0 0 14px #fff5d1}.food-circle:before{content:"";position:absolute;inset:45px;border-radius:50%;background:repeating-conic-gradient(#d85132 0deg 12deg,#f8ad5a 12deg 24deg)}.food-circle:after{content:"";position:absolute;inset:82px;border-radius:50%;background:#e5a64f;border:10px solid #f8d9a0}.food-copy{position:absolute;left:24px;bottom:32px;color:#532a20;z-index:2}.food-copy small{font-size:8px;letter-spacing:2px;font-weight:800}.food-copy strong{display:block;font:800 37px/.98 var(--display);letter-spacing:-1.8px;margin-top:9px}.food-sticker{position:absolute;right:20px;top:45px;width:85px;height:85px;border-radius:50%;background:#fff8df;color:#a63f26;display:grid;align-content:center;text-align:center;font-size:9px;line-height:1.4;transform:rotate(12deg);z-index:3}.food-sticker b{font-size:11px}.work-product{background:#d8e7df}.product-sun{width:160px;height:160px;border-radius:50%;background:#f6bd67;position:absolute;right:10px;top:25px}.product-bottle{position:absolute;width:58px;height:125px;background:linear-gradient(90deg,#4c685c,#9db6a5,#3c5d50);border-radius:13px 13px 8px 8px;left:32%;bottom:16px;box-shadow:15px 8px 20px #3d5b4b30;display:grid;place-items:center;color:#fff;font-size:9px;letter-spacing:1px;text-align:center}.product-bottle:before{content:"";position:absolute;width:25px;height:22px;background:#536d60;top:-19px;border-radius:5px 5px 0 0}.product-word{position:absolute;left:20px;bottom:20px;font:800 22px/.95 var(--display);color:#28493b;letter-spacing:-1px}.work-retail{background:#e5d8f7}.retail-bag{position:absolute;width:94px;height:110px;background:#f6f1ff;left:24%;bottom:12px;transform:rotate(-8deg);box-shadow:12px 10px 20px #3f24541a;display:grid;place-content:center;text-align:center;color:#6741a4;font-size:12px}.retail-bag:before{content:"";position:absolute;width:35px;height:22px;border:3px solid #f6f1ff;border-bottom:0;border-radius:15px 15px 0 0;top:-18px;left:28px}.retail-copy{position:absolute;right:17px;bottom:25px;font-size:10px;line-height:1.3;color:#563b79;font-weight:700}.retail-copy strong{font-size:15px}.retail-spark{position:absolute;right:20px;top:40px;font-size:45px;color:#8d65c5}.work-service{background:#d9e9ff}.service-circle{position:absolute;width:170px;height:170px;border-radius:50%;background:#0b5cff;color:#fff;left:calc(50% - 85px);top:30px;display:grid;align-content:center;text-align:center;font-size:13px;line-height:1.3;box-shadow:0 12px 30px #0b5cff33}.service-circle b{font:800 22px var(--display)}.service-circle small{font-size:6px;letter-spacing:1.2px;margin-top:8px}.service-side-text{position:absolute;bottom:13px;left:15px;font-size:7px;letter-spacing:2px;color:#2b5da6;font-weight:800}.work-meta{display:flex;align-items:center;justify-content:space-between;padding:13px 2px 20px}.work-meta span:first-child{font-size:8px;font-weight:800;color:#8b94a5;letter-spacing:1.2px}.work-meta h3{font:800 13px var(--display);margin:3px 0 0}.work-arrow{width:31px;height:31px;border:1px solid #e5eaf2;border-radius:50%;display:grid;place-items:center;color:var(--blue);flex-shrink:0}.work-foot{border-top:1px solid var(--line);padding-top:20px;display:flex;justify-content:space-between;align-items:center;gap:20px}.work-foot>span{font-size:10px;color:#8992a2}.work-foot .text-link{margin:0}
.about{background:#f8faff}.about-grid{display:grid;grid-template-columns:.95fr 1fr;align-items:center;gap:100px}.about-visual{height:490px;position:relative;display:grid;place-items:center}.about-backdrop{position:absolute;width:82%;height:82%;background:#e4edff;border-radius:50%;left:4%;top:7%}.about-main-card{position:relative;z-index:1;width:285px;height:360px;background:var(--blue);border-radius:18px;color:white;padding:30px;box-shadow:0 24px 50px #0b5cff2e;transform:rotate(-4deg);display:flex;flex-direction:column;justify-content:center}.about-plus{position:absolute;right:25px;top:20px;font-size:30px;color:#9ebaff}.about-main-card>small{font-size:8px;letter-spacing:2px;color:#d5e2ff;font-weight:800}.about-main-card>strong{font:800 38px/1.12 var(--display);letter-spacing:-2px;margin-top:28px}.about-main-card em{font-style:normal;color:#b8d0ff}.about-card-line{height:1px;background:#ffffff4c;margin-top:30px}.about-card-foot{font-size:8px;letter-spacing:1.7px;margin-top:13px}.about-note{position:absolute;z-index:2;background:#fff;border:1px solid #edf0f7;box-shadow:0 12px 35px #233e6b12;border-radius:10px;padding:12px 15px;font-size:10px;font-weight:700;display:flex;align-items:center;gap:10px}.about-note span{color:var(--blue);font-size:9px}.note-top{top:35px;right:-5px}.note-bottom{bottom:42px;left:-10px}.about-copy h2{font-size:43px}.about-copy>p{font-size:12px;line-height:1.9;color:var(--muted);margin:22px 0 0}.values-list{display:grid;gap:15px;margin:26px 0}.values-list>div{display:flex;gap:12px;align-items:center}.values-list>div>span{width:24px;height:24px;border-radius:50%;background:#e2ebff;color:var(--blue);display:grid;place-items:center;font-size:12px;flex-shrink:0}.values-list p{margin:0}.values-list strong,.values-list small{display:block}.values-list strong{font-size:11px}.values-list small{font-size:10px;color:#8b94a5;margin-top:3px}.btn-dark{background:#101727;color:#fff}.btn-dark:hover{background:var(--blue);transform:translateY(-2px)}
.video-offer{background:#fff;padding-bottom:100px}.offer-panel{background:#0e1830;border-radius:24px;overflow:hidden;display:grid;grid-template-columns:1fr 1fr;min-height:450px;color:#fff;position:relative}.offer-copy{padding:55px 60px;position:relative;z-index:2}.eyebrow-light{color:#9dbaff}.eyebrow-light .eyebrow-line{background:#6c9aff}.offer-copy h2{font:800 clamp(35px,4vw,50px)/1.13 var(--display);letter-spacing:-2.5px;margin:0}.offer-copy h2 span{color:#8fb1ff}.offer-copy>p{font-size:12px;line-height:1.9;color:#aeb8cb;max-width:400px;margin:20px 0}.offer-price{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin:22px 0}.offer-price span{font-size:11px;color:#c4ccdb}.offer-price strong{font:800 28px var(--display);color:#fff}.offer-price small{font-size:9px;color:#8e9bb3;flex-basis:100%;margin-top:-10px}.btn-white{background:white;color:#102044}.btn-white:hover{background:#e7efff;transform:translateY(-2px)}.offer-visual{position:relative;display:grid;place-items:center;min-height:400px;background:radial-gradient(circle at 55% 45%,#183a82,#101b36 60%)}.offer-screen{width:300px;height:280px;border:7px solid #24314c;border-radius:15px;background:linear-gradient(140deg,#1769ff,#0b2f89);padding:18px;box-shadow:0 25px 60px #0005;transform:rotate(4deg);position:relative;z-index:2}.offer-screen-top,.offer-screen-bottom{display:flex;justify-content:space-between;align-items:center;font-size:7px;letter-spacing:1.5px;color:#d7e3ff;font-weight:700}.offer-screen-big{font:800 54px/.95 var(--display);letter-spacing:-3px;margin-top:46px}.offer-screen-big em{font-style:normal;color:#a9c6ff}.offer-screen-bottom{position:absolute;bottom:17px;left:18px;right:18px}.offer-play{width:30px;height:30px;background:#fff;color:var(--blue);border-radius:50%;display:grid;place-items:center}.offer-sticker{position:absolute;right:6%;top:17%;z-index:3;width:94px;height:94px;border-radius:50%;background:#d4f47b;color:#243319;display:grid;align-content:center;text-align:center;font-size:12px;font-weight:700;line-height:1.2;transform:rotate(10deg)}.offer-sticker b{font-size:16px}.offer-orbit{position:absolute;width:380px;height:380px;border:1px solid #ffffff18;border-radius:50%;right:-20px;bottom:-180px}.deliverables{display:grid;grid-template-columns:.8fr 1.2fr;gap:100px;padding-top:95px}.deliverable-intro h2{font-size:35px}.deliverable-intro>p{font-size:12px;color:var(--muted);line-height:1.8;margin-top:20px}.deliverable-list{border-top:1px solid var(--line)}.deliverable-row{display:grid;grid-template-columns:35px 1fr 25px;gap:15px;align-items:center;padding:20px 0;border-bottom:1px solid var(--line)}.deliverable-number{font-size:10px;font-weight:800;color:var(--blue)}.deliverable-row h3{font:800 13px var(--display);margin:0}.deliverable-row p{font-size:10px;color:#818b9d;line-height:1.7;margin:5px 0 0}.deliverable-icon{width:24px;height:24px;border-radius:50%;display:grid;place-items:center;background:#eff4ff;color:var(--blue);font-size:12px}
.process{background:#f8faff}.process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.process-step{position:relative;background:#fff;border:1px solid #e8edf6;border-radius:16px;padding:25px 22px;min-height:240px;overflow:hidden}.step-num{position:absolute;right:17px;top:15px;font:800 12px var(--display);color:#c5d4f4}.step-icon{width:42px;height:42px;background:#eaf1ff;color:var(--blue);border-radius:12px;display:grid;place-items:center;font-size:19px;margin-bottom:27px}.process-step h3{font:800 15px/1.4 var(--display);letter-spacing:-.4px;margin:0 0 9px;max-width:190px}.process-step p{font-size:11px;color:var(--muted);line-height:1.8;margin:0}.step-line{position:absolute;bottom:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--blue),#8bb0ff);transform:scaleX(0);transform-origin:left;transition:transform .4s}.process-step:hover .step-line{transform:scaleX(1)}
.contact{background:#0e1830;color:#fff;position:relative;overflow:hidden}.contact:before{content:"";position:absolute;width:650px;height:650px;border:1px solid #ffffff0c;border-radius:50%;right:-250px;top:-230px}.contact-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:100px;position:relative;z-index:1}.contact-copy h2{font:800 clamp(43px,5vw,60px)/1.05 var(--display);letter-spacing:-3px;margin:0}.contact-copy h2 span{color:#8fb1ff}.contact-copy>p{font-size:12px;line-height:1.9;color:#aeb8cb;max-width:400px;margin:20px 0 30px}.contact-links{display:grid;gap:0;border-top:1px solid #ffffff1a}.contact-links>a{display:flex;align-items:center;gap:13px;padding:15px 0;border-bottom:1px solid #ffffff1a}.contact-link-icon{width:36px;height:36px;border:1px solid #ffffff2b;border-radius:10px;display:grid;place-items:center;font-size:16px}.contact-links small,.contact-links strong{display:block}.contact-links small{font-size:8px;letter-spacing:1.5px;color:#8290aa}.contact-links strong{font-size:11px;margin-top:2px}.contact-link-arrow{margin-left:auto;color:#9dbaff}.whatsapp-link{margin-top:22px;display:inline-flex;align-items:center;gap:10px;font-size:11px;font-weight:700;background:#143c37;color:#b5f5d5;border:1px solid #2a6556;border-radius:10px;padding:12px 15px}.whatsapp-link b{margin-left:14px}.contact-form{background:#fff;color:var(--ink);border-radius:18px;padding:32px}.form-heading>span{font-size:9px;letter-spacing:1.7px;font-weight:800;color:var(--blue)}.form-heading h3{font:800 24px var(--display);letter-spacing:-.7px;margin:5px 0}.form-heading p{font-size:10px;color:#8c95a5;margin:0 0 23px}.contact-form label{display:block;font-size:10px;font-weight:700;margin:14px 0 6px}.contact-form input,.contact-form select,.contact-form textarea{width:100%;border:1px solid #e1e6ef;border-radius:8px;background:#fbfcfe;padding:11px 12px;font-size:11px;outline:none;color:var(--ink);transition:border .2s,box-shadow .2s}.contact-form input:focus,.contact-form select:focus,.contact-form textarea:focus{border-color:#7da5ff;box-shadow:0 0 0 3px #0b5cff13}.contact-form input::placeholder,.contact-form textarea::placeholder{color:#a4acba}.contact-form textarea{resize:vertical;min-height:95px}.form-row{display:grid;grid-template-columns:1fr 1fr;gap:12px}.form-submit{margin-top:18px;width:100%;border:0}.form-note{font-size:9px;color:#929aaa;line-height:1.7;margin:12px 0 0}.form-feedback{font-size:11px;color:var(--blue);margin:8px 0 0;min-height:0}
.footer{background:#091021;color:#fff;padding:28px 0 18px}.footer-main{display:flex;align-items:center;gap:30px;padding-bottom:25px}.brand-footer .brand-copy{color:#fff}.footer-main>p{font-size:11px;line-height:1.6;color:#fff;margin:0}.footer-main>p span{font-size:10px;color:#8590a6}.footer-top{margin-left:auto;font-size:9px;letter-spacing:1.5px;color:#9aabc9;font-weight:800}.footer-bottom{border-top:1px solid #ffffff17;padding-top:17px;display:flex;justify-content:space-between;gap:15px;color:#7f8aa0;font-size:9px}.floating-whatsapp{position:fixed;right:20px;bottom:20px;z-index:80;width:48px;height:48px;border-radius:50%;background:#20c879;color:#fff;display:grid;place-items:center;font-size:22px;box-shadow:0 8px 25px #0d754633;transition:transform .2s}.floating-whatsapp:hover{transform:translateY(-4px)}.reveal{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}.reveal.is-visible{opacity:1;transform:translateY(0)}.reveal-delay{transition-delay:.15s}.reveal-delay-1{transition-delay:.1s}.reveal-delay-2{transition-delay:.2s}.reveal-delay-3{transition-delay:.3s}
@media(max-width:1050px){.service-grid{grid-template-columns:repeat(2,1fr)}.service-card>p{min-height:unset}.hero-grid{gap:35px}.about-grid,.contact-grid{gap:55px}.deliverables{gap:55px}.nav-links{gap:22px}.work-grid{grid-template-columns:1fr 1fr}.work-large{grid-row:span 2}.work-large .work-image{height:480px}}
@media(max-width:760px){.container{width:min(100% - 36px,560px)}.section-pad{padding:76px 0}.announcement{font-size:9px;gap:6px;flex-wrap:wrap}.announcement a{margin-left:3px}.nav{height:68px}.menu-toggle{display:block;z-index:102}.nav-links{position:fixed;inset:68px 0 auto;display:flex;flex-direction:column;align-items:stretch;gap:0;background:#fff;padding:10px 24px 24px;border-bottom:1px solid var(--line);box-shadow:0 20px 30px #152b5014;transform:translateY(-140%);opacity:0;pointer-events:none;transition:transform .3s,opacity .3s}.nav-links.open{transform:translateY(0);opacity:1;pointer-events:auto}.nav-links>a:not(.nav-cta){padding:14px 0;border-bottom:1px solid #edf0f5}.nav-cta{justify-content:space-between;margin-top:16px}.hero{padding:65px 0 22px}.hero-grid{grid-template-columns:1fr;gap:30px}.hero h1{font-size:clamp(58px,15vw,80px);letter-spacing:-4px}.hero-lead{font-size:19px}.hero-desc{font-size:13px}.hero-visual{max-width:520px;width:100%;margin:0 auto;padding:18px 8px 22px 16px}.visual-content{min-height:270px;padding:29px 24px}.visual-title{font-size:49px}.visual-bottom{left:24px}.floating-card-top{right:-2px}.floating-card-bottom{left:-3px}.hero-bottom{margin-top:50px;gap:9px;flex-wrap:wrap;font-size:8px}.section-heading{align-items:flex-start;flex-direction:column;gap:16px;margin-bottom:30px}.section-heading h2,.about-copy h2{font-size:37px;letter-spacing:-1.7px}.section-heading>p{max-width:100%}.service-grid{gap:12px}.service-card{padding:15px;border-radius:14px}.service-art{height:125px;margin:14px 0}.service-card h3{font-size:14px}.service-card>p{font-size:10px}.status{font-size:7px;letter-spacing:.3px}.service-price strong{font-size:19px}.work-grid{grid-template-columns:1fr 1fr;gap:10px}.work-large{grid-row:auto;grid-column:span 2}.work-large .work-image{height:340px}.work-image{height:185px}.food-circle{width:230px;height:230px;right:-30px;bottom:28px}.food-copy{left:18px;bottom:22px}.food-copy strong{font-size:29px}.food-sticker{right:12px;top:38px;width:70px;height:70px}.work-meta{align-items:flex-start;padding:10px 1px 15px}.work-meta h3{font-size:11px}.work-meta span:first-child{font-size:7px;letter-spacing:.7px}.work-arrow{width:26px;height:26px}.work-foot{align-items:flex-start;flex-direction:column;gap:5px}.about-grid{grid-template-columns:1fr;gap:32px}.about-visual{height:420px;max-width:480px;width:100%;margin:auto}.about-main-card{width:260px;height:325px}.about-main-card>strong{font-size:34px}.note-top{right:0}.note-bottom{left:0;bottom:30px}.about-copy>p{font-size:12px}.offer-panel{grid-template-columns:1fr}.offer-copy{padding:36px 26px 28px}.offer-copy h2{font-size:39px}.offer-visual{min-height:350px}.offer-screen{width:min(300px,75%);height:255px}.offer-screen-big{font-size:48px}.offer-sticker{right:8%;top:12%}.deliverables{grid-template-columns:1fr;gap:25px;padding-top:60px}.deliverable-intro h2{font-size:32px}.process-grid{grid-template-columns:1fr 1fr;gap:12px}.process-step{padding:20px 16px;min-height:225px}.process-step h3{font-size:14px}.contact-grid{grid-template-columns:1fr;gap:35px}.contact-copy h2{font-size:51px}.contact-form{padding:25px 20px}.footer-main{flex-wrap:wrap;gap:15px}.footer-main>p{flex:1}.footer-top{width:100%;margin-left:0;padding-top:15px;border-top:1px solid #ffffff17}.footer-bottom{flex-direction:column;gap:7px}.floating-whatsapp{right:14px;bottom:14px;width:44px;height:44px}}
@media(max-width:420px){.container{width:calc(100% - 28px)}.service-grid{grid-template-columns:1fr}.service-art{height:145px}.service-card>p{min-height:unset}.work-grid{grid-template-columns:1fr}.work-large{grid-column:auto}.work-large .work-image,.work-image{height:260px}.work-foot .text-link{font-size:10px}.process-grid{grid-template-columns:1fr}.process-step{min-height:unset}.step-icon{margin-bottom:20px}.form-row{grid-template-columns:1fr;gap:0}.hero-actions{gap:8px}.btn{padding:0 15px;gap:12px}.visual-content{min-height:235px}.visual-title{font-size:42px}.floating-card{padding:9px 10px}.floating-card strong{font-size:10px}.floating-card small{font-size:8px}.about-visual{height:380px}.about-main-card{width:230px;height:300px;padding:24px}.about-main-card>strong{font-size:31px}.about-note{font-size:9px;padding:10px}.note-top{top:22px}.note-bottom{bottom:18px}.offer-copy h2{font-size:35px}.offer-price{gap:8px}.deliverable-row{grid-template-columns:25px 1fr 22px;gap:10px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important}.reveal{opacity:1;transform:none}}
''',
"js/main.js": r'''document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");
  const closeMenu = () => {
    navLinks?.classList.remove("open");
    menuToggle?.setAttribute("aria-expanded", "false");
    document.body.classList.remove("menu-open");
  };

  menuToggle?.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    document.body.classList.toggle("menu-open", isOpen);
  });
  navLinks?.querySelectorAll("a").forEach(link => link.addEventListener("click", closeMenu));
  window.addEventListener("resize", () => { if (window.innerWidth > 760) closeMenu(); });

  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -30px 0px" });
    revealEls.forEach(el => observer.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add("is-visible"));
  }

  document.querySelectorAll("[data-service]").forEach(link => {
    link.addEventListener("click", () => {
      const service = link.getAttribute("data-service");
      const select = document.querySelector("#service");
      if (select && service) select.value = service;
    });
  });

  const form = document.querySelector("#enquiry-form");
  const feedback = document.querySelector(".form-feedback");
  form?.addEventListener("submit", event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const name = data.get("name");
    const email = data.get("email");
    const phone = data.get("phone") || "Not provided";
    const business = data.get("business") || "Not provided";
    const service = data.get("service");
    const message = data.get("message");
    const subject = encodeURIComponent(`Website enquiry: ${service}`);
    const body = encodeURIComponent(
      `Hello Adstrak Media,\n\nI'd like to enquire about your services.\n\nName: ${name}\nEmail: ${email}\nPhone/WhatsApp: ${phone}\nBusiness: ${business}\nService: ${service}\n\nProject details:\n${message}\n\nThank you.`
    );
    if (feedback) feedback.textContent = "Opening your email app with the enquiry details…";
    window.location.href = `mailto:hello@adstrakmedia.in?subject=${subject}&body=${body}`;
  });

  const year = document.querySelector("#year");
  if (year) year.textContent = new Date().getFullYear();
});'''
}
files["README.md"] = r'''# Adstrak Media — Business Growth Partner Website

A responsive static website built with HTML, CSS and vanilla JavaScript. This version is for **Adstrak Media — Build. Grow. Scale.**, not a logistics company.

## Run locally
1. Extract the ZIP.
2. Open `index.html` in a browser, or open the folder in VS Code and use Live Server.
3. No build step or package installation is required.

## Website sections
- Hero: Build. Grow. Scale. / Your Business Growth Partner
- Services with availability status:
  - Promotional Video Creation — Available Now, starting at ₹1,499
  - Social Media Management — Coming Soon
  - Digital Marketing & Lead Generation — Coming Soon
  - Brand Building & Marketing Strategy — Planned
- Concept portfolio, labelled as concept samples
- About Adstrak Media and values
- Promotional video offer and project expectations
- Four-step process
- Contact form, email, Instagram, Facebook and WhatsApp enquiry links
- Responsive mobile navigation, smooth scrolling, reveal-on-scroll motion and reduced-motion support

## Before publishing — important
Edit `index.html` and replace the following demo details with your real business information:
- `hello@adstrakmedia.in` if this is not your actual inbox
- Instagram and Facebook links (currently generic profile URLs)
- WhatsApp links (currently generic wa.me links without a phone number)
- Service deliverables, video length, revisions, turnaround time, footage/shooting terms, and payment terms once confirmed
- Concept samples with real work as it becomes available

The enquiry form uses `mailto:` and opens the visitor's email app; it does **not** send or store submissions on its own. Connect a form backend (for example Formspree, Netlify Forms or your own server) before relying on it for leads.

The page uses Google Fonts from a CDN. If you need offline support, download and self-host the font files.

## Brand style
- Blue: `#0B5CFF`
- Dark navy/black: `#101522` and `#0E1830`
- White: `#FFFFFF`
- Soft background: `#F8FAFF`

These are a cohesive proposed palette based on the brief. If you need exact color matching to an existing reference website, sample the colors from that site and update the CSS variables at the top of `css/style.css`.
'''
files["assets/README.txt"] = "No local image files are required for this design. Portfolio visuals are created with CSS shapes so the page loads without external stock imagery. Replace concept samples with authentic client work as your portfolio grows.\n"

for rel, content in files.items():
    path = os.path.join(base, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

zip_path = "/mnt/data/adstrak-media-business-growth.zip"
if os.path.exists(zip_path):
    os.remove(zip_path)
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, filenames in os.walk(base):
        for filename in filenames:
            full = os.path.join(root, filename)
            arc = os.path.relpath(full, os.path.dirname(base))
            zf.write(full, arc)
print(zip_path, os.path.getsize(zip_path), "bytes")

