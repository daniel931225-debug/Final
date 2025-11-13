<script lang="ts">
	import '../app.css';
	import { resolve } from '$app/paths';
</script>

<div
	class="min-h-screen bg-gray-50 text-gray-800 transition-colors duration-300 dark:bg-gray-900 dark:text-gray-100"
>
	<header
		class="sticky top-0 z-50 flex items-center justify-between border-b border-gray-200/50 bg-white/80 px-8 py-4 backdrop-blur-md transition-colors dark:border-white/10 dark:bg-gray-800/80"
	>
		<div class="flex flex-1 justify-start"></div>

		<div class="flex flex-1 justify-center">
			<div class="text-2xl font-bold">
				<a href={resolve('/')} class="text-gray-800 no-underline dark:text-white">Blog</a>
			</div>
		</div>

		<div class="flex flex-1 justify-end">
			<nav class="flex items-center gap-5">
				<a
					href={resolve('/login')}
					class="font-medium text-gray-600 transition hover:text-blue-600 dark:text-gray-300 dark:hover:text-blue-400"
					>登入</a
				>
				<a
					href={resolve('/register')}
					class="rounded-md bg-blue-600 px-4 py-2 text-white transition hover:bg-blue-700">註冊</a
				>
			</nav>
		</div>
	</header>

	<main class="pt-4">
		<slot />
	</main>
</div>
