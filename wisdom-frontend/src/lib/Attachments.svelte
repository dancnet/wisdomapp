<script>
    import { query } from "./api";
    import { node_selected } from "./store";
    import ImageUpload from "./ImageUpload.svelte";

    const remove = (img) => { 
        query(`/attachments/${img}`, 'DELETE').then(result => load_data());
    }

    let imgs = [];
    const load_data = () => {
        imgs = [];
        query(`/nodes/${$node_selected}/attachments/`).then(result => { imgs = result.map(i => i.id) });
    }
    load_data();

    const copy = img => {
        if (navigator.clipboard) {
            navigator.clipboard.writeText(`![](/a/${img})`);
        } else {
            alert ('Clipboard API not available');
        }
    }

    let show = null;
    let timeout = null;
    const show_image = img => timeout = setTimeout(() => show = img, 500);
    const clear_timeout = () => clearTimeout(timeout);
    const clear_image = () => show = null;

</script>

<ImageUpload on:upload={load_data} />
<div class=" w3-section w3-row">
    {#each imgs as img (img)}
    <div class="w3-col s6 boxwrapper">
        <div class="box w3-card">
            <div role="img" class="w3-white imgwrapper" on:mouseenter={() => show_image(img)} on:mouseleave={clear_timeout}>
                <img src={`/a/${img}`} class="w3-round" alt="Attachment preview">
            </div>
            <div class="buttons">
                <button class="w3-button" on:click={() => copy(img)}><i class="fa-regular fa-copy"></i> Copy</button>
                <button class="w3-button" on:click={() => remove(img)}><i class="fa-regular fa-trash-can"></i> Delete</button>
            </div>
        </div>
    </div>
    {#if show === img}
    <div on:mousemove={clear_image} role="img" class="image-popup">
        <div class="w3-animate-opacity w3-round-xlarge w3-border w3-border-deep-orange">
            <img src={`/a/${img}`} alt="Attachment">
        </div>
    </div>
    {/if}
    {/each}
</div>

<style>
.boxwrapper {
    padding: 10px;
}
.image-popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 95vw;
    height: 95vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: transparent;
}
.image-popup > div {
    overflow: hidden;
}
.image-popup img {
    max-height: 95vh;
    max-width: 95vw;
    object-fit: scale-down;
}
.imgwrapper > img {
    width: 100%;
    height: 75px;
    object-fit: cover;
    object-position: center;
}
.box {
    display: flex;
}
.imgwrapper {
    width: 100%;
}
.buttons {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
}
</style>