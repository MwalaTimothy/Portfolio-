const mobileMenu = document.getElementById('mobile-menu');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');
const navbar = document.querySelector('.navbar');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function showNotification(message, type = 'info') {
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) existingNotification.remove();

    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);

    window.setTimeout(() => notification.classList.add('notification-visible'), 10);
    window.setTimeout(() => {
        notification.classList.remove('notification-visible');
        window.setTimeout(() => notification.remove(), 250);
    }, 4500);
}

function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

if (mobileMenu && navMenu) {
    mobileMenu.addEventListener('click', () => {
        const expanded = mobileMenu.getAttribute('aria-expanded') === 'true';
        mobileMenu.setAttribute('aria-expanded', String(!expanded));
        mobileMenu.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    mobileMenu.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            mobileMenu.click();
        }
    });
}

navLinks.forEach((link) => {
    link.addEventListener('click', () => {
        if (mobileMenu && navMenu) {
            mobileMenu.classList.remove('active');
            navMenu.classList.remove('active');
            mobileMenu.setAttribute('aria-expanded', 'false');
        }
    });
});

document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function handleAnchorClick(event) {
        const target = document.querySelector(this.getAttribute('href'));
        if (!target) return;

        event.preventDefault();
        target.scrollIntoView({
            behavior: prefersReducedMotion ? 'auto' : 'smooth',
            block: 'start'
        });
    });
});

window.addEventListener('scroll', () => {
    let current = '';
    document.querySelectorAll('section').forEach((section) => {
        if (window.scrollY >= section.offsetTop - 220) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach((link) => {
        link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
    });

    if (navbar) {
        navbar.classList.toggle('navbar-scrolled', window.scrollY > 80);
    }
}, { passive: true });

const contactForm = document.querySelector('.email-contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(contactForm);
        const name = String(formData.get('name') || '').trim();
        const email = String(formData.get('email') || '').trim();
        const subject = String(formData.get('subject') || '').trim();
        const message = String(formData.get('message') || '').trim();
        const recipient = contactForm.dataset.recipient || 'mwalatimo@gmail.com';

        if (!name || !email || !subject || !message) {
            showNotification('Please fill in every field before opening the email draft.', 'error');
            return;
        }

        if (!isValidEmail(email)) {
            showNotification('Please enter a valid email address.', 'error');
            return;
        }

        const body = [
            `Hello Timothy,`,
            '',
            message,
            '',
            '---',
            `From: ${name}`,
            `Reply-to: ${email}`
        ].join('\n');

        const mailto = `mailto:${encodeURIComponent(recipient)}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        window.location.href = mailto;
        showNotification('Opening your email app with the message ready to send.', 'success');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    if (!prefersReducedMotion) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

        document.querySelectorAll('.skill-category, .project-card, .case-card, .contact-shell, .about-stats .stat').forEach((element) => {
            element.classList.add('animate-on-scroll');
            observer.observe(element);
        });
    }
});
