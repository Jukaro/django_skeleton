export class Input extends HTMLInputElement {
  constructor() {
	super();
  }

	// handleUsernameInput(e) {
	// 	if (e.target.value.length > lengthUserMax)
	// 	{
	// 		this.style.color = "#C0192A";
	// 		// createPopover(e.target, "popover-user", "Le nom d'utilisateur ne peux pas depasser 10 charactere");
	// 	}
	// 	else
	// 		this.style.color = "";
	// 		// removeError(inputUser, "popover-user");
	// }

	logInput() {
		console.log(this.value);
	}

	handleUsernameInput() {
		if (this.value.length > 10)
			this.style.color = "#C0192A";
		else
			this.style.color = "";
	}

	connectedCallback() {
		this.setAttribute("placeholder", "Username");
		this.setAttribute("type", "User");
		console.log("type: ", this.type);
		console.log("type: ", this.getAttribute("type"));
		this.classList.add("form-control");
		this.addEventListener("input", this.logInput);
		this.addEventListener("input", this.handleUsernameInput);
	}
}

customElements.define("c-input", Input, { extends: "input" });
