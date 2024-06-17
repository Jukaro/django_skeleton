import { Router } from "../Router.js";

export class RedirectButton extends HTMLElement {
  constructor() {
    super();
  }

  handleClick() {
    Router.push(this.getAttribute("href"));
  }

  connectedCallback() {
    this.innerHTML = `
    <button>
      ${this.getAttribute("name")}
    </button>
    `;

    this.addEventListener("click", this.handleClick, true);
  }
}

customElements.define("c-redirbutton", RedirectButton);
