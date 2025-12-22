<script lang="ts">
	import { fly, fade } from 'svelte/transition';

	let { data } = $props();
</script>

{#snippet dateDisplay(dateString: string)}
	<time
		datetime={dateString}
		class="flex items-center gap-1.5 font-medium text-blue-600 dark:text-blue-400"
	>
		<svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
			/>
		</svg>

		{new Date(dateString).toLocaleDateString('zh-TW', {
			year: 'numeric',
			month: 'long',
			day: 'numeric'
		})}
	</time>
{/snippet}

<div class="mx-auto max-w-4xl px-4 py-12 sm:px-6 lg:py-16">
	<header class="mb-10 text-center sm:text-left">
		<h1 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl dark:text-white">
			最新文章
		</h1>

		<p class="mt-4 text-lg text-slate-600 dark:text-slate-400">探索我們的最新見解與技術分享</p>
	</header>

	<div class="grid gap-8 sm:grid-cols-1">
		{#each data.data as post, i (post.id)}
			<article
				in:fly={{ y: 20, duration: 400, delay: i * 100 }}
				class="group relative flex flex-col overflow-hidden rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300
				hover:-translate-y-1 hover:border-blue-200/50 hover:shadow-xl
				dark:border-slate-800 dark:bg-slate-900 dark:hover:border-blue-900/50"
			>
				<div
					class="absolute -top-10 -right-10 h-32 w-32 rounded-full bg-blue-500/10 opacity-0 blur-3xl transition-opacity group-hover:opacity-100 dark:bg-blue-400/10"
				></div>

				<div class="flex flex-col gap-4">
					<div class="flex items-center gap-3 text-sm text-slate-500 dark:text-slate-400">
						{@render dateDisplay(post.created_at)}

						<span class="h-1 w-1 rounded-full bg-slate-300 dark:bg-slate-700"></span>

						<span>文章</span>
					</div>

					<h2 class="text-2xl font-bold tracking-tight text-slate-900 dark:text-white">
						<a href={`/post/${post.id}`} class="before:absolute before:inset-0 focus:outline-none">
							<span
								class="bg-gradient-to-r from-slate-900 to-slate-900 bg-[length:0%_2px] bg-left-bottom bg-no-repeat transition-all duration-300 group-hover:bg-[length:100%_2px] dark:from-blue-400 dark:to-blue-400"
							>
								{post.title}
							</span>
						</a>
					</h2>

					<p class="line-clamp-3 text-base leading-relaxed text-slate-600 dark:text-slate-300">
						{post.content}
					</p>

					<div
						class="mt-2 flex items-center pt-4 text-sm font-semibold text-blue-600 transition-colors group-hover:text-blue-700 dark:text-blue-400 dark:group-hover:text-blue-300"
					>
						閱讀全文
						<svg
							class="ml-2 h-4 w-4 transition-transform duration-300 group-hover:translate-x-1"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
							stroke-width="2"
						>
							<path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3" />
						</svg>
					</div>
				</div>
			</article>
		{/each}
	</div>

	{#if data.data.length === 0}
		<div
			in:fade
			class="flex min-h-[300px] flex-col items-center justify-center rounded-2xl border border-dashed border-slate-300 bg-slate-50 px-4 py-12 text-center dark:border-slate-700 dark:bg-slate-800/50"
		>
			<div class="rounded-full bg-slate-100 p-4 dark:bg-slate-800">
				<svg class="h-10 w-10 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="1.5"
						d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"
					/>
				</svg>
			</div>

			<h3 class="mt-4 text-lg font-semibold text-slate-900 dark:text-white">暫無文章</h3>

			<p class="mt-2 text-slate-500 dark:text-slate-400">
				目前還沒有發布任何內容，請稍後再回來查看。
			</p>
		</div>
	{/if}
</div>
