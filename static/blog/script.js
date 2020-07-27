// variables
const lightbox = document.getElementById('lightbox');
const allImages = document.querySelectorAll('.js-gallery-img');
let currentIndex = 0

// get arrow elements
const arrowLeft = document.getElementById('arrow-left');
const arrowRight = document.getElementById('arrow-right');

// functions
function handleImageClick() {
    currentIndex = [...allImages].indexOf(this);
    lightbox.classList.add('active');
    window.addEventListener("keydown", checkKeyPress, false);
    lightboxImg = document.getElementById('lightbox-img');
    lightboxImg.src = allImages[currentIndex].dataset.fullImg;
}

function checkKeyPress(key) {
    if (key.keyCode == "37") {
       currentIndex--;
        if(currentIndex < 0) {
            currentIndex = allImages.length - 1;
        }
        lightboxImg.src = allImages[currentIndex].dataset.fullImg;
    }
    else if (key.keyCode == "39") {
        currentIndex++;
        if(currentIndex > allImages.length - 1) {
            currentIndex = 0;
        }
        lightboxImg.src = allImages[currentIndex].dataset.fullImg;
    }
    else if (key.keyCode == "27") {
        lightbox.classList.remove('active');
        window.removeEventListener("keydown", checkKeyPress, false);
    }
}

// func handle arrow click
function arrrowClick() {
    if (event.target == arrowLeft) {
        currentIndex -= 1;
        if(currentIndex < 0) {
            currentIndex = allImages.length - 1;
        }
        lightboxImg.src = allImages[currentIndex].dataset.fullImg;
    }
    else if (event.target == arrowRight) {
        currentIndex += 1;
        if(currentIndex > allImages.length - 1) {
            currentIndex = 0;
        }
        lightboxImg.src = allImages[currentIndex].dataset.fullImg;
    }
}

// event bindings
allImages.forEach(image => {
    image.addEventListener('click', handleImageClick);
})

lightbox.addEventListener('click', e => {
    if(e.target !== e.currentTarget) return
    lightbox.classList.remove('active');
    window.removeEventListener("keydown", checkKeyPress, false);
})

arrowLeft.addEventListener('click', arrrowClick)
arrowRight.addEventListener('click', arrrowClick)


// bind handler to arrows (handle arrow click)  / update src