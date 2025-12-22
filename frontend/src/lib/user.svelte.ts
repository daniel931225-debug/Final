import { api, type User } from './api';

type ConditionalOrNull<B extends boolean, T> = B extends true ? T : null;

export class UserState<LoggedIn extends boolean = boolean> {
	public current: ConditionalOrNull<LoggedIn, User>;
	private loggedIn: LoggedIn;

	constructor(init?: User | null) {
		this.loggedIn = !!init as LoggedIn;
		this.current = $state<User | null>(init ?? null) as ConditionalOrNull<LoggedIn, User>;
	}

	public isLoggedIn(): this is UserState<true> {
		return this.loggedIn;
	}

	public update(user: User) {
		this.loggedIn = true as LoggedIn;
		this.current = user as ConditionalOrNull<true, User> & null;
	}

	public async logout() {
		if (!this.isLoggedIn()) {
			return;
		}

		await api.auth.logout();
		this.loggedIn = false as LoggedIn & true;
		this.current = null as ConditionalOrNull<false, User> & User;
	}
}

export const USER_KEY = Symbol('user');
