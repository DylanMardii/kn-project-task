// Back to top visibility
window.addEventListener('scroll', (e) => {
  const btn = document.getElementById('backToTop');
  if (window.scrollY > 400) {
    btn.classList.add('show');
  } else {
    btn.classList.remove('show');
  }
});

// Contact form toast
document.querySelector('#contact .btn-primary')?.addEventListener('click', (e) => {
  e.preventDefault();
  const toast = new bootstrap.Toast(document.getElementById('liveToast'));
  toast.show();
});

// Navbar collapse on link click (mobile)
document.querySelectorAll('.navbar-nav .nav-link').forEach((link) => {
  link.addEventListener('click', () => {
    const collapse = document.getElementById('navbarNav');
    const bsCollapse = bootstrap.Collapse.getInstance(collapse);
    if (bsCollapse) bsCollapse.hide();
  });
});
