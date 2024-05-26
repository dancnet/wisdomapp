<script>
    import { query } from "./api";
    import { node_selected } from "./store";
    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    let files, file_input, dragging = false;

    $: if (files && files[0]) upload(files[0]);

    const upload = async file => query(`/nodes/${$node_selected}/attachments/`, 'POST', file, 'FILE').then(result => {
        console.log(result);
        dispatch('upload', result);
    });

    const paste = async () => {
        if (!navigator.clipboard) {
            alert('Clipboard API not available');
            return;
        }
        const clipboardItems = await navigator.clipboard.read();
        if (clipboardItems.length === 1) {
            const clipboardItem = clipboardItems[0];
            const imageTypes = clipboardItem.types.filter(type => type.startsWith('image/'));
            if (imageTypes.length === 1) {
                const blob = await clipboardItem.getType(imageTypes[0]);
                upload(blob);
            } else console.error('The clipboard does not contain exactly one image.');
        } else console.error('There is not exactly one item in the clipboard.');
    }

    const drop = e => {
        dragging = false;
        const files = e.dataTransfer.files;
        if (files.length === 1 && files[0].type.startsWith('image/')) {
            upload(files[0]);
        } else if (files.length > 1) console.error("Trying to drop more than one image");
        else if (!files[0].type.startsWith('image/')) console.error("Trying to drop something else than an image");
    }
</script>

<input type="file" bind:files={files} bind:this={file_input} accept="image/*">
<div class="upload-area {dragging ? 'w3-deep-orange' : 'w3-light-grey'} w3-border w3-border-deep-orange " role="region" on:drop|preventDefault={drop} on:dragover|preventDefault={() => dragging = true}
on:dragleave|preventDefault={() => dragging = false}>
    <button class="w3-button w3-round-xxlarge w3-hover-deep-orange" on:click={() => file_input.click()}><i class="fa-solid fa-upload"></i> Select image</button>
    <p class="w3-large"><i class="fa-solid fa-fill-drip"></i> Drop image here</p>
    <button class="w3-button w3-round-xxlarge w3-hover-deep-orange" on:click={() => paste()}><i class="fa-regular fa-paste"></i> Paste image</button>
</div>

<style>
    .upload-area {
        height: 100px;
        width: 100%;
        overflow: hidden;
        user-select: none;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    input[type="file"] {
        display: none;
    }
</style>