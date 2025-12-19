import { api } from '$lib/api';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ url }) => {
	try {
		const page = Number(url.searchParams.get('page') ?? '0');

		return api.posts.list(page);
	} catch (err) {
		console.error(err);
		return {
			message: '無法連線至伺服器，請稍後再試。',
			data: []
		};
	}
};
