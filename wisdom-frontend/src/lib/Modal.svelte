<script>
    import { show_modal } from '$lib/store';

    const close_modal = () => show_modal.set(null);
</script>

<div class="w3-modal" role="dialog" on:dblclick|self={close_modal}>
    <div class="w3-modal-content w3-card-4 w3-animate-zoom w3-round-large">
        <slot></slot>
        <div class="bottom-bar w3-light-grey w3-padding">
            <slot name="footer"></slot>
            <slot name="footer2"></slot>
            <button class="w3-button w3-white w3-border" on:click={close_modal}>Close</button>
        </div>
    </div> 
</div>

<style>
    .bottom-bar {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
    }
    .w3-modal {
        display: block;
        backdrop-filter: blur(2px);
    }
    .w3-modal-content {
        overflow: hidden;
    }
</style>