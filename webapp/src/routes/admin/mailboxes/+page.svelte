<script>
    import add from '$lib/assets/icons/add.svg';
    import filter from '$lib/assets/icons/filter.svg';
    import locker from '$lib/assets/icons/locker_light.svg';
    import sort from '$lib/assets/icons/sort.svg';
    import search from '$lib/assets/icons/search.svg';

    import Modal from '$lib/components/modal.svelte';
	import Navbar from '$lib/components/navbar.svelte';

    let searchValue = $state("");

    let isNavbarActive = $state(true);
    let isAddLockerActive = $state(true);
</script>

<!-- Add Locker Modal -->
{#snippet modal_content()}
	<div class="text-center">
		<h1 class="text-mlb-orange mb-4 text-4xl font-bold">Add Parcel to Locker</h1>

		<div class="my-10">
			<p class="mb-8 font-bold text-2xl">Insert Free Locker Number Here</p>
            <form class="flex w-full flex-col items-center justify-center p-3">
                <label for="tracking_num" class="text-lg font-bold w-full">Input Parcel Tracking Number Here:</label>
                <input
                    type="text"
                    id="tracking_num"
                    class="w-100 bg-mlb-gray/50 text-mlb-black hover:border-mlb-orange/60 w-3/4 rounded-3xl border-1 border-white px-2 py-1.5 text-center mt-4"
                    placeholder="RR123456785PH"
                />
            </form>
		</div>

		<button
			class="bg-mlb-orange text-mlb-white text-l m-3 rounded-2xl px-7 py-3 font-medium drop-shadow-sm hover:brightness-90"
		>
			Add
		</button>
	</div>
{/snippet}

{#if isAddLockerActive}
	<Modal {modal_content} bind:active={isAddLockerActive} />
{/if}

<div class="h-screen w-screen bg-mlb-gray/30 flex flex-row relative">
	<Navbar bind:active={isNavbarActive} />

    <div class="flex flex-row flex-wrap py-12 px-16 z-0 {isNavbarActive ? 'w-4/5' : 'w-full'}">
        <!-- Title & Utilities -->
        <div class="flex w-3/5 text-3xl text-mlb-black font-bold h-1/10">
            Mailboxes
        </div>
        
        <div class="flex w-2/5 h-1/10">
            <button class="flex place-content-center w-1/10">
                <img src={filter} class="max-w-8" alt="Filter">
            </button>

            <button class="flex w-1/10 place-content-center">
                <img src={sort} class="max-w-8" alt="Sort">
            </button>

            <button class="flex flex-row m-4 w-3/5 bg-mlb-gray/50 rounded-full px-4 py-2">
                <img src={search} class="flex s-1/5 mr-2" alt="Search">
                <input type="text" placeholder="Search..." class="flex w-7/8 text-sm" bind:value={searchValue}>
            </button>

            <div class="flex w-1/4 place-content-center items-center">
                <button 
                    class="flex py-2 px-4 place-content-center items-center bg-mlb-orange/90 rounded-3xl text-mlb-white font-bold hover:brightness-90"
                    onclick={() => {isAddLockerActive = true}}
                >
                    <img src={add} class="max-w-8" alt="Add">
                    <img src={locker} class="max-w-8" alt="Mailbox">
                </button>
            </div>
        </div>

        <!-- Header for the Logs -->
        <div class="flex flex-row w-full mb-4">
            <div class="w-1/8 font-bold text-lg text-center content-center">
                Locker Number
            </div>

            <div class="w-1/4 font-bold text-lg text-center content-center">
                Recipient
            </div>

            <div class="w-1/4 font-bold text-lg text-center content-center">
                Delivered By
            </div>

            <div class="w-1/4 font-bold text-lg text-center content-center">
                Claim By
            </div>

            <div class="w-1/8 font-bold text-lg text-center content-center">
                
            </div>
        </div>

        <!-- Content (Actual Logs) -->
        <div class="flex flex-row flex-wrap w-full h-8/10 overflow-auto">
            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>

            <div class="flex flex-row w-full rounded-2xl h-1/12 bg-mlb-white mb-4">
                <div class="w-1/8 text-center content-center">
                    24
                </div>

                <div class="w-1/4 text-center content-center">
                    DELA CRUZ, Juan A.
                </div>

                <div class="w-1/4 text-center content-center">
                    April 28, 2026
                </div>

                <div class="w-1/4 text-center content-center">
                    May 5, 2026
                </div>

                <div class="w-1/8 text-sm text-center content-center">
                    <button class="bg-mlb-red px-5 py-2 rounded-lg text-mlb-white mr-4">
                        Unlock
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
