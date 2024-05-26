<script>
    import { saved_just_now } from '$lib/store';
</script>

{#if $saved_just_now}
<span><i class="fa-regular fa-floppy-disk"></i> Saved just now! <i class="fa-regular fa-floppy-disk"></i></span>
{/if}