<template>
    <div class="column is-four-fifths py-1">
        <div class="box">
            <article class="media">
                <div class="media-left mt-3 ml-3">
                    <figure class="image is-128x128">
                        <img v-bind:src="company.get_image">
                    </figure>
                </div>
                <div class="media-content ml-5">
                    <div class="content">
                        <p style="text-align:left">
                            <strong style="font-size:1.063rem;">{{ company.name }}</strong> 
                            <br>
                            <div class="description-container">
                                <strong style="font-size:0.875rem">{{ company.get_description }}</strong>
                            </div>
                            <br>
                            User Rating:<star-rating :rating="company.get_rating" :star-style="starStyle" :is-indicator-active="false"></star-rating>
                        </p>
                    </div>
                </div>
            </article>
        </div>
    </div>
    <div class="column is-one-fifth py-1">
        <div class="box px-3">
            <div class="quote" style="margin-bottom:0.938rem">
                <a class="button is-success" style="font-size:0.938rem;">GET A QUOTE</a>
            </div>
            <div class="review">
                <a class="button" style="font-size:0.938rem;">WRITE A REVIEW</a>
            </div>
        </div>
    </div>
</template>

<style>
.content {
    word-break: break-all;
}
.button {
    width:100%;
    height:100%;
}
.star-rating {
    width:40%;
}
.box {
    height:10rem;
    border-radius:0rem;
}
.description-container {
    height:2rem;
}
</style>

<script>
import StarRating from 'vue-dynamic-star-rating'

export default {
    name: 'CompanyBox',
    data() {
        return {
            starStyle: {
                fullStarColor: '#ed8a19',
                emptyStarColor: '#737373',
                starWidth: 30,
                starHeight: 25,
            }
        }
    },
    props: {
        company: Object
    },
    components: {
        StarRating
    },
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>