<script>
    import Modal from "$lib/Modal.svelte";
    import { Random } from "$lib/random";
    import Viewer from "$lib/Viewer.svelte";
    import { query } from "$lib/api";

    let quiz, position, length, question, answer;
    const next = () => {
        answer = null;
        position = quiz.position;
        question = quiz.next();
    }
    const show_answer = () => {
        query(`/nodes/${question.node_id}`).then(response => answer = response.markdown);
    }
    Random.init_quiz().then(resource => {
        quiz = resource;
        length = resource.length;
        next();
    });
</script>

<Modal>
    <div>
        {#if question}
        <Viewer markdown={question.question} />
        {#if answer !== null}
        <hr>
        <Viewer markdown={answer} />
        {/if}
        {:else}
        <div class="w3-container w3-section">Nothing to show...</div>
        {/if}
    </div>
    <div slot="footer">
        {#if question}
        <button class="w3-button w3-white w3-border" on:click={next}><i class="fa-solid fa-magnifying-glass-arrow-right"></i> Query Next</button>
        <button class="w3-button w3-white w3-border" on:click={show_answer}><i class="fa-regular fa-eye"></i> Show answer</button>
        {/if}
    </div>
    <div slot="footer2">
        {#if question}
        {position} / {length}
        {/if}
    </div>
</Modal>

<style>
    hr {
        margin: 0;
    }
</style>