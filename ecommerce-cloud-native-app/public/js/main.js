document.addEventListener("DOMContentLoaded", function() {
    fetch('/products')
      .then(response => response.json())
      .then(data => {
        const productsDiv = document.getElementById('products');
        data.forEach(product => {
          const productElement = document.createElement('div');
          productElement.innerHTML = `<h2>${product.name}</h2><p>$${product.price}</p>`;
          productsDiv.appendChild(productElement);
        });
      });
  });
  