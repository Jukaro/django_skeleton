export class VeryBadComponent extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `<h1 style="background-color: red;">Salut</h1>`;
  }

  static maFonction() {
    console.log("mdr");
  }
}

customElements.define("c-verybadcomponent", VeryBadComponent);
