export class VeryBadComponent extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <input class="form-control" />
    `;
  }

  static maFonction() {
    console.log("mdr");
  }
}

customElements.define("c-verybadcomponent", VeryBadComponent);
