<script>
    export let markdown;
    import { Marked } from 'marked';
    import { markedHighlight } from 'marked-highlight';
    import hljs from 'highlight.js';
    import 'highlight.js/styles/github-dark-dimmed.css';

    const marked = new Marked(
        markedHighlight({
            langPrefix: 'hljs language-',
            highlight(code, lang, info) {
            const language = hljs.getLanguage(lang) ? lang : 'plaintext';
            return hljs.highlight(code, { language }).value;
            }
        })
    );

    let html;
    $: html = marked.parse(markdown);
</script>

<div class="markdown-content w3-container" contenteditable="false" bind:innerHTML={html} />