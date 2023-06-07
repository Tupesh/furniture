var images = [
    "https://i.ibb.co/Lvs6BvR/IMG-20210210-170640.jpg",
    "https://i.ibb.co/WchsLLF/IMG-20210517-201224.jpg",
    "https://i.ibb.co/KzLjvJw/IMG-20210707-132752.jpg",
    "https://i.ibb.co/Z6bHY54/IMG-20210720-161707.jpg",
    "https://i.ibb.co/YDTTmSn/IMG-20211028-171937.jpg",
    "https://i.ibb.co/FK5MH7W/IMG-20221004-093816.jpg",
    "https://i.ibb.co/C6HpDB7/IMG-20220324-195406.jpg",
    "https://i.ibb.co/GFZFW2h/IMG-20221123-084005.jpg",
    "https://i.ibb.co/0Y0TyMy/IMG-20210930-144409.jpg",
    "https://i.ibb.co/rG0wxd6/IMG-20220918-111144.jpg",
    "https://i.ibb.co/4NTxzLf/IMG-20211009-164731.jpg",
  
    // Add the URLs for the remaining images here
  ];

  var currentIndex = 0;
  var slideshowImage = document.getElementById("slideshow-image");

  function startSlideshow() {
    setInterval(changeImage, 3000); // Change image every 2 seconds
  }

  function changeImage() {
    currentIndex = (currentIndex + 1) % images.length;
    var imageUrl = images[currentIndex];
    slideshowImage.src = imageUrl;
  }

  startSlideshow();