<script lang="ts">
	import { resolve } from '$app/paths';
	let username = '';
	let password = '';
	let confirmPassword = '';

	function handleSubmit() {
		if (password !== confirmPassword) {
			alert('密碼和確認密碼不相符！');
			return;
		}
		console.log('註冊中...', { username, password });
	}
</script>

<div class="flex min-h-[80vh] items-start justify-center px-4 py-16">
	<div
		class="w-full max-w-md rounded-xl border border-gray-200 bg-white p-10 shadow-lg dark:border-gray-700 dark:bg-gray-800"
	>
		<h1 class="mb-8 text-center text-3xl font-bold">建立您的帳號</h1>

		<form class="flex flex-col gap-5" on:submit|preventDefault={handleSubmit}>
			<div class="text-left">
				<label for="username" class="mb-2 block font-medium text-gray-700 dark:text-gray-200"
					>使用者名稱</label
				>
				<input
					type="text"
					id="username"
					bind:value={username}
					required
					placeholder="您希望被如何稱呼"
					class="w-full rounded-md border border-gray-300 bg-white px-4 py-3 text-base text-gray-800 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 focus:outline-none dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400"
				/>
			</div>

			<div class="text-left">
				<label for="password" class="mb-2 block font-medium text-gray-700 dark:text-gray-200"
					>密碼</label
				>
				<input
					type="password"
					id="password"
					bind:value={password}
					required
					minlength="8"
					placeholder="至少 8 個字元"
					class="w-full rounded-md border border-gray-300 bg-white px-4 py-3 text-base text-gray-800 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 focus:outline-none dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400"
				/>
			</div>

			<div class="text-left">
				<label for="confirmPassword" class="mb-2 block font-medium text-gray-700 dark:text-gray-200"
					>確認密碼</label
				>
				<input
					type="password"
					id="confirmPassword"
					bind:value={confirmPassword}
					required
					placeholder="再次輸入密碼"
					class="w-full rounded-md border border-gray-300 bg-white px-4 py-3 text-base text-gray-800 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 focus:outline-none dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400"
				/>
			</div>

			<button
				type="submit"
				class="mt-2 rounded-md bg-blue-600 px-4 py-3.5 text-lg font-semibold text-white transition hover:bg-blue-700 focus:ring-4 focus:ring-blue-500/50 focus:outline-none"
			>
				註冊
			</button>

			<div class="mt-4 flex items-center justify-center text-sm">
				<a href={resolve('/login')} class="text-blue-600 hover:underline dark:text-blue-400"
					>已經有帳號了? 前往登入</a
				>
			</div>
		</form>
	</div>
</div>
