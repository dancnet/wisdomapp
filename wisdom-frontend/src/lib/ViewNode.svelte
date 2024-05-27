<script>
    import Viewer from "$lib/Viewer.svelte";
    import Modal from "$lib/Modal.svelte";
    import { node_selected } from '$lib/store';
    import { query } from "$lib/api";
    import { show } from "jsmind";
    let markdown;
    query(`/nodes/${$node_selected}`).then(result => {
        markdown = result.markdown;
    });
</script>

<Modal>
    <div>
        {#if markdown}
        <Viewer {markdown} />
        {:else}
        <div class="w3-section w3-container">
            Nothing to show...
        </div>
        {/if}
    </div>
    <div slot="footer">

    </div>
</Modal>