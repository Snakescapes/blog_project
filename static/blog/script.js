const lightbox = document.createElement('div')
lightbox.id = 'lightbox'
document.body.appendChild(lightbox)

const arrowLeft = document.createElement('a')
arrowLeft.id = 'arrow-left'
arrowLeft.classList.add('arrow')

const arrowRight = document.createElement('div')
arrowRight.id = 'arrow-right'
arrowRight.classList.add('arrow')



const images = document.querySelectorAll('.gallery img')
for (let [index, image] of images.entries()) {
    image.addEventListener('click', e => {
        lightbox.classList.add('active')

        const img = document.createElement('img')
        img.src = image.dataset.fullImg



        while (lightbox.firstChild) {
            lightbox.removeChild(lightbox.firstChild)
        }
        lightbox.appendChild(img)
        lightbox.appendChild(arrowLeft)
        lightbox.appendChild(arrowRight)

        prevImageUrl = images[i-1].src
        nextImageUrl = images[i+1].src
        arrowLeft.href = prevImageUrl
        arrowRight.href = nextImageUrl

    })
}

lightbox.addEventListener('click', e => {
    if(e.target !== e.currentTarget) return
    lightbox.classList.remove('active')
})

//let nextImage = $(".class").eq( $(".class").index( $(element) ) + 1 )


arrowLeft.addEventListener('click', e => {
    let prevImage = $(".class").eq( $(".class").index( $(element) ) - 1 )
    const img = document.createElement('img')
        img.src = prevImage.dataset.fullImg
})

// Clear all images
function reset() {
    for(let i = 0; i < images.length; i++) {
        images[i].style.display = 'none'
    }
}

function startSlide(){
    reset()
}


let galleries = document.querySelectorAll('div.gallery')
