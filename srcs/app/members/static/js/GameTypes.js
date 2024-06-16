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
        return `<a href="/user/${username}">${username}</a>`
    }

    connectedCallback()
    {
        const at = new Date(this.getAttribute("at"));
        const player = JSON.parse(atob(this.getAttribute("player")));
		const all_players = JSON.parse(atob(this.getAttribute("all-players")));

        // console.log("player: ", player)
        // console.log("players: ", all_players)

        // let players = []
        // let otherScore = 0
        // let mate = None

        // for (const p of all_players)
        // {
        //     if (player.score != p.score)
        //         otherScore = p.score;
        //     else
        //         mate = p.user.username;
        //     players.push(p.user.username)
        // }

        // let indexOfPlayer = all_players.indexOf(game.target_user_info.user.username)
        // const indexOfMate = indexOfPlayer % 2 ? indexOfPlayer - 1 : indexOfPlayer + 1

        // players.splice(indexOfPlayer, 1)
        // players.splice(indexOfMate % 2 ? indexOfMate - 1 : indexOfMate, 1)

        // const bgColor = this.getAttribute('has_won') == 'true' ? 'text-bg-success' : 'text-bg-danger'

        // this.innerHTML = /*html*/`<li class="row d-flex align-items-center">
        //     <div class="col">
        //         ${at.getHours()}h${at.getMinutes()}
        //     </div>
        //     <div class="col ms-2 fw-bold">
        //         ${this.getAttribute("player-1-username")} - ${this.link(this.getAttribute("player-2-username"))}
        //     </div>
        //     <div class="col d-flex justify-content-center">
        //         <span class="badge rounded-pill ${bgColor}">${this.getAttribute('team-1-score')} - ${this.getAttribute('team-2-score')}</span>
        //     </div>
        //     <div class="col ms-2 fw-bold text-end">
        //         ${this.link(this.getAttribute("player-3-username"))} - ${this.link(this.getAttribute("player-4-username"))}
        //     </div>
        // </li>`;
        this.innerHTML = `
            <li class="row d-flex align-items-center">
                <div class="col">
                    ${at.getHours()}h${at.getMinutes()}
                </div>
                <p>Other Game Type</p>
            </li>
        `;
    }
}

customElements.define("c-quickgame", QuickGame);
customElements.define("c-squaregame", SquareGame);
customElements.define("c-teamgame", TeamGame);
