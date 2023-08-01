function scrollToElement(elementId) {
    const element = document.querySelector(elementId);
    if (element) {
        element.scrollIntoView({ behavior: "smooth" });
    }
}

document.getElementById('sushiContainer').addEventListener('click', function () {
    scrollToElement('#rolu_opuckania');
});

document.getElementById('pizzaContainer').addEventListener('click', function () {
    scrollToElement('#pizza_id');
});

document.getElementById('salateContainer').addEventListener('click', function () {
    scrollToElement('#salate_id');
});
document.getElementById('hotContainer').addEventListener('click', function () {
    scrollToElement('#hotter_id');
});

document.getElementById('basisContainer').addEventListener('click', function () {
    scrollToElement('#ocnove_id');
});

document.getElementById('soupContainer').addEventListener('click', function () {
    scrollToElement('#supu_id');
});

document.getElementById('snacksContainer').addEventListener('click', function () {
    scrollToElement('#zakysku_id');
});

document.getElementById('garnishContainer').addEventListener('click', function () {
    scrollToElement('#garniru_id');
});

document.getElementById('nopoiContainer').addEventListener('click', function () {
    scrollToElement('#xolod_id');
});

document.getElementById('puvoContainer').addEventListener('click', function () {
    scrollToElement('#puvo_id');
});
