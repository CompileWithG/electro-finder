<template>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Fjalla+One&family=Paytone+One&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap"
        rel="stylesheet">
    <NavBar />
    <div class="responsive-container-block bigContainer">
        <div class="responsive-container-block Container">
            <div class="responsive-container-block leftSide">
                <p class="text-blk heading">Meet Our Creative Team</p>

                <h1> 23BRS1164 Shantnu Kumar</h1>
                <h1>23BRS1156 Karthik Anish</h1>
                <h1> 23BRS1173 Vaibhav Vats</h1>
            </div>
            <div class="responsive-container-block rightSide">
                <img class="number1img"
                    src="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/ET32.jpg" alt="Image 1">
                <img class="number2img" src="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/d14.png"
                    alt="Image 2">
                <img class="number3img"
                    src="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/b245.png" alt="Image 3">
                <img class="number5img"
                    src="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/Customer supports.png"
                    alt="Image 5">
                <iframe allowfullscreen="allowfullscreen" class="number4vid"
                    poster="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/b242.png"
                    src="https://www.youtube.com/embed/svg%3E?"></iframe>
                <img class="number7img" src="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/d51.png"
                    alt="Image 7">
                <img class="number6img" src="https://workik-widget-assets.s3.amazonaws.com/widget-assets/images/d12.png"
                    alt="Image 6">
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'
export default {
    name: 'About'
}
</script>

<style scoped>
h1 {
    font-family: "Paytone One", serif;
    font-weight: 400;
    font-style: normal;
    font-size: 20px;
}

* {
    font-family: Nunito, sans-serif;
}

.text-blk {
    padding: 0;
    line-height: 20px;
    color: white;
    font-size: 14px;
    margin-bottom: 40px;
}

.responsive-container-block {
    min-height: 75px;
    width: 100%;
    padding: 10px;
    display: flex;
    flex-wrap: wrap;
    margin: 0 auto;
    justify-content: flex-start;
}

.responsive-container-block.bigContainer {
    background-color: rgb(51, 51, 51);
    padding: 10px 20px;
}

.responsive-container-block.Container {
    max-width: 1320px;
    align-items: center;
    justify-content: center;
    margin: 80px auto;
}

.responsive-container-block.leftSide {
    max-width: 300px;
    flex-direction: column;
}

.text-blk.heading {
    font-size: 40px;
    line-height: 64px;
    font-weight: 900;
    color: #00B2EB;
    margin-bottom: 40px;
}

.text-blk.subHeading {
    font-size: 14px;
    line-height: 25px;
}

.responsive-container-block.rightSide {
    width: 675px;
    position: relative;
    display: flex;
    height: 700px;
}

.number1img {
    margin-top: 39%;
    margin-right: 80%;
    height: 32%;
    width: 20%;
    position: absolute;
}

.number2img {
    margin-top: 19%;
    margin-right: 42%;
    width: 35%;
    height: 39%;
    position: absolute;
}

.number3img {
    width: 13%;
    height: 21%;
    position: absolute;
    margin-top: 62%;
    margin-right: 64%;
}

.number4vid {
    width: 34%;
    height: 33%;
    position: absolute;
    margin-top: 62%;
    margin-right: 27%;
    margin-left: 39%;
}

.number5img {
    position: absolute;
    width: 13%;
    height: 21%;
    margin-top: 38%;
    margin-right: 27%;
    margin-left: 60%;
}

.number6img {
    position: absolute;
    margin-top: 0;
    margin-right: 3%;
    width: 35%;
    height: 33%;
}

.number7img {
    position: absolute;
    width: 25%;
    margin-top: 40%;
    margin-left: 75%;
    height: 42%;
}

@media (max-width: 1024px) {
    .responsive-container-block.Container {
        flex-direction: column-reverse;
    }

    .text-blk.heading {
        text-align: center;
        max-width: 370px;
    }

    .text-blk.subHeading {
        text-align: center;
    }

    .responsive-container-block.leftSide {
        align-items: center;
        max-width: 480px;
    }

    .responsive-container-block.rightSide {
        margin: 0 auto 100px auto;
    }
}

@media (max-width: 768px) {
    .responsive-container-block.rightSide {
        width: 450px;
        height: 450px;
    }

    .responsive-container-block.leftSide {
        max-width: 450px;
    }
}

@media (max-width: 500px) {

    .number1img,
    .number2img,
    .number3img,
    .number5img,
    .number6img,
    .number7img {
        display: none;
    }

    .responsive-container-block.rightSide {
        width: 100%;
        height: 250px;
    }

    .number4vid {
        position: static;
        width: 100%;
        height: 100%;
    }

    .text-blk.heading {
        font-size: 25px;
        line-height: 40px;
        max-width: 370px;
    }

    .responsive-container-block.leftSide {
        width: 100%;
    }
}

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600;700;800&display=swap');

*,
*:before,
*:after {
    box-sizing: border-box;
}

body {
    margin: 0;
}
</style>
