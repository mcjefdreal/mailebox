<script>
	import x from '$lib/assets/icons/x.svg';

	let { modal_content, active = $bindable() } = $props();
</script>

<div
	id="otp_modal"
	class="absolute top-0 left-0 z-100 flex h-screen w-screen place-content-center items-center justify-center bg-black/50"
>
	<div class="bg-mlb-white m-auto flex w-80 flex-col rounded-xl p-4 md:w-1/2">
		<!-- Close Button -->
		<button class="ml-auto" onclick={() => (active = false)}>
			<img src={x} alt="Close Modal" />
		</button>

		<div class="m-auto flex w-full items-center justify-center">
			{@render modal_content()}
		</div>
	</div>
</div>
