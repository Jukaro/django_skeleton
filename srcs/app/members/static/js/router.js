class Router {
  static async push(pathname) {
    const url = new URL(pathname, window.location.origin);
    const response = await fetch(url, { headers: { "X-Source": "SPA" } });
    const text = await response.text();
    document.querySelector("#content").innerHTML = text;
    document.title = "oui";
    window.history.pushState(undefined, "", url);
  }
}

window.addEventListener("load", () =>
  Router.push(window.location.pathname + window.location.search)
);
