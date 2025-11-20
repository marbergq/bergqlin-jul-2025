document.addEventListener('DOMContentLoaded', () => {
  renderList('frans', wishlistData.frans);
  renderList('bosse', wishlistData.bosse);
  createSnow();
});

function renderList(personId, items) {
  const listContainer = document.getElementById(`${personId}-list`);
  
  items.forEach(item => {
    const li = document.createElement('li');
    li.className = 'wishlist-item';
    
    let linkHtml = '';
    if (item.link) {
      linkHtml = `<a href="${item.link}" target="_blank" class="item-link">Se produkt</a>`;
    }

    let boughtHtml = '';
    if (item.bought) {
      boughtHtml = `<div class="bought-badge">Köpt!</div>`;
    }

    li.innerHTML = `
      ${boughtHtml}
      ${item.image ? `<div class="item-image-container"><img src="${item.image}" alt="${item.title}" class="item-image" loading="lazy"></div>` : ''}
      <span class="item-title">${item.title}</span>
      <div class="item-desc">${item.description}</div>
      <span class="item-price">${item.price} kr</span>
      ${linkHtml}
    `;
    
    listContainer.appendChild(li);
  });
}

function createSnow() {
  const snowContainer = document.createElement('div');
  snowContainer.className = 'snow-container';
  document.body.appendChild(snowContainer);

  const snowflakeCount = 50;

  for (let i = 0; i < snowflakeCount; i++) {
    const snowflake = document.createElement('div');
    snowflake.className = 'snowflake';
    snowflake.innerHTML = '❄';
    
    // Random positioning and animation properties
    const left = Math.random() * 100;
    const duration = Math.random() * 5 + 5; // 5-10s
    const delay = Math.random() * 5;
    const size = Math.random() * 1 + 0.5; // 0.5-1.5em
    
    snowflake.style.left = `${left}%`;
    snowflake.style.animationDuration = `${duration}s`;
    snowflake.style.animationDelay = `${delay}s`;
    snowflake.style.fontSize = `${size}em`;
    
    snowContainer.appendChild(snowflake);
    
    // Reset animation to keep it going continuously without gaps if we just did one batch, 
    // but CSS animation with infinite iteration is better handled in CSS if we want simple loop.
    // However, for random "rain" effect, we often need to reset. 
    // My CSS has 'forwards', let's change it to 'infinite' in JS or CSS.
    // Actually, let's just make the CSS infinite. I'll update the style via JS injection or just rely on the CSS I wrote?
    // Wait, I wrote 'forwards' in CSS. I should have written 'infinite'. 
    // I will fix this by injecting a style fix or just updating the animation property here.
    snowflake.style.animationIterationCount = 'infinite';
  }
}
