<template>
    <div class="column is-four-fifths py-1">
        <div class="box">
            <article class="media">
                <div class="media-left">
                    <figure class="image">
                        <img v-bind:src="company.get_image">
                    </figure>
                </div>
                <div class="media-content">
                    <p style="text-align:left">
                        <strong style="font-size:1.063rem;">{{ company.name }}</strong> 
                        <br>
                        <strong style="font-size:0.875rem">{{ company.get_description }}</strong>
                        <br>
                        <br>
                        <div style="display:inline-block; align-items: center;">
                            User Rating:  <star-rating :inline="true" :star-size="20" :read-only="true" :show-rating="false" :rating="company.get_rating"></star-rating>
                        </div>
                    </p>
                </div>
            </article>
        </div>
    </div>
    <div class="column is-one-fifth py-1">
        <div class="box px-2" id="button-box">
            <a id="button-quote" class="button is-success">GET A QUOTE</a>
            <a class="button">WRITE A REVIEW</a>
        </div>
    </div>
</template>

<style>
.media-content {
    word-break: break-all;
    white-space: pre-wrap;
    word-break: keep-all;
    margin-left: 10px;
}
.media-left {
    height: auto;
    width: 20%;
    margin-top: 0.30rem;
}
.button {
    width:100%;
    height: auto;
    margin-bottom: 0.75rem;
    white-space: normal;
}
#button-quote {
    margin-top: 0.30rem;
}
.box {
    border-radius:0rem;
    height: 100%;
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
}
</style>

<script>
import StarRating from 'vue-star-rating'

export default {
    name: 'CompanyBox',
    props: {
        company: Object
    },
    components: {
        StarRating
    }
}
</script>