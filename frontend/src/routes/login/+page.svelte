<script lang="ts">
	import { resolve } from '$app/paths';
	let username = '';
	let password = '';

	function handleSubmit() {
		console.log('登入中...', { username, password });
	}
</script>

<div class="flex min-h-[80vh] items-start justify-center px-4 py-16">
	<div
		class="w-full max-w-md rounded-xl border border-gray-200 bg-white p-10 shadow-lg dark:border-gray-700 dark:bg-gray-800"
	>
		<h1 class="mb-8 text-center text-3xl font-bold">登入</h1>

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
					placeholder="••••••••"
					class="w-full rounded-md border border-gray-300 bg-white px-4 py-3 text-base text-gray-800 focus:border-blue-500 focus:ring-4 focus:ring-blue-500/20 focus:outline-none dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400"
				/>
			</div>

			<button
				type="submit"
				class="mt-2 rounded-md bg-blue-600 px-4 py-3.5 text-lg font-semibold text-white transition hover:bg-blue-700 focus:ring-4 focus:ring-blue-500/50 focus:outline-none"
			>
				登入
			</button>

			<div class="mt-4 flex items-center justify-center text-sm">
				<a href={resolve('/register')} class="text-blue-600 hover:underline dark:text-blue-400"
					>還沒有帳號? 註冊</a
				>
			</div>
		</form>
	</div>
</div>
