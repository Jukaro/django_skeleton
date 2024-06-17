export class QuickGame extends HTMLElement
{
    connectedCallback()
    {
		const at = new Date(this.getAttribute("at"));
		const player = JSON.parse(atob(this.getAttribute("player")));
		const opponents = JSON.parse(atob(this.getAttribute("opponents")));
        const bgColor = player.win ? 'text-bg-success' : 'text-bg-danger';

        this.innerHTML = /*html*/`
        <li class="row d-flex align-items-center">
            <div class="col">
                ${at.getHours()}h${at.getMinutes()}
            </div>
            <div class="col ms-2 fw-bold">
                ${player.user.username}
            </div>
            <div class="col d-flex justify-content-center">
                <span class="badge rounded-pill ${bgColor}">${player.score} - ${opponents[0].score}</span>
            </div>
            <div class="col ms-2 fw-bold text-end">
                <a href="/user/${opponents[0].user.username}">${opponents[0].user.username}</a>
            </div>
        </li>
        `;
    }
}

export class SquareGame extends HTMLElement
{
    connectedCallback()
    {
		const at = new Date (this.getAttribute("at"));
		const player = JSON.parse(atob(this.getAttribute("player")));
		const opponents = JSON.parse(atob(this.getAttribute("opponents")));

        this.innerHTML = `
			<li class="d-flex justify-content-between align-items-center text-center">
				<div class="">
					${at.getHours()}h${at.getMinutes()}
				</div>
				${addPlayer(player.user.username, player.win, player.score, true)}
				${addPlayer(opponents[0].user.username, opponents[0].win, opponents[0].score, false)}
				${addPlayer(opponents[1].user.username, opponents[1].win, opponents[1].score, false)}
				${addPlayer(opponents[2].user.username, opponents[2].win, opponents[2].score, false)}
			</li>
		`;
    }
}

const addPlayer = (username, win, score, me) => {
	const userHTML = me ? username : `<a href="/profile/${username}">${username}</a>`;

	return `
		<div class=" ms-2 fw-bold">
			${userHTML}
			<span class="badge rounded-pill text-bg-${win ? "success" : "danger"}">${score}</span>
		</div>
	`;
}

export class TeamGame extends HTMLElement
{
    link(username)
    {
        return `<a href="/profile/${username}">${username}</a>`
    }

    connectedCallback()
    {
        const at = new Date(this.getAttribute("at"));
        const player = JSON.parse(atob(this.getAttribute("player")));
		const all_players = JSON.parse(atob(this.getAttribute("all-players")));

        let players_team = [];
        let opponents_team = [];

        players_team.push(player);

        for (const p of all_players) {
            if (p.score == player.score && p.user.id != player.user.id)
                players_team.push(p);
            else if (p.user.id != player.user.id)
                opponents_team.push(p);
        }

        const bgColor = player.win ? 'text-bg-success' : 'text-bg-danger';

        this.innerHTML = `
            <li class="row d-flex align-items-center justify-content-between">
                <div class="col">
                    ${at.getHours()}h${at.getMinutes()}
                </div>
                <div class="col ms-2 fw-bold">
                    ${players_team[0].user.username} - ${this.link(players_team[1].user.username)}
                </div>
                <div class="col d-flex justify-content-center">
                    <span class="badge rounded-pill ${bgColor}">${players_team[0].score} - ${opponents_team[0].score}</span>
                </div>
                <div class="col ms-2 fw-bold text-end">
                    ${this.link(opponents_team[0].user.username)} - ${this.link(opponents_team[1].user.username)}
                </div>
            </li>
        `;
    }
}

customElements.define("c-quickgame", QuickGame);
customElements.define("c-squaregame", SquareGame);
customElements.define("c-teamgame", TeamGame);
