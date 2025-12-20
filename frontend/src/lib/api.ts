import { PUBLIC_API_URL } from '$env/static/public';

export interface User {
	id: number;
	username: string;
}

interface Post {
	id: number;
	title: string;
	content: string;
	created_at: string;
	owner_id: number;
}

async function send<T>(
	method: string,
	endpoint: string,
	data?: object
): Promise<{ message: string; data: T }> {
	const options: RequestInit = { method };

	if (data) {
		options.headers = { 'Content-Type': 'application/json' };
		options.body = JSON.stringify(data);
	}

	const res = await fetch(`${PUBLIC_API_URL}${endpoint}`, options);

	if (!res.ok) {
		throw new Error(`API request failed with status ${res.status}`);
	}

	return res.json();
}

export const api = {
	auth: {
		register: (data: { username: string; password: string }) =>
			send<void>('POST', '/auth/register', data),
		login: (data: { username: string; password: string }) => send<User>('POST', '/auth/login', data)
	},
	posts: {
		list: (page: number) => send<Post[]>('GET', `/posts?page=${page}`),
		create: (data: Omit<Post, 'id' | 'created_at'>) => send<Post>('POST', '/posts', data),
		edit: (id: number, data: Partial<Omit<Post, 'id' | 'created_at'>>) =>
			send<Post>('PUT', `/posts/${id}`, data),
		delete: (id: number) => send<void>('DELETE', `/posts/${id}`)
	}
};
