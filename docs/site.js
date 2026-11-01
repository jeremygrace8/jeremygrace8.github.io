const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
function closeMenu(){toggle?.setAttribute('aria-expanded','false');nav?.classList.remove('open')}
toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle?.getAttribute('aria-expanded')==='true'){closeMenu();toggle.focus()}});
for(const link of document.querySelectorAll('nav a')){if(link.pathname===location.pathname)link.setAttribute('aria-current','page')}
const gallery=document.querySelector('.photo-hero');
if(gallery){
 const slides=[...gallery.querySelectorAll('.hero-slide')];
 const dots=[...gallery.querySelectorAll('.slide-dot')];
 const labels=['Bathroom inspiration','Kitchen inspiration','Bathroom inspiration','Laundry room inspiration','Fixture inspiration'];
 let active=0;
 function show(index){active=(index+slides.length)%slides.length;slides.forEach((slide,i)=>slide.hidden=i!==active);dots.forEach((dot,i)=>dot.setAttribute('aria-pressed',String(i===active)));document.querySelector('#slide-label').innerHTML=labels[active]+' <span class="photo-label">/ Illustrative image</span>'}
 gallery.querySelector('.slide-prev').addEventListener('click',()=>show(active-1));
 gallery.querySelector('.slide-next').addEventListener('click',()=>show(active+1));
 dots.forEach((dot,i)=>dot.addEventListener('click',()=>show(i)));
 gallery.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();show(active+(e.key==='ArrowRight'?1:-1))}});
 // Intentionally manual: no motion or slide changes while a visitor is reading.
}
