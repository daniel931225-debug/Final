<script lang="ts">
	import { fade, slide } from 'svelte/transition';
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { api } from '$lib/api';

	let username = $state('');
	let password = $state('');
	let confirmPassword = $state('');

	let showPassword = $state(false);
	let isLoading = $state(false);
	let errorMessage = $state('');

	let passwordMismatch = $derived(confirmPassword !== '' && password !== confirmPassword);
	let isFormValid = $derived(username.length > 0 && password.length >= 8 && !passwordMismatch);

	async function handleSubmit(e: Event) {
		e.preventDefault();
		errorMessage = '';

		if (password !== confirmPassword) {
			errorMessage = '密碼與確認密碼不相符';
			return;
		}

		try {
			isLoading = true;

			await api.auth.register({ username, password });
			await goto('/login');
		} catch (err) {
			console.error(err);
			errorMessage = '註冊失敗，請稍後再試';
		} finally {
			isLoading = false;
		}
	}
</script>

{#snippet iconSpinner()}
	<svg
		class="mr-3 h-5 w-5 animate-spin text-white"
		xmlns="http://www.w3.org/2000/svg"
		fill="none"
		viewBox="0 0 24 24"
	>
		<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />

		<path
			class="opacity-75"
			fill="currentColor"
			d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
		/>
	</svg>
{/snippet}

{#snippet iconArrowRight()}
	<svg
		class="ml-2 h-4 w-4 transition-transform group-hover:translate-x-1"
		fill="none"
		viewBox="0 0 24 24"
		stroke="currentColor"
	>
		<path
			stroke-linecap="round"
			stroke-linejoin="round"
			stroke-width="2"
			d="M17 8l4 4m0 0l-4 4m4-4H3"
		/>
	</svg>
{/snippet}

{#snippet iconEye(visible: boolean)}
	{#if visible}
		<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"
			/>
		</svg>
	{:else}
		<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
			/>

			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
			/>
		</svg>
	{/if}
{/snippet}

<div class="flex min-h-[85vh] items-center justify-center px-4 py-12">
	<div
		in:fade={{ duration: 300, delay: 100 }}
		class="w-full max-w-md overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-xl shadow-slate-200/50 dark:border-slate-800 dark:bg-slate-900 dark:shadow-slate-900/50"
	>
		<div class="h-2 w-full bg-gradient-to-r from-blue-500 to-purple-600"></div>

		<div class="p-8 sm:p-10">
			<div class="mb-8 text-center">
				<h1 class="text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
					建立您的帳號
				</h1>

				<p class="mt-2 text-sm text-slate-500 dark:text-slate-400">加入我們，開始您的創作之旅</p>
			</div>

			{#if errorMessage}
				<div
					transition:slide
					class="mb-6 rounded-lg bg-red-50 p-4 text-sm text-red-600 dark:bg-red-900/20 dark:text-red-400"
				>
					<div class="flex items-center gap-2">
						<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
							/>
						</svg>
						{errorMessage}
					</div>
				</div>
			{/if}

			<form class="flex flex-col gap-5" onsubmit={handleSubmit}>
				<div class="group">
					<label
						for="username"
						class="mb-1.5 block text-sm font-semibold text-slate-700 dark:text-slate-300"
					>
						使用者名稱
					</label>

					<div class="relative">
						<input
							type="text"
							id="username"
							bind:value={username}
							required
							placeholder="e.g. jason_wang"
							class="peer w-full rounded-lg border border-slate-300 bg-white px-4 py-3 pl-11 text-slate-900 placeholder-slate-400 transition-all focus:border-blue-500 focus:ring-4 focus:ring-blue-500/10 focus:outline-none dark:border-slate-700 dark:bg-slate-800 dark:text-white dark:focus:ring-blue-500/20"
						/>

						<div
							class="pointer-events-none absolute top-0 left-0 flex h-full w-11 items-center justify-center text-slate-400 transition-colors peer-focus:text-blue-500"
						>
							<svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
								/>
							</svg>
						</div>
					</div>
				</div>

				<div>
					<label
						for="password"
						class="mb-1.5 block text-sm font-semibold text-slate-700 dark:text-slate-300"
					>
						密碼
					</label>

					<div class="relative">
						<input
							type={showPassword ? 'text' : 'password'}
							id="password"
							bind:value={password}
							required
							minlength="8"
							placeholder="至少 8 個字元"
							class="w-full rounded-lg border border-slate-300 bg-white px-4 py-3 pr-12 text-slate-900 placeholder-slate-400 transition-all focus:border-blue-500 focus:ring-4 focus:ring-blue-500/10 focus:outline-none dark:border-slate-700 dark:bg-slate-800 dark:text-white dark:focus:ring-blue-500/20"
						/>

						<button
							type="button"
							onclick={() => (showPassword = !showPassword)}
							class="absolute top-0 right-0 flex h-full w-12 items-center justify-center text-slate-400 hover:text-slate-600 focus:outline-none dark:hover:text-slate-200"
						>
							{@render iconEye(showPassword)}
						</button>
					</div>
				</div>

				<div>
					<label
						for="confirmPassword"
						class="mb-1.5 block text-sm font-semibold text-slate-700 dark:text-slate-300"
					>
						確認密碼
					</label>

					<input
						type="password"
						id="confirmPassword"
						bind:value={confirmPassword}
						required
						placeholder="再次輸入密碼"
						class="w-full rounded-lg border bg-white px-4 py-3 text-slate-900 placeholder-slate-400 transition-all focus:ring-4 focus:outline-none dark:bg-slate-800 dark:text-white
						{passwordMismatch
							? 'border-red-300 focus:border-red-500 focus:ring-red-500/10 dark:border-red-900'
							: 'border-slate-300 focus:border-blue-500 focus:ring-blue-500/10 dark:border-slate-700 dark:focus:ring-blue-500/20'}"
					/>

					{#if passwordMismatch}
						<p transition:slide class="mt-1 text-sm text-red-500">密碼不相符</p>
					{/if}
				</div>

				<button
					type="submit"
					disabled={isLoading || !isFormValid}
					class="group relative mt-2 flex w-full items-center justify-center rounded-lg bg-blue-600 px-4 py-3 text-base font-bold text-white transition-all
					hover:bg-blue-700 hover:shadow-lg hover:shadow-blue-500/30
					focus:ring-4 focus:ring-blue-500/50 focus:outline-none
					disabled:cursor-not-allowed disabled:opacity-70 disabled:hover:shadow-none"
				>
					{#if isLoading}
						{@render iconSpinner()}
						處理中...
					{:else}
						註冊帳號
						{@render iconArrowRight()}
					{/if}
				</button>

				<div class="mt-4 text-center text-sm text-slate-500 dark:text-slate-400">
					已經有帳號了？
					<a
						href={resolve('/login')}
						class="font-semibold text-blue-600 hover:text-blue-700 hover:underline dark:text-blue-400"
					>
						立即登入
					</a>
				</div>
			</form>
		</div>
	</div>
</div>
