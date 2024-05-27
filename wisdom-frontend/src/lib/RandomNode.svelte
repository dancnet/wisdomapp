<script>
    import Modal from "$lib/Modal.svelte";
    import { Random } from "$lib/random";
    import Viewer from "$lib/Viewer.svelte";

    let random_node = null;
    let position, length, node;
    const next = () => {
        position = random_node.position;
        node = random_node.next();
    }
    Random.init_random_node().then(resource => {
        random_node = resource;
        length = resource.length;
        next();
    });
</script>

<Modal>
    <div>
        {#if node}
        <div class="w3-center w3-border">
            <h3>{node.topic}</h3>
        </div>
        <Viewer markdown={node.markdown} />
        {:else}
        <div class="w3-container w3-section">Nothing to show...</div>
        {/if}
    </div>
    <div slot="footer">
        {#if node}
        <button class="w3-button w3-white w3-border" on:click={next}><i class="fa-solid fa-magnifying-glass-arrow-right"></i> Query Next</button>
        {/if}
    </div>
    <div slot="footer2">
        {#if node}
        {position} / {length}
        {/if}
    </div>
</Modal>