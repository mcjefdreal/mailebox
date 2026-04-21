<script>
    import logo from '$lib/assets/mlb_logo.png';

    let {
        tracking_num = 'RR123456785PH',
        status = 'Delivered',
        locker_num = '24',
        deadline = '1'
    } = $props();
</script>

<div class="from-mlb-blue/20 to-mlb-orange/20 flex h-screen flex-col items-center justify-center bg-linear-to-t">
    <div class="bg-mlb-white m-6 w-80 rounded-xl p-5 flex flex-col items-center justify-center drop-shadow-md">
        <img src={logo} alt="MaiLeBox logo" class="max-w-50 pt-5">
        
        <div class="flex flex-col w-full p-3">
            <p class="text-sm font-extrabold text-left py-1"> Tracking Number </p>
            <p class="bg-mlb-gray/50 rounded-3xl py-1.5 px-2 text-center text-mlb-black font-bold"> {tracking_num} </p>
        </div>

        <div class="w-full p-3 grid grid-cols-3 gap-2 gap-x-2">
            <div class="text-sm font-bold"> Status: </div>
            <div class="col-span-2 text-sm"> {status} </div>

            <div class="text-sm font-bold"> Parcel at: </div>
            <div class="col-span-2 text-sm underline"> #{locker_num} </div>

            <div class="text-sm font-bold"> Claim in: </div>
            <div class="col-span-2 text-sm"> {deadline} days </div>
        </div>

        <div>
            <p class="italic"> status tba </p>
        </div>

        <button class="m-3 px-4 py-1.5 bg-mlb-orange rounded-2xl text-sm font-medium text-mlb-white hover:brightness-90 drop-shadow-sm"> Unlock </button>
	</div>
</div>
