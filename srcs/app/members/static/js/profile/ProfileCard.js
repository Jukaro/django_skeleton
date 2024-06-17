export class ProfileCard extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
		<div class="card-body">
			<h5 class="card-title">${this.getAttribute("title")}</h5>
			<p class="card-text">${this.getAttribute("value")}</p>
		</div>
	  `;
  }
}

customElements.define("c-profilecard", ProfileCard);
