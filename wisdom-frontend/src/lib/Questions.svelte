<script>
    import Editor from "$lib/Editor.svelte";
    import { node_selected } from '$lib/store';
    import { query } from '$lib/api';
    let questions = [];

    const get_questions = () => {
        query(`/nodes/${$node_selected}/questions/`).then(result => { questions = result });
    }
    get_questions();

    const add_question = () => {
        query(`/nodes/${$node_selected}/questions/`, 'POST', {question: ''});
        get_questions();
    }

    const save = (id, question) => {
        query(`/questions/${id}`, 'PUT', {question}).then(result => console.log(result));
    }

    const remove = id => {
        query(`/questions/${id}`, 'DELETE').then(result => console.log(result));
        get_questions();
    }
</script>

<div class="w3-container w3-section">
    <ul class="w3-ul w3-card-2">
        {#each questions as question (question.id)}
        <li class="w3-display-container">
            <Editor on:change={e => save(question.id, e.detail)} value={question.question} />
            <button on:click={() => remove(question.id)} class="w3-button w3-transparent w3-display-right">
                <i class="fa-regular fa-trash-can"></i>
            </button>
        </li>
        {/each}
        <li class="w3-display-container right">
            <button class="w3-button" on:click={add_question}><i class="fa-regular fa-square-plus"></i></button>
        </li>
    </ul>
</div>

<style>
li {
    padding: 0px;
}
.right {
    text-align: right;
}
</style>