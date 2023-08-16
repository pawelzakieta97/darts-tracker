<template>
    <div class="scores_container">
        <div class="scores_content">
            <h1>scores</h1>
            <ul class="scores_list">
                <li v-for="score in scores" :key="score.id">
                    <h2>{{ score.x }}</h2>
                    <p>{{ score.y }}</p>
                    <button @click="deletescore(score)">Delete</button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                // scores
                scores: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch scores
                    const response = await this.$http.get('http://localhost:8000/api/scores/');
                    // set the data returned as scores
                    this.scores = response.data; 
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
        },
        created() {
            // Fetch scores on page load
            this.getData();
        }
    }
</script>