export class RedirectMenu extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
	<nav class="navbar fixed-bottom navbar-expand bg-body-tertiary user-select-none">
		<div class="container-fluid text-center">
			<div class="collapse navbar-collapse justify-content-between" id="navbarNav">
				<div class="d-flex align-items-center justify-content-center">
					<c-redirbutton name="Home" href="/"></c-redirbutton>
					<c-redirbutton name="MyFirst" href="myfirst"></c-redirbutton>
					<c-redirbutton name="Testing" href="testing"></c-redirbutton>
					<c-redirbutton name="JSPage" href="jspage"></c-redirbutton>
					<c-redirbutton name="Profile" href="profile"></c-redirbutton>
				</div>
			</div>
		</div>
	</nav>
	`;
  }
}

customElements.define("c-redirmenu", RedirectMenu);
