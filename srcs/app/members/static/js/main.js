// import { Component } from "./component.js";
// import { Clock } from "./clock.js";

// Component.loader([
//   Clock,
// ]);

// const navigateTo = (url) => {
//   history.pushState(null, null, url);
//   Router.run();
// };

// window.addEventListener("popstate", (e) => {
//   Router.run();
// });

// document.addEventListener("DOMContentLoaded", () => {
//   document.body.addEventListener("click", (e) => {
//     if (e.target.localName == "a") console.log("bite");
//     if (e.target.localName == "a" && e.target.id != 1) {
//       console.log("cul");
//       e.preventDefault();
//       navigateTo(e.target.href);
//     }
//   });

//   Router.run();
// });

// document.getElementById("demo").innerHTML = "Aled";

import { Component } from "./component.js";

export class Increment extends Component {
  constructor() {
    super();
  }

  initState() {
    this.state = { count: 0 };
  }

  render() {
    return `
			<div>
				<h1>${this.state.count}</h1>
				<button onclick="${this.setState({
          count: this.state.count + 1,
        })}">Increment</button>
			</div>
		`;
  }
}

customElements.define("c-increment", Increment);

export function test() {
  if (document.getElementById("demo2") != null) console.log("demo2 existe");
  else console.log("demo2 n'existe pas");
}
